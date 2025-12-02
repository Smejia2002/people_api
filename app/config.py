import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL no está configurada")

    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 5,           
        'pool_recycle': 300,      
        'pool_pre_ping': True,    
        'max_overflow': 2,        
        'pool_timeout': 30,       
        'connect_args': {
            'connect_timeout': 10,
            'options': '-c statement_timeout=30000'  # 30 segundos
        }
    }