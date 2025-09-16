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
                  <span class="ml-2 text-sm font-medium text-gray-500">Financeiro</span>
                </div>
              </li>
              <li>
                <div class="flex items-center">
                  <svg class="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                  <span class="ml-2 text-sm font-medium text-gray-900">Controle de Ganhos</span>
                </div>
              </li>
            </ol>
          </nav>
          <h1 class="mt-2 text-2xl font-bold text-gray-900">Controle Financeiro</h1>
          <p class="mt-1 text-sm text-gray-500">Acompanhe seus ganhos e faturamento de trabalhos realizados</p>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 py-8">
      <!-- Summary Cards -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div class="bg-gradient-to-r from-green-500 to-green-600 text-white rounded-lg shadow-lg p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-green-100 text-sm">Faturamento Total</p>
              <p class="text-3xl font-bold">R$ {{ formatCurrency(totalEarnings) }}</p>
              <p class="text-green-100 text-xs mt-1">{{ closedJobs.length }} trabalhos fechados</p>
            </div>
            <div class="bg-green-400 bg-opacity-30 p-3 rounded-lg">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
              </svg>
            </div>
          </div>
        </div>

        <div class="bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg shadow-lg p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-blue-100 text-sm">Este Mês</p>
              <p class="text-3xl font-bold">R$ {{ formatCurrency(monthlyEarnings) }}</p>
              <p class="text-blue-100 text-xs mt-1">{{ monthlyJobs }} trabalhos</p>
            </div>
            <div class="bg-blue-400 bg-opacity-30 p-3 rounded-lg">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-lg shadow-lg p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-purple-100 text-sm">Este Ano</p>
              <p class="text-3xl font-bold">R$ {{ formatCurrency(yearlyEarnings) }}</p>
              <p class="text-purple-100 text-xs mt-1">{{ yearlyJobs }} trabalhos</p>
            </div>
            <div class="bg-purple-400 bg-opacity-30 p-3 rounded-lg">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="bg-gradient-to-r from-orange-500 to-orange-600 text-white rounded-lg shadow-lg p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-orange-100 text-sm">Ticket Médio</p>
              <p class="text-3xl font-bold">R$ {{ formatCurrency(averageTicket) }}</p>
              <p class="text-orange-100 text-xs mt-1">por projeto</p>
            </div>
            <div class="bg-orange-400 bg-opacity-30 p-3 rounded-lg">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Financial Timeline -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
        <!-- Monthly Breakdown -->
        <div class="lg:col-span-2 bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Breakdown Mensal</h3>
          <div class="space-y-4">
            <div v-for="month in monthlyBreakdown" :key="month.month" class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div>
                <p class="text-sm font-medium text-gray-900">{{ month.month }}</p>
                <p class="text-sm text-gray-500">{{ month.jobs }} trabalho(s) fechado(s)</p>
              </div>
              <div class="text-right">
                <p class="text-lg font-semibold text-gray-900">R$ {{ formatCurrency(month.earnings) }}</p>
                <p class="text-sm text-gray-500">{{ month.hours }}h trabalhadas</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Top Services -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Serviços Mais Lucrativos</h3>
          <div class="space-y-4">
            <div v-for="service in topServices" :key="service.type" class="flex items-center justify-between">
              <div class="flex items-center">
                <div class="w-3 h-3 rounded-full mr-3" :style="{ backgroundColor: service.color }"></div>
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ service.name }}</p>
                  <p class="text-xs text-gray-500">{{ service.count }} projeto(s)</p>
                </div>
              </div>
              <div class="text-right">
                <p class="text-sm font-semibold text-gray-900">R$ {{ formatCurrency(service.earnings) }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Detailed Jobs List -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Trabalhos Fechados</h3>
          <div class="flex items-center space-x-4">
            <select 
              v-model="filterPeriod" 
              class="text-sm border border-gray-300 rounded-md px-3 py-1"
            >
              <option value="all">Todos os períodos</option>
              <option value="month">Este mês</option>
              <option value="year">Este ano</option>
            </select>
            <select 
              v-model="filterService" 
              class="text-sm border border-gray-300 rounded-md px-3 py-1"
            >
              <option value="all">Todos os serviços</option>
              <option value="website">Website</option>
              <option value="ecommerce">E-commerce</option>
              <option value="app">App Mobile</option>
              <option value="sistema">Sistema Web</option>
              <option value="landing">Landing Page</option>
              <option value="blog">Blog</option>
            </select>
          </div>
        </div>

        <div v-if="filteredJobs.length === 0" class="text-center py-8">
          <svg class="w-16 h-16 text-gray-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-gray-500">Nenhum trabalho fechado encontrado</p>
          <p class="text-sm text-gray-400 mt-1">Marque orçamentos como trabalhos fechados no Dashboard para começar a acompanhar seus ganhos</p>
        </div>

        <div v-else class="space-y-4">
          <div v-for="(job, index) in filteredJobs" :key="index" class="border border-gray-200 rounded-lg p-4 hover:bg-gray-50 transition-colors">
            <div class="flex items-center justify-between">
              <div class="flex-1">
                <div class="flex items-center space-x-3">
                  <span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full font-medium">
                    Fechado
                  </span>
                  <h4 class="text-lg font-semibold text-gray-900">
                    {{ getServiceTypeName(job.serviceType) }}
                  </h4>
                </div>
                <div class="mt-2 grid grid-cols-2 md:grid-cols-4 gap-4 text-sm text-gray-600">
                  <div>
                    <span class="font-medium">Fechado em:</span> 
                    {{ formatDate(job.closedAt) }}
                  </div>
                  <div>
                    <span class="font-medium">Urgência:</span> 
                    {{ getUrgencyName(job.urgency) }}
                  </div>
                  <div>
                    <span class="font-medium">Localização:</span> 
                    {{ getLocationName(job.location) }}
                  </div>
                  <div>
                    <span class="font-medium">Complexidade:</span> 
                    {{ job.complexity ? getComplexityName(job.complexity) : 'Simples' }}
                  </div>
                </div>
              </div>
              <div class="text-right ml-6">
                <p class="text-2xl font-bold text-green-600">R$ {{ formatCurrency(job.quote.total_cost) }}</p>
                <p class="text-sm text-gray-500">{{ job.quote.total_hours }}h • R$ {{ job.quote.hourly_rate }}/h</p>
              </div>
            </div>
            
            <div v-if="job.description" class="mt-3 pt-3 border-t border-gray-100">
              <p class="text-sm text-gray-700">{{ job.description.substring(0, 150) }}{{ job.description.length > 150 ? '...' : '' }}</p>
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
const filterPeriod = ref('all')
const filterService = ref('all')

// Computed
const closedJobs = computed(() => {
  return quotes.value.filter(quote => quote.isClosed)
})

const totalEarnings = computed(() => {
  return closedJobs.value.reduce((sum, quote) => sum + quote.quote.total_cost, 0)
})

const monthlyEarnings = computed(() => {
  const currentMonth = new Date().getMonth()
  const currentYear = new Date().getFullYear()
  
  return closedJobs.value
    .filter(quote => {
      const closedDate = new Date(quote.closedAt)
      return closedDate.getMonth() === currentMonth && closedDate.getFullYear() === currentYear
    })
    .reduce((sum, quote) => sum + quote.quote.total_cost, 0)
})

const yearlyEarnings = computed(() => {
  const currentYear = new Date().getFullYear()
  
  return closedJobs.value
    .filter(quote => {
      const closedDate = new Date(quote.closedAt)
      return closedDate.getFullYear() === currentYear
    })
    .reduce((sum, quote) => sum + quote.quote.total_cost, 0)
})

const monthlyJobs = computed(() => {
  const currentMonth = new Date().getMonth()
  const currentYear = new Date().getFullYear()
  
  return closedJobs.value.filter(quote => {
    const closedDate = new Date(quote.closedAt)
    return closedDate.getMonth() === currentMonth && closedDate.getFullYear() === currentYear
  }).length
})

const yearlyJobs = computed(() => {
  const currentYear = new Date().getFullYear()
  
  return closedJobs.value.filter(quote => {
    const closedDate = new Date(quote.closedAt)
    return closedDate.getFullYear() === currentYear
  }).length
})

const averageTicket = computed(() => {
  if (closedJobs.value.length === 0) return 0
  return totalEarnings.value / closedJobs.value.length
})

const monthlyBreakdown = computed(() => {
  const breakdown = {}
  
  closedJobs.value.forEach(job => {
    const date = new Date(job.closedAt)
    const monthKey = `${date.getFullYear()}-${date.getMonth()}`
    const monthName = date.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' })
    
    if (!breakdown[monthKey]) {
      breakdown[monthKey] = {
        month: monthName,
        earnings: 0,
        jobs: 0,
        hours: 0
      }
    }
    
    breakdown[monthKey].earnings += job.quote.total_cost
    breakdown[monthKey].jobs += 1
    breakdown[monthKey].hours += job.quote.total_hours
  })
  
  return Object.values(breakdown).sort((a, b) => b.month.localeCompare(a.month)).slice(0, 6)
})

const topServices = computed(() => {
  const services = {}
  const colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4']
  
  closedJobs.value.forEach(job => {
    const type = job.serviceType
    if (!services[type]) {
      services[type] = {
        type,
        name: getServiceTypeName(type),
        earnings: 0,
        count: 0,
        color: colors[Object.keys(services).length % colors.length]
      }
    }
    
    services[type].earnings += job.quote.total_cost
    services[type].count += 1
  })
  
  return Object.values(services)
    .sort((a, b) => b.earnings - a.earnings)
    .slice(0, 5)
})

const filteredJobs = computed(() => {
  let jobs = [...closedJobs.value]
  
  // Filter by period
  if (filterPeriod.value === 'month') {
    const currentMonth = new Date().getMonth()
    const currentYear = new Date().getFullYear()
    jobs = jobs.filter(job => {
      const closedDate = new Date(job.closedAt)
      return closedDate.getMonth() === currentMonth && closedDate.getFullYear() === currentYear
    })
  } else if (filterPeriod.value === 'year') {
    const currentYear = new Date().getFullYear()
    jobs = jobs.filter(job => {
      const closedDate = new Date(job.closedAt)
      return closedDate.getFullYear() === currentYear
    })
  }
  
  // Filter by service
  if (filterService.value !== 'all') {
    jobs = jobs.filter(job => job.serviceType === filterService.value)
  }
  
  // Sort by closed date (most recent first)
  return jobs.sort((a, b) => new Date(b.closedAt) - new Date(a.closedAt))
})

// Methods
const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}

const getServiceTypeName = (type) => {
  const names = {
    'website': 'Website Institucional',
    'ecommerce': 'E-commerce',
    'app': 'App Mobile',
    'sistema': 'Sistema Web',
    'landing': 'Landing Page',
    'blog': 'Blog/Portal',
    'api': 'API',
    'erp': 'Sistema ERP',
    'crm': 'Sistema CRM'
  }
  return names[type] || 'Projeto'
}

const getUrgencyName = (urgency) => {
  const names = {
    'normal': 'Normal',
    'urgent': 'Urgente',
    'super_urgent': 'Super Urgente',
    'flexible': 'Flexível'
  }
  return names[urgency] || 'Normal'
}

const getLocationName = (location) => {
  const names = {
    'SP': 'Capital',
    'interior': 'Interior',
    'remoto': 'Remoto'
  }
  return names[location] || 'Não informado'
}

const getComplexityName = (complexity) => {
  const names = {
    'baixa': 'Baixa',
    'media': 'Média',
    'alta': 'Alta',
    'enterprise': 'Enterprise'
  }
  return names[complexity] || 'Simples'
}

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

// Lifecycle
onMounted(() => {
  loadQuotes()
})
</script>