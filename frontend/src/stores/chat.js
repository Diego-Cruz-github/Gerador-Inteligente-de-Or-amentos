import { defineStore } from 'pinia'
import { chatAPI } from '@/services/api'

export const useChatStore = defineStore('chat', {
  state: () => ({
    sessionId: null,
    conversationId: null,
    messages: [],
    isLoading: false,
    isTyping: false,
    requirements: {},
    currentQuote: null,
    error: null
  }),

  getters: {
    hasActiveSession: (state) => !!state.sessionId,
    lastMessage: (state) => state.messages[state.messages.length - 1],
    userMessages: (state) => state.messages.filter(msg => msg.role === 'user'),
    assistantMessages: (state) => state.messages.filter(msg => msg.role === 'assistant')
  },

  actions: {
    async startNewConversation() {
      try {
        this.isLoading = true
        this.error = null
        
        const response = await chatAPI.startConversation()
        
        if (response.data.success) {
          this.sessionId = response.data.session_id
          this.conversationId = response.data.conversation_id
          this.messages = response.data.messages || []
        } else {
          throw new Error('Falha ao iniciar conversa')
        }
      } catch (error) {
        this.error = error.response?.data?.error || error.message
        console.error('Erro ao iniciar conversa:', error)
      } finally {
        this.isLoading = false
      }
    },

    async startDetailedConversation() {
      try {
        this.isLoading = true
        this.error = null
        
        const response = await chatAPI.startDetailedConversation()
        
        if (response.data.success) {
          this.sessionId = response.data.session_id
          this.conversationId = response.data.conversation_id
          this.messages = response.data.messages || []
        } else {
          throw new Error('Falha ao iniciar conversa detalhada')
        }
      } catch (error) {
        this.error = error.response?.data?.error || error.message
        console.error('Erro ao iniciar conversa detalhada:', error)
      } finally {
        this.isLoading = false
      }
    },

    async sendMessage(message, includeMarketResearch = false) {
      if (!this.sessionId || !message.trim()) return

      try {
        this.isLoading = true
        this.isTyping = true
        this.error = null

        // Adicionar mensagem do usuário imediatamente
        this.addMessage('user', message)

        const response = await chatAPI.sendMessage(this.sessionId, message, includeMarketResearch)

        if (response.data.success) {
          // Adicionar resposta do assistente
          this.addMessage('assistant', response.data.message)
          
          // Atualizar requisitos
          if (response.data.requirements) {
            this.requirements = { ...this.requirements, ...response.data.requirements }
          }

          // Se foi gerado um orçamento
          if (response.data.quote_generated && response.data.quote) {
            this.currentQuote = response.data.quote
          }
        } else {
          throw new Error(response.data.error || 'Erro ao enviar mensagem')
        }
      } catch (error) {
        this.error = error.response?.data?.error || error.message
        this.addMessage('assistant', 'Desculpe, ocorreu um erro. Tente novamente.')
        console.error('Erro ao enviar mensagem:', error)
      } finally {
        this.isLoading = false
        this.isTyping = false
      }
    },

    addMessage(role, content) {
      this.messages.push({
        role,
        content,
        timestamp: new Date().toISOString()
      })
    },

    async loadConversation(sessionId) {
      try {
        this.isLoading = true
        this.error = null

        const response = await chatAPI.getConversation(sessionId)
        
        if (response.data.success) {
          this.sessionId = sessionId
          this.conversationId = response.data.conversation_id
          this.messages = response.data.messages || []
          this.requirements = response.data.requirements || {}
        } else {
          throw new Error('Conversa não encontrada')
        }
      } catch (error) {
        this.error = error.response?.data?.error || error.message
        console.error('Erro ao carregar conversa:', error)
      } finally {
        this.isLoading = false
      }
    },

    clearConversation() {
      this.sessionId = null
      this.conversationId = null
      this.messages = []
      this.requirements = {}
      this.currentQuote = null
      this.error = null
    },

    clearError() {
      this.error = null
    }
  }
})