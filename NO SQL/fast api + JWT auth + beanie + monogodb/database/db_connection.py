from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from .models import User, Blog

async def init_db():
    client = AsyncIOMotorClient("mongodb+srv://iamshimantadas:9icJV6nfGTlFB0v5@cluster0.nyxj0fc.mongodb.net/")
    
    await init_beanie(database=client.testAuth, document_models=[User,Blog])