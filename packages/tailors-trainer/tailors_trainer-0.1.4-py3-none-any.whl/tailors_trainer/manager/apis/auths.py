import time

import hao
from jose import JWTError, jwt
from ldap3 import ALL, Connection, Server
from passlib.context import CryptContext

from ..domains import Permission, User
from ..exceptions import BadTokenException, ExpiredTokenException, InvalidUserOrPasswordException, UnAuthedException

SECRET = hao.config.get('app.secret', 'FqX1wLk55d462TbT')
_PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
_ALGORITHM = "HS256"

_SERVER = Server('ldap.bl-ai.com', get_info=ALL)
_BASE_DN_USER = 'ou=users,dc=bailian,dc=ai'
TOKEN_TTL_SECONDS = 3600 * 24 * 7


def get_hashed_password(password: str) -> str:
    return _PWD_CONTEXT.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return _PWD_CONTEXT.verify(password, hashed_pass)


def encode_token(data):
    return jwt.encode(data, SECRET, _ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=[_ALGORITHM])
    except JWTError:
        raise BadTokenException()


def encode_user(user: User):
    return encode_token(user.dict(exclude_none=True))


def decode_user(token):
    if token is None:
        raise UnAuthedException()
    user = User(**decode_token(token))
    if user.timestamp is None or user.timestamp < (time.time() - TOKEN_TTL_SECONDS):
        raise ExpiredTokenException()
    return user


def login(username: str, password: str):
    user = f"cn={username},{_BASE_DN_USER}"
    conn = Connection(_SERVER, user=user, password=password)
    if not conn.bind():
        raise InvalidUserOrPasswordException()
    search_filter = f'(&(objectclass=inetOrgPerson)(cn={username}))'
    conn.search(_BASE_DN_USER, search_filter, attributes=['sn', 'mail', 'userPassword'])
    entry = conn.entries[0]
    user = User(
        name=entry.sn.value,
        username=username,
        email=entry.mail.value,
        permissions=get_permissions(username)
    )
    token = encode_user(user)
    return user, token


def get_permissions(username: str):
    if username == 'chenhao':
        return [Permission.ADMIN.value, Permission.AI.value]
    return []
