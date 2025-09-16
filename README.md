# 🚀 Gerador Inteligente de Orçamentos - DEMO

[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-brightgreen.svg)](https://vuejs.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-lightblue.svg)](https://sqlite.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-blue.svg)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **🚀 PROJETO DEMO** - Sistema conversacional inteligente que gera orçamentos profissionais através de chat com IA. A solução coleta requisitos via conversa natural e produz estimativas precisas baseadas em dados reais de mercado.

## ⚡ DEMO - Projeto Conceito

Este é um **projeto DEMO** que demonstra as possibilidades de sistemas conversacionais aplicados ao mundo dos negócios. O código é **100% editável** e pode ser adaptado para diversos tipos de projetos além de orçamentos.

### 🎯 Por que este DEMO é Especial?

- **Conversação Natural**: Chat inteligente que entende contexto e faz perguntas relevantes
- **Frontend Totalmente Editável**: Modifique cores, layout, textos, funcionalidades
- **BI Integrado**: Power BI e Google Data Studio com dashboards automáticos
- **API Analytics**: Endpoints completos para integração com ferramentas empresariais
- **Flexibilidade Total**: Adapte para qualquer tipo de consultoria ou serviço

## 🎯 Conceito

Sistema inovador que transforma conversas em orçamentos profissionais precisos. O usuário conversa com IA e recebe estimativas detalhadas em tempo real, simulando uma consultoria real.

## 📸 Screenshots

<div align="center">

### Funcionalidades
![Funcionalidades](Screenshots%20e%20vídeos/funcionalidades.gif)

### Funcionalidades 2
![Funcionalidades 2](Screenshots%20e%20vídeos/Funcionalidades2.gif)

### Orçamento Rápido
![Orçamento Rápido](Screenshots%20e%20vídeos/Orçamento-Rápido.gif)

### Orçamento Detalhado
![Orçamento Detalhado](Screenshots%20e%20vídeos/OrçamentoDetalhado.gif)

### Integração com Power BI
![Integração com Power BI](Screenshots%20e%20vídeos/integração-com-powerbi.gif)

### Integração Data Studio (Google)
![Integração Data Studio Google](Screenshots%20e%20vídeos/IntegraçãoDataStudioGoogle.gif)

</div>

## 🔥 Novas Funcionalidades Disponíveis

### 📊 Integração Business Intelligence
- **Dashboard em tempo real** com métricas atualizadas automaticamente
- **Integração Power BI** e Google Data Studio com templates prontos
- **API Analytics** para conectar com ferramentas de BI empresariais
- **Preview de dados** com estatísticas dinâmicas

### 🎛️ Interface Aprimorada
- **Orçamento Rápido** com formulário inteligente e estatísticas em tempo real
- **Dashboard Gerencial** com visão completa de todos os orçamentos
- **Sistema de Status** para acompanhar trabalhos fechados vs pipeline
- **Relatórios Automáticos** com exportação em PDF profissional

### 🔗 Sistema Modular
- **API RESTful** completa para integração com outros sistemas
- **Frontend totalmente editável** - modifique interface, cores, textos
- **Backend Python modular** - adapte lógica de negócio facilmente
- **Banco de dados flexível** - SQLite para desenvolvimento, PostgreSQL para produção

## 🛠️ Stack Tecnológico

- **Backend**: Flask + SQLite/PostgreSQL + SQLAlchemy
- **Frontend**: Vue.js 3 + Vite + TailwindCSS  
- **IA**: OpenAI GPT + Processamento de Linguagem Natural
- **BI**: Power BI + Google Data Studio + API Analytics
- **PDF**: jsPDF + Relatórios automatizados
- **Deploy**: Docker Ready + Ambiente de desenvolvimento

## 🎨 Totalmente Personalizável

### Frontend Editável
```javascript
// Cores, textos, layouts - tudo personalizável
const themeConfig = {
  primaryColor: '#667eea',
  companyName: 'Sua Empresa',
  logo: '/assets/seu-logo.png'
}
```

### Adapte para Seu Negócio
- **Consultoria Financeira**: Orçamentos de investimentos
- **Agência de Marketing**: Campanhas publicitárias  
- **Construção Civil**: Estimativas de obras
- **Consultoria Jurídica**: Honorários advocatícios
- **E muito mais...** - adapte a lógica para qualquer área!

## 🎨 Frontend 100% Personalizável

### 🎯 Elementos Editáveis
- **Cores e Tema**: TailwindCSS configurável
- **Textos e Labels**: Todos centralizados em arquivos config
- **Logos e Imagens**: Pasta public/ para assets personalizados
- **Layout**: Componentes Vue modulares
- **Funcionalidades**: Adicione/remova páginas facilmente

### 🔧 Como Personalizar
```javascript
// frontend/src/style.css - Modifique cores
:root {
  --primary-color: #667eea;
  --secondary-color: #f093fb;
}

// frontend/src/App.vue - Modifique layout
const appConfig = {
  companyName: 'Sua Empresa',
  logo: '/assets/seu-logo.png',
  theme: 'custom'
}
```

### 🔧 Exemplos de Adaptação para Outros Negócios
- **Consultoria Financeira**: Orçamentos de investimentos e planejamento
- **Agência de Marketing**: Campanhas publicitárias e estratégias digitais
- **Construção Civil**: Estimativas de obras e reformas
- **Consultoria Jurídica**: Honorários advocatícios e serviços legais
- **Consultoria TI**: Projetos de software e infraestrutura
- **E muito mais...** - adapte a lógica para qualquer área de consultoria!

## 🚀 Instalação Rápida

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

### Acesso
- **Frontend**: http://localhost:3000
- **API**: http://localhost:5000
- **BI Integration**: http://localhost:3000/bi-integration

## 📁 Estrutura do Projeto

```
gerador-orcamentos/
├── backend/                 # API Flask
│   ├── app.py              # Servidor principal
│   ├── models/             # Modelos de dados
│   ├── services/           # Lógica de negócio
│   ├── routes/             # Endpoints da API
│   └── requirements.txt    # Dependências Python
├── frontend/               # Interface Vue.js
│   ├── src/
│   │   ├── views/          # Páginas da aplicação
│   │   ├── components/     # Componentes reutilizáveis
│   │   ├── services/       # Conexão com API
│   │   └── composables/    # Lógica reutilizável
│   ├── public/
│   └── package.json
├── templates/              # Templates BI (Power BI)
└── docs/                   # Documentação
```

## 🌟 Como Usar

1. **Clone o repositório**
2. **Instale as dependências** (backend e frontend)
3. **Configure sua API OpenAI** no backend
4. **Execute ambos servidores**
5. **Acesse http://localhost:3000**
6. **Experimente as funcionalidades**:
   - Chat conversacional para orçamentos
   - Orçamento rápido via formulário
   - Dashboard com métricas em tempo real
   - Integração BI com Power BI/Data Studio

## 🔐 Segurança

### Medidas Implementadas
- ✅ Validação de entrada em todos os endpoints
- ✅ CORS configurado adequadamente
- ✅ Sanitização de dados do usuário
- ✅ Rate limiting por IP (futuro)
- ✅ Logs de segurança e auditoria
- ✅ SQLite com prepared statements

### Recomendações para Produção
- Use HTTPS obrigatoriamente
- Configure firewall adequadamente
- Monitore logs de acesso
- Mantenha dependências atualizadas
- Configure backup automático do banco

## 📝 Roadmap

- [ ] Sistema de autenticação e usuários
- [ ] Dashboard administrativo avançado
- [ ] Integração com mais APIs de IA
- [ ] Sistema de templates personalizáveis
- [ ] Exportação para Excel/CSV
- [ ] Webhooks para integrações
- [ ] App mobile (React Native)
- [ ] Sistema de notificações
- [ ] Multi-idiomas (i18n)
- [ ] Deploy automatizado (Docker + CI/CD)

## ❓ FAQ

**Q: Como configurar minha própria API de IA?**
A: Edite o arquivo `backend/services/ai_service.py` e configure sua chave API.

**Q: Posso personalizar os cálculos de preço?**
A: Sim! Modifique o arquivo `backend/services/pricing_service.py` com sua lógica de negócio.

**Q: Como adicionar novos tipos de serviços?**
A: Edite os arquivos de configuração em `frontend/src/views/` e adicione na lógica do backend.

**Q: É possível integrar com meu CRM existente?**
A: Sim! Use os endpoints da API Analytics ou crie webhooks personalizados.

## 🔗 Projetos Relacionados

Confira outros projetos DEMO similares:
- 🤖 **[Chatbot Personalizado](https://github.com/Diego-Cruz-github/chatbot-personalizado-diversos)** - Sistema de chatbot multi-persona totalmente personalizável

## 👨‍💻 Autor

**Diego Fonte** - Desenvolvedor Full Stack | Consultor de Cyber Segurança e IA

- 🌐 Website: [www.diegofontedev.com.br](https://www.diegofontedev.com.br)
- 🏢 Empresa: [www.zowti.com](https://www.zowti.com)
- 📧 Email: contato@diegofontedev.com.br

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

---

### 🎯 Projeto DEMO Profissional

Este é um **projeto de demonstração profissional** que showcases tecnologias modernas de desenvolvimento e IA aplicadas a sistemas conversacionais de negócios.

**Ready for Production** | **BI Integrated** | **100% Customizable** | **Enterprise Ready**