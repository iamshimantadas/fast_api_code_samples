
import bcrypt
from fastapi import APIRouter, status, Depends, HTTPException
from database import schemas
from database.models import User, Blog
from jwt_auth.auth_handler import sign_access_token, sign_refresh_token, token_response, decode_access_token
from jwt_auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post('/user', status_code=status.HTTP_201_CREATED)
async def create_user(users: schemas.User):
    user_email = users.email
    try:
        hashed_password = bcrypt.hashpw(users.password.encode('utf-8'), bcrypt.gensalt())
        user_obj = User(first_name=users.first_name,last_name=users.last_name,email=users.email,password=hashed_password)
        user_rec = await user_obj.insert()
        # Your user creation logic
        access_token = sign_access_token(user_email)  # Replace user_id with actual user ID
        refresh_token = sign_refresh_token(user_email)  # Replace user_id with actual user ID
        return {"user instance":user_rec,"token":token_response(access_token, refresh_token)}
    except Exception as e:
        print(e)
        return {"message": "error"}

@router.post('/login')
async def login_user(users: schemas.LoginUser):
    user_obj = await User.find_one({"email": users.email})
    user_email = users.email
    if user_obj:
        stored_hashed_password = user_obj.password.encode('utf-8')
        input_password = users.password.encode('utf-8')
        
        if bcrypt.checkpw(input_password, stored_hashed_password):
            access_token = sign_access_token(user_email) 
            refresh_token = sign_refresh_token(user_email) 
            return {"user instance": user_obj, "token": token_response(access_token, refresh_token)}
            
        else:
            return {"message":"credentials not match"}
        
    else:
        return {"message": "user not exist"}


@router.post("/refresh-token/", tags=['refresh token'])
async def refresh_token(token: schemas.RefreshToken):
    try:
        token = token.access_token
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )

        access_token = sign_access_token(payload["user_email"])
        refresh_token = sign_refresh_token(payload["user_email"])

        return {"access_token": access_token, "refresh_token": refresh_token}
    except Exception as e:
        print(e)
        return {"message":"error occured"}


@router.post('/blog_post', dependencies=[Depends(JWTBearer())], tags=['new blog'])
async def create_new_post(blog: schemas.Blogs):
    try:
        blog_obj = Blog(title=blog.title, description=blog.description)
        await blog_obj.insert()
        return {"message":"blog published"}
    except Exception as e:
        print(e)
        return {"message":"error"}