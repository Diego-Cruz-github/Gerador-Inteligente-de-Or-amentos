import json
import re
from models.conversation import Conversation
from models.projeto_template import ProjetoTemplate
from services.pricing_service import PricingService
from services.ai_service import AIService
from extensions import db

class ChatService:
    def __init__(self):
        self.pricing_service = PricingService()
        self.ai_service = AIService()
        
        # Templates de perguntas por categoria
        self.question_templates = {
            'tipo_projeto': [
                "Que tipo de projeto você tem em mente?",
                "Vou te ajudar a criar um orçamento personalizado! Para começar, me conte sobre seu projeto.",
                "Olá! Sou especialista em orçamentos de TI. Qual tipo de solução você precisa?"
            ],
            'app_mobile': [
                "Quantos usuários você espera que usem o app?",
                "O app precisa funcionar offline?", 
                "Vai precisar de notificações push?",
                "Precisa integrar com redes sociais?",
                "Vai ter sistema de pagamento integrado?"
            ],
            'website': [
                "O site é institucional ou e-commerce?",
                "Quantas páginas aproximadamente?",
                "Precisa de área administrativa?",
                "Vai integrar com algum sistema externo?",
                "Precisa de sistema de blog/notícias?"
            ],
            'sistema': [
                "Quantos usuários simultâneos o sistema terá?",
                "Precisa de diferentes níveis de acesso?",
                "Vai integrar com sistemas existentes?",
                "Precisa de relatórios complexos?",
                "Vai ter módulo financeiro?"
            ]
        }
        
        # Keywords para identificar tipo de projeto
        self.project_keywords = {
            'app': ['app', 'aplicativo', 'mobile', 'android', 'ios', 'react native', 'flutter'],
            'website': ['site', 'website', 'landing page', 'e-commerce', 'loja virtual', 'portal'],
            'sistema': ['sistema', 'erp', 'crm', 'dashboard', 'painel', 'plataforma', 'web app']
        }

    def start_conversation(self, session_id):
        """Inicia uma nova conversa"""
        conversation = Conversation(session_id=session_id)
        db.session.add(conversation)
        db.session.commit()
        
        # Gera mensagem de boas-vindas usando IA
        welcome_message = self.ai_service.generate_welcome_message()
        
        conversation.add_message('assistant', welcome_message)
        db.session.commit()
        
        return conversation

    def process_message(self, session_id, user_message, include_market_research=False):
        """Processa mensagem do usuário e gera resposta"""
        conversation = Conversation.query.filter_by(session_id=session_id).first()
        
        if not conversation:
            conversation = self.start_conversation(session_id)
        
        # Adiciona mensagem do usuário
        conversation.add_message('user', user_message)
        
        # Analisa o contexto da conversa
        messages = conversation.get_messages()
        requirements = conversation.get_requirements()
        
        # Gera resposta usando IA do Groq
        ai_response = self.ai_service.generate_response(messages, user_message)
        
        # Adiciona resposta do assistente
        conversation.add_message('assistant', ai_response['response'])
        
        # Se deve gerar orçamento, extrai informações usando IA
        should_generate_quote = ai_response['should_generate_quote']
        if should_generate_quote:
            # Extrai informações do projeto usando IA
            extracted_info = self.ai_service.extract_project_info(messages)
            
            # Garantir informações mínimas necessárias
            if not extracted_info.get('project_type'):
                # Tenta identificar pelo contexto das mensagens
                conversation_text = ' '.join([msg['content'].lower() for msg in messages if msg['role'] == 'user'])
                if any(word in conversation_text for word in ['app', 'aplicativo', 'mobile']):
                    extracted_info['project_type'] = 'app'
                elif any(word in conversation_text for word in ['site', 'website', 'landing']):
                    extracted_info['project_type'] = 'website'  
                elif any(word in conversation_text for word in ['sistema', 'erp', 'crm']):
                    extracted_info['project_type'] = 'sistema'
                else:
                    extracted_info['project_type'] = 'app'  # fallback
            
            if not extracted_info.get('complexity'):
                extracted_info['complexity'] = 'media'
                
            if not extracted_info.get('region'):
                extracted_info['region'] = 'interior'
            
            requirements.update(extracted_info)
            conversation.set_requirements(requirements)
            
            # Se deve gerar orçamento, fazê-lo agora
            if should_generate_quote:
                try:
                    quote = self.pricing_service.generate_quote(
                        conversation.id, 
                        requirements, 
                        include_market_research=include_market_research
                    )
                    
                    # Formatar mensagem do orçamento
                    quote_message = self._format_quote_message(quote, include_market_research)
                    conversation.add_message('assistant', quote_message)
                    
                    db.session.commit()
                    
                    return {
                        'message': ai_response['response'],
                        'conversation_id': conversation.id,
                        'should_generate_quote': True,
                        'requirements': requirements,
                        'quote': quote,
                        'quote_message': quote_message
                    }
                except Exception as e:
                    print(f"Erro ao gerar orçamento: {e}")
                    error_message = "Desculpe, houve um erro ao gerar seu orçamento. Pode tentar novamente ou reformular sua solicitação?"
                    conversation.add_message('assistant', error_message)
        
        db.session.commit()
        
        return {
            'message': ai_response['response'],
            'conversation_id': conversation.id,
            'should_generate_quote': should_generate_quote,
            'requirements': requirements
        }

    def _generate_response(self, conversation, user_message, messages, requirements):
        """Gera resposta baseada no contexto da conversa"""
        
        # Identifica tipo de projeto se ainda não foi definido
        if not requirements.get('project_type'):
            project_type = self._identify_project_type(user_message)
            if project_type:
                requirements['project_type'] = project_type
                requirements['project_description'] = user_message
                
                # Primeira pergunta específica do tipo de projeto
                next_question = self._get_next_question(project_type, requirements)
                return {
                    'message': f"Perfeito! Entendi que você quer desenvolver um {project_type}. {next_question}",
                    'requirements_update': requirements
                }
            else:
                return {
                    'message': "Não consegui identificar o tipo de projeto. Pode me dar mais detalhes? Por exemplo: app mobile, site, sistema web, e-commerce, etc."
                }
        
        # Se já temos o tipo, fazer perguntas específicas
        project_type = requirements.get('project_type')
        
        # Extrair informações da resposta atual
        extracted_info = self._extract_information(user_message, project_type)
        if extracted_info:
            requirements.update(extracted_info)
        
        # Verificar se temos informações suficientes para gerar orçamento
        if self._has_sufficient_info(requirements):
            return {
                'message': "Ótimo! Com base nas informações que você me passou, vou gerar seu orçamento personalizado. Um momento...",
                'should_generate_quote': True,
                'requirements_update': requirements
            }
        
        # Próxima pergunta
        next_question = self._get_next_question(project_type, requirements)
        return {
            'message': next_question,
            'requirements_update': requirements
        }

    def _identify_project_type(self, message):
        """Identifica o tipo de projeto baseado na mensagem"""
        message_lower = message.lower()
        
        for project_type, keywords in self.project_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                return project_type
        
        return None

    def _extract_information(self, message, project_type):
        """Extrai informações específicas da mensagem"""
        info = {}
        message_lower = message.lower()
        
        # Extrair números (usuários, páginas, etc.)
        numbers = re.findall(r'\d+', message)
        
        if project_type == 'app':
            if any(word in message_lower for word in ['mil', 'thousand', 'k']):
                if numbers:
                    info['expected_users'] = int(numbers[0]) * 1000
            elif numbers:
                info['expected_users'] = int(numbers[0])
                
            if any(word in message_lower for word in ['offline', 'sem internet']):
                info['offline_support'] = True
            if any(word in message_lower for word in ['push', 'notificação']):
                info['push_notifications'] = True
            if any(word in message_lower for word in ['pagamento', 'pagar', 'cartão']):
                info['payment_integration'] = True
                
        elif project_type == 'website':
            if numbers:
                info['pages_count'] = int(numbers[0])
            if any(word in message_lower for word in ['e-commerce', 'loja', 'venda']):
                info['is_ecommerce'] = True
            if any(word in message_lower for word in ['admin', 'administrativo', 'gerencial']):
                info['needs_admin'] = True
                
        elif project_type == 'sistema':
            if numbers:
                info['concurrent_users'] = int(numbers[0])
            if any(word in message_lower for word in ['relatório', 'report', 'dashboard']):
                info['needs_reports'] = True
            if any(word in message_lower for word in ['financeiro', 'contábil']):
                info['financial_module'] = True
        
        # Complexidade implícita
        if any(word in message_lower for word in ['simples', 'básico', 'pequeno']):
            info['complexity'] = 'baixa'
        elif any(word in message_lower for word in ['complexo', 'avançado', 'grande', 'robusto']):
            info['complexity'] = 'alta'
        else:
            info['complexity'] = 'media'
            
        # Localização/região
        if any(word in message_lower for word in ['são paulo', 'sp', 'capital']):
            info['region'] = 'SP'
        elif any(word in message_lower for word in ['remoto', 'online', 'distância']):
            info['region'] = 'remoto'
        else:
            info['region'] = 'interior'
        
        return info

    def _get_next_question(self, project_type, requirements):
        """Gera próxima pergunta baseada no tipo e requisitos já coletados"""
        
        if project_type == 'app':
            if not requirements.get('expected_users'):
                return "Quantos usuários você espera que usem o app? (Por exemplo: 1000, 10 mil, 50 mil usuários)"
            elif not requirements.get('platform_specific'):
                return "O app precisa rodar em Android e iOS ou apenas uma plataforma?"
            elif requirements.get('offline_support') is None:
                return "O app precisa funcionar offline ou sempre precisará de internet?"
            elif requirements.get('push_notifications') is None:
                return "Vai precisar de notificações push para os usuários?"
                
        elif project_type == 'website':
            if not requirements.get('pages_count'):
                return "Quantas páginas aproximadamente o site terá? (Ex: 5-10 páginas, 20-30 páginas)"
            elif requirements.get('is_ecommerce') is None:
                return "O site é para vendas online (e-commerce) ou é mais institucional?"
            elif requirements.get('needs_admin') is None:
                return "Precisa de uma área administrativa para gerenciar o conteúdo?"
                
        elif project_type == 'sistema':
            if not requirements.get('concurrent_users'):
                return "Quantos usuários vão usar o sistema ao mesmo tempo? (Ex: 10, 50, 200 usuários)"
            elif requirements.get('needs_reports') is None:
                return "O sistema precisa gerar relatórios e dashboards?"
            elif requirements.get('user_levels') is None:
                return "Precisa de diferentes níveis de acesso (admin, usuário comum, etc.)?"
        
        return "Me conte mais sobre alguma funcionalidade específica que é importante para você."

    def _has_sufficient_info(self, requirements):
        """Verifica se temos informações suficientes para gerar orçamento"""
        project_type = requirements.get('project_type')
        
        if not project_type:
            return False
        
        base_requirements = ['project_type', 'complexity']
        
        if project_type == 'app':
            specific_requirements = ['expected_users']
        elif project_type == 'website':
            specific_requirements = ['pages_count']
        elif project_type == 'sistema':
            specific_requirements = ['concurrent_users']
        else:
            specific_requirements = []
        
        required_fields = base_requirements + specific_requirements
        
        return all(requirements.get(field) for field in required_fields)

    def _format_quote_message(self, quote, include_market_research=False):
        """Formata mensagem do orçamento para o chat"""
        
        base_message = f"""
Perfeito! Aqui está seu orçamento personalizado:

📊 **{quote['project_name']}**
💰 **Valor Total**: R$ {quote['total_cost']:,.2f}
⏱️ **Prazo**: {quote['timeline_weeks']} semanas
📈 **Complexidade**: {quote['complexity'].title()}
📍 **Região**: {quote['region']}

**Breakdown de Horas:**
• Design: {quote['hours_breakdown']['design']}h
• Frontend: {quote['hours_breakdown']['frontend']}h  
• Backend: {quote['hours_breakdown']['backend']}h
• Testes: {quote['hours_breakdown']['testing']}h
• Gerenciamento: {quote['hours_breakdown']['pm']}h

**Total**: {quote['total_hours']} horas × R$ {quote['hourly_rate']}/h

O orçamento inclui {len(quote['features'])} funcionalidades principais e foi calculado com base em dados reais do mercado brasileiro."""

        # Adicionar pesquisa de mercado se disponível
        if include_market_research and quote.get('market_research'):
            base_message += f"\n\n{quote['market_research']}"
        
        base_message += "\n\nGostaria de ver o detalhamento completo ou fazer algum ajuste?"
        
        return base_message