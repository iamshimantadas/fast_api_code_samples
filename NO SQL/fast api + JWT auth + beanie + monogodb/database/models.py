from beanie import Document

class User(Document):
    first_name : str
    last_name : str
    email : str
    password : str
    address : str | None = None

class Blog(Document):
    title : str
    description : str
    
