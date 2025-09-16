<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-7xl mx-auto px-4">
      <!-- Header -->
      <div class="mb-8">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-3xl font-bold text-gray-900 mb-2">Dashboard de Orçamentos</h1>
            <p class="text-gray-600">Visualize e gerencie todos os orçamentos gerados nesta sessão</p>
          </div>
          <button
            @click="clearAllQuotes"
            v-if="quotes.length > 0"
            class="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-lg transition-colors flex items-center space-x-2"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
            <span>Limpar Tudo</span>
          </button>
        </div>

        <!-- Statistics Cards -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mt-6" v-if="quotes.length > 0">
          <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <div class="flex items-center">
              <div class="bg-blue-100 p-2 rounded-lg mr-3">
                <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div>
                <p class="text-2xl font-bold text-gray-900">{{ quotes.length }}</p>
                <p class="text-sm text-gray-600">Orçamentos Gerados</p>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <div class="flex items-center">
              <div class="bg-green-100 p-2 rounded-lg mr-3">
                <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
                </svg>
              </div>
              <div>
                <p class="text-2xl font-bold text-gray-900">R$ {{ formatCurrency(totalValue) }}</p>
                <p class="text-sm text-gray-600">Valor Total</p>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <div class="flex items-center">
              <div class="bg-purple-100 p-2 rounded-lg mr-3">
                <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <p class="text-2xl font-bold text-gray-900">{{ totalHours }}h</p>
                <p class="text-sm text-gray-600">Total de Horas</p>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <div class="flex items-center">
              <div class="bg-orange-100 p-2 rounded-lg mr-3">
                <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <div>
                <p class="text-2xl font-bold text-gray-900">R$ {{ averageHourlyRate }}</p>
                <p class="text-sm text-gray-600">Valor/Hora Médio</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Reports Section -->
        <div v-if="quotes.length > 0" class="mt-8">
          <div class="bg-white rounded-xl shadow-lg p-6 border border-gray-200">
            <div class="flex items-center justify-between mb-6">
              <div>
                <h2 class="text-xl font-semibold text-gray-900 flex items-center">
                  <svg class="w-6 h-6 mr-2 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                  Sistema de Relatórios
                </h2>
                <p class="text-gray-600">Gere relatórios personalizados e análises dos seus orçamentos</p>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <!-- Relatório Geral -->
              <button
                @click="generateGeneralReport"
                class="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-medium py-4 px-6 rounded-lg transition-all duration-200 flex flex-col items-center space-y-2"
              >
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <span class="text-center">Relatório Geral</span>
                <span class="text-xs opacity-80">Estatísticas gerais</span>
              </button>

              <!-- Relatório por Tipo de Serviço -->
              <button
                @click="generateServiceReport"
                class="bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 text-white font-medium py-4 px-6 rounded-lg transition-all duration-200 flex flex-col items-center space-y-2"
              >
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <span class="text-center">Por Tipo de Serviço</span>
                <span class="text-xs opacity-80">Análise por categoria</span>
              </button>

              <!-- Relatório de Preços -->
              <button
                @click="generatePricingReport"
                class="bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-700 hover:to-purple-800 text-white font-medium py-4 px-6 rounded-lg transition-all duration-200 flex flex-col items-center space-y-2"
              >
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
                </svg>
                <span class="text-center">Análise de Preços</span>
                <span class="text-xs opacity-80">Tendências de valor</span>
              </button>

              <!-- Relatório Comparativo -->
              <button
                @click="generateComparativeReport"
                class="bg-gradient-to-r from-orange-600 to-orange-700 hover:from-orange-700 hover:to-orange-800 text-white font-medium py-4 px-6 rounded-lg transition-all duration-200 flex flex-col items-center space-y-2"
              >
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <span class="text-center">Comparativo</span>
                <span class="text-xs opacity-80">Rápido vs Detalhado</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="quotes.length === 0" class="text-center py-12">
        <div class="bg-white rounded-xl shadow-lg p-8">
          <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 class="text-lg font-medium text-gray-900 mb-2">Nenhum orçamento gerado ainda</h3>
          <p class="text-gray-600 mb-6">Crie seu primeiro orçamento para vê-lo aparecer aqui no dashboard</p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link 
              to="/" 
              class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              <span>Orçamento Rápido</span>
            </router-link>
            <router-link 
              to="/detailed-app" 
              class="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <span>Orçamento Detalhado</span>
            </router-link>
          </div>
        </div>
      </div>

      <!-- Quotes List -->
      <div v-if="quotes.length > 0" class="space-y-6">
        <div 
          v-for="(quote, index) in quotes" 
          :key="index"
          class="bg-white rounded-xl shadow-lg p-6 border border-gray-200"
        >
          <!-- Quote Header -->
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-3">
              <div class="bg-gradient-to-r from-blue-600 to-purple-600 p-2 rounded-lg">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-semibold text-gray-900">
                  {{ getServiceTypeName(quote.serviceType) }}
                  <span v-if="quote.isDetailed" class="ml-2 px-2 py-1 bg-green-100 text-green-800 text-xs font-semibold rounded-full">
                    DETALHADO
                  </span>
                </h3>
                <p class="text-sm text-gray-600">Gerado em {{ formatDate(quote.createdAt) }}</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <button
                @click="downloadQuotePDF(quote, index)"
                class="bg-red-600 hover:bg-red-700 text-white p-2 rounded-lg transition-colors"
                title="Baixar PDF"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </button>
              <button
                @click="removeQuote(index)"
                class="bg-gray-600 hover:bg-gray-700 text-white p-2 rounded-lg transition-colors"
                title="Remover"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Quote Summary -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
            <div class="text-center p-3 bg-green-50 rounded-lg border border-green-200">
              <div class="text-lg font-bold text-green-600">
                R$ {{ formatCurrency(quote.quote.total_cost) }}
              </div>
              <div class="text-xs text-gray-600">Valor Total</div>
            </div>
            <div class="text-center p-3 bg-blue-50 rounded-lg border border-blue-200">
              <div class="text-lg font-bold text-blue-600">
                {{ quote.quote.total_hours }}h
              </div>
              <div class="text-xs text-gray-600">Total de Horas</div>
            </div>
            <div class="text-center p-3 bg-purple-50 rounded-lg border border-purple-200">
              <div class="text-lg font-bold text-purple-600">
                {{ quote.quote.timeline_weeks }}
              </div>
              <div class="text-xs text-gray-600">Prazo</div>
            </div>
            <div class="text-center p-3 bg-orange-50 rounded-lg border border-orange-200">
              <div class="text-lg font-bold text-orange-600">
                R$ {{ quote.quote.hourly_rate }}
              </div>
              <div class="text-xs text-gray-600">Valor/Hora</div>
            </div>
          </div>

          <!-- Quote Details (Collapsible) -->
          <div class="border-t border-gray-200 pt-4">
            <button
              @click="toggleDetails(index)"
              class="flex items-center justify-between w-full text-left hover:bg-gray-50 p-2 rounded-lg transition-colors"
            >
              <span class="text-sm font-medium text-gray-700 flex items-center">
                <svg class="w-4 h-4 mr-2 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {{ quote.showDetails ? 'Ocultar detalhes' : 'Ver detalhes completos' }}
              </span>
              <svg 
                class="w-4 h-4 text-gray-500 transition-transform duration-200"
                :class="{ 'rotate-180': quote.showDetails }"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            
            <div v-if="quote.showDetails" class="mt-4 space-y-4">
              <!-- Form Data -->
              <div class="bg-gray-50 rounded-lg p-4">
                <h4 class="font-medium text-gray-900 mb-2">Dados do Projeto</h4>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
                  <div><strong>Tipo de Serviço:</strong> {{ getServiceTypeName(quote.serviceType) }}</div>
                  <div><strong>Urgência:</strong> {{ getUrgencyName(quote.urgency) }}</div>
                  <div><strong>Localização:</strong> {{ getLocationName(quote.location) }}</div>
                  <div><strong>Faixa de Orçamento:</strong> {{ getBudgetTierName(quote.budgetTier) }}</div>
                  <div v-if="quote.complexity" class="md:col-span-2"><strong>Complexidade:</strong> {{ getComplexityName(quote.complexity) }}</div>
                  <div v-if="quote.expectedUsers" class="md:col-span-2"><strong>Usuários Esperados:</strong> {{ getUsersName(quote.expectedUsers) }}</div>
                </div>
                <div v-if="quote.description" class="mt-3">
                  <strong>Descrição:</strong>
                  <p class="text-gray-700 mt-1">{{ quote.description }}</p>
                </div>
              </div>

              <!-- AI Analysis -->
              <div v-if="quote.aiAnalysis" class="bg-blue-50 rounded-lg p-4 border border-blue-200">
                <h4 class="font-medium text-blue-900 mb-2">Análise da IA</h4>
                <div class="text-blue-800 text-sm" v-html="formatMessage(quote.aiAnalysis)"></div>
              </div>

              <!-- Market Research -->
              <div v-if="quote.marketResearch" class="bg-green-50 rounded-lg p-4 border border-green-200">
                <h4 class="font-medium text-green-900 mb-2">Pesquisa de Mercado</h4>
                <div class="text-green-800 text-sm" v-html="formatMessage(quote.marketResearch)"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import jsPDF from 'jspdf'

