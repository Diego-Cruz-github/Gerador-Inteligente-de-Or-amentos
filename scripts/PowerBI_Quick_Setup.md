# Power BI - Configuração Automática

## 🚀 URLs Prontas para Usar

### Endpoints da API:
- Summary: http://localhost:5000/api/analytics/summary
- Dados Detalhados: http://localhost:5000/api/analytics/detailed-jobs
- Série Temporal: http://localhost:5000/api/analytics/time-series
- KPIs: http://localhost:5000/api/analytics/kpis
- CSV Export: http://localhost:5000/api/analytics/export/csv

## 📋 Passos no Power BI:

### 1. Obter Dados
1. Abra Power BI Desktop
2. Clique em "Obter Dados"
3. Selecione "Web"
4. Cole uma das URLs acima

### 2. Configurar Fonte Principal (Recomendado)
- URL: http://localhost:5000/api/analytics/summary
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
- Use: http://localhost:5000/api/analytics/export/csv
- Tipo: CSV via URL

## 🔧 Para Tableau:
- Web Data Connector
- URL: http://localhost:5000/api/analytics/summary

---
Gerado em: 2025-09-16 17:17:58
