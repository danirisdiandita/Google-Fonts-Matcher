import os 
from dotenv import load_dotenv 
load_dotenv()
class Config(): 
    def __init__(self) -> None:
        self.db_host = os.getenv("DB_HOST") 
        self.db_port = os.getenv("DB_PORT")
        self.db_user = os.getenv("DB_USER")
        self.db_name = os.getenv("DB_NAME")
        self.db_pass = os.getenv("DB_PASS")
        self.database_url = f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
        self.jwt_key = os.getenv("SECRET_KEY")
        self.jwt_algorithm = os.getenv("ALGORITHM")