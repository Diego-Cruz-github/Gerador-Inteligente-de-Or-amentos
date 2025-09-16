from flask import Blueprint, jsonify, request, session
from datetime import datetime, timedelta
import json
import os

analytics_bp = Blueprint('analytics', __name__)

# Armazenar dados em memória (em produção seria banco de dados)
_cached_data = []
_last_update = None

# Função para buscar dados reais do localStorage via API ou usar dados de exemplo
@analytics_bp.route('/update-data', methods=['POST'])
def update_data():
    """Endpoint para receber dados atualizados do frontend"""
    global _cached_data, _last_update
    try:
        data = request.get_json()
        if data and 'quotes' in data:
            _cached_data = data['quotes']
            _last_update = datetime.now()
            return jsonify({'success': True, 'message': 'Dados atualizados com sucesso'})
        else:
            return jsonify({'success': False, 'error': 'Dados inválidos'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

def get_current_data():
    """Retorna dados atuais (cache ou exemplos)"""
    global _cached_data
    
    # Se tem dados em cache e não são muito antigos, use-os (incluindo arrays vazios)
    if _cached_data is not None and _last_update and (datetime.now() - _last_update).seconds < 3600:
        return _cached_data
    
    # Caso contrário, retorna dados de exemplo
    return [
        {
            "id": "1",
            "serviceType": "website",
            "location": "SP",
            "budgetTier": "premium",
            "urgency": "normal",
            "description": "Website institucional para empresa de consultoria",
            "quote": {
                "total_cost": 8500,
                "total_hours": 85,
                "timeline_weeks": "6-8 semanas",
                "hourly_rate": 100
            },
            "isClosed": True,
            "closedAt": "2024-01-15T10:30:00Z",
            "createdAt": "2024-01-10T14:20:00Z"
        },
        {
            "id": "2",
            "serviceType": "ecommerce",
            "location": "remoto",
            "budgetTier": "enterprise",
            "urgency": "urgent",
            "description": "Loja virtual completa com integração de pagamentos",
            "quote": {
                "total_cost": 15000,
                "total_hours": 120,
                "timeline_weeks": "8-10 semanas",
                "hourly_rate": 125
            },
            "isClosed": True,
            "closedAt": "2024-01-20T16:45:00Z",
            "createdAt": "2024-01-12T09:15:00Z"
        },
        {
            "id": "3",
            "serviceType": "app",
            "location": "interior",
            "budgetTier": "padrao",
            "urgency": "normal",
            "description": "App móvel para delivery de comida",
            "quote": {
                "total_cost": 12000,
                "total_hours": 96,
                "timeline_weeks": "10-12 semanas",
                "hourly_rate": 125
            },
            "isClosed": False,
            "closedAt": None,
            "createdAt": "2024-01-18T11:30:00Z"
        },
        {
            "id": "4",
            "serviceType": "sistema",
            "location": "SP",
            "budgetTier": "premium",
            "urgency": "super_urgent",
            "description": "Sistema de gestão de estoque",
            "quote": {
                "total_cost": 20000,
                "total_hours": 160,
                "timeline_weeks": "12-14 semanas",
                "hourly_rate": 125
            },
            "isClosed": True,
            "closedAt": "2024-02-01T08:20:00Z",
            "createdAt": "2024-01-25T13:45:00Z"
        },
        {
            "id": "5",
            "serviceType": "landing",
            "location": "remoto",
            "budgetTier": "economico",
            "urgency": "normal",
            "description": "Landing page para campanha de marketing",
            "quote": {
                "total_cost": 2500,
                "total_hours": 25,
                "timeline_weeks": "2-3 semanas",
                "hourly_rate": 100
            },
            "isClosed": True,
            "closedAt": "2024-02-05T14:15:00Z",
            "createdAt": "2024-01-30T16:20:00Z"
        }
    ]

@analytics_bp.route('/summary', methods=['GET'])
def get_analytics_summary():
    """Endpoint principal para dashboards BI - Resumo geral"""
    try:
        data = get_current_data()
        closed_jobs = [job for job in data if job.get('isClosed', False)]
        
        # Métricas principais
        total_quotes = len(data)
        total_closed = len(closed_jobs)
        conversion_rate = (total_closed / total_quotes * 100) if total_quotes > 0 else 0
        
        total_revenue = sum(job['quote']['total_cost'] for job in closed_jobs)
        total_hours = sum(job['quote']['total_hours'] for job in closed_jobs)
        avg_hourly_rate = total_revenue / total_hours if total_hours > 0 else 0
        avg_project_value = total_revenue / total_closed if total_closed > 0 else 0
        
        # Distribuição por tipo de serviço
        service_distribution = {}
        for job in closed_jobs:
            service = job.get('serviceType', 'unknown')
            if service not in service_distribution:
                service_distribution[service] = {'count': 0, 'revenue': 0}
            service_distribution[service]['count'] += 1
            service_distribution[service]['revenue'] += job['quote']['total_cost']
        
        # Distribuição por localização
        location_distribution = {}
        for job in closed_jobs:
            location = job.get('location', 'unknown')
            if location not in location_distribution:
                location_distribution[location] = {'count': 0, 'revenue': 0}
            location_distribution[location]['count'] += 1
            location_distribution[location]['revenue'] += job['quote']['total_cost']
        
        # Distribuição por faixa de orçamento
        budget_distribution = {}
        for job in closed_jobs:
            budget = job.get('budgetTier', 'unknown')
            if budget not in budget_distribution:
                budget_distribution[budget] = {'count': 0, 'revenue': 0}
            budget_distribution[budget]['count'] += 1
            budget_distribution[budget]['revenue'] += job['quote']['total_cost']
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_quotes': total_quotes,
                'total_closed_jobs': total_closed,
                'conversion_rate': round(conversion_rate, 2),
                'total_revenue': total_revenue,
                'total_hours': total_hours,
                'avg_hourly_rate': round(avg_hourly_rate, 2),
                'avg_project_value': round(avg_project_value, 2)
            },
            'distributions': {
                'by_service': service_distribution,
                'by_location': location_distribution,
                'by_budget': budget_distribution
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@analytics_bp.route('/time-series', methods=['GET'])
def get_time_series_data():
    """Dados de série temporal para gráficos de tendência"""
    try:
        data = get_current_data()
        closed_jobs = [job for job in data if job.get('isClosed', False)]
        
        # Agrupar por data de fechamento
        daily_data = {}
        for job in closed_jobs:
            if job.get('closedAt'):
                date = job['closedAt'][:10]  # YYYY-MM-DD
                if date not in daily_data:
                    daily_data[date] = {
                        'date': date,
                        'jobs_closed': 0,
                        'revenue': 0,
                        'hours': 0
                    }
                daily_data[date]['jobs_closed'] += 1
                daily_data[date]['revenue'] += job['quote']['total_cost']
                daily_data[date]['hours'] += job['quote']['total_hours']
        
        # Converter para lista ordenada
        time_series = sorted(daily_data.values(), key=lambda x: x['date'])
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'time_series': time_series
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@analytics_bp.route('/detailed-jobs', methods=['GET'])
def get_detailed_jobs():
    """Lista detalhada de todos os trabalhos para análise granular"""
    try:
        data = get_current_data()
        
        # Adicionar campos calculados
        for job in data:
            if job.get('createdAt') and job.get('closedAt'):
                created = datetime.fromisoformat(job['createdAt'].replace('Z', '+00:00'))
                closed = datetime.fromisoformat(job['closedAt'].replace('Z', '+00:00'))
                job['days_to_close'] = (closed - created).days
            else:
                job['days_to_close'] = None
                
            # ROI calculado baseado em custo base de R$ 50/hora
            base_cost = job['quote']['total_hours'] * 50
            job['roi_percentage'] = ((job['quote']['total_cost'] - base_cost) / base_cost * 100) if base_cost > 0 else 0
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'total_records': len(data),
            'jobs': data
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@analytics_bp.route('/kpis', methods=['GET'])
def get_kpis():
    """KPIs principais para dashboards executivos"""
    try:
        data = get_current_data()
        closed_jobs = [job for job in data if job.get('isClosed', False)]
        
        # Calcular KPIs
        current_month = datetime.now().month
        current_year = datetime.now().year
        
        monthly_jobs = [
            job for job in closed_jobs 
            if job.get('closedAt') and 
            datetime.fromisoformat(job['closedAt'].replace('Z', '+00:00')).month == current_month and
            datetime.fromisoformat(job['closedAt'].replace('Z', '+00:00')).year == current_year
        ]
        
        monthly_revenue = sum(job['quote']['total_cost'] for job in monthly_jobs)
        
        # Tempo médio de fechamento
        avg_days_to_close = 0
        valid_jobs = [job for job in closed_jobs if job.get('days_to_close')]
        if valid_jobs:
            avg_days_to_close = sum(job.get('days_to_close', 0) for job in valid_jobs) / len(valid_jobs)
        
        # Projeto mais lucrativo
        most_profitable = max(closed_jobs, key=lambda x: x['quote']['total_cost']) if closed_jobs else None
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'kpis': {
                'monthly_revenue': monthly_revenue,
                'monthly_jobs': len(monthly_jobs),
                'avg_days_to_close': round(avg_days_to_close, 1),
                'total_pipeline_value': sum(job['quote']['total_cost'] for job in data if not job.get('isClosed')),
                'most_profitable_project': {
                    'service': most_profitable.get('serviceType') if most_profitable else None,
                    'value': most_profitable['quote']['total_cost'] if most_profitable else 0
                }
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@analytics_bp.route('/export/csv', methods=['GET'])
def export_csv():
    """Exportação em CSV para ferramentas de BI"""
    try:
        import csv
        import io
        
        data = get_current_data()
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Cabeçalhos
        headers = [
            'id', 'service_type', 'location', 'budget_tier', 'urgency',
            'total_cost', 'total_hours', 'hourly_rate', 'timeline_weeks',
            'is_closed', 'created_at', 'closed_at', 'description'
        ]
        writer.writerow(headers)
        
        # Dados
        for job in data:
            writer.writerow([
                job.get('id'),
                job.get('serviceType'),
                job.get('location'),
                job.get('budgetTier'),
                job.get('urgency'),
                job['quote']['total_cost'],
                job['quote']['total_hours'],
                job['quote']['hourly_rate'],
                job['quote']['timeline_weeks'],
                job.get('isClosed', False),
                job.get('createdAt'),
                job.get('closedAt'),
                job.get('description', '').replace('\n', ' ')
            ])
        
        csv_content = output.getvalue()
        output.close()
        
        return csv_content, 200, {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=orcamentos_data.csv'
        }
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@analytics_bp.route('/config', methods=['GET'])
def get_bi_config():
    """Configurações e metadados para ferramentas de BI"""
    return jsonify({
        'success': True,
        'api_version': '1.0.0',
        'endpoints': {
            'summary': '/api/analytics/summary',
            'time_series': '/api/analytics/time-series',
            'detailed_jobs': '/api/analytics/detailed-jobs',
            'kpis': '/api/analytics/kpis',
            'csv_export': '/api/analytics/export/csv'
        },
        'data_schema': {
            'job': {
                'id': 'string',
                'serviceType': 'enum[website,ecommerce,app,sistema,landing,blog]',
                'location': 'enum[SP,interior,remoto]',
                'budgetTier': 'enum[economico,padrao,premium,enterprise]',
                'urgency': 'enum[normal,urgent,super_urgent]',
                'total_cost': 'number',
                'total_hours': 'number',
                'hourly_rate': 'number',
                'isClosed': 'boolean',
                'createdAt': 'datetime',
                'closedAt': 'datetime'
            }
        },
        'refresh_rate': '5 minutes',
        'authentication': 'none'
    })