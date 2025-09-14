from flask import Blueprint, jsonify
from models.orcamento import Orcamento
from models.conversation import Conversation
from sqlalchemy import func
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/stats', methods=['GET'])
def get_dashboard_stats():
    """Estatísticas gerais do sistema"""
    try:
        # Contadores básicos
        total_orcamentos = Orcamento.query.count()
        total_conversas = Conversation.query.count()
        conversas_ativas = Conversation.query.filter_by(status='active').count()
        
        # Valor total dos orçamentos
        total_value = Orcamento.query.with_entities(func.sum(Orcamento.total_cost)).scalar() or 0
        
        # Orçamentos por tipo de projeto
        project_types = Orcamento.query.with_entities(
            Orcamento.project_type,
            func.count(Orcamento.id).label('count')
        ).group_by(Orcamento.project_type).all()
        
        # Orçamentos por complexidade
        complexity_stats = Orcamento.query.with_entities(
            Orcamento.complexity_level,
            func.count(Orcamento.id).label('count'),
            func.avg(Orcamento.total_cost).label('avg_cost')
        ).group_by(Orcamento.complexity_level).all()
        
        # Orçamentos por região
        region_stats = Orcamento.query.with_entities(
            Orcamento.region,
            func.count(Orcamento.id).label('count'),
            func.avg(Orcamento.total_cost).label('avg_cost')
        ).group_by(Orcamento.region).all()
        
        # Últimos 30 dias
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        recent_orcamentos = Orcamento.query.filter(
            Orcamento.created_at >= thirty_days_ago
        ).count()
        
        return jsonify({
            'success': True,
            'stats': {
                'total_orcamentos': total_orcamentos,
                'total_conversas': total_conversas,
                'conversas_ativas': conversas_ativas,
                'total_value': round(total_value, 2),
                'recent_orcamentos': recent_orcamentos,
                'project_types': [
                    {'type': pt.project_type, 'count': pt.count} 
                    for pt in project_types
                ],
                'complexity_stats': [
                    {
                        'level': cs.complexity_level, 
                        'count': cs.count,
                        'avg_cost': round(cs.avg_cost or 0, 2)
                    } 
                    for cs in complexity_stats
                ],
                'region_stats': [
                    {
                        'region': rs.region,
                        'count': rs.count,
                        'avg_cost': round(rs.avg_cost or 0, 2)
                    }
                    for rs in region_stats
                ]
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@dashboard_bp.route('/charts', methods=['GET'])
def get_dashboard_charts():
    """Dados para gráficos do dashboard"""
    try:
        # Gráfico de pizza - Tipos de projeto
        project_types = Orcamento.query.with_entities(
            Orcamento.project_type,
            func.count(Orcamento.id).label('count')
        ).group_by(Orcamento.project_type).all()
        
        pie_chart = {
            'labels': [pt.project_type.title() for pt in project_types],
            'values': [pt.count for pt in project_types]
        }
        
        # Gráfico de barras - Valor médio por complexidade
        complexity_values = Orcamento.query.with_entities(
            Orcamento.complexity_level,
            func.avg(Orcamento.total_cost).label('avg_cost')
        ).group_by(Orcamento.complexity_level).all()
        
        bar_chart = {
            'labels': [cv.complexity_level.title() for cv in complexity_values],
            'values': [round(cv.avg_cost or 0, 2) for cv in complexity_values]
        }
        
        # Timeline - Orçamentos por mês (últimos 6 meses)
        six_months_ago = datetime.utcnow() - timedelta(days=180)
        monthly_data = Orcamento.query.filter(
            Orcamento.created_at >= six_months_ago
        ).with_entities(
            func.date_trunc('month', Orcamento.created_at).label('month'),
            func.count(Orcamento.id).label('count'),
            func.sum(Orcamento.total_cost).label('total_value')
        ).group_by(
            func.date_trunc('month', Orcamento.created_at)
        ).order_by('month').all()
        
        timeline_chart = {
            'labels': [md.month.strftime('%Y-%m') for md in monthly_data],
            'counts': [md.count for md in monthly_data],
            'values': [round(md.total_value or 0, 2) for md in monthly_data]
        }
        
        return jsonify({
            'success': True,
            'charts': {
                'project_types_pie': pie_chart,
                'complexity_bar': bar_chart,
                'monthly_timeline': timeline_chart
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@dashboard_bp.route('/recent', methods=['GET'])
def get_recent_activity():
    """Atividade recente do sistema"""
    try:
        # Últimos 10 orçamentos
        recent_orcamentos = Orcamento.query.order_by(
            Orcamento.created_at.desc()
        ).limit(10).all()
        
        # Últimas 10 conversas
        recent_conversations = Conversation.query.order_by(
            Conversation.updated_at.desc()
        ).limit(10).all()
        
        return jsonify({
            'success': True,
            'recent': {
                'orcamentos': [
                    {
                        'id': o.id,
                        'project_name': o.project_name,
                        'project_type': o.project_type,
                        'total_cost': o.total_cost,
                        'created_at': o.created_at.isoformat()
                    }
                    for o in recent_orcamentos
                ],
                'conversations': [
                    {
                        'id': c.id,
                        'session_id': c.session_id,
                        'project_type': c.project_type,
                        'status': c.status,
                        'updated_at': c.updated_at.isoformat()
                    }
                    for c in recent_conversations
                ]
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500