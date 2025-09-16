# 📊 Guia de Integração Tableau - Gerador de Orçamentos

## 🚀 Conector Web Data Connector (WDC) Criado!

### 📡 **URL do Conector:**
```
http://localhost:3000/tableau/orcamentos_wdc.html
```

## 🔧 **Como Usar no Tableau:**

### **Opção 1: Tableau Desktop**
1. **Abra Tableau Desktop**
2. **Conectar** → **Para um Servidor**
3. **Web Data Connector**
4. **Cole a URL**: `http://localhost:3000/tableau/orcamentos_wdc.html`
5. **Configure** fonte de dados e teste conexão
6. **Conectar ao Tableau**

### **Opção 2: Tableau Online/Server**
1. **Acesse Tableau Online**
2. **Criar** → **Pasta de Trabalho**
3. **Conectar aos Dados** → **Web Data Connector**
4. **URL**: `http://localhost:3000/tableau/orcamentos_wdc.html`

## 📊 **Fontes de Dados Disponíveis:**

### 1. **Resumo Analytics** (Recomendado para início)
- **Total de Orçamentos**
- **Trabalhos Fechados** 
- **Taxa de Conversão (%)**
- **Receita Total**
- **Total de Horas**
- **Taxa/Hora Média**
- **Valor Médio por Projeto**

### 2. **Trabalhos Detalhados** (Análise granular)
- **ID do Trabalho**
- **Tipo de Serviço** (Website, E-commerce, App, etc.)
- **Localização** (Capital, Interior, Remoto)
- **Faixa de Orçamento** (Econômico, Padrão, Premium)
- **Urgência** (Normal, Urgente, Super Urgente)
- **Custo Total, Horas, Taxa/Hora**
- **Status** (Fechado/Aberto)
- **Datas** (Criação e Fechamento)
- **Descrição**

### 3. **Série Temporal** (Análise de tendências)
- **Data**
- **Trabalhos Fechados por dia**
- **Receita por dia**
- **Horas trabalhadas por dia**

### 4. **KPIs Executivos** (Dashboard gerencial)
- **Receita Mensal**
- **Trabalhos Mensais**
- **Tempo Médio de Fechamento**
- **Valor Total do Pipeline**

## 🎯 **Dashboards Sugeridos:**

### **Dashboard Executivo:**
```
📊 Cartões KPI: Receita Total, Taxa Conversão, Ticket Médio
🥧 Gráfico Pizza: Receita por Tipo de Serviço
📈 Gráfico Linha: Tendência de Receita Mensal
📊 Gráfico Barra: Performance por Localização
```

### **Dashboard Operacional:**
```
📋 Tabela: Lista de Todos os Trabalhos
🔍 Filtros: Por Status, Tipo, Urgência, Data
📊 Gráfico Coluna: Trabalhos por Semana
⏱️ Gráfico: Tempo Médio de Fechamento
```

### **Dashboard Financeiro:**
```
💰 Cartões: Receita Mensal, Anual, Pipeline
📈 Gráfico Área: Evolução da Receita
📊 Gráfico Barra: ROI por Tipo de Projeto
🎯 Indicadores: Metas vs Realizado
```

## ⚡ **Configurações Recomendadas:**

### **Atualização de Dados:**
- **Frequência**: 5-10 minutos
- **Automática**: Sim
- **Cache**: Habilitado

### **Filtros Úteis:**
- **Período**: Últimos 30/90 dias
- **Status**: Trabalhos Fechados
- **Tipo de Serviço**: Múltipla seleção
- **Localização**: Capital/Interior/Remoto

## 🔍 **Funcionalidades do Conector:**

### ✅ **Recursos Implementados:**
- **Teste de Conexão** automático
- **4 Fontes de Dados** estruturadas
- **Schema bem definido** com tipos corretos
- **Interface amigável** de configuração
- **Tratamento de Erros** robusto
- **Atualização em Tempo Real**

### 📊 **Tipos de Dados Suportados:**
- **Números**: Inteiros e decimais
- **Texto**: Strings e categóricos
- **Datas**: DateTime e Date
- **Booleanos**: Status true/false
- **Moeda**: Valores formatados

## 🚨 **Solução de Problemas:**

### **Erro de Conexão:**
1. Verifique se API está rodando: `http://localhost:5000/health`
2. Teste manualmente: `http://localhost:5000/api/analytics/summary`
3. Confirme CORS habilitado no backend

### **Dados não Carregam:**
1. Teste o conector independentemente
2. Verifique logs do browser (F12)
3. Confirme formato JSON da resposta

### **Performance Lenta:**
1. Use "Resumo Analytics" para dashboards rápidos
2. Filtre dados por período
3. Configure cache adequadamente

## 📚 **Recursos Avançados:**

### **Filtros Dinâmicos:**
- Conecte múltiplas fontes
- Use parâmetros para filtrar
- Implemente drill-down

### **Cálculos Personalizados:**
```
Taxa de Conversão = [Trabalhos Fechados] / [Total Orçamentos]
ROI = ([Receita] - [Custo Base]) / [Custo Base]
Produtividade = [Receita] / [Total Horas]
```

### **Alertas e Notificações:**
- Configure alertas para metas
- Notificações de performance
- Monitoramento de KPIs críticos

## 🔗 **URLs de Referência:**

- **Conector WDC**: http://localhost:3000/tableau/orcamentos_wdc.html
- **API Summary**: http://localhost:5000/api/analytics/summary
- **API Health**: http://localhost:5000/health
- **Interface BI**: http://localhost:3000/bi-integration

## 📞 **Suporte:**

Em caso de problemas:
1. Teste na **interface BI** primeiro
2. Verifique **logs do browser**
3. Confirme **API funcionando**
4. Use **dados de exemplo** para teste

---

*🎯 **Dica Pro**: Comece com "Resumo Analytics" para familiarizar-se com os dados, depois explore as outras fontes para análises mais detalhadas.*

**Made by Diego Fonte** - https://www.diegofontedev.com.br