<template>
  <div class="bg-gray-100 min-h-screen">
    <!-- ERP-style Breadcrumb -->
    <div class="bg-white border-b border-gray-200 px-6 py-4">
      <div class="flex items-center justify-between">
        <div>
          <nav class="flex" aria-label="Breadcrumb">
            <ol class="flex items-center space-x-4">
              <li>
                <div class="flex items-center">
                  <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2-2z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5v4" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v4" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 5v4" />
                  </svg>
                  <span class="ml-2 text-sm font-medium text-gray-500">Configurações</span>
                </div>
              </li>
              <li>
                <div class="flex items-center">
                  <svg class="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                  <span class="ml-2 text-sm font-medium text-gray-900">Integração BI</span>
                </div>
              </li>
            </ol>
          </nav>
          <h1 class="mt-2 text-2xl font-bold text-gray-900">Integração com Business Intelligence</h1>
          <p class="mt-1 text-sm text-gray-500">Configure e teste conexões com ferramentas de BI</p>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 py-8">
      <!-- API Status -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-semibold text-gray-900 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Status da API
          </h3>
          <button 
            @click="checkApiStatus"
            :disabled="loading"
            class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors disabled:opacity-50"
          >
            <span v-if="loading">Verificando...</span>
            <span v-else>Verificar Conexão</span>
          </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="flex items-center p-4 bg-gray-50 rounded-lg">
            <div :class="apiStatus.connected ? 'bg-green-100' : 'bg-red-100'" class="p-2 rounded-full mr-3">
              <svg class="w-5 h-5" :class="apiStatus.connected ? 'text-green-600' : 'text-red-600'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" v-if="apiStatus.connected" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" v-else />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-gray-700">Conexão API</p>
              <p :class="apiStatus.connected ? 'text-green-600' : 'text-red-600'" class="text-sm">
                {{ apiStatus.connected ? 'Conectado' : 'Desconectado' }}
              </p>
            </div>
          </div>
          
          <div class="flex items-center p-4 bg-gray-50 rounded-lg">
            <div class="bg-blue-100 p-2 rounded-full mr-3">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-gray-700">Endpoints</p>
              <p class="text-blue-600 text-sm">{{ totalEndpoints }} disponíveis</p>
            </div>
          </div>
          
          <div class="flex items-center p-4 bg-gray-50 rounded-lg">
            <div class="bg-purple-100 p-2 rounded-full mr-3">
              <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4" />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-gray-700">Última Atualização</p>
              <p class="text-purple-600 text-sm">{{ lastUpdate }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Available Endpoints -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
        <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
          </svg>
          Endpoints Disponíveis
        </h3>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div v-for="endpoint in endpoints" :key="endpoint.name" class="border border-gray-200 rounded-lg p-4">
            <div class="flex items-center justify-between mb-2">
              <h4 class="font-semibold text-gray-900">{{ endpoint.name }}</h4>
              <button 
                @click="testEndpoint(endpoint)"
                :disabled="loading"
                class="px-3 py-1 bg-green-600 hover:bg-green-700 text-white text-sm rounded transition-colors disabled:opacity-50"
              >
                Testar
              </button>
            </div>
            <p class="text-sm text-gray-600 mb-3">{{ endpoint.description }}</p>
            <div class="bg-gray-50 p-3 rounded text-sm font-mono text-gray-700">
              <div class="flex items-center justify-between">
                <span>{{ endpoint.url }}</span>
                <button 
                  @click="copyToClipboard(endpoint.url)"
                  class="text-blue-600 hover:text-blue-800"
                  title="Copiar URL"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- BI Tools Integration Guide -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
        <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
          </svg>
          Guia de Integração
        </h3>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Power BI -->
          <div class="border border-gray-200 rounded-lg p-4">
            <div class="flex items-center mb-3">
              <div class="bg-yellow-100 p-2 rounded mr-3">
                <svg class="w-6 h-6 text-yellow-600" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M10.5 2v20l11-10-11-10z"/>
                </svg>
              </div>
              <h4 class="font-semibold text-gray-900">Power BI</h4>
            </div>
            <div class="space-y-2 text-sm text-gray-600">
              <p>1. Abra Power BI Desktop</p>
              <p>2. Obter Dados → Web</p>
              <p>3. Cole a URL do endpoint</p>
              <p>4. Configure atualização automática</p>
            </div>
            <button 
              @click="downloadPowerBITemplate"
              class="mt-3 w-full px-3 py-2 bg-yellow-600 hover:bg-yellow-700 text-white text-sm rounded transition-colors"
            >
              Download Template
            </button>
          </div>

          <!-- Data Studio (Google) -->
          <div class="border border-gray-200 rounded-lg p-4">
            <div class="flex items-center mb-3">
              <div class="bg-green-100 p-2 rounded mr-3">
                <svg class="w-6 h-6 text-green-600" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                </svg>
              </div>
              <h4 class="font-semibold text-gray-900">Data Studio (Google)</h4>
            </div>
            <div class="space-y-2 text-sm text-gray-600">
              <p>1. Criar → Fonte de dados</p>
              <p>2. Conector → URL file</p>
              <p>3. Use endpoint CSV</p>
              <p>4. Conectar e criar relatório</p>
            </div>
            <button 
              @click="openDataStudio"
              class="mt-3 w-full px-3 py-2 bg-green-600 hover:bg-green-700 text-white text-sm rounded transition-colors"
            >
              Abrir Data Studio
            </button>
          </div>

        </div>
      </div>

      <!-- Real-time Data Preview -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-semibold text-gray-900 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
            Preview dos Dados
          </h3>
          <button 
            @click="refreshPreview"
            :disabled="loading"
            class="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg transition-colors disabled:opacity-50"
          >
            Atualizar
          </button>
        </div>
        
        <div v-if="previewData" class="overflow-x-auto">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="text-sm text-blue-600 font-medium">Total de Orçamentos</p>
              <p class="text-2xl font-bold text-blue-900">{{ previewData.summary?.total_quotes || 0 }}</p>
            </div>
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="text-sm text-green-600 font-medium">Trabalhos Fechados</p>
              <p class="text-2xl font-bold text-green-900">{{ previewData.summary?.total_closed_jobs || 0 }}</p>
            </div>
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="text-sm text-purple-600 font-medium">Taxa de Conversão</p>
              <p class="text-2xl font-bold text-purple-900">{{ previewData.summary?.conversion_rate || 0 }}%</p>
            </div>
            <div class="bg-orange-50 p-4 rounded-lg">
              <p class="text-sm text-orange-600 font-medium">Receita Total</p>
              <p class="text-2xl font-bold text-orange-900">R$ {{ formatCurrency(previewData.summary?.total_revenue || 0) }}</p>
            </div>
          </div>
          
          <pre class="bg-gray-50 p-4 rounded text-sm overflow-auto max-h-64">{{ JSON.stringify(previewData, null, 2) }}</pre>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          Clique em "Atualizar" para carregar preview dos dados
        </div>
      </div>
    </div>

    <!-- Success/Error Messages -->
    <div 
      v-if="message" 
      :class="messageType === 'success' ? 'bg-green-100 border-green-400 text-green-700' : 'bg-red-100 border-red-400 text-red-700'"
      class="fixed bottom-4 right-4 border px-4 py-3 rounded-lg shadow-lg max-w-md"
    >
      {{ message }}
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAnalyticsSync } from '@/composables/useAnalyticsSync.js'