// State
const quotes = ref([])

// Computed
const totalValue = computed(() => {
  return quotes.value.reduce((sum, quote) => sum + quote.quote.total_cost, 0)
})

const totalHours = computed(() => {
  return quotes.value.reduce((sum, quote) => sum + quote.quote.total_hours, 0)
})

const averageHourlyRate = computed(() => {
  if (quotes.value.length === 0) return 0
  const totalRate = quotes.value.reduce((sum, quote) => sum + parseFloat(quote.quote.hourly_rate), 0)
  return Math.round(totalRate / quotes.value.length)
})

// Methods
const loadQuotes = () => {
  try {
    const savedQuotes = localStorage.getItem('generatedQuotes')
    if (savedQuotes) {
      quotes.value = JSON.parse(savedQuotes)
    }
  } catch (error) {
    console.error('Erro ao carregar orçamentos:', error)
  }
}

const clearAllQuotes = () => {
  if (confirm('Tem certeza que deseja limpar todos os orçamentos? Esta ação não pode ser desfeita.')) {
    quotes.value = []
    localStorage.removeItem('generatedQuotes')
  }
}

const removeQuote = (index) => {
  if (confirm('Tem certeza que deseja remover este orçamento?')) {
    quotes.value.splice(index, 1)
    localStorage.setItem('generatedQuotes', JSON.stringify(quotes.value))
  }
}

