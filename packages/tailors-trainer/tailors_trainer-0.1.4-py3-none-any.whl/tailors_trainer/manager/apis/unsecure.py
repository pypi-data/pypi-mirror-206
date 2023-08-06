from typing import Optional

from fastapi import Request
from fastapi.security import OAuth2PasswordBearer

from . import TOKEN_KEY


class UnsecureBearer(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        token = await super().__call__(request)
        if token:
            return token
        return request.cookies.get(TOKEN_KEY)