// Composables
const { syncLocalStorageToAPI, watchLocalStorage } = useAnalyticsSync()

// State
const loading = ref(false)
const message = ref('')
const messageType = ref('success')
const apiStatus = ref({ connected: false })
const previewData = ref(null)
const lastUpdate = ref('Nunca')

// API Base URL
const API_BASE = 'http://localhost:5000'

// Computed
const totalEndpoints = computed(() => endpoints.value.length)

// Endpoints Configuration
const endpoints = ref([
  {
    name: 'Resumo Analytics',
    description: 'KPIs principais e métricas resumidas',
    url: `${API_BASE}/api/analytics/summary`,
    method: 'GET'
  },
  {
    name: 'Série Temporal',
    description: 'Dados históricos para gráficos de tendência',
    url: `${API_BASE}/api/analytics/time-series`,
    method: 'GET'
  },
  {
    name: 'Trabalhos Detalhados',
    description: 'Lista completa de orçamentos e trabalhos',
    url: `${API_BASE}/api/analytics/detailed-jobs`,
    method: 'GET'
  },
  {
    name: 'KPIs Executivos',
    description: 'Indicadores chave para dashboards executivos',
    url: `${API_BASE}/api/analytics/kpis`,
    method: 'GET'
  },
  {
    name: 'Exportação CSV',
    description: 'Dados em formato CSV para importação',
    url: `${API_BASE}/api/analytics/export/csv`,
    method: 'GET'
  },
  {
    name: 'Configuração BI',
    description: 'Metadados e esquema da API',
    url: `${API_BASE}/api/analytics/config`,
    method: 'GET'
  }
])

