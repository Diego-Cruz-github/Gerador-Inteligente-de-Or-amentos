import json
from datetime import datetime
from models.orcamento import Orcamento
from models.projeto_template import ProjetoTemplate
from extensions import db

class PricingService:
    def __init__(self):
        # Dados de mercado brasileiros (Set/2024)
        self.hourly_rates = {
            'SP': {'junior': 60, 'pleno': 90, 'senior': 130},
            'interior': {'junior': 45, 'pleno': 70, 'senior': 100},
            'remoto': {'junior': 50, 'pleno': 80, 'senior': 115}
        }
        
        # Templates base de projetos
        self.project_templates = {
            'app': {
                'name': 'Aplicativo Mobile',
                'base_hours': {
                    'design': 80,
                    'frontend': 120,
                    'backend': 100,
                    'testing': 40,
                    'pm': 60
                },
                'complexity_multipliers': {
                    'baixa': 0.7,
                    'media': 1.0,
                    'alta': 1.6
                }
            },
            'website': {
                'name': 'Website/Portal',
                'base_hours': {
                    'design': 60,
                    'frontend': 80,
                    'backend': 60,
                    'testing': 30,
                    'pm': 40
                },
                'complexity_multipliers': {
                    'baixa': 0.6,
                    'media': 1.0,
                    'alta': 1.4
                }
            },
            'sistema': {
                'name': 'Sistema Web',
                'base_hours': {
                    'design': 100,
                    'frontend': 160,
                    'backend': 200,
                    'testing': 80,
                    'pm': 100
                },
                'complexity_multipliers': {
                    'baixa': 0.8,
                    'media': 1.0,
                    'alta': 1.8
                }
            }
        }

    def generate_quote(self, conversation_id, requirements):
        """Gera orçamento baseado nos requisitos coletados"""
        
        project_type = requirements.get('project_type')
        complexity = requirements.get('complexity', 'media')
        region = requirements.get('region', 'interior')
        
        # Buscar template do projeto
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
        hourly_rate = self.hourly_rates[region][seniority_level]
        
        # Calcular totais
        total_hours = sum(calculated_hours.values())
        total_cost = total_hours * hourly_rate
        
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
        
        return self._format_quote_response(orcamento, calculated_hours, hourly_rate)

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
        """Calcula timeline em semanas (assumindo 40h/semana)"""
        return max(4, int(total_hours / 40) + 2)  # Mínimo 4 semanas

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

    def _format_quote_response(self, orcamento, hours_breakdown, hourly_rate):
        """Formata resposta do orçamento"""
        cost_breakdown = orcamento.calculate_breakdown()
        
        return {
            'id': orcamento.id,
            'project_name': orcamento.project_name,
            'project_type': orcamento.project_type,
            'total_cost': orcamento.total_cost,
            'total_hours': orcamento.total_hours,
            'hourly_rate': hourly_rate,
            'timeline_weeks': orcamento.timeline_weeks,
            'complexity': orcamento.complexity_level,
            'region': orcamento.region,
            'hours_breakdown': hours_breakdown,
            'cost_breakdown': cost_breakdown,
            'features': orcamento.get_features(),
            'assumptions': orcamento.get_assumptions(),
            'risks': orcamento.get_risks(),
            'created_at': orcamento.created_at.isoformat()
        }