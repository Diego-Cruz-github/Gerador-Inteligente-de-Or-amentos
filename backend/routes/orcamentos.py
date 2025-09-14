from flask import Blueprint, request, jsonify
from models.orcamento import Orcamento, orcamento_schema, orcamentos_schema
from services.pdf_service import PDFService

orcamentos_bp = Blueprint('orcamentos', __name__)
pdf_service = PDFService()

@orcamentos_bp.route('/', methods=['GET'])
def list_orcamentos():
    """Lista todos os orçamentos"""
    try:
        orcamentos = Orcamento.query.order_by(Orcamento.created_at.desc()).all()
        return jsonify({
            'success': True,
            'orcamentos': orcamentos_schema.dump(orcamentos)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@orcamentos_bp.route('/<int:orcamento_id>', methods=['GET'])
def get_orcamento(orcamento_id):
    """Busca orçamento específico"""
    try:
        orcamento = Orcamento.query.get(orcamento_id)
        
        if not orcamento:
            return jsonify({'success': False, 'error': 'Orçamento não encontrado'}), 404
        
        # Formatar dados completos
        data = orcamento_schema.dump(orcamento)
        data['hours_breakdown'] = {
            'design': orcamento.design_hours,
            'frontend': orcamento.frontend_hours,
            'backend': orcamento.backend_hours,
            'testing': orcamento.testing_hours,
            'pm': orcamento.pm_hours
        }
        data['cost_breakdown'] = orcamento.calculate_breakdown()
        data['features'] = orcamento.get_features()
        data['assumptions'] = orcamento.get_assumptions()
        data['risks'] = orcamento.get_risks()
        
        return jsonify({
            'success': True,
            'orcamento': data
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@orcamentos_bp.route('/<int:orcamento_id>/pdf', methods=['GET'])
def generate_pdf(orcamento_id):
    """Gera PDF do orçamento"""
    try:
        orcamento = Orcamento.query.get(orcamento_id)
        
        if not orcamento:
            return jsonify({'success': False, 'error': 'Orçamento não encontrado'}), 404
        
        pdf_path = pdf_service.generate_quote_pdf(orcamento)
        
        return jsonify({
            'success': True,
            'pdf_url': f'/static/pdfs/{pdf_path}',
            'message': 'PDF gerado com sucesso'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@orcamentos_bp.route('/<int:orcamento_id>/charts', methods=['GET'])
def get_charts_data(orcamento_id):
    """Retorna dados para gráficos do orçamento"""
    try:
        orcamento = Orcamento.query.get(orcamento_id)
        
        if not orcamento:
            return jsonify({'success': False, 'error': 'Orçamento não encontrado'}), 404
        
        # Dados para gráfico de pizza (breakdown de custos)
        cost_breakdown = orcamento.calculate_breakdown()
        pie_data = {
            'labels': ['Design', 'Frontend', 'Backend', 'Testes', 'Gerenciamento'],
            'values': [
                cost_breakdown['design'],
                cost_breakdown['frontend'], 
                cost_breakdown['backend'],
                cost_breakdown['testing'],
                cost_breakdown['pm']
            ]
        }
        
        # Dados para gráfico de barras (horas por categoria)
        bar_data = {
            'labels': ['Design', 'Frontend', 'Backend', 'Testes', 'Gerenciamento'],
            'values': [
                orcamento.design_hours,
                orcamento.frontend_hours,
                orcamento.backend_hours,
                orcamento.testing_hours,
                orcamento.pm_hours
            ]
        }
        
        # Timeline do projeto
        timeline_data = {
            'phases': [
                {'name': 'Design', 'duration': round(orcamento.design_hours / 40, 1)},
                {'name': 'Frontend', 'duration': round(orcamento.frontend_hours / 40, 1)},
                {'name': 'Backend', 'duration': round(orcamento.backend_hours / 40, 1)},
                {'name': 'Testes', 'duration': round(orcamento.testing_hours / 40, 1)},
                {'name': 'Finalização', 'duration': round(orcamento.pm_hours / 40, 1)}
            ]
        }
        
        return jsonify({
            'success': True,
            'charts': {
                'cost_breakdown': pie_data,
                'hours_breakdown': bar_data,
                'timeline': timeline_data
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500