// Composable para sincronizar dados com API Analytics
import { ref, watch } from 'vue'

export function useAnalyticsSync() {
  const API_BASE = 'http://localhost:5000'
  
  // Função para enviar dados para API
  const syncDataToAPI = async (quotes) => {
    try {
      const response = await fetch(`${API_BASE}/api/analytics/update-data`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ quotes })
      })
      
      const result = await response.json()
      
      if (response.ok) {
        console.log('✅ Dados sincronizados com API Analytics:', result.message)
        return true
      } else {
        console.error('❌ Erro ao sincronizar:', result.error)
        return false
      }
    } catch (error) {
      console.error('❌ Erro de conexão:', error)
      return false
    }
  }
  
  // Função para buscar dados do localStorage e sincronizar
  const syncLocalStorageToAPI = async () => {
    try {
      const savedQuotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
      return await syncDataToAPI(savedQuotes)
    } catch (error) {
      console.error('❌ Erro ao ler localStorage:', error)
      return false
    }
  }
  
  // Função para monitorar mudanças no localStorage
  const watchLocalStorage = () => {
    // Sincronizar imediatamente
    syncLocalStorageToAPI()
    
    // Monitorar mudanças (polling simples)
    setInterval(syncLocalStorageToAPI, 30000) // A cada 30 segundos
    
    // Escutar eventos de storage
    window.addEventListener('storage', (e) => {
      if (e.key === 'generatedQuotes') {
        syncLocalStorageToAPI()
      }
    })
  }
  
  return {
    syncDataToAPI,
    syncLocalStorageToAPI,
    watchLocalStorage
  }
}