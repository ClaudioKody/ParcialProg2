class Config:
    USER = os.getenv('MYSQL_USER')
    PASSWORD = os.getenv('MYSQL_PASSWORD')
    HOST = os.getenv('MYSQL_HOST', 'localhost')
    PORT = os.getenv('MYSQL_PORT', '3306')
    DB = os.getenv('MYSQL_DB')
    
    # Construcción inteligente de la URL
    if PASSWORD:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    else:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}@{HOST}:{PORT}/{DB}"