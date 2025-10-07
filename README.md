# Gerador Inteligente de Orçamentos - DEMO

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

## 🎬 Demonstrações

<details open>
<summary><strong>⚡ Sistema de Orçamentos</strong> <em>(demonstração)</em></summary>

![Orçamento Rápido](Screenshots%20e%20vídeos/Orçamento-Rápido.gif)
![Orçamento Detalhado](Screenshots%20e%20vídeos/OrçamentoDetalhado.gif)

</details>

<details>
<summary><strong>🚀 Funcionalidades Principais</strong> <em>(clique aqui para ver demonstração)</em></summary>

![Funcionalidades](Screenshots%20e%20vídeos/funcionalidades.gif)
![Funcionalidades 2](Screenshots%20e%20vídeos/Funcionalidades2.gif)

</details>

<details>
<summary><strong>📊 Integração BI</strong> <em>(clique aqui para ver demonstração)</em></summary>

![Integração com Power BI](Screenshots%20e%20vídeos/integração-com-powerbi.gif)
![Integração Data Studio Google](Screenshots%20e%20vídeos/IntegraçãoDataStudioGoogle.gif)

</details>

## 👨‍💻 Autor

**Diego Fonte** - Desenvolvedor Full Stack | Consultor de Cyber Segurança e IA

- 🌐 Website: [www.diegofontedev.com.br](https://www.diegofontedev.com.br) | [English](https://www.diegofontedev.com.br/index-en.html) | [Español](https://www.diegofontedev.com.br/index-es.html)
- 📧 Email: contato@diegofontedev.com.br

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
- **Deploy**: Docker + Docker Compose + Nginx
- **Containerização**: Multi-stage builds otimizados para produção
- **Database**: SQLite (dev) / PostgreSQL (produção)

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

## 🎨 Sistema Totalmente Personalizável

### 🔧 Exemplos de Adaptação para Outros Negócios
- **Consultoria Financeira**: Orçamentos de investimentos e planejamento
- **Agência de Marketing**: Campanhas publicitárias e estratégias digitais
- **Construção Civil**: Estimativas de obras e reformas
- **Consultoria Jurídica**: Honorários advocatícios e serviços legais
- **Consultoria TI**: Projetos de software e infraestrutura
- **E muito mais...** - adapte a lógica para qualquer área de consultoria!

## 🚀 Instalação Rápida

### 🐳 Instalação com Docker (Recomendado)

#### Pré-requisitos
- Docker e Docker Compose instalados
- Chave da API OpenAI

#### 1. Clone e Configure
```bash
git clone https://github.com/seu-usuario/gerador-orcamentos.git
cd gerador-orcamentos

# Configure suas variáveis de ambiente
cp .env.example .env
# Edite o .env e adicione sua OPENAI_API_KEY
```

#### 2. Execute com Docker
```bash
# Desenvolvimento (com hot reload)
docker-compose -f docker-compose.dev.yml up --build

# Produção
docker-compose up --build -d

# Com PostgreSQL (produção completa)
docker-compose --profile production up --build -d
```

#### 3. Acesso
- **Frontend**: http://localhost:3000 (produção) ou http://localhost:3001 (dev)
- **API**: http://localhost:5000
- **BI Integration**: http://localhost:3000/bi-integration

#### 4. Comandos Úteis
```bash
# Ver logs
docker-compose logs -f

# Parar containers
docker-compose down

# Rebuild completo
docker-compose down && docker-compose up --build
```

### 📋 Instalação Manual (Alternativa)

#### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend  
```bash
cd frontend
npm install
npm run dev
```

#### Acesso Manual
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

### 🎯 Acesso Rápido às Funcionalidades

1. **🚀 Página Principal** - `http://localhost:3000`
   - Dashboard com visão geral de todos os orçamentos
   - Estatísticas em tempo real de conversão
   - Acesso rápido a todas as funcionalidades

2. **💬 Chat Conversacional** - `http://localhost:3000/chat`
   - Sistema de IA que coleta requisitos via conversa natural
   - Geração automática de orçamentos baseados na conversa
   - Histórico completo de interações

3. **⚡ Orçamento Rápido** - `http://localhost:3000/app`
   - Formulário inteligente para orçamentos express
   - Validação em tempo real e sugestões automáticas
   - Geração instantânea de estimativas

4. **🔍 Orçamento Detalhado** - `http://localhost:3000/detailed-app`
   - Análise completa com pesquisa de mercado automática
   - Comparação com concorrência em tempo real
   - Relatórios profissionais em PDF

5. **📊 BI Integration** - `http://localhost:3000/bi-integration`
   - Dashboards interativos Power BI e Google Data Studio
   - Métricas em tempo real de performance
   - Exportação de dados para ferramentas corporativas

6. **🔧 API Endpoints** - `http://localhost:5000/api`
   - `/api/chat` - Conversação com IA
   - `/api/quotes` - Gestão de orçamentos
   - `/api/analytics` - Dados para BI
   - `/api/dashboard` - Estatísticas gerais

### 🛠️ Configuração Técnica

1. **Configure Variáveis de Ambiente**:
   ```bash
   # Backend (.env)
   OPENAI_API_KEY=sua_chave_aqui
   FLASK_ENV=development
   
   # Frontend (opcional)
   VITE_API_URL=http://localhost:5000
   ```

2. **Primeira Execução**:
   - O banco SQLite é criado automaticamente
   - As tabelas são inicializadas no primeiro acesso
   - Dados de exemplo são populados para demonstração

3. **Personalização Rápida**:
   - Modifique cores em `frontend/src/style.css`
   - Adapte textos em `frontend/src/views/`
   - Configure preços em `backend/services/pricing_service.py`

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

## 📝 Roadmap do Projeto

### 🚀 Próximas Funcionalidades
- [ ] **Sistema de Clientes**: Gestão completa de leads e conversões
- [ ] **Templates de Orçamento**: Modelos personalizáveis por tipo de projeto
- [ ] **Assinatura Digital**: Aprovação eletrônica de orçamentos
- [ ] **CRM Integrado**: Funil de vendas completo
- [ ] **Relatórios Avançados**: Analytics de performance e ROI

### 🔧 Melhorias Técnicas
- [ ] **Autenticação JWT**: Sistema completo de usuários e permissões
- [ ] **Banco PostgreSQL**: Migração completa para produção
- [ ] **Cache Redis**: Otimização de performance para consultas BI
- [ ] **Webhooks**: Integração automática com sistemas externos
- [ ] **API Rate Limiting**: Controle de uso e segurança avançada

### 📱 Expansões
- [ ] **App Mobile PWA**: Versão otimizada para dispositivos móveis
- [ ] **Integração WhatsApp**: Envio automático de orçamentos
- [ ] **Multi-idiomas**: Suporte para inglês e espanhol
- [ ] **Marketplace**: Conexão com freelancers e fornecedores
- [ ] **AI Avançada**: Análise preditiva de fechamento

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

- 🌐 Website: [www.diegofontedev.com.br](https://www.diegofontedev.com.br) | [English](https://www.diegofontedev.com.br/index-en.html) | [Español](https://www.diegofontedev.com.br/index-es.html)
- 📧 Email: contato@diegofontedev.com.br

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

---

### 🎯 Projeto DEMO Profissional

Este é um **projeto de demonstração profissional** que showcases tecnologias modernas de desenvolvimento e IA aplicadas a sistemas conversacionais de negócios.

**Ready for Production** | **BI Integrated** | **100% Customizable** | **Enterprise Ready**