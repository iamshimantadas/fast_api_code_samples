from pydantic import BaseModel

class User(BaseModel):
    name : str
    email : str
    phone : int
    password : str

class AuthUser(BaseModel):
    email : str
    password : str

class PatchUser(BaseModel):
    name : str | None = None
    email : str | None = None
    phone : int | None = None

class DeleteUser(BaseModel):
    id : int    

class Blogs(BaseModel):
    title : str
    description : str    