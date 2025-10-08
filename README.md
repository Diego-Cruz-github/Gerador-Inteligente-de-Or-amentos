# 🚀 Gerador Inteligente de Orçamentos

[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-brightgreen.svg)](https://vuejs.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-lightblue.svg)](https://sqlite.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-blue.svg)](https://tailwindcss.com/)
[![Docker](https://img.shields.io/badge/Docker-20.x-blue.svg)](https://docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema conversacional inteligente que gera orçamentos profissionais através de chat com IA. Coleta requisitos via conversa natural e produz estimativas precisas baseadas em dados reais de mercado.

![Orçamento Rápido](Screenshots%20e%20vídeos/Orçamento-Rápido.gif)

## 🎯 Conceito Técnico

Sistema que transforma conversas em orçamentos profissionais precisos através de processamento de linguagem natural e algoritmos de precificação inteligente.

## 🏗️ Arquitetura

**Backend Python (Flask)**
- API RESTful com endpoints especializados
- Processamento de linguagem natural
- Sistema de cálculo de preços dinâmico
- Integração com OpenAI GPT para análise conversacional

**Frontend Vue.js**
- Interface responsiva com TailwindCSS
- Chat em tempo real via WebSockets
- Dashboard analítico com métricas
- Geração de PDFs automatizada

**Integração BI**
- Conectores Power BI nativos
- API Analytics para Google Data Studio
- Dashboards em tempo real
- Exportação de dados empresariais

## 🎬 Demonstrações Principais

<details open>
<summary><strong>⚡ Sistema de Orçamentos</strong></summary>

![Orçamento Detalhado](Screenshots%20e%20vídeos/OrçamentoDetalhado.gif)

</details>

<details>
<summary><strong>📊 Integração BI</strong></summary>

![Integração com Power BI](Screenshots%20e%20vídeos/integração-com-powerbi.gif)

</details>

## 🛠️ Stack Tecnológico

- **Backend**: Flask + SQLAlchemy + OpenAI API
- **Frontend**: Vue.js 3 + Vite + TailwindCSS  
- **IA**: GPT + Processamento de Linguagem Natural
- **BI**: Power BI + Google Data Studio
- **Database**: SQLite (dev) / PostgreSQL (produção)
- **Deploy**: Docker + Docker Compose
- **PDF**: jsPDF + Relatórios automatizados

## 🚀 Funcionalidades Técnicas

### 💬 Sistema Conversacional
- Parser de linguagem natural para extração de requisitos
- Algoritmo de precificação baseado em contexto
- Histórico de conversas com análise de padrões
- Validação inteligente de dados de entrada

### 📊 Analytics Integrado
- Métricas de conversão em tempo real
- API RESTful para integração BI
- Dashboard gerencial com KPIs
- Relatórios automáticos em PDF

### 🔧 Arquitetura Modular
- Microserviços com responsabilidades específicas
- API documentada para integrações externas
- Sistema de plugins para novos tipos de orçamento
- Containerização completa com Docker

## 🐳 Deploy e Configuração

### Instalação Rápida
```bash
git clone https://github.com/Diego-Cruz-github/Gerador-Inteligente-de-Orcamentos.git
cd Gerador-Inteligente-de-Orcamentos

# Configurar ambiente
cp .env.example .env
# Adicionar OPENAI_API_KEY no .env

# Deploy com Docker
docker-compose up --build -d
```

### Acesso
- **Frontend**: http://localhost:3000
- **API**: http://localhost:5000
- **BI Integration**: http://localhost:3000/bi-integration

## 🔐 Segurança e Performance

### Implementações de Segurança
- Validação de entrada em todos os endpoints
- CORS configurado para produção
- Sanitização de dados do usuário
- Logs de auditoria e monitoramento

### Otimizações de Performance
- Cache de consultas frequentes
- Lazy loading no frontend
- Compressão de assets
- Database indexing otimizado

## 📋 Estrutura do Projeto

```
gerador-orcamentos/
├── backend/                 # API Flask
│   ├── models/             # Modelos de dados
│   ├── services/           # Lógica de negócio
│   └── routes/             # Endpoints da API
├── frontend/               # Interface Vue.js
│   ├── src/views/          # Páginas da aplicação
│   └── src/components/     # Componentes reutilizáveis
└── templates/              # Templates BI
```

## 🔗 Projetos Relacionados

- 🤖 **[Chatbot Personalizado](https://github.com/Diego-Cruz-github/chatbot-personalizado-diversos)** - Sistema conversacional multi-persona

---

**Diego Fonte**  
Full Stack Developer | AI & Cybersecurity Specialist  
[Portfolio PT](https://diegofontedev.com.br/) | [EN](https://diegofontedev.com.br/index-en.html) | [ES](https://diegofontedev.com.br/index-es.html)