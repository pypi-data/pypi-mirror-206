# -*- coding: utf-8 -*-
import hao
import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from tailors_trainer import __version__

from .apis import SECRET, passport_api
from .exceptions import AuthException

LOGGER = hao.logs.get_logger(__name__)

app = FastAPI(title='Tailors Manager', version=__version__)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(SessionMiddleware, secret_key=SECRET)


@app.get('/_ping')
async def handle_ping():
    return {'msg': 'running'}


app.include_router(passport_api.router)
app.mount("/", StaticFiles(directory="dist", html=True), name="static")


@app.on_event("startup")
async def startup_event():
    LOGGER.info('server started')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    sw = hao.stopwatch.Stopwatch()
    response = await call_next(request)
    LOGGER.debug(f"{request.url} took: {sw.took()}")
    return response


@app.exception_handler(AuthException)
async def handle_auth_exceptions(request: Request, ex: Exception):
    return JSONResponse(status_code=401, content={'error': str(ex)}, headers={'WWW-Authenticate': 'Bearer'})


@app.exception_handler(AssertionError)
async def assertion_exception_handler(request, ex):
    return JSONResponse(status_code=400, content={'error': str(ex)})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, ex):
    error = '; '.join([
        f"[{e._loc[-1]}] {e.exc.msg_template}"
        for e in ex.raw_errors
    ])
    return JSONResponse(status_code=400, content={'error': error})


@app.exception_handler(Exception)
async def handle_exceptions(request: Request, ex: Exception):
    return JSONResponse(status_code=500, content={'error': f"Oops! {str(ex)}"})


def run():
    try:
        uvicorn.run(app, host="0.0.0.0", port=8050, server_header=False)
    except KeyboardInterrupt:
        print('[ctrl-c]')
    except Exception as err:
        LOGGER.exception(err)


if __name__ == '__main__':
    run()
