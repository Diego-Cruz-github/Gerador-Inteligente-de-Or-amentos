<template>
  <div class="p-6 bg-gradient-to-r from-green-50 to-blue-50 border-t border-green-200">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="flex items-center justify-between mb-6">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Orçamento Gerado</h3>
            <p class="text-sm text-gray-600">{{ quote.project_name }}</p>
          </div>
        </div>
        
        <div class="flex space-x-2">
          <button 
            @click="viewDetails"
            class="btn-secondary text-sm"
          >
            Ver Detalhes
          </button>
          <button 
            @click="generatePDF"
            class="btn-primary text-sm"
          >
            Gerar PDF
          </button>
        </div>
      </div>

      <!-- Summary Cards -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
        <div class="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
          <div class="text-2xl font-bold text-green-600">
            R$ {{ formatCurrency(quote.total_cost) }}
          </div>
          <div class="text-sm text-gray-600">Valor Total</div>
        </div>
        
        <div class="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
          <div class="text-2xl font-bold text-blue-600">
            {{ quote.total_hours }}h
          </div>
          <div class="text-sm text-gray-600">Total de Horas</div>
        </div>
        
        <div class="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
          <div class="text-2xl font-bold text-purple-600">
            {{ quote.timeline_weeks }} sem
          </div>
          <div class="text-sm text-gray-600">Prazo</div>
        </div>
        
        <div class="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
          <div class="text-2xl font-bold text-orange-600">
            R$ {{ quote.hourly_rate }}
          </div>
          <div class="text-sm text-gray-600">Valor/Hora</div>
        </div>
      </div>

      <!-- Breakdown Chart Preview -->
      <div class="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
        <h4 class="font-semibold text-gray-900 mb-3">Breakdown de Custos</h4>
        <div class="space-y-2">
          <div 
            v-for="(item, key) in breakdownItems" 
            :key="key"
            class="flex items-center justify-between"
          >
            <div class="flex items-center space-x-2">
              <div 
                class="w-3 h-3 rounded-full"
                :style="{ backgroundColor: item.color }"
              ></div>
              <span class="text-sm text-gray-700">{{ item.label }}</span>
            </div>
            <div class="flex space-x-4">
              <span class="text-sm text-gray-600">{{ quote.hours_breakdown[key] }}h</span>
              <span class="text-sm font-medium text-gray-900">
                R$ {{ formatCurrency(quote.cost_breakdown[key]) }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { orcamentosAPI } from '@/services/api'

const props = defineProps({
  quote: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const breakdownItems = computed(() => ({
  design: { label: 'Design/UX', color: '#3B82F6' },
  frontend: { label: 'Frontend', color: '#10B981' },
  backend: { label: 'Backend', color: '#F59E0B' },
  testing: { label: 'Testes', color: '#EF4444' },
  pm: { label: 'Gerenciamento', color: '#8B5CF6' }
}))

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(value)
}

const viewDetails = () => {
  router.push(`/quote/${props.quote.id}`)
}

const generatePDF = async () => {
  try {
    const response = await orcamentosAPI.generatePDF(props.quote.id)
    if (response.data.success) {
      // Open PDF in new tab
      window.open(response.data.pdf_url, '_blank')
    }
  } catch (error) {
    console.error('Erro ao gerar PDF:', error)
  }
}
</script>