*** if anyone creating new accout .. the it's response as:
{
  "user instance": {
    "_id": "65c3332e57efdf2662dca1c3",
    "first_name": "tez",
    "last_name": "parker",
    "email": "tez@mail.com",
    "password": "$2b$12$FSXPx43DLlPIgnjNTvFCweSvQ1KFMT6y1P2R9nDZPZh/FAg6YpDiu",
    "address": null
  },
  "token": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2VtYWlsIjoidGV6QG1haWwuY29tIiwiZXhwIjoxNzA3MjkzMjM4Ljc1MTk1ODF9.bC87dnTO-rhvEixz-4F-Dcf11LE278YjkAP07gLx5jI",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2VtYWlsIjoidGV6QG1haWwuY29tIiwiZXhwIjoxNzA3ODk2MjM4Ljc1MjQwMTR9.JtxWrogmtcDX2sZizMfyF9bkwlJNOronX0aykWGRn3U",
    "token_type": "bearer"
  }
}
-----------------------------------------------------------------------------
** if user makes success login with email and password, teh  he/she get's a response as:
{
  "user instance": {
    "_id": "65c3332e57efdf2662dca1c3",
    "first_name": "tez",
    "last_name": "parker",
    "email": "tez@mail.com",
    "password": "$2b$12$FSXPx43DLlPIgnjNTvFCweSvQ1KFMT6y1P2R9nDZPZh/FAg6YpDiu",
    "address": null
  },
  "token": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2VtYWlsIjoidGV6QG1haWwuY29tIiwiZXhwIjoxNzA3MjkzNDcwLjU2MzQ1NDR9.6eRBHEtk5LG8a_3Te3TZEaZqYskHT4_YIf8-wa_6awM",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2VtYWlsIjoidGV6QG1haWwuY29tIiwiZXhwIjoxNzA3ODk2NDcwLjU2MzgyMDF9.0MYwlgEm95Wj7y_1rk0AMqplbjH8O2vrtPhhyuJqXL8",
    "token_type": "bearer"
  }
}
--------------------------------------------------------------------------------------



## basic packages
pip install fastapi, uvicorn, beanie

## iportant packages install command
pip install PyJWT
pip install bcrypt
pip install passlib
pip install python-jose