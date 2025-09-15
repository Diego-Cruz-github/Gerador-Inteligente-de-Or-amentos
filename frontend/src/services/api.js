import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

// Chat API
export const chatAPI = {
  startConversation: () => api.post('/chat/start'),
  
  startDetailedConversation: () => api.post('/chat/start-detailed'),
  
  sendMessage: (sessionId, message, includeMarketResearch = false) => api.post('/chat/message', {
    session_id: sessionId,
    message: message,
    include_market_research: includeMarketResearch
  }),
  
  getConversation: (sessionId) => api.get(`/chat/conversation/${sessionId}`)
}

// Orçamentos API  
export const orcamentosAPI = {
  list: () => api.get('/orcamentos'),
  
  get: (id) => api.get(`/orcamentos/${id}`),
  
  getChartsData: (id) => api.get(`/orcamentos/${id}/charts`),
  
  generatePDF: (id) => api.get(`/orcamentos/${id}/pdf`)
}

// Dashboard API
export const dashboardAPI = {
  getStats: () => api.get('/dashboard/stats'),
  
  getCharts: () => api.get('/dashboard/charts'),
  
  getRecent: () => api.get('/dashboard/recent')
}

export default api