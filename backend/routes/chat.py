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

@chat_bp.route('/message', methods=['POST'])
def send_message():
    """Envia mensagem e recebe resposta do chat"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        message = data.get('message')
        
        if not session_id or not message:
            return jsonify({'success': False, 'error': 'session_id e message são obrigatórios'}), 400
        
        # Processar mensagem
        response = chat_service.process_message(session_id, message)
        
        # Se deve gerar orçamento, fazer isso
        if response.get('should_generate_quote'):
            try:
                quote = pricing_service.generate_quote(
                    response['conversation_id'], 
                    response['requirements']
                )
                
                # Adicionar mensagem com o orçamento
                quote_message = chat_service._format_quote_message(quote)
                chat_service.process_message(session_id, quote_message)
                
                return jsonify({
                    'success': True,
                    'message': response['message'],
                    'quote_generated': True,
                    'quote': quote,
                    'requirements': response['requirements']
                })
            except Exception as e:
                error_message = f"Erro ao gerar orçamento: {str(e)}"
                chat_service.process_message(session_id, error_message)
                return jsonify({
                    'success': True,
                    'message': error_message,
                    'quote_generated': False
                })
        
        return jsonify({
            'success': True,
            'message': response['message'],
            'quote_generated': False,
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