const toggleDetails = (index) => {
  quotes.value[index].showDetails = !quotes.value[index].showDetails
}

const downloadQuotePDF = (quote, index) => {
  try {
    // Criar PDF usando jsPDF
    const doc = new jsPDF()
    
    // Header
    doc.setFontSize(20)
    doc.setTextColor(59, 130, 246) // blue-600
    const title = quote.isDetailed ? 'Orçamento Detalhado + Pesquisa de Mercado' : 'Orçamento Rápido - Gerador Inteligente'
    doc.text(title, 20, 30)
    
    doc.setFontSize(12)
    doc.setTextColor(107, 114, 128) // gray-500
    doc.text('Gerado em: ' + formatDate(quote.createdAt), 20, 40)
    
    // Dados do orçamento
    doc.setFontSize(16)
    doc.setTextColor(0, 0, 0)
    doc.text('Resumo do Orçamento', 20, 60)
    
    doc.setFontSize(12)
    doc.text(`Valor Total: R$ ${formatCurrency(quote.quote.total_cost)}`, 20, 75)
    doc.text(`Total de Horas: ${quote.quote.total_hours}h`, 20, 85)
    doc.text(`Prazo: ${quote.quote.timeline_weeks}`, 20, 95)
    doc.text(`Valor/Hora: R$ ${quote.quote.hourly_rate}`, 20, 105)
    
    // Análise da IA
    if (quote.aiAnalysis) {
      doc.setFontSize(16)
      doc.text('Análise da IA', 20, 125)
      doc.setFontSize(10)
      const aiText = quote.aiAnalysis.replace(/\*\*(.*?)\*\*/g, '$1').replace(/<br>/g, '\n')
      const splitAI = doc.splitTextToSize(aiText, 170)
      doc.text(splitAI, 20, 135)
    }
    
    // Pesquisa de Mercado
    if (quote.marketResearch) {
      const yPos = quote.aiAnalysis ? 180 : 125
      doc.setFontSize(16)
      doc.text('Pesquisa de Mercado', 20, yPos)
      doc.setFontSize(10)
      const marketText = quote.marketResearch.replace(/\*\*(.*?)\*\*/g, '$1').replace(/<br>/g, '\n')
      const splitMarket = doc.splitTextToSize(marketText, 170)
      doc.text(splitMarket, 20, yPos + 10)
    }
    
    // Gerar nome do arquivo
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
    
    const serviceType = serviceTypeMap[quote.serviceType] || 'Projeto'
    const timestamp = new Date(quote.createdAt).toISOString().slice(0, 10)
    const prefix = quote.isDetailed ? 'Orcamento-Detalhado' : 'Orcamento-Rapido'
    const filename = `${prefix}-${serviceType}-${timestamp}.pdf`
    
    // Fazer download do PDF
    doc.save(filename)
    
    console.log('✅ PDF baixado:', filename)
    
  } catch (err) {
    console.error('❌ Erro ao gerar PDF:', err)
    alert('Erro ao gerar PDF: ' + err.message)
  }
}

