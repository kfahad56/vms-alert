from fastapi.security.http import HTTPBase
from fastapi.param_functions import Depends

from api.utils.jwt import decode_token

def authenticate_user(token: str = Depends(HTTPBase(scheme='Bearer'))):
    payload = decode_token(token.credentials)
    return payload
    