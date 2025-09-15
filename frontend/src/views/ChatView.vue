<template>
  <div class="p-8">
    <div class="max-w-4xl mx-auto">
      <!-- Welcome Section -->
      <div v-if="!chatStore.hasActiveSession" class="text-center py-16">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">
          Bem-vindo ao Gerador Inteligente de Orçamentos
        </h1>
        <p class="text-xl text-gray-600 mb-8">
          Converse comigo e receba orçamentos profissionais personalizados em tempo real.
        </p>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">Apps Mobile</h3>
            <p class="text-sm text-gray-600">iOS, Android, React Native, Flutter, PWA</p>
          </div>
          
          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9v-9m0-9v9" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">Websites</h3>
            <p class="text-sm text-gray-600">Landing pages, e-commerce, portais, blogs</p>
          </div>
          
          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">Sistemas Web</h3>
            <p class="text-sm text-gray-600">ERP, CRM, dashboards, plataformas</p>
          </div>

          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">APIs & Backend</h3>
            <p class="text-sm text-gray-600">REST APIs, microserviços, integrações</p>
          </div>

          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">DevOps & Cloud</h3>
            <p class="text-sm text-gray-600">CI/CD, Docker, AWS, Azure, monitoramento</p>
          </div>

          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">IA & Automação</h3>
            <p class="text-sm text-gray-600">Chatbots, ML, automação de processos</p>
          </div>
        </div>

        <button 
          @click="startChat"
          :disabled="chatStore.isLoading"
          class="group relative bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-semibold py-4 px-8 rounded-xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 disabled:opacity-50 disabled:transform-none"
        >
          <span v-if="!chatStore.isLoading" class="flex items-center space-x-3">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
            <span>Vamos Conversar!</span>
            <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </span>
          <span v-else class="flex items-center space-x-2">
            <svg class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span>Conectando com IA...</span>
          </span>
        </button>
      </div>

      <!-- Chat Messages -->
      <div v-else class="space-y-4">
        <div 
          v-for="(message, index) in chatStore.messages"
          :key="index"
          class="flex"
          :class="message.role === 'user' ? 'justify-end' : 'justify-start'"
        >
          <div 
            class="max-w-md px-4 py-3 rounded-lg"
            :class="message.role === 'user' 
              ? 'bg-blue-500 text-white' 
              : 'bg-white text-gray-800 border border-gray-200'"
          >
            <div v-html="formatMessage(message.content)"></div>
          </div>
        </div>
        
        <!-- Message Input -->
        <div class="flex space-x-4 mt-8">
          <input
            v-model="messageText"
            @keypress.enter="sendMessage"
            :disabled="chatStore.isLoading"
            placeholder="Digite sua mensagem..."
            class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
          />
          <button
            @click="sendMessage"
            :disabled="chatStore.isLoading || !messageText.trim()"
            class="bg-blue-500 hover:bg-blue-600 text-white font-medium py-3 px-6 rounded-lg disabled:opacity-50"
          >
            Enviar
          </button>
        </div>
        
        <button 
          @click="clearChat"
          class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-lg"
        >
          Nova Conversa
        </button>
      </div>

      <!-- Quote Display -->
      <div v-if="chatStore.currentQuote" class="mt-8 p-6 bg-green-50 border border-green-200 rounded-lg">
        <h3 class="text-lg font-bold text-green-800 mb-4">Orçamento Gerado!</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div class="bg-white p-4 rounded-lg">
            <div class="text-2xl font-bold text-green-600">
              R$ {{ formatCurrency(chatStore.currentQuote.total_cost) }}
            </div>
            <div class="text-sm text-gray-600">Valor Total</div>
          </div>
          <div class="bg-white p-4 rounded-lg">
            <div class="text-2xl font-bold text-blue-600">
              {{ chatStore.currentQuote.total_hours }}h
            </div>
            <div class="text-sm text-gray-600">Total de Horas</div>
          </div>
          <div class="bg-white p-4 rounded-lg">
            <div class="text-2xl font-bold text-purple-600">
              {{ chatStore.currentQuote.timeline_weeks }} sem
            </div>
            <div class="text-sm text-gray-600">Prazo</div>
          </div>
          <div class="bg-white p-4 rounded-lg">
            <div class="text-2xl font-bold text-orange-600">
              R$ {{ chatStore.currentQuote.hourly_rate }}
            </div>
            <div class="text-sm text-gray-600">Valor/Hora</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Error Display -->
  <div v-if="chatStore.error" class="fixed top-4 right-4 bg-red-500 text-white px-6 py-4 rounded-lg shadow-lg">
    <div class="flex items-center justify-between">
      <span class="font-medium">Erro: {{ chatStore.error }}</span>
      <button @click="chatStore.clearError()" class="text-white hover:text-red-200 ml-4">
        ✕
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useChatStore } from '@/stores/chat'

const chatStore = useChatStore()
const messageText = ref('')

const startChat = async () => {
  await chatStore.startNewConversation()
}

const sendMessage = async () => {
  if (!messageText.value.trim()) return
  
  const message = messageText.value
  messageText.value = ''
  
  await chatStore.sendMessage(message)
}

const clearChat = async () => {
  chatStore.clearConversation()
  await startChat()
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

const formatMessage = (content) => {
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>')
}
</script>