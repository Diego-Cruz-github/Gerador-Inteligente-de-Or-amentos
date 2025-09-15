<template>
  <div class="flex" :class="message.role === 'user' ? 'justify-end' : 'justify-start'">
    <div 
      class="chat-bubble"
      :class="message.role === 'user' ? 'chat-bubble-user' : 'chat-bubble-assistant'"
    >

      <!-- Message Content -->
      <div v-if="!isQuoteMessage">
        <!-- Para mensagens do usuário, manter texto simples -->
        <div v-if="message.role === 'user'" class="whitespace-pre-wrap">
          {{ message.content }}
        </div>
        <!-- Para mensagens do assistente, aplicar formatação markdown -->
        <div v-else class="formatted-message">
          <div v-html="formatMessage(message.content)"></div>
        </div>
      </div>
      
      <!-- Quote Message Format -->
      <div v-else class="space-y-3">
        <div class="font-semibold text-green-600">
          ✅ Orçamento Gerado!
        </div>
        <div v-html="formatQuoteMessage(message.content)"></div>
      </div>
      
      <!-- Timestamp -->
      <div class="text-xs opacity-70 mt-2">
        {{ formatTime(message.timestamp) }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  message: {
    type: Object,
    required: true
  }
})

const isQuoteMessage = computed(() => {
  return props.message.content.includes('Valor Total') && props.message.content.includes('Breakdown')
})

const formatTime = (timestamp) => {
  const date = new Date(timestamp)
  return date.toLocaleTimeString('pt-BR', { 
    hour: '2-digit', 
    minute: '2-digit' 
  })
}

const formatMessage = (content) => {
  if (!content) return ''
  
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>')
}

const formatQuoteMessage = (content) => {
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/•/g, '&bull;')
    .replace(/📊|💰|⏱️|📈|📍/g, '<span class="text-lg">$&</span>')
    .replace(/\n/g, '<br>')
}
</script>

<style scoped>
.formatted-message {
  line-height: 1.6;
  word-wrap: break-word;
}

.formatted-message strong {
  font-weight: 600;
  color: #1d4ed8;
}

.chat-bubble {
  padding: 12px 16px;
  border-radius: 12px;
  max-width: 70%;
}

.chat-bubble-user {
  background: #3b82f6;
  color: white;
}

.chat-bubble-assistant {
  background: #f3f4f6;
  color: #1f2937;
}
</style>