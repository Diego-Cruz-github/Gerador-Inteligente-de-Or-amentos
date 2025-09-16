<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 py-8">
    <div class="max-w-5xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-8">
        <div class="flex items-center justify-center mb-4">
          <div class="bg-gradient-to-r from-green-600 to-blue-600 p-3 rounded-lg mr-4">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
          <div class="text-left">
            <h1 class="text-3xl font-bold text-gray-900 mb-1">
              Orçamento Detalhado com Pesquisa de Mercado
            </h1>
            <div class="flex items-center text-sm text-gray-600">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
              Análise Avançada de Mercado
            </div>
          </div>
        </div>
        <p class="text-gray-600 max-w-3xl mx-auto mb-4">
          Interface profissional com análise automática de preços praticados no mercado, comparação com concorrência e insights avançados de IA
        </p>
        <div class="bg-green-100 border border-green-300 rounded-lg p-4 inline-block">
          <div class="flex items-center text-green-800">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <span class="font-medium">Inclui pesquisa automática na internet + comparação com concorrência</span>
          </div>
        </div>
        
        <!-- Navigation hint -->
        <div class="mt-2 text-sm text-gray-600">
          <router-link to="/" class="text-blue-600 hover:text-blue-800 underline">
            ← Voltar para Orçamento Rápido
          </router-link>
        </div>
      </div>

      <!-- Main Form Card -->
      <div class="bg-white rounded-xl shadow-lg p-8 mb-8 border-l-4 border-green-500">
        <h2 class="text-xl font-semibold text-gray-800 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Dados Detalhados do Projeto
        </h2>

        <form @submit.prevent="generateDetailedQuote" class="space-y-6">
          <!-- Service Type with more options -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Tipo de Serviço * <span class="text-green-600">(Versão Detalhada)</span>
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
              <option value="app">Aplicativo Mobile (iOS/Android)</option>
              <option value="sistema">Sistema Web / Dashboard</option>
              <option value="landing">Landing Page Profissional</option>
              <option value="blog">Blog / Portal de Conteúdo</option>
              <option value="api">API / Microserviços</option>
              <option value="erp">Sistema ERP</option>
              <option value="crm">Sistema CRM</option>
            </select>
          </div>

          <!-- Complexity Level (new for detailed) -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Nível de Complexidade * <span class="text-green-600">(Análise Detalhada)</span>
            </label>
            <select
              v-model="formData.complexity"
              required
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione a complexidade</option>
              <option value="baixa">Baixa - Projeto simples e direto</option>
              <option value="media">Média - Funcionalidades moderadas</option>
              <option value="alta">Alta - Sistema complexo com integrações</option>
              <option value="enterprise">Enterprise - Solução corporativa avançada</option>
            </select>
          </div>

          <!-- Expected Users (new for detailed) -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Usuários Esperados * <span class="text-green-600">(Para dimensionamento)</span>
            </label>
            <select
              v-model="formData.expectedUsers"
              required
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione o número de usuários</option>
              <option value="small">Pequeno (até 100 usuários)</option>
              <option value="medium">Médio (100 - 1.000 usuários)</option>
              <option value="large">Grande (1.000 - 10.000 usuários)</option>
              <option value="enterprise">Enterprise (10.000+ usuários)</option>
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
              <option value="flexible">Flexível (sem pressa)</option>
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
              Faixa de Investimento *
            </label>
            <select
              v-model="formData.budgetTier"
              required
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione a faixa de investimento</option>
              <option value="economico">Econômico - Foco em custo-benefício</option>
              <option value="padrao">Padrão - Recursos completos</option>
              <option value="premium">Premium - Tecnologia de ponta</option>
              <option value="enterprise">Enterprise - Solução corporativa</option>
            </select>
          </div>

          <!-- Market Research Options (new for detailed) -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Opções de Pesquisa de Mercado * <span class="text-green-600">(Exclusivo Detalhado)</span>
            </label>
            <div class="space-y-3">
              <label class="flex items-center">
                <input type="checkbox" v-model="formData.includeCompetitorAnalysis" class="mr-2">
                <span>Análise de concorrentes diretos</span>
              </label>
              <label class="flex items-center">
                <input type="checkbox" v-model="formData.includePricingTrends" class="mr-2">
                <span>Tendências de preços no mercado</span>
              </label>
              <label class="flex items-center">
                <input type="checkbox" v-model="formData.includeTechTrends" class="mr-2">
                <span>Tecnologias mais utilizadas no setor</span>
              </label>
              <label class="flex items-center">
                <input type="checkbox" v-model="formData.includeTimeEstimates" class="mr-2">
                <span>Comparação de prazos do mercado</span>
              </label>
            </div>
          </div>

          <!-- Description/Proposal -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Descrição Detalhada do Projeto ou Proposta
            </label>
            <textarea
              v-model="formData.description"
              rows="8"
              placeholder="Descreva seu projeto em detalhes máximos: funcionalidades, integrações necessárias, requisitos técnicos, público-alvo, objetivos de negócio, etc. Quanto mais informações, melhor será a pesquisa de mercado e análise..."
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors"
            ></textarea>
            <p class="text-sm text-green-600 mt-1 flex items-start">
              <svg class="w-4 h-4 mr-1 mt-0.5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <span><strong>Pesquisa de Mercado:</strong> Quanto mais detalhes, mais precisa será a comparação com concorrentes e análise de preços praticados</span>
            </p>
          </div>

          <!-- Submit Button -->
          <div class="pt-4">
            <button
              type="submit"
              :disabled="isLoading || !isFormValid"
              class="w-full bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white font-medium py-4 px-6 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 flex items-center justify-center space-x-2"
            >
              <svg v-if="isLoading" class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <span v-if="isLoading">Pesquisando no mercado e analisando...</span>
              <span v-else>Gerar Orçamento Detalhado + Pesquisa de Mercado</span>
            </button>
          </div>
        </form>
      </div>

      <!-- Quote Result -->
      <div v-if="generatedQuote" class="bg-white rounded-xl shadow-lg p-8 border-l-4 border-green-500">
        <h2 class="text-xl font-semibold text-gray-800 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          Orçamento Detalhado + Pesquisa de Mercado
        </h2>

        <!-- Quote Summary -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div class="text-center p-4 bg-green-50 rounded-lg border border-green-200">
            <div class="text-2xl font-bold text-green-600">
              R$ {{ formatCurrency(generatedQuote.total_cost) }}
            </div>
            <div class="text-sm text-gray-600">Valor Total</div>
          </div>
          <div class="text-center p-4 bg-blue-50 rounded-lg border border-blue-200">
            <div class="text-2xl font-bold text-blue-600">
              {{ generatedQuote.total_hours }}h
            </div>
            <div class="text-sm text-gray-600">Total de Horas</div>
          </div>
          <div class="text-center p-4 bg-purple-50 rounded-lg border border-purple-200">
            <div class="text-2xl font-bold text-purple-600">
              {{ generatedQuote.timeline_weeks }}
            </div>
            <div class="text-sm text-gray-600">Prazo</div>
          </div>
          <div class="text-center p-4 bg-orange-50 rounded-lg border border-orange-200">
            <div class="text-2xl font-bold text-orange-600">
              R$ {{ generatedQuote.hourly_rate }}
            </div>
            <div class="text-sm text-gray-600">Valor/Hora</div>
          </div>
        </div>

        <!-- Market Research Results -->
        <div v-if="marketResearch" class="bg-green-50 border border-green-200 rounded-lg p-6 mb-6">
          <h3 class="font-semibold text-green-900 mb-3 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            Pesquisa de Mercado Automática
          </h3>
          <div class="text-green-800 whitespace-pre-line" v-html="formatMessage(marketResearch)"></div>
        </div>

        <!-- AI Analysis -->
        <div v-if="aiAnalysis" class="bg-blue-50 border border-blue-200 rounded-lg p-6 mb-6">
          <h3 class="font-semibold text-blue-900 mb-3 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
            Análise Detalhada da IA
          </h3>
          <div class="text-blue-800" v-html="formatMessage(aiAnalysis)"></div>
        </div>

        <!-- Action Buttons -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <button
            @click="downloadDetailedPDF"
            class="bg-red-600 hover:bg-red-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <span>PDF Detalhado</span>
          </button>
          <button
            @click="sendDetailedEmail"
            class="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span>Email Completo</span>
          </button>
          <button
            @click="goToDashboard"
            class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <span>Ver Dashboard</span>
          </button>
          <button
            @click="resetForm"
            class="bg-gray-600 hover:bg-gray-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            <span>Novo Orçamento</span>
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
import { useRouter } from 'vue-router'
import { chatAPI } from '@/services/api'
import jsPDF from 'jspdf'

