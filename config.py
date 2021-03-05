class Config:
    SECRET_KEY = "8tFXLF46fRUkRFqJrfMjIbYAYeEJKyqB"

    # jwt config
    ALGORITHM = "HS256"
    DECODING = "utf-8"

    ACCESS_TOKEN_EXPIRE = 36000 # in seconds
    REFRESH_TOKEN_EXPIRE = 36000 # in seconds

    ticketing_base_url = "http://ticketing:8118/api/v1/"
