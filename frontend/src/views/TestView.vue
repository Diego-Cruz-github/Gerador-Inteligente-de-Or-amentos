<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-2xl mx-auto px-4">
      <h1 class="text-2xl font-bold mb-6">🔧 Teste de Interface Simples</h1>
      
      <div class="bg-white rounded-lg shadow p-6">
        <div class="space-y-4">
          <!-- Teste básico de select -->
          <div>
            <label class="block text-sm font-medium mb-2">Tipo de Serviço:</label>
            <select v-model="serviceType" class="w-full p-2 border rounded">
              <option value="">Selecione...</option>
              <option value="website">Website</option>
              <option value="app">App</option>
              <option value="sistema">Sistema</option>
            </select>
            <p class="text-sm text-gray-600 mt-1">Selecionado: {{ serviceType }}</p>
          </div>
          
          <!-- Teste básico de input -->
          <div>
            <label class="block text-sm font-medium mb-2">Descrição:</label>
            <input v-model="description" type="text" class="w-full p-2 border rounded" placeholder="Digite algo...">
            <p class="text-sm text-gray-600 mt-1">Texto: {{ description }}</p>
          </div>
          
          <button @click="testar" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Testar
          </button>
          
          <div v-if="resultado" class="bg-green-100 p-3 rounded">
            {{ resultado }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const serviceType = ref('')
const description = ref('')
const resultado = ref('')

const testar = () => {
  resultado.value = `Serviço: ${serviceType.value}, Descrição: ${description.value}`
}
</script>