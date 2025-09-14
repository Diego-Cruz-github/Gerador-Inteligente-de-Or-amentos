from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from extensions import db, ma

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///orcamentos.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensões
    db.init_app(app)
    ma.init_app(app)
    CORS(app)
    
    return app

app = create_app()

with app.app_context():
    # Importar modelos
    from models.conversation import Conversation
    from models.orcamento import Orcamento
    from models.projeto_template import ProjetoTemplate
    
    # Importar rotas
    from routes.chat import chat_bp
    from routes.orcamentos import orcamentos_bp
    from routes.dashboard import dashboard_bp
    
    # Registrar blueprints
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    app.register_blueprint(orcamentos_bp, url_prefix='/api/orcamentos')
    app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')

@app.route('/')
def index():
    return jsonify({
        'message': 'Gerador Inteligente de Orçamentos API',
        'version': '1.0.0',
        'description': 'Sistema conversacional para geração de orçamentos profissionais',
        'endpoints': {
            'chat': '/api/chat',
            'orcamentos': '/api/orcamentos',
            'dashboard': '/api/dashboard'
        }
    })

@app.route('/health')
def health():
    return jsonify({'status': 'OK', 'database': 'connected'})

# Criar tabelas
with app.app_context():
    db.create_all()
    print("Sistema inicializado com sucesso!")

if __name__ == '__main__':
    app.run(debug=True, port=5000)