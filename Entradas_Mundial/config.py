class Config:
    USER = os.getenv('MYSQL_USER', 'root')
    PASSWORD = os.getenv('MYSQL_PASSWORD', '220724')
    HOST = os.getenv('MYSQL_HOST', 'localhost')
    PORT = os.getenv('MYSQL_PORT', '3307')
    DB = os.getenv('MYSQL_DB', 'mundial')
    
    if PASSWORD:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    else:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}@{HOST}:{PORT}/{DB}"