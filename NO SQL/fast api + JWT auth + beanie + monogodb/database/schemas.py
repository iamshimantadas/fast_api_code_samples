from pydantic import BaseModel


class User(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str

class LoginUser(BaseModel):
    email : str
    password : str

class Blogs(BaseModel):
    title : str
    description : str        

class RefreshToken(BaseModel):
    access_token : str    