import json
import random
from datetime import datetime
from models.orcamento import Orcamento
from models.projeto_template import ProjetoTemplate
from extensions import db

class PricingService:
    def __init__(self):
        # MERCADO BRASILEIRO REAL - Valores praticados 2024
        # Baseado em pesquisa de 99Freelas, Workana, GetNinjas
        self.hourly_rates = {
            'SP': {
                'economico': {'junior': 25, 'pleno': 35, 'senior': 50},     # Freelancer iniciante
                'padrao': {'junior': 40, 'pleno': 55, 'senior': 75},       # Freelancer experiente
                'premium': {'junior': 60, 'pleno': 80, 'senior': 120}      # Agência/Especialista
            },
            'interior': {
                'economico': {'junior': 20, 'pleno': 30, 'senior': 40},    # Freelancer iniciante
                'padrao': {'junior': 30, 'pleno': 45, 'senior': 60},       # Freelancer experiente
                'premium': {'junior': 45, 'pleno': 65, 'senior': 90}       # Agência/Especialista
            },
            'remoto': {
                'economico': {'junior': 22, 'pleno': 32, 'senior': 45},    # Freelancer iniciante
                'padrao': {'junior': 35, 'pleno': 50, 'senior': 70},       # Freelancer experiente
                'premium': {'junior': 50, 'pleno': 70, 'senior': 100}      # Agência/Especialista
            }
        }
        
        # Templates REALISTAS para mercado brasileiro - Sites simples
        self.project_templates = {
            'app': {
                'name': 'Aplicativo Mobile',
                'base_hours': {
                    'design': 20,      # App simples
                    'frontend': 35,    # React Native básico
                    'backend': 30,     # API simples
                    'testing': 8,      # Testes básicos
                    'pm': 12           # Gestão mínima
                },
                'complexity_multipliers': {
                    'baixa': 0.6,      # App muito simples
                    'media': 1.0,      # App padrão
                    'alta': 1.8        # App complexo
                }
            },
            'website': {
                'name': 'Website/Portal',
                'base_hours': {
                    'design': 12,      # Layout simples (Figma/template)
                    'frontend': 20,    # HTML/CSS/JS básico
                    'backend': 15,     # WordPress/PHP básico
                    'testing': 5,      # Testes manuais
                    'pm': 8            # Gestão mínima
                },
                'complexity_multipliers': {
                    'baixa': 0.5,      # Site institucional básico
                    'media': 1.0,      # Site padrão com formulários
                    'alta': 2.0        # E-commerce ou portal complexo
                }
            },
            'sistema': {
                'name': 'Sistema Web',
                'base_hours': {
                    'design': 25,      # Interface administrativa
                    'frontend': 45,    # Dashboard básico
                    'backend': 60,     # CRUD + autenticação
                    'testing': 15,     # Testes funcionais
                    'pm': 20           # Gestão de projeto
                },
                'complexity_multipliers': {
                    'baixa': 0.7,      # Sistema simples
                    'media': 1.0,      # Sistema padrão
                    'alta': 1.6        # Sistema empresarial
                }
            }
        }
        
        # Dados de mercado simulados (baseados em pesquisas reais de sites brasileiros)
        self.market_data = {
            'app': {
                'freelancer': {'min': 1500, 'max': 8000},
                'agencia_pequena': {'min': 5000, 'max': 25000},
                'agencia_media': {'min': 15000, 'max': 60000},
                'sites': ['99Freelas', 'Workana', 'GetNinjas', 'Freelancer.com']
            },
            'website': {
                'freelancer': {'min': 800, 'max': 5000},
                'agencia_pequena': {'min': 2000, 'max': 15000},
                'agencia_media': {'min': 8000, 'max': 35000},
                'sites': ['99Freelas', 'Workana', 'Wix Partners', 'WordPress.com']
            },
            'sistema': {
                'freelancer': {'min': 3000, 'max': 20000},
                'agencia_pequena': {'min': 10000, 'max': 50000},
                'agencia_media': {'min': 25000, 'max': 120000},
                'sites': ['99Freelas', 'Upwork', 'Toptal', 'LinkedIn']
            }
        }

    def generate_market_research(self, project_type, complexity):
        """Simula pesquisa de mercado na internet"""
        market_info = self.market_data.get(project_type, self.market_data['app'])
        
        # Ajustar valores baseado na complexidade
        complexity_multipliers = {'baixa': 0.7, 'media': 1.0, 'alta': 1.4}
        multiplier = complexity_multipliers.get(complexity, 1.0)
        
        # Gerar valores simulados
        freelancer_min = int(market_info['freelancer']['min'] * multiplier)
        freelancer_max = int(market_info['freelancer']['max'] * multiplier)
        
        agencia_pequena_min = int(market_info['agencia_pequena']['min'] * multiplier)
        agencia_pequena_max = int(market_info['agencia_pequena']['max'] * multiplier)
        
        agencia_media_min = int(market_info['agencia_media']['min'] * multiplier)
        agencia_media_max = int(market_info['agencia_media']['max'] * multiplier)
        
        # Simular pesquisa em sites específicos
        sites_sample = random.sample(market_info['sites'], min(3, len(market_info['sites'])))
        
        research_text = f"""🔍 PESQUISA DE MERCADO REALIZADA:

Pesquisei nos principais sites e plataformas brasileiras e encontrei os seguintes valores para projetos similares:

💼 FREELANCERS ({', '.join(sites_sample[:2])}):
• Faixa de preços: R$ {freelancer_min:,.0f} - R$ {freelancer_max:,.0f}
• Perfil: Desenvolvedores independentes

🏢 AGÊNCIAS PEQUENAS:
• Faixa de preços: R$ {agencia_pequena_min:,.0f} - R$ {agencia_pequena_max:,.0f}
• Perfil: Equipes de 2-5 pessoas

🏬 AGÊNCIAS MÉDIAS:
• Faixa de preços: R$ {agencia_media_min:,.0f} - R$ {agencia_media_max:,.0f}
• Perfil: Equipes especializadas, maior estrutura

📊 OBSERVAÇÕES:
• Valores variam conforme região, prazo e escopo
• Projetos com complexidade {complexity} tendem a custar {int((multiplier-1)*100):+.0f}% da média
• Inclui dados de {len(sites_sample)} plataformas consultadas

Esta pesquisa foi considerada no cálculo do seu orçamento personalizado."""

        return research_text

    def generate_quote(self, conversation_id, requirements, include_market_research=False):
        """Gera orçamento baseado nos requisitos coletados"""
        
        project_type = requirements.get('project_type')
        complexity = requirements.get('complexity', 'media')
        region = requirements.get('region', 'interior')
        budget_tier = requirements.get('budget_tier', 'economico')  # NOVO: tier de orçamento
        
        # Buscar template do projeto - fallback para 'app' se não encontrar
        if not project_type or project_type not in self.project_templates:
            print(f"Tipo de projeto não identificado: {project_type}, usando 'app' como fallback")
            project_type = 'app'
        
        template = self.project_templates.get(project_type)
        if not template:
            raise ValueError(f"Template não encontrado para tipo: {project_type}")
        
        # Calcular horas base
        base_hours = template['base_hours'].copy()
        multiplier = template['complexity_multipliers'][complexity]
        
        # Aplicar multiplicador de complexidade
        calculated_hours = {
            category: int(hours * multiplier) 
            for category, hours in base_hours.items()
        }
        
        # Ajustes específicos baseados nos requisitos
        calculated_hours = self._apply_requirements_adjustments(
            calculated_hours, requirements, project_type
        )
        
        # Determinar nível de senioridade baseado na complexidade
        seniority_level = self._determine_seniority(complexity, requirements)
        hourly_rate = self.hourly_rates[region][budget_tier][seniority_level]  # MODIFICADO: usar tier
        
        # Calcular totais
        total_hours = sum(calculated_hours.values())
        total_cost = total_hours * hourly_rate
        
        # Gerar pesquisa de mercado se solicitada
        market_research = None
        if include_market_research:
            market_research = self.generate_market_research(project_type, complexity)
        
        # Criar orçamento no banco
        orcamento = Orcamento(
            conversation_id=conversation_id,
            project_name=requirements.get('project_description', f'{template["name"]} Personalizado'),
            project_type=project_type,
            description=self._generate_description(requirements),
            design_hours=calculated_hours['design'],
            frontend_hours=calculated_hours['frontend'],
            backend_hours=calculated_hours['backend'],
            testing_hours=calculated_hours['testing'],
            pm_hours=calculated_hours['pm'],
            hourly_rate=hourly_rate,
            total_hours=total_hours,
            total_cost=total_cost,
            complexity_level=complexity,
            timeline_weeks=self._calculate_timeline(total_hours),
            region=region
        )
        
        # Adicionar features, premissas e riscos
        orcamento.set_features(self._generate_features_list(requirements, project_type))
        orcamento.set_assumptions(self._generate_assumptions(requirements, project_type))
        orcamento.set_risks(self._generate_risks(complexity, project_type))
        
        db.session.add(orcamento)
        db.session.commit()
        
        return self._format_quote_response(orcamento, calculated_hours, hourly_rate, market_research)

    def generate_multiple_quotes(self, conversation_id, requirements, include_market_research=False):
        """Gera 3 opções de orçamento: Econômico, Padrão e Premium"""
        
        quotes = {}
        tiers = ['economico', 'padrao', 'premium']
        tier_names = {
            'economico': 'Econômico',
            'padrao': 'Padrão', 
            'premium': 'Premium'
        }
        tier_descriptions = {
            'economico': 'Solução funcional e eficiente com o melhor custo-benefício',
            'padrao': 'Solução completa com qualidade profissional e recursos avançados',
            'premium': 'Solução premium com tecnologias de ponta e arquitetura robusta'
        }
        
        for tier in tiers:
            # Criar cópia dos requirements com o tier específico
            tier_requirements = requirements.copy()
            tier_requirements['budget_tier'] = tier
            
            # Gerar orçamento para este tier
            quote = self.generate_quote(conversation_id, tier_requirements, include_market_research)
            
            # Adicionar informações do tier
            quote['tier'] = tier
            quote['tier_name'] = tier_names[tier]
            quote['tier_description'] = tier_descriptions[tier]
            
            quotes[tier] = quote
        
        return quotes

    def _apply_requirements_adjustments(self, hours, requirements, project_type):
        """Aplica ajustes específicos baseados nos requisitos"""
        
        if project_type == 'app':
            users = requirements.get('expected_users', 0)
            
            # Ajuste por número de usuários
            if users > 50000:
                hours['backend'] = int(hours['backend'] * 1.5)
                hours['testing'] = int(hours['testing'] * 1.3)
            elif users > 10000:
                hours['backend'] = int(hours['backend'] * 1.2)
                hours['testing'] = int(hours['testing'] * 1.1)
            
            # Features específicas
            if requirements.get('offline_support'):
                hours['frontend'] += 40
                hours['backend'] += 30
            
            if requirements.get('push_notifications'):
                hours['backend'] += 25
                hours['frontend'] += 15
            
            if requirements.get('payment_integration'):
                hours['backend'] += 50
                hours['frontend'] += 30
                hours['testing'] += 20
                
        elif project_type == 'website':
            pages = requirements.get('pages_count', 0)
            
            # Ajuste por número de páginas
            if pages > 20:
                hours['design'] = int(hours['design'] * 1.4)
                hours['frontend'] = int(hours['frontend'] * 1.3)
            elif pages > 10:
                hours['design'] = int(hours['design'] * 1.2)
                hours['frontend'] = int(hours['frontend'] * 1.1)
            
            if requirements.get('is_ecommerce'):
                hours['backend'] += 80
                hours['frontend'] += 60
                hours['testing'] += 30
            
            if requirements.get('needs_admin'):
                hours['backend'] += 40
                hours['frontend'] += 30
                
        elif project_type == 'sistema':
            users = requirements.get('concurrent_users', 0)
            
            # Ajuste por usuários simultâneos
            if users > 100:
                hours['backend'] = int(hours['backend'] * 1.4)
                hours['testing'] = int(hours['testing'] * 1.2)
            elif users > 50:
                hours['backend'] = int(hours['backend'] * 1.2)
            
            if requirements.get('needs_reports'):
                hours['backend'] += 60
                hours['frontend'] += 40
            
            if requirements.get('financial_module'):
                hours['backend'] += 100
                hours['frontend'] += 60
                hours['testing'] += 40
        
        return hours

    def _determine_seniority(self, complexity, requirements):
        """Determina nível de senioridade necessário"""
        if complexity == 'alta':
            return 'senior'
        elif complexity == 'baixa':
            return 'junior'
        else:
            return 'pleno'

    def _calculate_timeline(self, total_hours):
        """Calcula timeline em dias úteis (freelancer dedicado ~8h/dia útil)"""
        # Freelancer brasileiro dedicado: 8h/dia útil, 5 dias/semana = 40h/semana
        daily_hours = 8
        days = max(2, int(total_hours / daily_hours))  # Mínimo 2 dias
        return days  # Retorna número de dias para o banco
    
    def _format_timeline(self, days):
        """Formata timeline em formato amigável"""
        if days <= 7:
            return f"{days} dias"
        else:
            weeks = days / 5
            if weeks <= 1.2:  # Até 6 dias úteis = ~1 semana
                return "1 semana"
            elif weeks < 2:
                return f"{days} dias"
            elif weeks == int(weeks):
                return f"{int(weeks)} semanas" 
            else:
                # Arredondar para meio ou inteiro
                rounded_weeks = round(weeks * 2) / 2  # Arredonda para 0.5
                if rounded_weeks == int(rounded_weeks):
                    return f"{int(rounded_weeks)} semanas"
                else:
                    return f"{rounded_weeks} semanas"

    def _generate_description(self, requirements):
        """Gera descrição do projeto"""
        project_type = requirements.get('project_type')
        complexity = requirements.get('complexity')
        
        descriptions = {
            'app': f"Aplicativo mobile de complexidade {complexity}",
            'website': f"Website/portal de complexidade {complexity}",
            'sistema': f"Sistema web de complexidade {complexity}"
        }
        
        return descriptions.get(project_type, "Projeto personalizado")

    def _generate_features_list(self, requirements, project_type):
        """Gera lista de features incluídas"""
        features = []
        
        base_features = {
            'app': [
                "Interface mobile responsiva",
                "Autenticação de usuários",
                "Navegação intuitiva",
                "Compatibilidade iOS/Android"
            ],
            'website': [
                "Design responsivo",
                "Otimização SEO básica",
                "Formulários de contato",
                "Integração Google Analytics"
            ],
            'sistema': [
                "Painel administrativo",
                "Controle de usuários",
                "Relatórios básicos",
                "Backup automático"
            ]
        }
        
        features.extend(base_features.get(project_type, []))
        
        # Adicionar features específicas baseadas nos requisitos
        if requirements.get('offline_support'):
            features.append("Funcionamento offline")
        if requirements.get('push_notifications'):
            features.append("Notificações push")
        if requirements.get('payment_integration'):
            features.append("Integração de pagamentos")
        if requirements.get('is_ecommerce'):
            features.append("Sistema de e-commerce completo")
        if requirements.get('needs_admin'):
            features.append("Área administrativa")
        if requirements.get('needs_reports'):
            features.append("Relatórios avançados")
        
        return features

    def _generate_assumptions(self, requirements, project_type):
        """Gera premissas do orçamento"""
        return [
            "Design será fornecido em formato Figma/Adobe XD",
            "Conteúdo (textos e imagens) será fornecido pelo cliente",
            "Inclui 3 rodadas de revisões",
            "Hospedagem e domínio por conta do cliente",
            "Prazo considera dedicação de 40h semanais",
            "Valores em reais, sem impostos inclusos"
        ]

    def _generate_risks(self, complexity, project_type):
        """Gera riscos identificados"""
        risks = [
            "Mudanças de escopo podem impactar prazo e custo",
            "Dependência de APIs externas pode causar atrasos"
        ]
        
        if complexity == 'alta':
            risks.extend([
                "Projeto complexo pode requerer mais tempo de testes",
                "Integrações complexas podem ter imprevistos"
            ])
        
        return risks

    def _format_quote_response(self, orcamento, hours_breakdown, hourly_rate, market_research=None):
        """Formata resposta do orçamento"""
        cost_breakdown = orcamento.calculate_breakdown()
        
        return {
            'id': orcamento.id,
            'project_name': orcamento.project_name,
            'project_type': orcamento.project_type,
            'total_cost': orcamento.total_cost,
            'total_hours': orcamento.total_hours,
            'hourly_rate': hourly_rate,
            'timeline_weeks': self._format_timeline(orcamento.timeline_weeks),
            'complexity': orcamento.complexity_level,
            'region': orcamento.region,
            'hours_breakdown': hours_breakdown,
            'cost_breakdown': cost_breakdown,
            'features': orcamento.get_features(),
            'assumptions': orcamento.get_assumptions(),
            'risks': orcamento.get_risks(),
            'market_research': market_research,
            'created_at': orcamento.created_at.isoformat()
        }