// Router
const router = useRouter()

// Form Data - more detailed
const formData = ref({
  serviceType: '',
  complexity: '',
  expectedUsers: '',
  urgency: '',
  location: '',
  budgetTier: '',
  description: '',
  includeCompetitorAnalysis: true,
  includePricingTrends: true,
  includeTechTrends: false,
  includeTimeEstimates: true
})

// State
const isLoading = ref(false)
const generatedQuote = ref(null)
const aiAnalysis = ref('')
const marketResearch = ref('')
const error = ref('')

// Computed
const isFormValid = computed(() => {
  return formData.value.serviceType && 
         formData.value.complexity &&
         formData.value.expectedUsers &&
         formData.value.urgency && 
         formData.value.location && 
         formData.value.budgetTier
})

// Methods
const generateDetailedQuote = async () => {
  try {
    isLoading.value = true
    error.value = ''
    
    console.log('📋 Enviando dados detalhados:', formData.value)
    
    // Preparar dados com informações adicionais para pesquisa de mercado
    const detailedData = {
      ...formData.value,
      detailed_mode: true,
      market_research_options: {
        competitor_analysis: formData.value.includeCompetitorAnalysis,
        pricing_trends: formData.value.includePricingTrends,
        tech_trends: formData.value.includeTechTrends,
        time_estimates: formData.value.includeTimeEstimates
      }
    }
    
    // Chamar endpoint específico para orçamento detalhado
    const response = await chatAPI.generateDetailedFromForm(detailedData)
    
    if (response.data.success) {
      generatedQuote.value = response.data.quote
      aiAnalysis.value = response.data.ai_analysis || ''
      marketResearch.value = response.data.market_research || ''
      
      // Salvar no localStorage para dashboard
      saveQuoteToLocalStorage({
        quote: generatedQuote.value,
        aiAnalysis: aiAnalysis.value,
        marketResearch: marketResearch.value,
        serviceType: formData.value.serviceType,
        complexity: formData.value.complexity,
        expectedUsers: formData.value.expectedUsers,
        urgency: formData.value.urgency,
        location: formData.value.location,
        budgetTier: formData.value.budgetTier,
        description: formData.value.description,
        isDetailed: true,
        createdAt: new Date().toISOString()
      })
      
      console.log('✅ Orçamento detalhado gerado:', response.data)
    } else {
      throw new Error(response.data.error || 'Erro desconhecido')
    }
    
  } catch (err) {
    console.error('❌ Erro ao gerar orçamento detalhado:', err)
    error.value = err.response?.data?.error || err.message || 'Erro ao gerar orçamento detalhado'
  } finally {
    isLoading.value = false
  }
}

