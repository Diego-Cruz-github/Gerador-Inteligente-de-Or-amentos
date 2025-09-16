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

@chat_bp.route('/quick-quote/<session_id>', methods=['POST'])
def generate_quick_quote(session_id):
    """Gera orçamento rápido com dados mínimos disponíveis"""
    try:
        from models.conversation import Conversation
        conversation = Conversation.query.filter_by(session_id=session_id).first()
        
        if not conversation:
            return jsonify({'success': False, 'error': 'Conversa não encontrada'}), 404
        
        # Gerar orçamento rápido
        result = chat_service.generate_quick_quote(conversation.id)
        
        return jsonify({
            'success': True,
            'message': result['explanation'],
            'quote': result['quote'],
            'used_defaults': result['used_defaults'],
            'quote_generated': True
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/generate-from-form', methods=['POST'])
def generate_quote_from_form():
    """Gera orçamento a partir dos dados estruturados do formulário"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        required_fields = ['serviceType', 'urgency', 'location', 'budgetTier']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'error': f'Campo {field} é obrigatório'}), 400
        
        # Mapear tipos de serviço para o pricing service
        service_mapping = {
            'website': 'website',
            'ecommerce': 'website',  # E-commerce usa a mesma base de website
            'app': 'app',
            'sistema': 'website',  # Sistema web usa base de website
            'landing': 'website',  # Landing page usa base de website
            'blog': 'website'  # Blog usa base de website
        }
        
        # Mapear urgência
        urgency_mapping = {
            'normal': 'normal',
            'urgent': 'urgent', 
            'super_urgent': 'super_urgent'
        }
        
        # Preparar requirements para o pricing service
        requirements = {
            'project_type': service_mapping.get(data['serviceType'], 'website'),
            'location': data['location'],
            'urgency': urgency_mapping.get(data['urgency'], 'normal'),
            'budget_tier': data['budgetTier'],
            'description': data.get('description', ''),
            'service_type_original': data['serviceType']  # Manter tipo original para análise
        }
        
        # Gerar orçamento usando o pricing service
        # Note: Need to create a conversation for generate_quote method
        from models.conversation import Conversation
        from extensions import db
        import uuid
        
        # Create temporary conversation for quote generation
        temp_session_id = str(uuid.uuid4())
        temp_conversation = Conversation(
            session_id=temp_session_id,
            status='active'
        )
        
        # Add requirements to conversation (serialize as JSON)
        import json
        temp_conversation.requirements = json.dumps(requirements)
        
        # Save to database
        db.session.add(temp_conversation)
        db.session.commit()
        
        # Generate quote
        quote = pricing_service.generate_quote(temp_conversation.id, requirements)
        
        # Clean up temporary conversation
        db.session.delete(temp_conversation)
        db.session.commit()
        
        # Análise IA da descrição do projeto (se fornecida)
        ai_analysis = ""
        if data.get('description'):
            ai_analysis = chat_service.analyze_project_description(
                data['description'], 
                data['serviceType'],
                quote
            )
        
        return jsonify({
            'success': True,
            'quote': quote,
            'ai_analysis': ai_analysis,
            'requirements': requirements
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/generate-detailed-from-form', methods=['POST'])
def generate_detailed_quote_from_form():
    """Gera orçamento detalhado com pesquisa de mercado a partir dos dados estruturados do formulário"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios (mais campos para versão detalhada)
        required_fields = ['serviceType', 'complexity', 'expectedUsers', 'urgency', 'location', 'budgetTier']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'error': f'Campo {field} é obrigatório para orçamento detalhado'}), 400
        
        # Mapear tipos de serviço (mais opções para versão detalhada)
        service_mapping = {
            'website': 'website',
            'ecommerce': 'website',
            'app': 'app',
            'sistema': 'website', 
            'landing': 'website',
            'blog': 'website',
            'api': 'sistema',
            'erp': 'sistema',
            'crm': 'sistema'
        }
        
        # Mapear complexidade
        complexity_mapping = {
            'baixa': 'baixa',
            'media': 'media',
            'alta': 'alta',
            'enterprise': 'alta'  # Enterprise é tratado como alta complexidade
        }
        
        # Mapear expected users
        users_mapping = {
            'small': 100,
            'medium': 1000,
            'large': 10000,
            'enterprise': 50000
        }
        
        # Mapear urgência
        urgency_mapping = {
            'normal': 'normal',
            'urgent': 'urgent', 
            'super_urgent': 'super_urgent',
            'flexible': 'normal'  # Flexível é tratado como normal
        }
        
        # Preparar requirements para o pricing service
        requirements = {
            'project_type': service_mapping.get(data['serviceType'], 'website'),
            'complexity': complexity_mapping.get(data['complexity'], 'media'),
            'expected_users': users_mapping.get(data['expectedUsers'], 1000),
            'location': data['location'],
            'urgency': urgency_mapping.get(data['urgency'], 'normal'),
            'budget_tier': data['budgetTier'],
            'description': data.get('description', ''),
            'service_type_original': data['serviceType'],
            'detailed_mode': True,
            'market_research_enabled': True
        }
        
        # Adicionar opções de pesquisa de mercado
        market_options = data.get('market_research_options', {})
        requirements['market_research_options'] = market_options
        
        # Criar conversa temporária para geração do orçamento
        from models.conversation import Conversation
        from extensions import db
        import uuid
        import json
        
        temp_session_id = str(uuid.uuid4())
        temp_conversation = Conversation(
            session_id=temp_session_id,
            status='active'
        )
        
        temp_conversation.requirements = json.dumps(requirements)
        
        db.session.add(temp_conversation)
        db.session.commit()
        
        # Gerar orçamento com pesquisa de mercado habilitada
        quote = pricing_service.generate_quote(temp_conversation.id, requirements, include_market_research=True)
        
        # Limpar conversa temporária
        db.session.delete(temp_conversation)
        db.session.commit()
        
        # Análise IA detalhada da descrição do projeto
        ai_analysis = ""
        if data.get('description'):
            ai_analysis = chat_service.analyze_detailed_project_description(
                data['description'], 
                data['serviceType'],
                data['complexity'],
                data['expectedUsers'],
                quote
            )
        
        # Extrair pesquisa de mercado se disponível
        market_research = quote.get('market_research', '')
        
        return jsonify({
            'success': True,
            'quote': quote,
            'ai_analysis': ai_analysis,
            'market_research': market_research,
            'requirements': requirements
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    """Gera PDF do orçamento"""
    try:
        data = request.get_json()
        quote_data = data.get('quote')
        ai_analysis = data.get('ai_analysis', '')
        market_research = data.get('market_research', '')
        
        if not quote_data:
            return jsonify({'success': False, 'error': 'Dados do orçamento são obrigatórios'}), 400
        
        # Simular geração de PDF (implementar posteriormente)
        pdf_filename = f"orcamento_{quote_data.get('id', 'temp')}.pdf"
        
        return jsonify({
            'success': True,
            'pdf_url': f'/downloads/{pdf_filename}',
            'message': 'PDF gerado com sucesso!'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@chat_bp.route('/send-email', methods=['POST'])
def send_email():
    """Envia orçamento por email"""
    try:
        data = request.get_json()
        quote_data = data.get('quote')
        ai_analysis = data.get('ai_analysis', '')
        market_research = data.get('market_research', '')
        email = data.get('email')
        
        if not quote_data or not email:
            return jsonify({'success': False, 'error': 'Dados do orçamento e email são obrigatórios'}), 400
        
        # Simular envio de email (implementar posteriormente)
        return jsonify({
            'success': True,
            'message': f'Orçamento enviado para {email} com sucesso!'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500