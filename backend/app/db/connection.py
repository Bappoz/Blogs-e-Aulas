from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.client = None
        self.db = None
        
    def connect(self):
        """Conecta ao MongoDB"""
        try:
            # String de conexão do MongoDB
            mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
            database_name = os.getenv('DATABASE_NAME', 'blogs_e_aulas')
            
            # Cria a conexão
            self.client = MongoClient(mongodb_uri)
            
            # Testa a conexão
            self.client.admin.command('ping')
            
            # Seleciona o banco de dados
            self.db = self.client[database_name]
            
            print(f"MongoDB conectado com sucesso! Database: {database_name}")
            return self.db
            
        except ConnectionFailure as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None
    
    def get_database(self):
        """Retorna a instância do banco de dados"""
        if self.db is None:
            return self.connect()
        return self.db
    
    def close_connection(self):
        """Fecha a conexão com o MongoDB"""
        if self.client:
            self.client.close()
            print("Conexão com MongoDB fechada")

# Instância global da conexão
db_connection = DatabaseConnection()
