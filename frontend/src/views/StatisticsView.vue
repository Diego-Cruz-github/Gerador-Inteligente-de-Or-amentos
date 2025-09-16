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
                  <span class="ml-2 text-sm font-medium text-gray-500">Análises</span>
                </div>
              </li>
              <li>
                <div class="flex items-center">
                  <svg class="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                  <span class="ml-2 text-sm font-medium text-gray-900">Estatísticas</span>
                </div>
              </li>
            </ol>
          </nav>
          <h1 class="mt-2 text-2xl font-bold text-gray-900">Estatísticas</h1>
          <p class="mt-1 text-sm text-gray-500">Análise detalhada de dados e métricas de performance</p>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 py-8">
      <!-- Key Metrics -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">Taxa de Fechamento</p>
              <p class="text-3xl font-bold text-green-600">{{ conversionRate }}%</p>
              <p class="text-sm text-gray-500 mt-1">orçamentos → trabalhos</p>
            </div>
            <div class="bg-green-100 p-3 rounded-full">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">Tempo Médio</p>
              <p class="text-3xl font-bold text-blue-600">{{ averageTime }}min</p>
              <p class="text-sm text-gray-500 mt-1">sem dados históricos</p>
            </div>
            <div class="bg-blue-100 p-3 rounded-full">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">Satisfação</p>
              <p class="text-3xl font-bold text-purple-600">{{ satisfactionRate }}%</p>
              <p class="text-sm text-gray-500 mt-1">sem dados históricos</p>
            </div>
            <div class="bg-purple-100 p-3 rounded-full">
              <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-500">ROI Médio</p>
              <p class="text-3xl font-bold text-orange-600">{{ roiAverage }}%</p>
              <p class="text-sm text-gray-500 mt-1">sobre custo base</p>
            </div>
            <div class="bg-orange-100 p-3 rounded-full">
              <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Charts Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <!-- Service Types Distribution -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Trabalhos Fechados por Tipo</h3>
          <div class="space-y-4">
            <div v-for="service in serviceStats" :key="service.type" class="flex items-center justify-between">
              <div class="flex items-center">
                <div class="w-4 h-4 rounded" :style="{ backgroundColor: service.color }"></div>
                <span class="ml-3 text-sm font-medium text-gray-700">{{ service.name }}</span>
              </div>
              <div class="flex items-center space-x-2">
                <span class="text-sm text-gray-500">{{ service.count }}</span>
                <span class="text-sm font-medium text-gray-900">{{ service.percentage }}%</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Budget Tiers -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Trabalhos por Faixa de Valor</h3>
          <div class="space-y-4">
            <div v-for="tier in budgetStats" :key="tier.type" class="flex items-center justify-between">
              <div class="flex items-center">
                <div class="w-4 h-4 rounded" :style="{ backgroundColor: tier.color }"></div>
                <span class="ml-3 text-sm font-medium text-gray-700">{{ tier.name }}</span>
              </div>
              <div class="flex items-center space-x-2">
                <span class="text-sm text-gray-500">{{ tier.count }}</span>
                <span class="text-sm font-medium text-gray-900">{{ tier.percentage }}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Detailed Stats -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Performance Timeline -->
        <div class="lg:col-span-2 bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Timeline de Trabalhos Fechados</h3>
          <div class="space-y-4">
            <div v-for="day in performanceTimeline" :key="day.date" class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div>
                <p class="text-sm font-medium text-gray-900">{{ day.date }}</p>
                <p class="text-sm text-gray-500">{{ day.quotes }} trabalho(s) fechado(s)</p>
              </div>
              <div class="text-right">
                <p class="text-sm font-medium text-gray-900">R$ {{ formatCurrency(day.value) }}</p>
                <p class="text-sm text-gray-500">{{ day.hours }}h de trabalho</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Stats -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Estatísticas Rápidas</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">Orçamentos hoje:</span>
              <span class="text-sm font-medium text-gray-900">{{ todayQuotes }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">Esta semana:</span>
              <span class="text-sm font-medium text-gray-900">{{ weekQuotes }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">Este mês:</span>
              <span class="text-sm font-medium text-gray-900">{{ monthQuotes }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">Valor médio/hora:</span>
              <span class="text-sm font-medium text-gray-900">R$ {{ averageHourlyRate }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">Projeto mais comum:</span>
              <span class="text-sm font-medium text-gray-900">{{ mostCommonProject }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm text-gray-600">Localização principal:</span>
              <span class="text-sm font-medium text-gray-900">{{ primaryLocation }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// State
const quotes = ref([])

// Computed metrics based on real data
const conversionRate = computed(() => {
  if (quotes.value.length === 0) return 0
  const closedJobs = quotes.value.filter(quote => quote.isClosed).length
  return Math.round((closedJobs / quotes.value.length) * 100)
})

const averageTime = ref(0) // Tempo médio zerado - sem dados reais ainda
const satisfactionRate = ref(0) // Taxa de satisfação zerada - sem dados reais ainda

const roiAverage = computed(() => {
  const closedJobs = quotes.value.filter(quote => quote.isClosed)
  if (closedJobs.length === 0) return 0
  const totalEarnings = closedJobs.reduce((sum, quote) => sum + quote.quote.total_cost, 0)
  const totalHours = closedJobs.reduce((sum, quote) => sum + quote.quote.total_hours, 0)
  if (totalHours === 0) return 0
  const hourlyRate = totalEarnings / totalHours
  return Math.round(((hourlyRate - 50) / 50) * 100) // ROI baseado em custo base de R$ 50/h
})

// Computed
const serviceStats = computed(() => {
  const stats = {}
  const closedJobs = quotes.value.filter(quote => quote.isClosed)
  closedJobs.forEach(quote => {
    const type = quote.serviceType || 'unknown'
    stats[type] = (stats[type] || 0) + 1
  })
  
  const total = closedJobs.length || 1
  const colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4']
  
  return Object.entries(stats).map(([type, count], index) => ({
    type,
    name: getServiceName(type),
    count,
    percentage: Math.round((count / total) * 100),
    color: colors[index % colors.length]
  }))
})

const budgetStats = computed(() => {
  const stats = {}
  const closedJobs = quotes.value.filter(quote => quote.isClosed)
  closedJobs.forEach(quote => {
    const tier = quote.budgetTier || 'unknown'
    stats[tier] = (stats[tier] || 0) + 1
  })
  
  const total = closedJobs.length || 1
  const colors = ['#10b981', '#3b82f6', '#f59e0b', '#ef4444']
  
  return Object.entries(stats).map(([type, count], index) => ({
    type,
    name: getBudgetName(type),
    count,
    percentage: Math.round((count / total) * 100),
    color: colors[index % colors.length]
  }))
})

const performanceTimeline = computed(() => {
  const last7Days = []
  for (let i = 6; i >= 0; i--) {
    const date = new Date()
    date.setDate(date.getDate() - i)
    const dayJobs = quotes.value.filter(quote => {
      if (!quote.isClosed || !quote.closedAt) return false
      const closedDate = new Date(quote.closedAt)
      return closedDate.toDateString() === date.toDateString()
    })
    
    last7Days.push({
      date: date.toLocaleDateString('pt-BR', { weekday: 'short', day: 'numeric', month: 'short' }),
      quotes: dayJobs.length,
      value: dayJobs.reduce((sum, quote) => sum + (quote.quote?.total_cost || 0), 0),
      hours: dayJobs.reduce((sum, quote) => sum + (quote.quote?.total_hours || 0), 0)
    })
  }
  return last7Days
})

const todayQuotes = computed(() => {
  const today = new Date().toDateString()
  return quotes.value.filter(quote => new Date(quote.createdAt).toDateString() === today).length
})

const weekQuotes = computed(() => {
  const weekAgo = new Date()
  weekAgo.setDate(weekAgo.getDate() - 7)
  return quotes.value.filter(quote => new Date(quote.createdAt) > weekAgo).length
})

const monthQuotes = computed(() => {
  const thisMonth = new Date().getMonth()
  const thisYear = new Date().getFullYear()
  return quotes.value.filter(quote => {
    const quoteDate = new Date(quote.createdAt)
    return quoteDate.getMonth() === thisMonth && quoteDate.getFullYear() === thisYear
  }).length
})

const averageHourlyRate = computed(() => {
  const closedJobs = quotes.value.filter(quote => quote.isClosed)
  if (closedJobs.length === 0) return 0
  const total = closedJobs.reduce((sum, quote) => sum + (quote.quote?.hourly_rate || 0), 0)
  return Math.round(total / closedJobs.length)
})

const mostCommonProject = computed(() => {
  const stats = {}
  const closedJobs = quotes.value.filter(quote => quote.isClosed)
  closedJobs.forEach(quote => {
    const type = quote.serviceType || 'unknown'
    stats[type] = (stats[type] || 0) + 1
  })
  
  if (Object.keys(stats).length === 0) return 'Nenhum trabalho fechado'
  const mostCommon = Object.entries(stats).reduce((a, b) => a[1] > b[1] ? a : b, ['', 0])
  return getServiceName(mostCommon[0])
})

const primaryLocation = computed(() => {
  const stats = {}
  const closedJobs = quotes.value.filter(quote => quote.isClosed)
  closedJobs.forEach(quote => {
    const location = quote.location || 'unknown'
    stats[location] = (stats[location] || 0) + 1
  })
  
  if (Object.keys(stats).length === 0) return 'Nenhum trabalho fechado'
  const mostCommon = Object.entries(stats).reduce((a, b) => a[1] > b[1] ? a : b, ['', 0])
  return getLocationName(mostCommon[0])
})

// Methods
const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

const getServiceName = (type) => {
  const names = {
    'website': 'Website',
    'ecommerce': 'E-commerce',
    'app': 'App Mobile',
    'sistema': 'Sistema Web',
    'landing': 'Landing Page',
    'blog': 'Blog',
    'api': 'API',
    'erp': 'ERP',
    'crm': 'CRM'
  }
  return names[type] || 'Outros'
}

const getBudgetName = (type) => {
  const names = {
    'economico': 'Econômico',
    'padrao': 'Padrão',
    'premium': 'Premium',
    'enterprise': 'Enterprise'
  }
  return names[type] || 'Outros'
}

const getLocationName = (type) => {
  const names = {
    'SP': 'Capital',
    'interior': 'Interior',
    'remoto': 'Remoto'
  }
  return names[type] || 'Outros'
}

const loadQuotes = () => {
  try {
    const savedQuotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    quotes.value = savedQuotes
  } catch (error) {
    console.error('Erro ao carregar orçamentos:', error)
    quotes.value = []
  }
}

// Lifecycle
onMounted(() => {
  loadQuotes()
})
</script>