// Methods
const showMessage = (text, type = 'success') => {
  message.value = text
  messageType.value = type
  setTimeout(() => {
    message.value = ''
  }, 3000)
}

const checkApiStatus = async () => {
  loading.value = true
  try {
    const response = await fetch(`${API_BASE}/health`)
    const data = await response.json()
    apiStatus.value.connected = response.ok && data.status === 'OK'
    showMessage(apiStatus.value.connected ? 'API conectada com sucesso!' : 'Falha na conexão com API', 
              apiStatus.value.connected ? 'success' : 'error')
    lastUpdate.value = new Date().toLocaleTimeString()
  } catch (error) {
    apiStatus.value.connected = false
    showMessage('Erro ao conectar com API: ' + error.message, 'error')
  } finally {
    loading.value = false
  }
}

const testEndpoint = async (endpoint) => {
  loading.value = true
  try {
    const response = await fetch(endpoint.url)
    const data = await response.json()
    
    if (response.ok) {
      showMessage(`Endpoint ${endpoint.name} testado com sucesso!`)
      console.log(`${endpoint.name} Response:`, data)
    } else {
      showMessage(`Erro no endpoint ${endpoint.name}: ${data.error || 'Erro desconhecido'}`, 'error')
    }
  } catch (error) {
    showMessage(`Erro ao testar ${endpoint.name}: ${error.message}`, 'error')
  } finally {
    loading.value = false
  }
}

const refreshPreview = async () => {
  loading.value = true
  try {
    // Primeiro sincronizar dados do localStorage
    await syncLocalStorageToAPI()
    
    // Depois buscar dados atualizados
    const response = await fetch(`${API_BASE}/api/analytics/summary`)
    
    if (response.ok) {
      const data = await response.json()
      
      // Estruturar dados para preview organizado
      previewData.value = {
        success: data.success,
        timestamp: data.timestamp,
        summary: {
          total_quotes: data.summary?.total_quotes || 0,
          total_closed_jobs: data.summary?.total_closed_jobs || 0,
          conversion_rate: data.summary?.conversion_rate || 0,
          total_revenue: data.summary?.total_revenue || 0,
          avg_project_value: data.summary?.avg_project_value || 0,
          avg_hourly_rate: data.summary?.avg_hourly_rate || 0,
          total_hours: data.summary?.total_hours || 0
        },
        distributions: data.distributions,
        raw_response: data // Para debug se necessário
      }
      
      showMessage('Preview atualizado com dados reais!')
      lastUpdate.value = new Date().toLocaleTimeString('pt-BR')
    } else {
      const errorData = await response.json().catch(() => ({}))
      showMessage('Erro ao carregar preview: ' + (errorData.error || 'Erro de conexão'), 'error')
    }
  } catch (error) {
    showMessage('Erro ao carregar preview: ' + error.message, 'error')
    console.error('Preview error:', error)
  } finally {
    loading.value = false
  }
}

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text)
    showMessage('URL copiada para área de transferência!')
  } catch (error) {
    showMessage('Erro ao copiar URL', 'error')
  }
}

const downloadPowerBITemplate = () => {
  // Criar template PowerBI automaticamente
  const template = {
    dataSource: {
      url: "http://localhost:5000/api/analytics/summary",
      refreshRate: "5 minutes"
    },
    visuals: [
      {
        type: "card",
        title: "Receita Total", 
        field: "summary.total_revenue",
        format: "R$ #,##0"
      },
      {
        type: "card",
        title: "Taxa Conversão",
        field: "summary.conversion_rate", 
        format: "#0.0%"
      },
      {
        type: "card",
        title: "Trabalhos Fechados",
        field: "summary.total_closed_jobs",
        format: "#,##0"
      },
      {
        type: "donut",
        title: "Receita por Serviço",
        category: "distributions.by_service",
        values: "revenue"
      }
    ]
  }
  
  const blob = new Blob([JSON.stringify(template, null, 2)], {type: 'application/json'})
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'PowerBI_Dashboard_Template.json'
  a.click()
  URL.revokeObjectURL(url)
  
  showMessage('Template PowerBI baixado! Contém instruções para criar dashboard automático.')
}


const openDataStudio = () => {
  window.open('https://datastudio.google.com/', '_blank')
  showMessage('Google Data Studio aberto em nova aba')
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

// Lifecycle
onMounted(() => {
  checkApiStatus()
  refreshPreview()
  // Iniciar monitoramento automático dos dados
  watchLocalStorage()
})
</script>