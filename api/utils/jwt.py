from fastapi import HTTPException, status
from jose import JWTError, jwt
import datetime

from config import Config
from api.utils.logs import console_logger

_schema = {
    "access_token": {
        "iat": None,
        "sub": None,
        "exp": None
    },
    "refresh_token": {
        "iat": None,
        "sub": None,
        "exp": None
    }
}

def generate_token(token_type, payload):
    seconds = Config.ACCESS_TOKEN_EXPIRE if token_type == "access_token" else Config.REFRESH_TOKEN_EXPIRE
    _schema[token_type]["iat"] = datetime.datetime.now()
    _schema[token_type]["exp"] = _schema[token_type]["iat"] + datetime.timedelta(seconds=seconds)
    _schema[token_type]["sub"] = str(payload)
    try:
        token = jwt.encode(
            _schema[token_type], 
            Config.SECRET_KEY, 
            algorithm=Config.ALGORITHM)
        return token
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
    except Exception as e:
        console_logger.debug(e)


def decode_token(token):
    try:
        return jwt.decode(
            token, 
            Config.SECRET_KEY, 
            algorithms=Config.ALGORITHM)["sub"]
    except (jwt.JWTError, jwt.ExpiredSignatureError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
    except Exception as e:
        raise