// Helper functions
const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleString('pt-BR')
}

const formatMessage = (content) => {
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>')
}

const getServiceTypeName = (type) => {
  const types = {
    'website': 'Website Institucional',
    'ecommerce': 'E-commerce / Loja Virtual',
    'app': 'Aplicativo Mobile',
    'sistema': 'Sistema Web / Dashboard',
    'landing': 'Landing Page',
    'blog': 'Blog / Portal de Conteúdo',
    'api': 'API / Microserviços',
    'erp': 'Sistema ERP',
    'crm': 'Sistema CRM'
  }
  return types[type] || type
}

const getUrgencyName = (urgency) => {
  const urgencies = {
    'normal': 'Normal',
    'urgent': 'Urgente (7 a 15 dias)',
    'super_urgent': 'Super Urgente (até 7 dias)',
    'flexible': 'Flexível (sem pressa)'
  }
  return urgencies[urgency] || urgency
}

const getLocationName = (location) => {
  const locations = {
    'SP': 'Capital',
    'interior': 'Interior',
    'remoto': 'Remoto',
    'rj': 'Rio de Janeiro',
    'outros_estados': 'Outros Estados'
  }
  return locations[location] || location
}

const getBudgetTierName = (tier) => {
  const tiers = {
    'economico': 'Econômico',
    'padrao': 'Padrão',
    'premium': 'Premium',
    'enterprise': 'Enterprise'
  }
  return tiers[tier] || tier
}

const getComplexityName = (complexity) => {
  const complexities = {
    'baixa': 'Baixa',
    'media': 'Média',
    'alta': 'Alta',
    'enterprise': 'Enterprise'
  }
  return complexities[complexity] || complexity
}

const getUsersName = (users) => {
  const userRanges = {
    'small': 'Pequeno (até 100 usuários)',
    'medium': 'Médio (100 - 1.000 usuários)',
    'large': 'Grande (1.000 - 10.000 usuários)',
    'enterprise': 'Enterprise (10.000+ usuários)'
  }
  return userRanges[users] || users
}

