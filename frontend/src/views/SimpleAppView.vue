<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-8">
        <div class="flex items-center justify-center mb-4">
          <div class="bg-gradient-to-r from-blue-600 to-purple-600 p-3 rounded-lg mr-4">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <div class="text-left">
            <h1 class="text-3xl font-bold text-gray-900 mb-1">
              Gerador Inteligente de Orçamentos
            </h1>
            <div class="flex items-center text-sm text-gray-600">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              Análise Inteligente
            </div>
          </div>
        </div>
        <p class="text-gray-600 max-w-2xl mx-auto">
          Interface profissional para geração automatizada de orçamentos com análise inteligente de requisitos e precificação baseada em dados de mercado
        </p>
        
        <!-- Navigation hint -->
        <div class="mt-4 text-sm text-gray-600">
          <router-link to="/detailed-app" class="text-green-600 hover:text-green-800 underline">
            → Precisa de mais detalhes? Use o Orçamento Detalhado com Pesquisa de Mercado
          </router-link>
        </div>
      </div>

      <!-- Main Form Card -->
      <div class="bg-white rounded-xl shadow-lg p-8 mb-8">
        <div class="flex items-center mb-6">
          <div class="bg-blue-100 p-2 rounded-lg mr-3">
            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h2 class="text-xl font-semibold text-gray-800">
            Dados do Projeto
          </h2>
        </div>

        <form @submit.prevent="generateQuote" class="space-y-6">
          <!-- Service Type -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Tipo de Serviço *
            </label>
            <select
              v-model="formData.serviceType"
              required
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione o tipo de serviço</option>
              <option value="website">Website Institucional</option>
              <option value="ecommerce">E-commerce / Loja Virtual</option>
              <option value="app">Aplicativo Mobile</option>
              <option value="sistema">Sistema Web / Dashboard</option>
              <option value="landing">Landing Page</option>
              <option value="blog">Blog / Portal de Conteúdo</option>
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
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione a urgência</option>
              <option value="normal">Normal</option>
              <option value="urgent">Urgente (7 a 15 dias)</option>
              <option value="super_urgent">Super Urgente (até 7 dias)</option>
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
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione a localização</option>
              <option value="SP">Capital</option>
              <option value="interior">Interior</option>
              <option value="remoto">Remoto</option>
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
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione a faixa de orçamento</option>
              <option value="economico">Econômico - Melhor custo-benefício</option>
              <option value="padrao">Padrão - Recursos completos</option>
              <option value="premium">Premium - Tecnologia de ponta</option>
            </select>
          </div>

          <!-- Description -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Descrição do Projeto ou Proposta
            </label>
            <textarea
              v-model="formData.description"
              rows="6"
              placeholder="Descreva seu projeto detalhadamente ou cole uma proposta existente para análise..."
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px;"
            ></textarea>
            <p class="text-sm text-gray-500 mt-1 flex items-center">
              <svg class="w-4 h-4 mr-1 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
              Quanto mais detalhes, mais preciso será o orçamento gerado pela IA
            </p>
          </div>

          <!-- Submit Button -->
          <div class="pt-4">
            <button
              type="submit"
              :disabled="isLoading || !isFormValid"
              style="width: 100%; background: linear-gradient(to right, #2563eb, #7c3aed); color: white; font-weight: 500; padding: 12px 24px; border-radius: 8px; border: none; cursor: pointer; font-size: 16px;"
              :style="{ opacity: (isLoading || !isFormValid) ? 0.5 : 1 }"
            >
              <span v-if="isLoading">Analisando com IA...</span>
              <span v-else>Gerar Orçamento com IA</span>
            </button>
          </div>
        </form>
      </div>

      <!-- Quote Result -->
      <div v-if="generatedQuote" class="bg-white rounded-xl shadow-lg p-8">
        <div class="flex items-center mb-6">
          <div class="bg-green-100 p-2 rounded-lg mr-3">
            <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h2 class="text-xl font-semibold text-gray-800">
            Orçamento Gerado
          </h2>
        </div>

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
          <div class="flex items-center mb-2">
            <div class="bg-blue-100 p-1 rounded mr-2">
              <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 class="font-semibold text-blue-900">
              Análise da IA
            </h3>
          </div>
          <div class="text-blue-800" v-html="formatMessage(aiAnalysis)"></div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4">
          <button
            @click="downloadPDF"
            style="flex: 1; background-color: #dc2626; color: white; font-weight: 500; padding: 12px 24px; border-radius: 8px; border: none; cursor: pointer;"
          >
            Baixar PDF
          </button>
          <button
            @click="promptEmailAndSend"
            style="flex: 1; background-color: #16a34a; color: white; font-weight: 500; padding: 12px 24px; border-radius: 8px; border: none; cursor: pointer;"
          >
            Enviar por Email
          </button>
          <button
            @click="goToDashboard"
            style="flex: 1; background-color: #3b82f6; color: white; font-weight: 500; padding: 12px 24px; border-radius: 8px; border: none; cursor: pointer;"
          >
            Ver Dashboard
          </button>
          <button
            @click="resetForm"
            style="flex: 1; background-color: #6b7280; color: white; font-weight: 500; padding: 12px 24px; border-radius: 8px; border: none; cursor: pointer;"
          >
            Novo Orçamento
          </button>
        </div>
      </div>

      <!-- Error Display -->
      <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
        <div class="flex items-center">
          <span class="text-red-800 font-medium">❌ {{ error }}</span>
        </div>
      </div>

      <!-- Success Message -->
      <div v-if="successMessage" class="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
        <div class="flex items-center">
          <span class="text-green-800 font-medium">✅ {{ successMessage }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { chatAPI } from '@/services/api'
import jsPDF from 'jspdf'

// Router
const router = useRouter()

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
const successMessage = ref('')

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
    successMessage.value = ''
    
    console.log('📋 Enviando dados do formulário:', formData.value)
    
    const response = await chatAPI.generateFromForm(formData.value)
    
    if (response.data.success) {
      generatedQuote.value = response.data.quote
      aiAnalysis.value = response.data.ai_analysis || ''
      
      // Salvar no localStorage para dashboard
      saveQuoteToLocalStorage({
        quote: generatedQuote.value,
        aiAnalysis: aiAnalysis.value,
        serviceType: formData.value.serviceType,
        urgency: formData.value.urgency,
        location: formData.value.location,
        budgetTier: formData.value.budgetTier,
        description: formData.value.description,
        isDetailed: false,
        createdAt: new Date().toISOString()
      })
      
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
    successMessage.value = ''
    error.value = ''
    
    if (!generatedQuote.value) {
      error.value = 'Nenhum orçamento gerado para exportar'
      return
    }
    
    // Criar PDF usando jsPDF
    const doc = new jsPDF()
    
    // Header
    doc.setFontSize(20)
    doc.setTextColor(59, 130, 246) // blue-600
    doc.text('Orçamento Rápido - Gerador Inteligente', 20, 30)
    
    doc.setFontSize(12)
    doc.setTextColor(107, 114, 128) // gray-500
    doc.text('Gerado em: ' + new Date().toLocaleDateString('pt-BR'), 20, 40)
    
    // Dados do orçamento
    doc.setFontSize(16)
    doc.setTextColor(0, 0, 0)
    doc.text('Resumo do Orçamento', 20, 60)
    
    doc.setFontSize(12)
    doc.text(`Valor Total: R$ ${formatCurrency(generatedQuote.value.total_cost)}`, 20, 75)
    doc.text(`Total de Horas: ${generatedQuote.value.total_hours}h`, 20, 85)
    doc.text(`Prazo: ${generatedQuote.value.timeline_weeks}`, 20, 95)
    doc.text(`Valor/Hora: R$ ${generatedQuote.value.hourly_rate}`, 20, 105)
    
    // Análise da IA
    if (aiAnalysis.value) {
      doc.setFontSize(16)
      doc.text('Análise da IA', 20, 125)
      doc.setFontSize(10)
      const aiText = aiAnalysis.value.replace(/\*\*(.*?)\*\*/g, '$1').replace(/<br>/g, '\n')
      const splitAI = doc.splitTextToSize(aiText, 170)
      doc.text(splitAI, 20, 135)
    }
    
    // Gerar nome do arquivo baseado no tipo de serviço
    const serviceTypeMap = {
      'website': 'Website-Institucional',
      'ecommerce': 'E-commerce',
      'app': 'App-Mobile',
      'sistema': 'Sistema-Web',
      'landing': 'Landing-Page',
      'blog': 'Blog-Portal'
    }
    
    const serviceType = serviceTypeMap[formData.value.serviceType] || 'Projeto'
    const timestamp = new Date().toISOString().slice(0, 10) // YYYY-MM-DD
    const filename = `Orcamento-Rapido-${serviceType}-${timestamp}.pdf`
    
    // Fazer download do PDF
    doc.save(filename)
    
    successMessage.value = 'PDF gerado e baixado com sucesso!'
    console.log('✅ PDF gerado e baixado:', filename)
    
  } catch (err) {
    console.error('❌ Erro ao gerar PDF:', err)
    error.value = 'Erro ao gerar PDF: ' + err.message
  }
}

