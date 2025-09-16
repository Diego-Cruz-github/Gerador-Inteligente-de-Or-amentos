#!/usr/bin/env python3
"""
Configuração Simples BI - Gerador de Orçamentos
"""

import json
import requests
import webbrowser
from datetime import datetime

# Configurações
API_BASE = "http://localhost:5000"
FRONTEND_URL = "http://localhost:3000"

def test_api():
    """Testa conexão com API"""
    print("Testando API...")
    try:
        response = requests.get(f"{API_BASE}/health", timeout=5)
        if response.status_code == 200:
            print("OK: API funcionando!")
            return True
        else:
            print(f"ERRO: API retornou {response.status_code}")
            return False
    except Exception as e:
        print(f"ERRO: {e}")
        return False

def test_endpoints():
    """Testa endpoints de analytics"""
    print("\nTestando endpoints...")
    
    endpoints = {
        "Summary": f"{API_BASE}/api/analytics/summary",
        "Detailed": f"{API_BASE}/api/analytics/detailed-jobs", 
        "Time Series": f"{API_BASE}/api/analytics/time-series",
        "KPIs": f"{API_BASE}/api/analytics/kpis",
        "CSV": f"{API_BASE}/api/analytics/export/csv"
    }
    
    for name, url in endpoints.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"OK {name}: {url}")
            else:
                print(f"ERRO {name}: Status {response.status_code}")
        except Exception as e:
            print(f"ERRO {name}: {e}")

def create_powerbi_guide():
    """Cria guia para Power BI"""
    print("\nCriando guia Power BI...")
    
    guide = f"""# Power BI - Configuração Automática

## 🚀 URLs Prontas para Usar

### Endpoints da API:
- Summary: {API_BASE}/api/analytics/summary
- Dados Detalhados: {API_BASE}/api/analytics/detailed-jobs
- Série Temporal: {API_BASE}/api/analytics/time-series
- KPIs: {API_BASE}/api/analytics/kpis
- CSV Export: {API_BASE}/api/analytics/export/csv

## 📋 Passos no Power BI:

### 1. Obter Dados
1. Abra Power BI Desktop
2. Clique em "Obter Dados"
3. Selecione "Web"
4. Cole uma das URLs acima

### 2. Configurar Fonte Principal (Recomendado)
- URL: {API_BASE}/api/analytics/summary
- Nome: "Orçamentos_Analytics"

### 3. Configurar Atualização
1. Arquivo → Opções → Segurança
2. Marcar "Ignorar níveis de privacidade"
3. Configurar atualização a cada 5 minutos

### 4. Visualizações Sugeridas
- 📊 Cartão: Total Revenue
- 📈 Cartão: Conversion Rate  
- 🥧 Gráfico Pizza: Revenue by Service
- 📊 Gráfico Coluna: Monthly Trend

## 🔧 Para Google Data Studio:
- Use: {API_BASE}/api/analytics/export/csv
- Tipo: CSV via URL

## 🔧 Para Tableau:
- Web Data Connector
- URL: {API_BASE}/api/analytics/summary

---
Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    with open("PowerBI_Quick_Setup.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    print("OK: Guia salvo em PowerBI_Quick_Setup.md")

def create_urls_file():
    """Cria arquivo com URLs para copiar"""
    print("\nCriando arquivo de URLs...")
    
    urls = f"""# URLs para Business Intelligence

## Power BI / Tableau
{API_BASE}/api/analytics/summary
{API_BASE}/api/analytics/detailed-jobs
{API_BASE}/api/analytics/time-series

## Google Data Studio (CSV)
{API_BASE}/api/analytics/export/csv

## Teste de Saude
{API_BASE}/health

## Interface Web
{FRONTEND_URL}/bi-integration
"""
    
    with open("BI_URLs.txt", "w", encoding="utf-8") as f:
        f.write(urls)
    
    print("OK: URLs salvas em BI_URLs.txt")

def open_browser_links():
    """Abre links úteis no navegador"""
    print("\nAbrindo links no navegador...")
    
    # Interface BI local
    webbrowser.open(f"{FRONTEND_URL}/bi-integration")
    
    # Power BI Web (opcional)
    response = input("Abrir Power BI Web também? (s/n): ")
    if response.lower() in ['s', 'sim', 'y', 'yes']:
        webbrowser.open("https://app.powerbi.com/")

def main():
    print("CONFIGURACAO AUTOMATICA BI")
    print("=" * 40)
    
    # 1. Testar API
    if not test_api():
        print("\nERRO: API nao esta funcionando. Verifique se o backend esta rodando.")
        return
    
    # 2. Testar endpoints
    test_endpoints()
    
    # 3. Criar arquivos de configuração
    create_powerbi_guide()
    create_urls_file()
    
    # 4. Abrir navegador
    open_browser_links()
    
    print("\nCONFIGURACAO CONCLUIDA!")
    print("\nArquivos criados:")
    print("  PowerBI_Quick_Setup.md - Guia completo")
    print("  BI_URLs.txt - URLs para copiar")
    print("\nProximos passos:")
    print("  1. Abra Power BI Desktop")
    print("  2. Use as URLs do arquivo BI_URLs.txt")
    print("  3. Siga o guia PowerBI_Quick_Setup.md")

if __name__ == "__main__":
    main()