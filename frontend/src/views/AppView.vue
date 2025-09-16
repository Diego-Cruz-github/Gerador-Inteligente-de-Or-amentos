<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">
          🎯 Gerador Inteligente de Orçamentos
        </h1>
        <p class="text-gray-600">
          Interface profissional para geração automatizada de orçamentos
        </p>
      </div>

      <!-- Main Form Card -->
      <div class="bg-white rounded-xl shadow-lg p-8 mb-8">
        <h2 class="text-xl font-semibold text-gray-800 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Dados do Projeto
        </h2>

        <form @submit.prevent="generateQuote" class="space-y-6">
          <!-- Service Type -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Tipo de Serviço *
            </label>
            <select
              v-model="formData.serviceType"
              required
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
              style="appearance: menulist; background-color: white;"
              @change="(e) => e.target.blur()"
            >
              <option value="">Selecione o tipo de serviço</option>
              <option value="website">🌐 Website Institucional</option>
              <option value="ecommerce">🛒 E-commerce / Loja Virtual</option>
              <option value="app">📱 Aplicativo Mobile</option>
              <option value="sistema">💻 Sistema Web / Dashboard</option>
              <option value="landing">📄 Landing Page</option>
              <option value="blog">📝 Blog / Portal de Conteúdo</option>
            </select>
          </div>

          <!-- Urgency -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Urgência *
            </label>
            <select
              v-model="formData.urgency"
              required
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
              style="appearance: menulist; background-color: white;"
              @change="(e) => e.target.blur()"
            >
              <option value="">Selecione a urgência</option>
              <option value="normal">⏰ Normal</option>
              <option value="urgent">🚀 Urgente (7 a 15 dias)</option>
              <option value="super_urgent">⚡ Super Urgente (até 7 dias)</option>
            </select>
          </div>

          <!-- Location -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Localização *
            </label>
            <select
              v-model="formData.location"
              required
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
              style="appearance: menulist; background-color: white;"
              @change="(e) => e.target.blur()"
            >
              <option value="">Selecione a localização</option>
              <option value="SP">🏙️ Capital</option>
              <option value="interior">🌆 Interior</option>
              <option value="remoto">🌐 Remoto</option>
            </select>
          </div>

          <!-- Budget Tier -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Faixa de Orçamento *
            </label>
            <select
              v-model="formData.budgetTier"
              required
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
              style="appearance: menulist; background-color: white;"
              @change="(e) => e.target.blur()"
            >
              <option value="">Selecione a faixa de orçamento</option>
              <option value="economico">💰 Econômico - Melhor custo-benefício</option>
              <option value="padrao">⚡ Padrão - Recursos completos</option>
              <option value="premium">🚀 Premium - Tecnologia de ponta</option>
            </select>
          </div>

          <!-- Description/Proposal -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Descrição do Projeto ou Proposta
            </label>
            <textarea
              v-model="formData.description"
              rows="6"
              placeholder="Descreva seu projeto detalhadamente ou cole uma proposta existente para análise..."
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
            ></textarea>
            <p class="text-sm text-gray-500 mt-1">
              💡 Quanto mais detalhes, mais preciso será o orçamento gerado pela IA
            </p>
          </div>

          <!-- Submit Button -->
          <div class="pt-4">
            <button
              type="submit"
              :disabled="isLoading || !isFormValid"
              class="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-medium py-3 px-6 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 flex items-center justify-center space-x-2"
            >
              <svg v-if="isLoading" class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              <span v-if="isLoading">Analisando com IA...</span>
              <span v-else>🤖 Gerar Orçamento com IA</span>
            </button>
          </div>
        </form>
      </div>

      <!-- Quote Result -->
      <div v-if="generatedQuote" class="bg-white rounded-xl shadow-lg p-8">
        <h2 class="text-xl font-semibold text-gray-800 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          Orçamento Gerado
        </h2>

        <!-- Quote Summary -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div class="text-center p-4 bg-green-50 rounded-lg">
            <div class="text-2xl font-bold text-green-600">
              R$ {{ formatCurrency(generatedQuote.total_cost) }}
            </div>
            <div class="text-sm text-gray-600">Valor Total</div>
          </div>
          <div class="text-center p-4 bg-blue-50 rounded-lg">
            <div class="text-2xl font-bold text-blue-600">
              {{ generatedQuote.total_hours }}h
            </div>
            <div class="text-sm text-gray-600">Total de Horas</div>
          </div>
          <div class="text-center p-4 bg-purple-50 rounded-lg">
            <div class="text-2xl font-bold text-purple-600">
              {{ generatedQuote.timeline_weeks }}
            </div>
            <div class="text-sm text-gray-600">Prazo</div>
          </div>
          <div class="text-center p-4 bg-orange-50 rounded-lg">
            <div class="text-2xl font-bold text-orange-600">
              R$ {{ generatedQuote.hourly_rate }}
            </div>
            <div class="text-sm text-gray-600">Valor/Hora</div>
          </div>
        </div>

        <!-- AI Analysis -->
        <div v-if="aiAnalysis" class="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
          <h3 class="font-semibold text-blue-900 mb-2 flex items-center">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
            Análise da IA
          </h3>
          <div class="text-blue-800" v-html="formatMessage(aiAnalysis)"></div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4">
          <button
            @click="downloadPDF"
            class="flex-1 bg-red-600 hover:bg-red-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <span>📄 Baixar PDF</span>
          </button>
          <button
            @click="sendEmail"
            class="flex-1 bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span>📧 Enviar por Email</span>
          </button>
          <button
            @click="resetForm"
            class="flex-1 bg-gray-600 hover:bg-gray-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            <span>🔄 Novo Orçamento</span>
          </button>
        </div>
      </div>

      <!-- Error Display -->
      <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
        <div class="flex items-center">
          <svg class="w-5 h-5 text-red-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span class="text-red-800 font-medium">{{ error }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { chatAPI } from '@/services/api'

