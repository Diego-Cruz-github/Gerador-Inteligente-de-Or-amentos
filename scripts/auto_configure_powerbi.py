#!/usr/bin/env python3
"""
Auto configuração Power BI para Gerador de Orçamentos
Cria automaticamente connections e templates
"""

import json
import requests
import os
import webbrowser
from datetime import datetime

class PowerBIAutoConfig:
    def __init__(self):
        self.api_base = "http://localhost:5000"
        self.endpoints = {
            "summary": f"{self.api_base}/api/analytics/summary",
            "detailed": f"{self.api_base}/api/analytics/detailed-jobs", 
            "timeseries": f"{self.api_base}/api/analytics/time-series",
            "kpis": f"{self.api_base}/api/analytics/kpis",
            "csv": f"{self.api_base}/api/analytics/export/csv"
        }
        
    def test_api_connection(self):
        """Testa se a API está funcionando"""
        print("🔍 Testando conexão com API...")
        try:
            response = requests.get(f"{self.api_base}/health", timeout=5)
            if response.status_code == 200:
                print("✅ API conectada com sucesso!")
                return True
            else:
                print(f"❌ API retornou status {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao conectar com API: {e}")
            return False
    
    def test_all_endpoints(self):
        """Testa todos os endpoints analytics"""
        print("\n📊 Testando endpoints de analytics...")
        results = {}
        
        for name, url in self.endpoints.items():
            try:
                if name == "csv":
                    response = requests.get(url, timeout=10)
                    success = response.status_code == 200 and "csv" in response.headers.get('content-type', '')
                else:
                    response = requests.get(url, timeout=10)
                    data = response.json()
                    success = response.status_code == 200 and data.get('success', False)
                
                results[name] = success
                status = "✅" if success else "❌"
                print(f"  {status} {name}: {url}")
                
            except Exception as e:
                results[name] = False
                print(f"  ❌ {name}: Erro - {e}")
        
        return results
    
    def generate_powerbi_m_queries(self):
        """Gera queries M para Power BI"""
        print("\n🔧 Gerando queries M para Power BI...")
        
        queries = {
            "Summary_Analytics": f'''let
    Source = Json.Document(Web.Contents("{self.endpoints['summary']}")),
    Summary = Source[summary],
    Distributions = Source[distributions],
    ConvertedToTable = Record.ToTable(Summary),
    RenamedColumns = Table.RenameColumns(ConvertedToTable,{{"Name", "Metric"}, {"Value", "Value"}})
in
    RenamedColumns''',
            
            "Detailed_Jobs": f'''let
    Source = Json.Document(Web.Contents("{self.endpoints['detailed']}")),
    Jobs = Source[jobs],
    ConvertedToTable = Table.FromList(Jobs, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    ExpandedColumn1 = Table.ExpandRecordColumn(ConvertedToTable, "Column1", 
        {{"id", "serviceType", "location", "budgetTier", "urgency", "quote", "isClosed", "createdAt", "closedAt"}})
in
    ExpandedColumn1''',
            
            "Time_Series": f'''let
    Source = Json.Document(Web.Contents("{self.endpoints['timeseries']}")),
    TimeSeries = Source[time_series],
    ConvertedToTable = Table.FromList(TimeSeries, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    ExpandedColumn1 = Table.ExpandRecordColumn(ConvertedToTable, "Column1", 
        {{"date", "jobs_closed", "revenue", "hours"}})
in
    ExpandedColumn1'''
        }
        
        # Salvar queries em arquivo
        queries_file = "powerbi_queries.txt"
        with open(queries_file, 'w', encoding='utf-8') as f:
            f.write("# Power BI M Queries - Gerador de Orçamentos\n")
            f.write(f"# Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for name, query in queries.items():
                f.write(f"## {name}\n")
                f.write(f"```m\n{query.strip()}\n```\n\n")
        
        print(f"✅ Queries salvas em: {queries_file}")
        return queries_file
    
    def generate_powerbi_template_instructions(self):
        """Gera instruções passo a passo para Power BI"""
        instructions = f"""
# 📊 Configuração Automática Power BI - Gerador de Orçamentos

## ⚡ Configuração Rápida

### 1. Abrir Power BI Desktop
- Inicie o Power BI Desktop
- Selecione "Obter Dados" > "Web"

### 2. Configurar Fontes de Dados

#### Fonte 1: Analytics Summary
- URL: `{self.endpoints['summary']}`
- Nome: "Orçamentos_Summary"
- Tipo: JSON
- Atualização: A cada 5 minutos

#### Fonte 2: Detailed Jobs  
- URL: `{self.endpoints['detailed']}`
- Nome: "Orçamentos_Jobs"
- Tipo: JSON
- Atualização: A cada 5 minutos

#### Fonte 3: Time Series
- URL: `{self.endpoints['timeseries']}`
- Nome: "Orçamentos_TimeSeries" 
- Tipo: JSON
- Atualização: A cada 5 minutos

### 3. Configurar Atualizações Automáticas
1. Arquivo > Opções e configurações > Opções
2. CONFIGURAÇÕES ATUAIS > Segurança
3. Marcar "Ignorar níveis de privacidade"
4. Em cada fonte de dados:
   - Botão direito > Atualizar
   - Configurar agenda para 5 minutos

### 4. Criar Visualizações Recomendadas

#### Dashboard Executivo:
- 📊 Cartão: Total Revenue (summary.total_revenue)
- 📈 Cartão: Conversion Rate (summary.conversion_rate) 
- 🥧 Gráfico Rosca: Revenue by Service (distributions.by_service)
- 📊 Gráfico Coluna: Monthly Trend (time_series)

#### Dashboard Operacional:
- 📋 Tabela: All Jobs (jobs)
- 📊 Gráfico Barra: Jobs by Location (distributions.by_location)
- 📈 Gráfico Linha: Daily Performance (time_series)

### 5. URLs de Teste
Teste estes URLs no navegador antes de configurar:

✅ Health Check: {self.api_base}/health
✅ Summary: {self.endpoints['summary']}
✅ CSV Export: {self.endpoints['csv']}

### 6. Solução de Problemas
- Se API não conectar: Verifique se backend está rodando
- Se dados não carregam: Teste URLs manualmente
- Se erro de CORS: Adicione Power BI aos domínios permitidos

---
*Configuração gerada automaticamente em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        instructions_file = "PowerBI_Setup_Guide.md"
        with open(instructions_file, 'w', encoding='utf-8') as f:
            f.write(instructions)
        
        print(f"✅ Guia de configuração salvo em: {instructions_file}")
        return instructions_file

    def open_powerbi_web(self):
        """Abre Power BI Web para configuração online"""
        powerbi_url = "https://app.powerbi.com/"
        print(f"\n🌐 Abrindo Power BI Web: {powerbi_url}")
        webbrowser.open(powerbi_url)
        
    def run_auto_setup(self):
        """Executa configuração automática completa"""
        print("🚀 CONFIGURAÇÃO AUTOMÁTICA POWER BI")
        print("=" * 50)
        
        # 1. Testar API
        if not self.test_api_connection():
            print("\n❌ Não é possível continuar sem API funcionando")
            return False
        
        # 2. Testar endpoints
        endpoint_results = self.test_all_endpoints()
        failed_endpoints = [name for name, success in endpoint_results.items() if not success]
        
        if failed_endpoints:
            print(f"\n⚠️  Alguns endpoints falharam: {failed_endpoints}")
            print("Continuando com endpoints funcionais...")
        
        # 3. Gerar queries
        queries_file = self.generate_powerbi_m_queries()
        
        # 4. Gerar instruções
        guide_file = self.generate_powerbi_template_instructions()
        
        # 5. Abrir arquivos gerados
        print(f"\n📁 Arquivos gerados:")
        print(f"  📄 {queries_file}")
        print(f"  📄 {guide_file}")
        
        # 6. Oferecer abrir Power BI
        response = input("\n🤔 Deseja abrir Power BI Web agora? (s/n): ")
        if response.lower() in ['s', 'sim', 'y', 'yes']:
            self.open_powerbi_web()
        
        print("\n✅ Configuração automática concluída!")
        print("📖 Siga o guia no arquivo PowerBI_Setup_Guide.md")
        
        return True

def main():
    config = PowerBIAutoConfig()
    config.run_auto_setup()

if __name__ == "__main__":
    main()