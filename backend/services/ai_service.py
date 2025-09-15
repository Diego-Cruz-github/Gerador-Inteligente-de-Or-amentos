import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.model = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')
        self.max_tokens = int(os.getenv('MAX_TOKENS', '800'))
        self.temperature = float(os.getenv('TEMPERATURE', '0.7'))
        
        # System prompt para o consultor de orçamentos
        self.system_prompt = """Você é um consultor especialista em orçamentos de tecnologia no Brasil. 
Sua função é fazer perguntas inteligentes e contextuais para coletar os requisitos de projetos de tecnologia.

INSTRUÇÕES IMPORTANTES:
1. Seja conversacional, amigável e profissional
2. Faça UMA pergunta por vez, de forma natural
3. Adapte suas perguntas ao tipo de projeto mencionado
4. Colete informações sobre: tipo de projeto, complexidade, número de usuários, funcionalidades especiais
5. Quando tiver informações suficientes, diga "GERAR_ORCAMENTO" para finalizar
6. Use linguagem brasileira e seja direto

FORMATAÇÃO OBRIGATÓRIA DAS RESPOSTAS:
- SEMPRE use **negrito** (exatamente 2 asteriscos) para destacar informações importantes
- NUNCA use ***3 asteriscos*** - use apenas **2 asteriscos**
- SEMPRE use • para criar listas quando apropriado
- SEMPRE use emojis moderadamente para tornar mais amigável (📱 💻 🌐 ⚡ 📊 🚀 💡 ✅)
- SEMPRE use quebras de linha duplas para separar seções
- SEMPRE organize o texto em seções claras
- Seja claro e direto, evite texto muito longo

EXEMPLO EXATO DE FORMATAÇÃO:
Perfeito! Entendi que você quer um **app mobile**! 📱

**Para calcular o orçamento**, preciso saber:
• Quantos usuários você espera?
• Vai funcionar offline?
• Precisa de notificações?

🚀 **Próximo passo**: Me conte sobre essas funcionalidades!

ATENÇÃO: Use APENAS **texto** com 2 asteriscos, NUNCA ***texto*** com 3 asteriscos!

TIPOS DE PROJETO:
- Apps Mobile (iOS/Android) 📱
- Websites (institucional, e-commerce, landing pages) 💻
- Sistemas Web (ERP, CRM, dashboards) 🌐

RESPONDA SEMPRE EM PORTUGUÊS BRASILEIRO COM FORMATAÇÃO RICA."""

    def generate_response(self, conversation_messages, user_message):
        """
        Gera resposta da IA baseada no histórico da conversa
        """
        try:
            # Prepara as mensagens para o Groq
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Adiciona histórico da conversa
            for msg in conversation_messages:
                if msg['role'] in ['user', 'assistant']:
                    messages.append({
                        "role": msg['role'],
                        "content": msg['content']
                    })
            
            # Adiciona a nova mensagem do usuário
            messages.append({
                "role": "user", 
                "content": user_message
            })
            
            # Chama a API do Groq
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=0.9,
                stop=None
            )
            
            ai_response = response.choices[0].message.content
            
            # Pós-processamento: Garantir formatação consistente
            # Converter ***texto*** para **texto** (3 asteriscos para 2)
            ai_response = ai_response.replace('***', '**')
            
            # FORÇAR formatação SEMPRE (radical)
            # Quebras antes de qualquer negrito
            ai_response = ai_response.replace('. **', '.\n\n**')
            ai_response = ai_response.replace('! **', '!\n\n**')
            ai_response = ai_response.replace('? **', '?\n\n**')
            ai_response = ai_response.replace(') **', ')\n\n**')
            
            # Quebras antes de emojis + negrito
            ai_response = ai_response.replace('🚀 **', '\n\n🚀 **')
            ai_response = ai_response.replace('📝 **', '\n\n📝 **')
            ai_response = ai_response.replace('💻 **', '\n\n💻 **')
            ai_response = ai_response.replace('📱 **', '\n\n📱 **')
            ai_response = ai_response.replace('🔍 **', '\n\n🔍 **')
            
            # Quebras antes de qualquer emoji sozinho
            ai_response = ai_response.replace(' 🚀', '\n\n🚀')
            ai_response = ai_response.replace(' 📝', '\n\n📝')
            ai_response = ai_response.replace(' 💻', '\n\n💻')
            ai_response = ai_response.replace(' 📱', '\n\n📱')
            
            # Garantir quebra antes de listas
            ai_response = ai_response.replace(':\n•', ':\n\n•')
            ai_response = ai_response.replace(': •', ':\n\n•')
            
            # Limpar múltiplas quebras excessivas
            ai_response = ai_response.replace('\n\n\n\n', '\n\n')
            ai_response = ai_response.replace('\n\n\n', '\n\n')
            ai_response = ai_response.lstrip('\n')
            
            # Debug sem encoding issues
            try:
                print("Formatacao aplicada com sucesso")
            except:
                pass
            
            # Verifica se deve gerar orçamento
            should_generate_quote = "GERAR_ORCAMENTO" in ai_response.upper()
            
            # Remove a palavra-chave da resposta
            if should_generate_quote:
                ai_response = ai_response.replace("GERAR_ORCAMENTO", "").strip()
                if not ai_response:
                    ai_response = "Perfeito! Com base nas informações coletadas, vou gerar seu orçamento personalizado agora."
            
            return {
                'response': ai_response,
                'should_generate_quote': should_generate_quote
            }
            
        except Exception as e:
            try:
                print(f"Erro na API do Groq: {e}")
            except:
                print("Erro na API do Groq (encoding issues)")
            return {
                'response': "Desculpe, tive um problema técnico. Pode repetir sua mensagem?",
                'should_generate_quote': False
            }

    def extract_project_info(self, conversation_messages):
        """
        Extrai informações do projeto a partir da conversa usando IA
        """
        try:
            # Prepara prompt para extração de informações
            extraction_prompt = """Analise esta conversa e extraia as informações do projeto em formato JSON.

REGRAS IMPORTANTES:
1. Para project_type, use APENAS: "app", "website" ou "sistema"
2. Se mencionar: app, aplicativo, mobile → use "app"
3. Se mencionar: site, website, landing, ecommerce → use "website"  
4. Se mencionar: sistema, ERP, CRM, dashboard → use "sistema"
5. SEMPRE defina um project_type baseado no contexto
6. Se não conseguir identificar claramente, use "app" como padrão

FORMATO DE RESPOSTA (apenas JSON válido):
{
    "project_type": "app|website|sistema",
    "complexity": "baixa|media|alta",
    "expected_users": number,
    "concurrent_users": number,
    "pages_count": number,
    "region": "SP|interior|remoto",
    "offline_support": true/false,
    "push_notifications": true/false,
    "payment_integration": true/false,
    "is_ecommerce": true/false,
    "needs_admin": true/false,
    "needs_reports": true/false,
    "financial_module": true/false,
    "project_description": "string"
}

EXEMPLOS:
- "quero um app mobile" → "project_type": "app"
- "preciso de um site" → "project_type": "website"
- "sistema de gestão" → "project_type": "sistema"

Preencha apenas os campos identificados. Use null para campos não identificados."""

            # Monta o histórico da conversa
            conversation_text = ""
            for msg in conversation_messages:
                conversation_text += f"{msg['role']}: {msg['content']}\n"
            
            messages = [
                {"role": "system", "content": extraction_prompt},
                {"role": "user", "content": f"Conversa:\n{conversation_text}"}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.1,  # Baixa temperatura para extração precisa
                top_p=0.9
            )
            
            ai_response = response.choices[0].message.content
            
            # Tenta fazer parse do JSON
            import json
            try:
                extracted_info = json.loads(ai_response)
                # Remove campos null
                extracted_info = {k: v for k, v in extracted_info.items() if v is not None}
                return extracted_info
            except json.JSONDecodeError:
                print(f"Erro ao fazer parse do JSON: {ai_response}")
                return {}
                
        except Exception as e:
            print(f"Erro na extração de informações: {e}")
            return {}

    def generate_welcome_message(self):
        """Gera mensagem de boas-vindas personalizada para orçamento rápido"""
        # Mensagem fixa e bem formatada para orçamento rápido
        return """Olá! 👋 

**Bem-vindo ao Gerador Inteligente de Orçamentos**!

Sou seu consultor especializado em projetos de tecnologia. Vou te fazer algumas perguntas rápidas para criar um **orçamento personalizado** baseado nas suas necessidades.

📝 **Como funciona:**
• Você me conta sobre seu projeto
• Faço perguntas específicas para entender melhor
• Gero um orçamento detalhado em poucos minutos

🚀 **Para começar**, me conte: que tipo de projeto você tem em mente?
(App mobile, website, sistema web, e-commerce, etc.)"""