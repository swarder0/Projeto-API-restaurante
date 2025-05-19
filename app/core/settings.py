from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    USER_AGENT_NAME = os.getenv("USER_AGENT_NAME")
    USER_AGENT_CONTACT = os.getenv("USER_AGENT_CONTACT")

    SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    MONGO_APP_NAME = os.getenv("MONGO_APP_NAME")

    @property
    def MONGODB_URL(self):
        user = self.MONGO_USER
        password = self.MONGO_PASSWORD
        cluster = self.MONGO_CLUSTER
        app_name = self.MONGO_APP_NAME

        from urllib.parse import quote_plus
        user_enc = quote_plus(user)
        password_enc = quote_plus(password)

        return f"mongodb+srv://{user_enc}:{password_enc}@{cluster}/?retryWrites=true&w=majority&appName={app_name}"

settings = Settings()
