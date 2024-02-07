# import time
# from typing import Dict

# import jwt

# JWT_SECRET = "UIGYH4783GHQ7HWWIUH837"
# JWT_ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# REFRESH_TOKEN_EXPIRE_DAYS = 7


# def token_response(token: str):
#     return {
#         "access_token": token
#     }


# def signJWT(user_email: str) -> Dict[str, str]:
#     payload = {
#         "user_email": user_email,
#         "expires": time.time() + 600
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token)


# def decodeJWT(token: str) -> dict:
#     try:
#         decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#         return decoded_token if decoded_token["expires"] >= time.time() else None
#     except:
#         return {}



import secrets
import time
import jwt

JWT_SECRET = "UIGYH4783GHQ7HWWIUH837"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

def generate_refresh_token(user_email: str) -> str:
    return secrets.token_urlsafe(32)

def token_response(access_token: str, refresh_token: str):
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

def sign_access_token(user_email: str) -> str:
    payload = {
        "user_email": user_email,
        "exp": time.time() + (ACCESS_TOKEN_EXPIRE_MINUTES * 60)  # Expire in ACCESS_TOKEN_EXPIRE_MINUTES minutes
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def sign_refresh_token(user_email: str) -> str:
    payload = {
        "user_email": user_email,
        "exp": time.time() + (REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60)  # Expire in REFRESH_TOKEN_EXPIRE_DAYS days
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
