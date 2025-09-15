# Gerador Inteligente de Orçamentos

Sistema conversacional inteligente que gera orçamentos profissionais através de chat com IA. A solução coleta requisitos via conversa natural e produz estimativas precisas baseadas em dados reais de mercado.

## Conceito

Gerador inteligente de orçamentos com interface conversacional. Usuario conversa com IA e recebe orçamentos profissionais em tempo real.

## Como Funciona

- Chat conversacional coleta requisitos do projeto
- IA faz perguntas contextuais (tipo projeto, usuários, plataforma)
- Sistema calcula orçamento dinamicamente com preços realistas
- Visualizações interativas mostram breakdown de custos
- Export PDF do orçamento final

## Stack Tecnológico

- **Backend**: Flask + PostgreSQL
- **Frontend**: Vue.js
- **Gráficos**: Plotly
- **PDF**: WeasyPrint

## Features Demo

- Chat conversacional fluido
- Cálculo de orçamento em tempo real
- Gráficos animados (pizza, timeline)
- Templates por tipo de projeto (app, site, sistema)
- Preços regionalizados (SP vs interior vs remoto)
- Breakdown detalhado (design, dev, backend, testes)
- Export PDF profissional
- Interface responsiva moderna

## Dados de Mercado

Sistema utiliza dados realistas baseados em pesquisa de mercado atual. Custos empresariais completos incluindo desenvolvimento, infraestrutura, licenças e execução:
- Junior: R$ 65-85/h
- Pleno: R$ 95-120/h  
- Senior: R$ 140-180/h

## Diferencial

Interface que simula consultoria real ao invés de formulários chatos. IA contextual que adapta perguntas ao tipo de projeto com cálculos de custo precisos baseados em dados de mercado atualizados.

## Instalação

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Estrutura do Projeto

```
gerador-orcamentos/
├── backend/
│   ├── app.py
│   ├── models/
│   ├── services/
│   ├── routes/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
└── docs/
    └── screenshots/
```

Sistema inovador que transforma conversas em orçamentos profissionais precisos com dados reais de mercado!