const downloadDetailedPDF = async () => {
  try {
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
    doc.text('Orçamento Detalhado + Pesquisa de Mercado', 20, 30)
    
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
    
    // Pesquisa de Mercado
    if (marketResearch.value) {
      const yPos = aiAnalysis.value ? 180 : 125
      doc.setFontSize(16)
      doc.text('Pesquisa de Mercado', 20, yPos)
      doc.setFontSize(10)
      const marketText = marketResearch.value.replace(/\*\*(.*?)\*\*/g, '$1').replace(/<br>/g, '\n')
      const splitMarket = doc.splitTextToSize(marketText, 170)
      doc.text(splitMarket, 20, yPos + 10)
    }
    
    // Gerar nome do arquivo baseado no tipo de serviço
    const serviceTypeMap = {
      'website': 'Website-Institucional',
      'ecommerce': 'E-commerce',
      'app': 'App-Mobile',
      'sistema': 'Sistema-Web',
      'landing': 'Landing-Page',
      'blog': 'Blog-Portal',
      'api': 'API-Microservicos',
      'erp': 'Sistema-ERP',
      'crm': 'Sistema-CRM'
    }
    
    const serviceType = serviceTypeMap[formData.value.serviceType] || 'Projeto'
    const timestamp = new Date().toISOString().slice(0, 10) // YYYY-MM-DD
    const filename = `Orcamento-Detalhado-${serviceType}-${timestamp}.pdf`
    
    // Fazer download do PDF
    doc.save(filename)
    
    console.log('✅ PDF detalhado gerado e baixado:', filename)
    
  } catch (err) {
    console.error('❌ Erro ao gerar PDF:', err)
    error.value = 'Erro ao gerar PDF: ' + err.message
  }
}

const sendDetailedEmail = async () => {
  const email = prompt('Digite o email para envio do orçamento detalhado:')
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
      market_research: marketResearch.value,
      email: email
    }
    
    const response = await chatAPI.sendEmail(emailData)
    
    if (response.data.success) {
      alert(`Orçamento detalhado enviado para ${email} com sucesso!`)
    }
  } catch (err) {
    error.value = 'Erro ao enviar email: ' + (err.response?.data?.error || err.message)
  }
}

const resetForm = () => {
  formData.value = {
    serviceType: '',
    complexity: '',
    expectedUsers: '',
    urgency: '',
    location: '',
    budgetTier: '',
    description: '',
    includeCompetitorAnalysis: true,
    includePricingTrends: true,
    includeTechTrends: false,
    includeTimeEstimates: true
  }
  generatedQuote.value = null
  aiAnalysis.value = ''
  marketResearch.value = ''
  error.value = ''
}

const goToDashboard = () => {
  router.push('/dashboard')
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

const saveQuoteToLocalStorage = (quoteData) => {
  try {
    const existingQuotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    existingQuotes.push(quoteData)
    localStorage.setItem('generatedQuotes', JSON.stringify(existingQuotes))
    console.log('💾 Orçamento detalhado salvo no localStorage')
  } catch (error) {
    console.error('❌ Erro ao salvar orçamento:', error)
  }
}
</script>

<style scoped>
/* Estilos específicos para forçar fechamento dos selects */
select {
  -webkit-appearance: menulist !important;
  -moz-appearance: menulist !important;
  appearance: menulist !important;
  background-color: white !important;
  cursor: pointer !important;
  max-height: 48px !important;
}

select:focus {
  outline: 2px solid #10b981 !important;
  outline-offset: -2px !important;
}

select:not(:focus) {
  height: auto !important;
  max-height: 48px !important;
  overflow: hidden !important;
}

select option {
  background-color: white !important;
  color: black !important;
  padding: 8px !important;
}

/* Força fechamento específico para WebKit */
select::-webkit-details-marker {
  display: none !important;
}

select[aria-expanded="true"]:not(:focus) {
  aria-expanded: false !important;
}
</style>