from pydantic import BaseModel

class DefaultResponseModel(BaseModel):
    detail: str


def _400(desc='Bad Request', detail='Bad Request') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': 'Bad Request'}
            }
        }
    }

def _401(desc='Unauthorized', detail='Unauthorized') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': 'Unauthorized'}
            }
        }
    }

def _403(desc='Forbidden', detail='Forbidden') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': 'Requesting without authentication on a protected endpoint',
        'content': {
            'application/json': {
                'example': {'detail': 'Forbidden'}
            }
        }
    }

def _404(desc='Not Found', detail='Not Found') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': "Not Found"}
            }
        }
    }

def _406(desc='Not Acceptable', detail='Not Acceptable') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': "Not Acceptable"}
            }
        }
    }

def _409(desc='Conflict', detail='Conflict') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': "Conflict"}
            }
        }
    }

def _422(desc='Unprocessable Entity', detail='Unprocessable Entity') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': "Unprocessable Entity"}
            }
        }
    }

def _500(desc='Internal Server Error', detail='Internal Server Error') -> dict:
    return {
        'model': DefaultResponseModel,
        'description': desc,
        'content': {
            'application/json': {
                'example': {'detail': 'Internal Server Error'}
            }
        }
    }

responses = {
    400: _400(),
    401: _401(),
    403: _403(),
    404: _404(),
    406: _406(),
    409: _409(),
    422: _422(),
    500: _500()
}