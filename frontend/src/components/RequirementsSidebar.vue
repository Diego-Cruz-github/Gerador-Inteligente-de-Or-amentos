<template>
  <div class="h-full overflow-y-auto">
    <div class="p-6">
      <h3 class="text-lg font-semibold text-gray-900 mb-4">
        Requisitos Coletados
      </h3>
      
      <div v-if="Object.keys(requirements).length === 0" class="text-gray-500 text-sm">
        Os requisitos aparecerão aqui conforme você conversa...
      </div>
      
      <div v-else class="space-y-4">
        <!-- Tipo de Projeto -->
        <div v-if="requirements.project_type" class="requirement-item">
          <div class="requirement-label">Tipo de Projeto</div>
          <div class="requirement-value">
            {{ getProjectTypeLabel(requirements.project_type) }}
          </div>
        </div>
        
        <!-- Complexidade -->
        <div v-if="requirements.complexity" class="requirement-item">
          <div class="requirement-label">Complexidade</div>
          <div class="requirement-value">
            <span 
              class="px-2 py-1 rounded-full text-xs font-medium"
              :class="getComplexityClass(requirements.complexity)"
            >
              {{ requirements.complexity.charAt(0).toUpperCase() + requirements.complexity.slice(1) }}
            </span>
          </div>
        </div>
        
        <!-- Usuários Esperados -->
        <div v-if="requirements.expected_users" class="requirement-item">
          <div class="requirement-label">Usuários Esperados</div>
          <div class="requirement-value">
            {{ formatNumber(requirements.expected_users) }}
          </div>
        </div>
        
        <!-- Usuários Simultâneos -->
        <div v-if="requirements.concurrent_users" class="requirement-item">
          <div class="requirement-label">Usuários Simultâneos</div>
          <div class="requirement-value">
            {{ formatNumber(requirements.concurrent_users) }}
          </div>
        </div>
        
        <!-- Páginas -->
        <div v-if="requirements.pages_count" class="requirement-item">
          <div class="requirement-label">Número de Páginas</div>
          <div class="requirement-value">
            {{ requirements.pages_count }}
          </div>
        </div>
        
        <!-- Região -->
        <div v-if="requirements.region" class="requirement-item">
          <div class="requirement-label">Região</div>
          <div class="requirement-value">
            {{ getRegionLabel(requirements.region) }}
          </div>
        </div>
        
        <!-- Features Especiais -->
        <div class="space-y-2">
          <div v-if="requirements.offline_support" class="feature-badge feature-badge-blue">
            Suporte Offline
          </div>
          <div v-if="requirements.push_notifications" class="feature-badge feature-badge-green">
            Notificações Push
          </div>
          <div v-if="requirements.payment_integration" class="feature-badge feature-badge-yellow">
            Integração de Pagamentos
          </div>
          <div v-if="requirements.is_ecommerce" class="feature-badge feature-badge-purple">
            E-commerce
          </div>
          <div v-if="requirements.needs_admin" class="feature-badge feature-badge-red">
            Área Administrativa
          </div>
          <div v-if="requirements.needs_reports" class="feature-badge feature-badge-indigo">
            Relatórios
          </div>
          <div v-if="requirements.financial_module" class="feature-badge feature-badge-pink">
            Módulo Financeiro
          </div>
        </div>
        
        <!-- Descrição do Projeto -->
        <div v-if="requirements.project_description" class="requirement-item">
          <div class="requirement-label">Descrição</div>
          <div class="requirement-value text-sm">
            {{ requirements.project_description }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  requirements: {
    type: Object,
    default: () => ({})
  }
})

const getProjectTypeLabel = (type) => {
  const labels = {
    app: 'Aplicativo Mobile',
    website: 'Website/Portal',
    sistema: 'Sistema Web'
  }
  return labels[type] || type
}

const getComplexityClass = (complexity) => {
  const classes = {
    baixa: 'bg-green-100 text-green-800',
    media: 'bg-yellow-100 text-yellow-800',
    alta: 'bg-red-100 text-red-800'
  }
  return classes[complexity] || 'bg-gray-100 text-gray-800'
}

const getRegionLabel = (region) => {
  const labels = {
    SP: 'São Paulo',
    interior: 'Interior',
    remoto: 'Remoto'
  }
  return labels[region] || region
}

const formatNumber = (num) => {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M'
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'k'
  }
  return num.toString()
}
</script>

<style scoped>
.requirement-item {
  @apply border-b border-gray-100 pb-2;
}

.requirement-label {
  @apply text-xs font-medium text-gray-500 uppercase tracking-wide;
}

.requirement-value {
  @apply text-sm text-gray-900 mt-1;
}

.feature-badge {
  @apply inline-block px-2 py-1 rounded-full text-xs font-medium;
}

.feature-badge-blue {
  @apply bg-blue-100 text-blue-800;
}

.feature-badge-green {
  @apply bg-green-100 text-green-800;
}

.feature-badge-yellow {
  @apply bg-yellow-100 text-yellow-800;
}

.feature-badge-purple {
  @apply bg-purple-100 text-purple-800;
}

.feature-badge-red {
  @apply bg-red-100 text-red-800;
}

.feature-badge-indigo {
  @apply bg-indigo-100 text-indigo-800;
}

.feature-badge-pink {
  @apply bg-pink-100 text-pink-800;
}
</style>