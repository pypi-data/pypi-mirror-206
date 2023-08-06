from typing import List, Optional

import hao
from fastapi import Depends

from ..domains import Permission, User
from ..exceptions import PermissionDeniedException
from .auths import decode_user
from .unsecure import UnsecureBearer

_BEARER = UnsecureBearer(tokenUrl='api/passport/login', scheme_name='JWT', auto_error=False)

SECRET = hao.config.get('app.secret', 'Pz2VfqJjGl5a')
TOKEN_KEY = 'tailors-token'


def current_user(token: str = Depends(_BEARER)):
    return decode_user(token)


class Authed:
    def __init__(self, permissions: Optional[List[Permission]] = None) -> None:
        self.permissions = permissions

    def __call__(self, user: User = Depends(current_user)):
        if not self.permissions:
            return
        permissions_required = set(p.value for p in self.permissions)
        permissions_user = set(user.permissions)
        permissions_matched = permissions_required.intersection(permissions_user)
        if len(permissions_matched) == 0:
            raise PermissionDeniedException()