// Form Data
const formData = ref({
  serviceType: '',
  urgency: '',
  location: '',
  budgetTier: '',
  description: ''
})

// State
const isLoading = ref(false)
const generatedQuote = ref(null)
const aiAnalysis = ref('')
const error = ref('')

// Computed
const isFormValid = computed(() => {
  return formData.value.serviceType && 
         formData.value.urgency && 
         formData.value.location && 
         formData.value.budgetTier
})

// Methods
const generateQuote = async () => {
  try {
    isLoading.value = true
    error.value = ''
    
    console.log('📋 Enviando dados do formulário:', formData.value)
    
    // Chamar backend para gerar orçamento
    const response = await chatAPI.generateFromForm(formData.value)
    
    if (response.data.success) {
      generatedQuote.value = response.data.quote
      aiAnalysis.value = response.data.ai_analysis || ''
      
      console.log('✅ Orçamento gerado com sucesso:', response.data)
    } else {
      throw new Error(response.data.error || 'Erro desconhecido')
    }
    
  } catch (err) {
    console.error('❌ Erro ao gerar orçamento:', err)
    error.value = err.response?.data?.error || err.message || 'Erro ao gerar orçamento'
  } finally {
    isLoading.value = false
  }
}

const downloadPDF = async () => {
  try {
    error.value = ''
    
    const pdfData = {
      quote: generatedQuote.value,
      ai_analysis: aiAnalysis.value
    }
    
    const response = await chatAPI.generatePDF(pdfData)
    
    if (response.data.success) {
      console.log('✅ PDF gerado:', response.data.pdf_url)
      alert('PDF gerado com sucesso!')
    }
  } catch (err) {
    error.value = 'Erro ao gerar PDF: ' + (err.response?.data?.error || err.message)
  }
}

const sendEmail = async () => {
  const email = prompt('Digite o email para envio do orçamento:')
  if (!email) return
  
  if (!email.includes('@')) {
    error.value = 'Email inválido'
    return
  }
  
  try {
    error.value = ''
    
    const emailData = {
      quote: generatedQuote.value,
      ai_analysis: aiAnalysis.value,
      email: email
    }
    
    const response = await chatAPI.sendEmail(emailData)
    
    if (response.data.success) {
      alert(response.data.message)
    }
  } catch (err) {
    error.value = 'Erro ao enviar email: ' + (err.response?.data?.error || err.message)
  }
}

const resetForm = () => {
  formData.value = {
    serviceType: '',
    urgency: '',
    location: '',
    budgetTier: '',
    description: ''
  }
  generatedQuote.value = null
  aiAnalysis.value = ''
  error.value = ''
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