from flask import Blueprint, request, jsonify
from services.chat_service import ChatService
from services.pricing_service import PricingService
import uuid

chat_bp = Blueprint('chat', __name__)
chat_service = ChatService()
pricing_service = PricingService()

@chat_bp.route('/start', methods=['POST'])
def start_conversation():
    """Inicia uma nova conversa"""
    try:
        session_id = str(uuid.uuid4())
        conversation = chat_service.start_conversation(session_id)
        
        messages = conversation.get_messages()
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'conversation_id': conversation.id,
            'messages': messages
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/start-detailed', methods=['POST'])
def start_detailed_conversation():
    """Inicia uma nova conversa com funcionalidade de pesquisa de mercado"""
    try:
        session_id = str(uuid.uuid4())
        conversation = chat_service.start_conversation(session_id)
        
        # Mensagem inicial específica para orçamento detalhado
        detailed_welcome = """Olá! 👋 

Bem-vindo ao **Orçamento Detalhado com Pesquisa de Mercado**!

🔍 Aqui eu vou:
• Fazer uma pesquisa automática nos principais sites brasileiros
• Comparar valores praticados no mercado para projetos similares
• Gerar um orçamento baseado em dados reais de mercado
• Apresentar uma comparação detalhada com a concorrência

Para começar, me conte sobre seu projeto. Pode ser um app, website, sistema web, e-commerce, etc. 

Quanto mais detalhes você me der, melhor será a pesquisa de mercado! 🚀"""
        
        # Substituir a mensagem inicial
        from models.conversation import Conversation
        conv = Conversation.query.filter_by(session_id=session_id).first()
        if conv:
            # Limpar mensagens existentes e adicionar a nova
            conv.messages = []
            conv.add_message('assistant', detailed_welcome)
            from extensions import db
            db.session.commit()
        
        messages = conv.get_messages() if conv else []
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'conversation_id': conversation.id,
            'messages': messages,
            'market_research_enabled': True
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/message', methods=['POST'])
def send_message():
    """Envia mensagem e recebe resposta do chat"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        message = data.get('message')
        
        if not session_id or not message:
            return jsonify({'success': False, 'error': 'session_id e message são obrigatórios'}), 400
        
        # Verificar se é uma solicitação detalhada (com pesquisa de mercado)
        include_market_research = data.get('include_market_research', False)
        
        # Processar mensagem
        response = chat_service.process_message(session_id, message, include_market_research)
        
        # Verificar se já foi gerado um orçamento no process_message
        if response.get('quote'):
            return jsonify({
                'success': True,
                'message': response.get('quote_message', response['message']),
                'quote_generated': True,
                'quote': response['quote'],
                'requirements': response['requirements']
            })
        
        return jsonify({
            'success': True,
            'message': response['message'],
            'quote_generated': response.get('should_generate_quote', False),
            'requirements': response.get('requirements', {})
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/conversation/<session_id>', methods=['GET'])
def get_conversation(session_id):
    """Recupera conversa existente"""
    try:
        from models.conversation import Conversation
        conversation = Conversation.query.filter_by(session_id=session_id).first()
        
        if not conversation:
            return jsonify({'success': False, 'error': 'Conversa não encontrada'}), 404
        
        return jsonify({
            'success': True,
            'conversation_id': conversation.id,
            'session_id': conversation.session_id,
            'messages': conversation.get_messages(),
            'requirements': conversation.get_requirements(),
            'status': conversation.status
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500