// Report Generation Functions
const generateGeneralReport = () => {
  const doc = new jsPDF()
  
  // Header
  doc.setFontSize(20)
  doc.setTextColor(59, 130, 246)
  doc.text('Relatório Geral de Orçamentos', 20, 30)
  
  doc.setFontSize(12)
  doc.setTextColor(107, 114, 128)
  doc.text('Gerado em: ' + new Date().toLocaleDateString('pt-BR'), 20, 40)
  
  // Statistics
  doc.setFontSize(16)
  doc.setTextColor(0, 0, 0)
  doc.text('Estatísticas Gerais', 20, 60)
  
  doc.setFontSize(12)
  doc.text(`Total de Orçamentos: ${quotes.value.length}`, 20, 75)
  doc.text(`Valor Total dos Projetos: R$ ${formatCurrency(totalValue.value)}`, 20, 85)
  doc.text(`Total de Horas Estimadas: ${totalHours.value}h`, 20, 95)
  doc.text(`Valor/Hora Médio: R$ ${averageHourlyRate.value}`, 20, 105)
  
  // Service breakdown
  const serviceBreakdown = getServiceBreakdown()
  let yPos = 125
  doc.setFontSize(16)
  doc.text('Distribuição por Tipo de Serviço', 20, yPos)
  
  doc.setFontSize(10)
  Object.entries(serviceBreakdown).forEach(([service, data]) => {
    yPos += 15
    doc.text(`${getServiceTypeName(service)}: ${data.count} orçamentos (R$ ${formatCurrency(data.total)})`, 30, yPos)
  })
  
  const filename = `Relatorio-Geral-${new Date().toISOString().slice(0, 10)}.pdf`
  doc.save(filename)
}

const generateServiceReport = () => {
  const doc = new jsPDF()
  const serviceBreakdown = getServiceBreakdown()
  
  doc.setFontSize(20)
  doc.setTextColor(34, 197, 94)
  doc.text('Relatório por Tipo de Serviço', 20, 30)
  
  doc.setFontSize(12)
  doc.setTextColor(107, 114, 128)
  doc.text('Gerado em: ' + new Date().toLocaleDateString('pt-BR'), 20, 40)
  
  let yPos = 60
  Object.entries(serviceBreakdown).forEach(([service, data]) => {
    doc.setFontSize(16)
    doc.setTextColor(0, 0, 0)
    doc.text(getServiceTypeName(service), 20, yPos)
    
    doc.setFontSize(12)
    doc.text(`Quantidade: ${data.count} orçamentos`, 30, yPos + 15)
    doc.text(`Valor Total: R$ ${formatCurrency(data.total)}`, 30, yPos + 25)
    doc.text(`Valor Médio: R$ ${formatCurrency(data.average)}`, 30, yPos + 35)
    doc.text(`Horas Médias: ${Math.round(data.avgHours)}h`, 30, yPos + 45)
    
    yPos += 65
  })
  
  const filename = `Relatorio-Tipos-Servico-${new Date().toISOString().slice(0, 10)}.pdf`
  doc.save(filename)
}

const generatePricingReport = () => {
  const doc = new jsPDF()
  
  doc.setFontSize(20)
  doc.setTextColor(147, 51, 234)
  doc.text('Análise de Preços e Tendências', 20, 30)
  
  doc.setFontSize(12)
  doc.setTextColor(107, 114, 128)
  doc.text('Gerado em: ' + new Date().toLocaleDateString('pt-BR'), 20, 40)
  
  // Price statistics
  const prices = quotes.value.map(q => q.quote.total_cost)
  const minPrice = Math.min(...prices)
  const maxPrice = Math.max(...prices)
  const avgPrice = prices.reduce((a, b) => a + b, 0) / prices.length
  
  doc.setFontSize(16)
  doc.setTextColor(0, 0, 0)
  doc.text('Análise de Preços', 20, 60)
  
  doc.setFontSize(12)
  doc.text(`Menor Valor: R$ ${formatCurrency(minPrice)}`, 20, 75)
  doc.text(`Maior Valor: R$ ${formatCurrency(maxPrice)}`, 20, 85)
  doc.text(`Valor Médio: R$ ${formatCurrency(avgPrice)}`, 20, 95)
  doc.text(`Variação de Preços: R$ ${formatCurrency(maxPrice - minPrice)}`, 20, 105)
  
  // Budget tier analysis
  const budgetTierBreakdown = getBudgetTierBreakdown()
  let yPos = 125
  doc.setFontSize(16)
  doc.text('Distribuição por Faixa de Orçamento', 20, yPos)
  
  doc.setFontSize(10)
  Object.entries(budgetTierBreakdown).forEach(([tier, data]) => {
    yPos += 15
    doc.text(`${getBudgetTierName(tier)}: ${data.count} orçamentos (R$ ${formatCurrency(data.total)})`, 30, yPos)
  })
  
  const filename = `Relatorio-Precos-${new Date().toISOString().slice(0, 10)}.pdf`
  doc.save(filename)
}

