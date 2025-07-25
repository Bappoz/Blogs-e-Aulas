from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Importa as configurações e conexão do banco
from app.config.config import Config
from app.db.connection import db_connection

# Carrega as variáveis de ambiente
load_dotenv()

def create_app():
    # Cria a instância do Flask
    app = Flask(__name__)
    
    # Inicializa extensões
    CORS(app, origins=[Config.CORS_ORIGIN])
    
    # Conecta ao banco de dados
    db = db_connection.connect()
    if db is None:
        print("Erro: Não foi possível conectar ao banco de dados")
        return None
    
    # Rota de teste
    @app.route('/')
    def home():
        return jsonify({
            "message": "API Blogs e Aulas está funcionando!",
            "status": "success",
            "database": "MongoDB conectado" if db else "MongoDB desconectado"
        })
    
    # Rota de teste do banco de dados
    @app.route('/test-db')
    def test_database():
        try:
            # Testa uma operação simples no banco
            collections = db.list_collection_names()
            return jsonify({
                "message": "Conexão com MongoDB testada com sucesso!",
                "database": Config.DATABASE_NAME,
                "collections": collections
            })
        except Exception as e:
            return jsonify({
                "message": "Erro ao testar conexão com MongoDB",
                "error": str(e)
            }), 500

    return app

# Cria a aplicação
app = create_app()

if __name__ == '__main__':
    if app:
        app.run(
            host='0.0.0.0',
            port=Config.PORT,
            debug=Config.FLASK_DEBUG
        )
    else:
        print("Falha ao inicializar a aplicação")
