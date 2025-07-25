import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

class Config:
    """Configurações da aplicação"""
    
    # Configurações do servidor
    PORT = int(os.getenv('PORT', 5000))
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Configurações do banco de dados
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'entidades')
    
    # Configurações de CORS
    CORS_ORIGIN = os.getenv('CORS_ORIGIN', 'http://localhost:5173')
    
    @staticmethod
    def get_database_url():
        """Retorna a URL completa do banco de dados"""
        return f"{Config.MONGODB_URI}{Config.DATABASE_NAME}"
