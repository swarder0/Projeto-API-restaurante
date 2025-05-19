from urllib.parse import quote_plus
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

user = quote_plus(os.getenv("MONGO_USER"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
cluster = os.getenv("MONGO_CLUSTER")
app_name = os.getenv("MONGO_APP_NAME")
db_name = os.getenv("MONGO_DB_NAME")

MONGO_URL = f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority&appName={app_name}"

client = AsyncIOMotorClient(MONGO_URL)
db = client[db_name]