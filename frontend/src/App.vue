<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="flex items-center">
            <h1 class="text-xl font-bold text-gray-900">Gerador Inteligente de Orçamentos</h1>
            <div class="ml-4 px-3 py-1 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full">
              <a 
                href="https://www.diegofontedev.com.br" 
                target="_blank" 
                rel="noopener noreferrer"
                class="text-white text-xs font-medium hover:text-gray-200 transition-colors duration-200 flex items-center space-x-1"
              >
                <span>made by Diego Fonte</span>
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
          <nav class="flex space-x-8">
            <router-link 
              to="/" 
              class="text-blue-600 hover:text-blue-800 font-medium transition-colors duration-200"
              :class="{ 'border-b-2 border-blue-600': $route.path === '/' }"
            >
              Orçamento Rápido
            </router-link>
            <router-link 
              to="/detailed" 
              class="text-green-600 hover:text-green-800 font-medium transition-colors duration-200 flex items-center space-x-1"
              :class="{ 'border-b-2 border-green-600': $route.path === '/detailed' }"
            >
              <span>Orçamento Detalhado</span>
              <span class="text-xs bg-green-100 text-green-800 px-2 py-0.5 rounded-full font-semibold">NOVO</span>
            </router-link>
            <router-link 
              to="/dashboard" 
              class="text-gray-600 hover:text-gray-900 transition-colors duration-200"
              :class="{ 'border-b-2 border-gray-600': $route.path === '/dashboard' }"
            >
              Dashboard
            </router-link>
          </nav>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200">
      <div class="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
        <p class="text-center text-sm text-gray-600">
          Gerador Inteligente de Orçamentos - Sistema conversacional para orçamentos profissionais | 
          <span class="text-gray-800 font-medium">Made by 
            <a 
              href="https://www.diegofontedev.com.br" 
              target="_blank" 
              rel="noopener noreferrer"
              class="text-blue-600 hover:text-blue-800 transition-colors duration-200 font-semibold"
            >
              Diego Fonte
            </a>
          </span>
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Simplified App component
</script>