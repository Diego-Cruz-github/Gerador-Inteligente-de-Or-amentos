# 📊 Guia de Integração BI - Gerador de Orçamentos

## 🚀 Visão Geral
Sistema completo de integração com ferramentas de Business Intelligence implementado com APIs REST estruturadas.

## 📡 Endpoints Disponíveis

### Base URL: `http://localhost:5000/api/analytics`

| Endpoint | Descrição | Uso |
|----------|-----------|-----|
| `/summary` | KPIs principais e métricas resumidas | Dashboards executivos |
| `/time-series` | Dados históricos para gráficos | Análise de tendências |
| `/detailed-jobs` | Lista completa de orçamentos | Análise granular |
| `/kpis` | Indicadores chave executivos | Métricas estratégicas |
| `/export/csv` | Exportação em CSV | Importação em BI tools |
| `/config` | Metadados e esquema da API | Configuração automática |

## 🔧 Como Conectar com Ferramentas BI

### Power BI
1. Abra Power BI Desktop
2. **Obter Dados** → **Web**
3. Cole a URL: `http://localhost:5000/api/analytics/summary`
4. Configure atualização automática para 5 minutos

### Tableau
1. **Conectar** → **Para um Servidor**
2. **Web Data Connector**
3. Insira URL: `http://localhost:5000/api/analytics/summary`
4. Configure refresh automático

### Google Data Studio
1. **Criar** → **Fonte de dados**
2. **Conector** → **URL file**
3. Use endpoint CSV: `http://localhost:5000/api/analytics/export/csv`
4. Conectar e criar relatório

## 📊 Dados Disponíveis

### Métricas Principais
- **Total de Orçamentos**: Quantidade total gerada
- **Trabalhos Fechados**: Orçamentos convertidos em trabalhos
- **Taxa de Conversão**: % de orçamentos que viraram trabalhos
- **Receita Total**: Soma dos valores de trabalhos fechados
- **Ticket Médio**: Valor médio por projeto
- **Valor/Hora Médio**: Taxa horária média

### Dimensões de Análise
- **Por Tipo de Serviço**: Website, E-commerce, App, Sistema, Landing Page
- **Por Localização**: Capital, Interior, Remoto
- **Por Faixa Orçamentária**: Econômico, Padrão, Premium, Enterprise
- **Por Urgência**: Normal, Urgente, Super Urgente
- **Temporal**: Por dia, semana, mês, ano

### Campos Detalhados
```json
{
  "id": "string",
  "serviceType": "enum[website,ecommerce,app,sistema,landing,blog]",
  "location": "enum[SP,interior,remoto]", 
  "budgetTier": "enum[economico,padrao,premium,enterprise]",
  "urgency": "enum[normal,urgent,super_urgent]",
  "total_cost": "number",
  "total_hours": "number",
  "hourly_rate": "number",
  "isClosed": "boolean",
  "createdAt": "datetime",
  "closedAt": "datetime",
  "days_to_close": "number",
  "roi_percentage": "number"
}
```

## 🔄 Atualização de Dados

- **Frequência Recomendada**: 5 minutos
- **Método**: HTTP GET requests
- **Formato**: JSON (maioria) ou CSV (exportação)
- **Autenticação**: Não requerida (desenvolvimento)

## 🎯 Casos de Uso

### Dashboard Executivo
- KPIs principais em tempo real
- Tendências de receita
- Performance por período

### Análise Operacional  
- Tempo médio de fechamento
- Taxa de conversão por tipo
- Produtividade por localização

### Análise Financeira
- ROI por projeto
- Receita por categoria
- Previsão de faturamento

## 🔍 Exemplos de Queries

### Power BI (M Language)
```m
let
    Source = Json.Document(Web.Contents("http://localhost:5000/api/analytics/summary")),
    Summary = Source[summary]
in
    Summary
```

### Excel/Power Query
```
Data > Get Data > From Web
URL: http://localhost:5000/api/analytics/summary
```

## 📱 Interface Web

Acesse a página de configuração BI em:
`http://localhost:3000/bi-integration`

### Funcionalidades:
- ✅ Status da API em tempo real
- 🔗 Teste de endpoints  
- 📋 URLs para copiar
- 👁️ Preview dos dados
- 📚 Guias de integração
- 📥 Download de templates

## 🚨 Troubleshooting

### API não conecta
1. Verifique se backend está rodando na porta 5000
2. Teste `http://localhost:5000/health`
3. Verifique CORS se acessando de outro domínio

### Dados não atualizando
1. Verifique conexão de rede
2. Confirme refresh rate do BI tool
3. Teste endpoint manualmente

### Erro de formato
1. Valide JSON response
2. Verifique schema de dados
3. Confirme tipo de dados esperados

## 🔮 Próximos Passos

- [ ] Autenticação via API Key
- [ ] Filtros por data via query params
- [ ] Webhooks para push de dados
- [ ] Templates pré-configurados para BI tools
- [ ] Métricas de performance da API
- [ ] Cache inteligente de dados

## 📞 Suporte

Para questões técnicas ou solicitações de novas métricas, acesse a página de configuração BI no sistema.

---
*Made by Diego Fonte - https://www.diegofontedev.com.br*