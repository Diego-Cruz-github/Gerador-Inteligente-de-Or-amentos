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
                  <span class="ml-2 text-sm font-medium text-gray-500">Orçamentos</span>
                </div>
              </li>
              <li>
                <div class="flex items-center">
                  <svg class="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                  <span class="ml-2 text-sm font-medium text-gray-900">Geração Rápida</span>
                </div>
              </li>
            </ol>
          </nav>
          <h1 class="mt-2 text-2xl font-bold text-gray-900">Orçamento Rápido</h1>
          <p class="mt-1 text-sm text-gray-500">Gere orçamentos profissionais em poucos minutos</p>
        </div>
        
        <div class="flex items-center space-x-3">
          <button class="inline-flex items-center px-3 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.367 2.684 3 3 0 00-5.367-2.684z" />
            </svg>
            Compartilhar
          </button>
          <router-link 
            to="/detailed-app" 
            class="inline-flex items-center px-4 py-2 border border-transparent rounded-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            Versão Detalhada
          </router-link>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 py-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- Left Column - Form -->
        <div class="lg:col-span-2">
          <!-- Form Card -->
          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div class="flex items-center justify-between mb-6">
              <div class="flex items-center">
                <div class="bg-blue-100 p-2 rounded-lg mr-3">
                  <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <h2 class="text-lg font-semibold text-gray-900">
                  Formulário de Orçamento
                </h2>
              </div>
              <div class="text-sm text-gray-500">
                ID: #{{ Date.now().toString().slice(-6) }}
              </div>
            </div>

            <form @submit.prevent="generateQuote" class="space-y-6">
              <!-- Service Type -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">
                  Tipo de Serviço *
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
              <option value="app">Aplicativo Mobile</option>
              <option value="sistema">Sistema Web / Dashboard</option>
              <option value="landing">Landing Page</option>
              <option value="blog">Blog / Portal de Conteúdo</option>
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
                  Faixa de Orçamento *
                </label>
                <select
              v-model="formData.budgetTier"
              required
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px; background-color: white; appearance: menulist; -webkit-appearance: menulist; -moz-appearance: menulist;"
              @change="forceCloseSelect"
              @blur="(e) => e.target.removeAttribute('open')"
              size="1"
            >
              <option value="">Selecione a faixa de orçamento</option>
              <option value="economico">Econômico - Melhor custo-benefício</option>
              <option value="padrao">Padrão - Recursos completos</option>
              <option value="premium">Premium - Tecnologia de ponta</option>
                </select>
              </div>

              <!-- Description -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">
                  Descrição do Projeto ou Proposta
                </label>
                <textarea
              v-model="formData.description"
              rows="6"
              placeholder="Descreva seu projeto detalhadamente ou cole uma proposta existente para análise..."
              style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 16px;"
                ></textarea>
                <p class="text-sm text-gray-500 mt-1 flex items-center">
              <svg class="w-4 h-4 mr-1 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
                  Quanto mais detalhes, mais preciso será o orçamento gerado pela IA
                </p>
              </div>

              <!-- Submit Button -->
              <div class="pt-4">
                <button
                  type="submit"
              :disabled="isLoading || !isFormValid"
              style="width: 100%; background: linear-gradient(to right, #2563eb, #7c3aed); color: white; font-weight: 500; padding: 12px 24px; border-radius: 8px; border: none; cursor: pointer; font-size: 16px;"
              :style="{ opacity: (isLoading || !isFormValid) ? 0.5 : 1 }"
            >
                  <span v-if="isLoading">Analisando com IA...</span>
                  <span v-else>Gerar Orçamento com IA</span>
                </button>
              </div>
            </form>
          </div>

          <!-- Quote Result -->
          <div v-if="generatedQuote" class="mt-8 bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div class="flex items-center mb-6">
          <div class="bg-green-100 p-2 rounded-lg mr-3">
            <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h2 class="text-xl font-semibold text-gray-800">
            Orçamento Gerado
          </h2>
            </div>

            <!-- Quote Summary -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div class="text-center p-4 bg-green-50 rounded-lg">
            <div class="text-2xl font-bold text-green-600">
              R$ {{ formatCurrency(generatedQuote.total_cost) }}
            </div>
            <div class="text-sm text-gray-600">Valor Total</div>
          </div>
          <div class="text-center p-4 bg-blue-50 rounded-lg">
            <div class="text-2xl font-bold text-blue-600">
              {{ generatedQuote.total_hours }}h
            </div>
            <div class="text-sm text-gray-600">Total de Horas</div>
          </div>
          <div class="text-center p-4 bg-purple-50 rounded-lg">
            <div class="text-2xl font-bold text-purple-600">
              {{ generatedQuote.timeline_weeks }}
            </div>
            <div class="text-sm text-gray-600">Prazo</div>
          </div>
          <div class="text-center p-4 bg-orange-50 rounded-lg">
            <div class="text-2xl font-bold text-orange-600">
              R$ {{ generatedQuote.hourly_rate }}
            </div>
            <div class="text-sm text-gray-600">Valor/Hora</div>
          </div>
            </div>

            <!-- AI Analysis -->
            <div v-if="aiAnalysis" class="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
          <div class="flex items-center mb-2">
            <div class="bg-blue-100 p-1 rounded mr-2">
              <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 class="font-semibold text-blue-900">
              Análise da IA
            </h3>
          </div>
              <div class="text-blue-800" v-html="formatMessage(aiAnalysis)"></div>
            </div>

            <!-- Action Buttons -->
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
              <button
                @click="downloadPDF"
                class="bg-red-600 hover:bg-red-700 text-white font-medium py-3 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <span>PDF</span>
              </button>
              
              <button
                @click="shareWhatsApp"
                class="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.885 3.488"/>
                </svg>
                <span>WhatsApp</span>
              </button>

              <button
                @click="shareTelegram"
                class="bg-blue-500 hover:bg-blue-600 text-white font-medium py-3 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                </svg>
                <span>Telegram</span>
              </button>
              
              <button
                @click="promptEmailAndSend"
                class="bg-emerald-600 hover:bg-emerald-700 text-white font-medium py-3 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                <span>Email</span>
              </button>
              
              <button
                @click="goToDashboard"
                class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <span>Dashboard</span>
              </button>
              
              <button
                @click="resetForm"
                class="bg-gray-600 hover:bg-gray-700 text-white font-medium py-3 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                <span>Novo</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Right Column - Info Sidebar -->
        <div class="lg:col-span-1">
          <!-- Quick Stats -->
          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Estatísticas Rápidas</h3>
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-600">Orçamentos hoje:</span>
                <span class="text-sm font-medium text-gray-900">{{ getTodayQuotesCount }}</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-600">Tempo médio:</span>
                <span class="text-sm font-medium text-gray-900">{{ getAverageQuoteTime }}</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-600">Taxa de sucesso:</span>
                <span class="text-sm font-medium text-green-600">{{ getSuccessRate }}</span>
              </div>
            </div>
          </div>

          <!-- Process Flow -->
          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Fluxo do Processo</h3>
            <div class="space-y-4">
              <div class="flex items-center">
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                  <span class="text-blue-600 text-sm font-medium">1</span>
                </div>
                <span class="text-sm text-gray-600">Preencher formulário</span>
              </div>
              <div class="flex items-center">
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                  <span class="text-blue-600 text-sm font-medium">2</span>
                </div>
                <span class="text-sm text-gray-600">Análise pela IA</span>
              </div>
              <div class="flex items-center">
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                  <span class="text-blue-600 text-sm font-medium">3</span>
                </div>
                <span class="text-sm text-gray-600">Geração do orçamento</span>
              </div>
              <div class="flex items-center">
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                  <span class="text-blue-600 text-sm font-medium">4</span>
                </div>
                <span class="text-sm text-gray-600">Download ou envio</span>
              </div>
            </div>
          </div>

          <!-- Recent Activity -->
          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Atividades Recentes</h3>
            <div class="space-y-3">
              <div class="flex items-center text-sm">
                <div class="w-2 h-2 bg-green-400 rounded-full mr-3"></div>
                <span class="text-gray-600">Orçamento E-commerce gerado</span>
                <span class="text-gray-400 ml-auto">2min</span>
              </div>
              <div class="flex items-center text-sm">
                <div class="w-2 h-2 bg-blue-400 rounded-full mr-3"></div>
                <span class="text-gray-600">PDF baixado</span>
                <span class="text-gray-400 ml-auto">5min</span>
              </div>
              <div class="flex items-center text-sm">
                <div class="w-2 h-2 bg-purple-400 rounded-full mr-3"></div>
                <span class="text-gray-600">Email enviado</span>
                <span class="text-gray-400 ml-auto">8min</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Error Display -->
      <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
        <div class="flex items-center">
          <span class="text-red-800 font-medium">❌ {{ error }}</span>
        </div>
      </div>

      <!-- Success Message -->
      <div v-if="successMessage" class="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
        <div class="flex items-center">
          <span class="text-green-800 font-medium">✅ {{ successMessage }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { chatAPI } from '@/services/api'
import jsPDF from 'jspdf'
import { useAnalyticsSync } from '@/composables/useAnalyticsSync.js'

// Router
const router = useRouter()

// Composables
const { syncDataToAPI, syncLocalStorageToAPI } = useAnalyticsSync()

// Refs reativos para estatísticas
const statisticsKey = ref(0) // Usado para forçar re-render das estatísticas

// Form Data
const formData = ref({
  serviceType: '',
  urgency: '',
  location: '',
  budgetTier: '',
  description: ''
})

// State
const isLoading = ref(false)
const generatedQuote = ref(null)
const aiAnalysis = ref('')
const error = ref('')
const successMessage = ref('')

// Computed
const isFormValid = computed(() => {
  return formData.value.serviceType && 
         formData.value.urgency && 
         formData.value.location && 
         formData.value.budgetTier
})

// Methods
const generateQuote = async () => {
  try {
    isLoading.value = true
    error.value = ''
    successMessage.value = ''
    
    console.log('📋 Enviando dados do formulário:', formData.value)
    
    const response = await chatAPI.generateFromForm(formData.value)
    
    if (response.data.success) {
      generatedQuote.value = response.data.quote
      aiAnalysis.value = response.data.ai_analysis || ''
      
      // Salvar no localStorage para dashboard
      await saveQuoteToLocalStorage({
        quote: generatedQuote.value,
        aiAnalysis: aiAnalysis.value,
        serviceType: formData.value.serviceType,
        urgency: formData.value.urgency,
        location: formData.value.location,
        budgetTier: formData.value.budgetTier,
        description: formData.value.description,
        isDetailed: false,
        createdAt: new Date().toISOString()
      })
      
      console.log('✅ Orçamento gerado com sucesso:', response.data)
    } else {
      throw new Error(response.data.error || 'Erro desconhecido')
    }
    
  } catch (err) {
    console.error('❌ Erro ao gerar orçamento:', err)
    error.value = err.response?.data?.error || err.message || 'Erro ao gerar orçamento'
  } finally {
    isLoading.value = false
  }
}

const downloadPDF = async () => {
  try {
    successMessage.value = ''
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
    doc.text('Orçamento Rápido - Gerador Inteligente', 20, 30)
    
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
    
    // Gerar nome do arquivo baseado no tipo de serviço
    const serviceTypeMap = {
      'website': 'Website-Institucional',
      'ecommerce': 'E-commerce',
      'app': 'App-Mobile',
      'sistema': 'Sistema-Web',
      'landing': 'Landing-Page',
      'blog': 'Blog-Portal'
    }
    
    const serviceType = serviceTypeMap[formData.value.serviceType] || 'Projeto'
    const timestamp = new Date().toISOString().slice(0, 10) // YYYY-MM-DD
    const filename = `Orcamento-Rapido-${serviceType}-${timestamp}.pdf`
    
    // Fazer download do PDF
    doc.save(filename)
    
    successMessage.value = 'PDF gerado e baixado com sucesso!'
    console.log('✅ PDF gerado e baixado:', filename)
    
  } catch (err) {
    console.error('❌ Erro ao gerar PDF:', err)
    error.value = 'Erro ao gerar PDF: ' + err.message
  }
}

const promptEmailAndSend = async () => {
  const email = prompt('Digite o email para envio do orçamento:')
  if (!email) return
  
  if (!email.includes('@')) {
    error.value = 'Email inválido'
    return
  }
  
  try {
    successMessage.value = ''
    error.value = ''
    
    const emailData = {
      quote: generatedQuote.value,
      ai_analysis: aiAnalysis.value,
      email: email
    }
    
    const response = await chatAPI.sendEmail(emailData)
    
    if (response.data.success) {
      successMessage.value = response.data.message
    }
  } catch (err) {
    error.value = 'Erro ao enviar email: ' + (err.response?.data?.error || err.message)
  }
}

const resetForm = () => {
  formData.value = {
    serviceType: '',
    urgency: '',
    location: '',
    budgetTier: '',
    description: ''
  }
  generatedQuote.value = null
  aiAnalysis.value = ''
  error.value = ''
  successMessage.value = ''
}

const goToDashboard = () => {
  router.push('/dashboard')
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

const saveQuoteToLocalStorage = async (quoteData) => {
  try {
    const existingQuotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    existingQuotes.push(quoteData)
    localStorage.setItem('generatedQuotes', JSON.stringify(existingQuotes))
    console.log('💾 Orçamento salvo no localStorage')
    
    // Atualizar estatísticas locais
    refreshStatistics()
    
    // Sincronizar com API Analytics para atualizar BI
    await syncDataToAPI(existingQuotes)
    console.log('✅ Dados sincronizados com API Analytics')
  } catch (error) {
    console.error('❌ Erro ao salvar orçamento:', error)
  }
}

// Função para atualizar estatísticas
const refreshStatistics = () => {
  statisticsKey.value += 1
}

// Computed properties para estatísticas reativas
const getTodayQuotesCount = computed(() => {
  // Use statisticsKey para forçar reatividade
  statisticsKey.value
  try {
    const quotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    const today = new Date().toDateString()
    return quotes.filter(quote => new Date(quote.createdAt).toDateString() === today).length
  } catch (error) {
    return 0
  }
})

const getAverageQuoteTime = computed(() => {
  // Use statisticsKey para forçar reatividade  
  statisticsKey.value
  try {
    const quotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    if (quotes.length === 0) return '0 min'
    
    // Calcular tempo médio baseado na complexidade do projeto
    const totalComplexity = quotes.reduce((sum, quote) => {
      // Estimar complexidade baseada no valor total e horas
      const complexity = quote.quote?.total_hours || 50
      return sum + complexity
    }, 0)
    
    const avgComplexity = totalComplexity / quotes.length
    
    // Converter complexidade em tempo estimado (horas simples = 1-2 min, complexas = 3-5 min)
    const avgMinutes = Math.max(1, Math.min(5, Math.round(avgComplexity / 25)))
    
    return `${avgMinutes} min`
  } catch (error) {
    return '2 min'
  }
})

const getSuccessRate = computed(() => {
  // Use statisticsKey para forçar reatividade
  statisticsKey.value
  try {
    const quotes = JSON.parse(localStorage.getItem('generatedQuotes') || '[]')
    if (quotes.length === 0) return '100%'
    
    const closedJobs = quotes.filter(quote => quote.isClosed === true).length
    const rate = Math.round((closedJobs / quotes.length) * 100)
    
    return `${rate}%`
  } catch (error) {
    return '98%'
  }
})

const shareWhatsApp = () => {
  if (!generatedQuote.value) {
    alert('Gere um orçamento antes de compartilhar!')
    return
  }
  const message = createShareMessage()
  const encodedMessage = encodeURIComponent(message)
  const whatsappUrl = `https://wa.me/?text=${encodedMessage}`
  window.open(whatsappUrl, '_blank')
}

const shareTelegram = () => {
  if (!generatedQuote.value) {
    alert('Gere um orçamento antes de compartilhar!')
    return
  }
  const message = createShareMessage()
  const encodedMessage = encodeURIComponent(message)
  const telegramUrl = `https://t.me/share/url?text=${encodedMessage}`
  window.open(telegramUrl, '_blank')
}

const createShareMessage = () => {
  const serviceTypeMap = {
    'website': 'Website Institucional',
    'ecommerce': 'E-commerce',
    'app': 'App Mobile', 
    'sistema': 'Sistema Web',
    'landing': 'Landing Page',
    'blog': 'Blog/Portal'
  }
  
  const urgencyMap = {
    'normal': 'Normal',
    'urgent': 'Urgente',
    'super_urgent': 'Super Urgente'
  }
  
  const locationMap = {
    'SP': 'Capital',
    'interior': 'Interior', 
    'remoto': 'Remoto'
  }
  
  const budgetMap = {
    'economico': 'Econômico',
    'padrao': 'Padrão',
    'premium': 'Premium'
  }
  
  const serviceName = serviceTypeMap[formData.value.serviceType] || 'Projeto'
  const urgencyName = urgencyMap[formData.value.urgency] || 'Normal'
  const locationName = locationMap[formData.value.location] || 'Não informado'
  const budgetName = budgetMap[formData.value.budgetTier] || 'Padrão'
  
  let message = `📋 ORÇAMENTO GERADO\n\n`
  message += `🎯 *${serviceName}*\n\n`
  message += `💰 *Valor Total:* R$ ${formatCurrency(generatedQuote.value.total_cost)}\n`
  message += `⏱️ *Total de Horas:* ${generatedQuote.value.total_hours}h\n`
  message += `📅 *Prazo:* ${generatedQuote.value.timeline_weeks}\n`
  message += `💵 *Valor/Hora:* R$ ${generatedQuote.value.hourly_rate}\n\n`
  message += `📍 *Localização:* ${locationName}\n`
  message += `⚡ *Urgência:* ${urgencyName}\n`
  message += `🎁 *Categoria:* ${budgetName}\n\n`
  
  if (formData.value.description) {
    message += `📝 *Descrição:*\n${formData.value.description.substring(0, 100)}${formData.value.description.length > 100 ? '...' : ''}\n\n`
  }
  
  if (aiAnalysis.value) {
    message += `🤖 *Análise da IA:*\n${aiAnalysis.value.substring(0, 150)}${aiAnalysis.value.length > 150 ? '...' : ''}\n\n`
  }
  
  message += `🤖 *Gerado com IA - Sistema de Orçamentos*\n`
  message += `👨‍💻 *Made by Diego Fonte*\n`
  message += `🌐 https://www.diegofontedev.com.br`
  
  return message
}

// Lifecycle
onMounted(async () => {
  // Sincronizar dados com a API ao carregar a página
  await syncLocalStorageToAPI()
  console.log('✅ Dados sincronizados com API ao carregar SimpleApp')
  
  // Forçar atualização das estatísticas
  refreshStatistics()
})
</script>

<style scoped>
select {
  -webkit-appearance: menulist !important;
  -moz-appearance: menulist !important;
  appearance: menulist !important;
  background-color: white !important;
  cursor: pointer !important;
  border: 1px solid #d1d5db !important;
  border-radius: 8px !important;
  max-height: 200px !important;
  overflow-y: auto !important;
  position: relative !important;
  z-index: 10 !important;
}

select:focus {
  outline: 2px solid #3b82f6 !important;
  outline-offset: -2px !important;
  border-color: #3b82f6 !important;
  z-index: 50 !important;
}

select:not(:focus) {
  height: auto !important;
  max-height: 48px !important;
}

select option {
  background-color: white !important;
  color: black !important;
  padding: 8px 12px !important;
  border: none !important;
}

/* Força fechamento em WebKit browsers */
select::-webkit-details-marker {
  display: none !important;
}

/* Força fechamento em todos os browsers */
select[size="1"]:focus {
  size: 1 !important;
}

/* Garantir que o dropdown funcione corretamente no layout ERP */
.form-group {
  position: relative;
  z-index: 1;
}

.form-group:focus-within {
  z-index: 50;
}
</style>