const generateComparativeReport = () => {
  const doc = new jsPDF()
  
  const rapidQuotes = quotes.value.filter(q => !q.isDetailed)
  const detailedQuotes = quotes.value.filter(q => q.isDetailed)
  
  doc.setFontSize(20)
  doc.setTextColor(249, 115, 22)
  doc.text('Relatório Comparativo: Rápido vs Detalhado', 20, 30)
  
  doc.setFontSize(12)
  doc.setTextColor(107, 114, 128)
  doc.text('Gerado em: ' + new Date().toLocaleDateString('pt-BR'), 20, 40)
  
  // Rapid quotes stats
  doc.setFontSize(16)
  doc.setTextColor(0, 0, 0)
  doc.text('Orçamentos Rápidos', 20, 60)
  
  if (rapidQuotes.length > 0) {
    const rapidTotal = rapidQuotes.reduce((sum, q) => sum + q.quote.total_cost, 0)
    const rapidAvg = rapidTotal / rapidQuotes.length
    
    doc.setFontSize(12)
    doc.text(`Quantidade: ${rapidQuotes.length}`, 30, 75)
    doc.text(`Valor Total: R$ ${formatCurrency(rapidTotal)}`, 30, 85)
    doc.text(`Valor Médio: R$ ${formatCurrency(rapidAvg)}`, 30, 95)
  } else {
    doc.setFontSize(12)
    doc.text('Nenhum orçamento rápido gerado', 30, 75)
  }
  
  // Detailed quotes stats
  doc.setFontSize(16)
  doc.text('Orçamentos Detalhados', 20, 115)
  
  if (detailedQuotes.length > 0) {
    const detailedTotal = detailedQuotes.reduce((sum, q) => sum + q.quote.total_cost, 0)
    const detailedAvg = detailedTotal / detailedQuotes.length
    
    doc.setFontSize(12)
    doc.text(`Quantidade: ${detailedQuotes.length}`, 30, 130)
    doc.text(`Valor Total: R$ ${formatCurrency(detailedTotal)}`, 30, 140)
    doc.text(`Valor Médio: R$ ${formatCurrency(detailedAvg)}`, 30, 150)
  } else {
    doc.setFontSize(12)
    doc.text('Nenhum orçamento detalhado gerado', 30, 130)
  }
  
  const filename = `Relatorio-Comparativo-${new Date().toISOString().slice(0, 10)}.pdf`
  doc.save(filename)
}

// Helper functions for reports
const getServiceBreakdown = () => {
  const breakdown = {}
  quotes.value.forEach(quote => {
    const service = quote.serviceType
    if (!breakdown[service]) {
      breakdown[service] = { count: 0, total: 0, totalHours: 0 }
    }
    breakdown[service].count++
    breakdown[service].total += quote.quote.total_cost
    breakdown[service].totalHours += quote.quote.total_hours
  })
  
  // Calculate averages
  Object.keys(breakdown).forEach(service => {
    breakdown[service].average = breakdown[service].total / breakdown[service].count
    breakdown[service].avgHours = breakdown[service].totalHours / breakdown[service].count
  })
  
  return breakdown
}

const getBudgetTierBreakdown = () => {
  const breakdown = {}
  quotes.value.forEach(quote => {
    const tier = quote.budgetTier
    if (!breakdown[tier]) {
      breakdown[tier] = { count: 0, total: 0 }
    }
    breakdown[tier].count++
    breakdown[tier].total += quote.quote.total_cost
  })
  return breakdown
}

// Lifecycle
onMounted(() => {
  loadQuotes()
})
</script>