import hao
from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from tailors_trainer import __version__

from ..domains import User
from . import TOKEN_KEY, current_user
from .auths import TOKEN_TTL_SECONDS, login

LOGGER = hao.logs.get_logger(__name__)


router = APIRouter(prefix='/api/passport')


@router.post('/login')
def handle_login(response: Response, form: OAuth2PasswordRequestForm = Depends()):
    user, token = login(form.username, form.password)
    response.set_cookie(key=TOKEN_KEY, value=token, max_age=TOKEN_TTL_SECONDS, httponly=True)
    return {'user': user.dict(exclude_none=True), 'access_token': token, 'token_type': "bearer"}


@router.get('/logout')
def handle_logout(response: Response):
    token = None
    response.delete_cookie(key=TOKEN_KEY)
    return {'msg': 'You are logged out', 'access_token': token, 'token_type': "bearer"}


@router.get('/profile')
def handle_profile(user: User = Depends(current_user)):
    return user