const promptEmailAndSend = async () => {
  const email = prompt('Digite o email para envio do orçamento:')
  if (!email) return
  
  if (!email.includes('@')) {
    error.value = 'Email inválido'
    return
  }
  
  try {
    successMessage.value = ''
    error.value = ''
    
    const emailData = {
      quote: generatedQuote.value,
      ai_analysis: aiAnalysis.value,
      email: email
    }
    
    const response = await chatAPI.sendEmail(emailData)
    
    if (response.data.success) {
      successMessage.value = response.data.message
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
  successMessage.value = ''
}

const goToDashboard = () => {
  router.push('/dashboard')
}

const forceCloseSelect = (event) => {
  // Força o select a fechar após seleção - método mais agressivo
  const select = event.target
  select.blur()
  
  // Força fechamento com timeout
  setTimeout(() => {
    select.blur()
    document.activeElement.blur()
  }, 50)
  
  console.log('Select changed:', event.target.value)
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

const saveQuoteToLocalStorage = (quoteData) => {
  try {
    const existingQuotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    existingQuotes.push(quoteData)
    localStorage.setItem('generatedQuotes', JSON.stringify(existingQuotes))
    console.log('💾 Orçamento salvo no localStorage')
  } catch (error) {
    console.error('❌ Erro ao salvar orçamento:', error)
  }
}
</script>

<style scoped>
select {
  -webkit-appearance: menulist !important;
  -moz-appearance: menulist !important;
  appearance: menulist !important;
  background-color: white !important;
  cursor: pointer !important;
  border: 1px solid #d1d5db !important;
  border-radius: 8px !important;
  max-height: 200px !important;
  overflow-y: auto !important;
}

select:focus {
  outline: 2px solid #3b82f6 !important;
  outline-offset: -2px !important;
  border-color: #3b82f6 !important;
}

select:not(:focus) {
  height: auto !important;
  max-height: 48px !important;
}

select option {
  background-color: white !important;
  color: black !important;
  padding: 8px 12px !important;
  border: none !important;
}

/* Força fechamento em WebKit browsers */
select::-webkit-details-marker {
  display: none !important;
}

/* Força fechamento em todos os browsers */
select[size="1"]:focus {
  size: 1 !important;
}
</style>