#!/usr/bin/env python3
"""
Script para criar dashboard automático no Power BI
Gera instruções específicas com base nos dados atuais
"""

import json
import requests
from datetime import datetime

def get_current_data():
    """Busca dados atuais da API"""
    try:
        response = requests.get("http://localhost:5000/api/analytics/summary")
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def create_powerbi_instructions():
    """Cria instruções específicas para criar dashboard"""
    
    print("=" * 60)
    print("🎯 CRIANDO DASHBOARD AUTOMÁTICO POWER BI")
    print("=" * 60)
    
    # Buscar dados atuais
    data = get_current_data()
    if not data:
        print("❌ Erro: API não está funcionando")
        return
    
    summary = data.get('summary', {})
    distributions = data.get('distributions', {})
    
    print("\n📊 DADOS ENCONTRADOS:")
    print(f"   • Receita Total: R$ {summary.get('total_revenue', 0):,}")
    print(f"   • Taxa Conversão: {summary.get('conversion_rate', 0)}%")
    print(f"   • Trabalhos Fechados: {summary.get('total_closed_jobs', 0)}")
    print(f"   • Ticket Médio: R$ {summary.get('avg_project_value', 0):,}")
    
    print("\n" + "=" * 60)
    print("🚀 INSTRUÇÕES PARA CRIAR DASHBOARD AUTOMÁTICO")
    print("=" * 60)
    
    print("\n1. PRIMEIRO: Clique em 'Fechar e Aplicar' no Power Query")
    print("   (Para sair do editor e voltar para tela principal)")
    
    print("\n2. DEPOIS: Vou te dar comandos específicos para cada gráfico")
    
    # Instruções específicas baseadas nos dados
    print("\n" + "-" * 50)
    print("📈 GRÁFICO 1: CARTÃO RECEITA TOTAL")
    print("-" * 50)
    print("• Na área 'Campos' (direita), procure: 'summary.total_revenue'")
    print("• ARRASTE para o canvas (área central)")
    print("• Power BI criará um número grande automaticamente")
    print("• Clique no gráfico → Painel 'Visualizações' → Ícone 'Cartão'")
    print(f"• Deve mostrar: R$ {summary.get('total_revenue', 0):,}")
    
    print("\n" + "-" * 50)
    print("📊 GRÁFICO 2: CARTÃO TAXA CONVERSÃO")
    print("-" * 50)
    print("• Procure: 'summary.conversion_rate'")
    print("• ARRASTE para o canvas (ao lado do primeiro)")
    print("• Mude para 'Cartão' se necessário")
    print(f"• Deve mostrar: {summary.get('conversion_rate', 0)}%")
    
    print("\n" + "-" * 50)
    print("🎯 GRÁFICO 3: CARTÃO TRABALHOS FECHADOS")
    print("-" * 50)
    print("• Procure: 'summary.total_closed_jobs'")
    print("• ARRASTE para o canvas")
    print("• Mude para 'Cartão'")
    print(f"• Deve mostrar: {summary.get('total_closed_jobs', 0)}")
    
    print("\n" + "-" * 50)
    print("💰 GRÁFICO 4: CARTÃO TICKET MÉDIO")
    print("-" * 50)
    print("• Procure: 'summary.avg_project_value'")
    print("• ARRASTE para o canvas")
    print("• Mude para 'Cartão'")
    print(f"• Deve mostrar: R$ {summary.get('avg_project_value', 0):,}")
    
    # Gráficos mais complexos
    print("\n" + "-" * 50)
    print("🥧 GRÁFICO 5: PIZZA - RECEITA POR SERVIÇO")
    print("-" * 50)
    print("• Clique em área vazia do canvas")
    print("• No painel 'Visualizações' → Clique no ícone 'Gráfico de Pizza'")
    print("• ARRASTE campos das distribuições by_service para:")
    print("  - Legenda: tipos de serviço")
    print("  - Valores: valores de receita")
    
    if 'by_service' in distributions:
        services = distributions['by_service']
        print("• Dados que aparecerão:")
        for service, data in services.items():
            print(f"  - {service}: R$ {data.get('revenue', 0):,}")
    
    print("\n" + "-" * 50)
    print("📊 GRÁFICO 6: COLUNAS - RECEITA POR LOCALIZAÇÃO")
    print("-" * 50)
    print("• Clique em área vazia")
    print("• Selecione 'Gráfico de Colunas Agrupadas'")
    print("• ARRASTE campos das distribuições by_location")
    
    if 'by_location' in distributions:
        locations = distributions['by_location']
        print("• Dados que aparecerão:")
        for location, data in locations.items():
            location_name = {'SP': 'Capital', 'interior': 'Interior', 'remoto': 'Remoto'}.get(location, location)
            print(f"  - {location_name}: R$ {data.get('revenue', 0):,}")
    
    print("\n" + "=" * 60)
    print("✅ RESULTADO FINAL:")
    print("=" * 60)
    print("Você terá um dashboard com:")
    print("• 4 cartões com KPIs principais")
    print("• 1 gráfico pizza com receita por serviço")
    print("• 1 gráfico colunas com receita por localização")
    print("• Dados atualizados em tempo real")
    
    print("\n🎯 DICA: Comece pelos cartões (mais fácil)")
    print("📞 ME CHAME se tiver dúvida em qualquer passo!")
    
    # Salvar instruções em arquivo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"PowerBI_Instructions_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("INSTRUÇÕES DASHBOARD POWER BI\n")
        f.write("=" * 50 + "\n\n")
        f.write("URL dos dados: http://localhost:5000/api/analytics/summary\n\n")
        f.write("CAMPOS PRINCIPAIS:\n")
        f.write("• summary.total_revenue (Receita Total)\n")
        f.write("• summary.conversion_rate (Taxa Conversão)\n")
        f.write("• summary.total_closed_jobs (Trabalhos Fechados)\n")
        f.write("• summary.avg_project_value (Ticket Médio)\n\n")
        f.write("DISTRIBUIÇÕES:\n")
        f.write("• distributions.by_service (Por Serviço)\n")
        f.write("• distributions.by_location (Por Localização)\n")
        f.write("• distributions.by_budget (Por Faixa Orçamento)\n")
    
    print(f"\n📄 Instruções salvas em: {filename}")

if __name__ == "__main__":
    create_powerbi_instructions()