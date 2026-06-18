import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Le sumamos el puerto (y si no existe en el .env, usa el 3306 por defecto)
    port = os.getenv('MYSQL_PORT', '3307')
    
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:"
        f"{os.getenv('MYSQL_PASSWORD')}@"
        f"{os.getenv('MYSQL_HOST')}:{port}/"  # <-- ACÁ sumamos el :puerto
        f"{os.getenv('MYSQL_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False