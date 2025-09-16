<template>
  <div id="app" class="min-h-screen bg-gray-100">
    <!-- ERP Header -->
    <header class="bg-slate-900 shadow-lg border-b border-slate-700">
      <div class="max-w-full mx-auto px-6">
        <div class="flex justify-between items-center h-14">
          <!-- Logo & Brand -->
          <div class="flex items-center space-x-4">
            <div class="bg-blue-600 p-2 rounded-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <router-link to="/" class="text-white text-lg font-semibold hover:text-blue-300 transition-colors">
              Gerador de Orçamento Inteligente
            </router-link>
            <div class="hidden lg:block h-6 w-px bg-slate-600"></div>
            <div class="hidden lg:block text-slate-300 text-sm">
              <a 
                href="https://www.diegofontedev.com.br" 
                target="_blank" 
                rel="noopener noreferrer"
                class="hover:text-white transition-colors"
              >
                Made by Diego Fonte
              </a>
            </div>
          </div>

          <!-- Navigation & User -->
          <div class="flex items-center space-x-6">
            <!-- User Info -->
            <div class="flex items-center space-x-3 text-slate-300">
              <div class="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center">
                <span class="text-white text-sm font-medium">DF</span>
              </div>
              <div class="hidden md:block">
                <div class="text-sm font-medium text-white">Diego Fonte</div>
                <div class="text-xs text-slate-400">Administrador</div>
              </div>
            </div>
            
            <!-- Settings -->
            <router-link 
              to="/preferences" 
              class="text-slate-400 hover:text-white transition-colors"
              title="Configurações"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </router-link>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Layout with Sidebar -->
    <div class="flex">
      <!-- Sidebar -->
      <aside class="w-64 bg-slate-800 min-h-[calc(100vh-56px)] shadow-lg relative">
        <nav class="mt-4 px-4 pb-20">
          <!-- Main Modules -->
          <div class="space-y-1">
            <div class="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-3 px-3">
              Módulos Principais
            </div>
            
            <router-link 
              to="/" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              Orçamento Rápido
            </router-link>

            <router-link 
              to="/detailed-app" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/detailed-app' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              Orçamento Detalhado
              <span class="ml-auto bg-green-100 text-green-800 text-xs px-2 py-0.5 rounded-full">NOVO</span>
            </router-link>

            <router-link 
              to="/dashboard" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/dashboard' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
              Dashboard
            </router-link>
          </div>

          <!-- Financial Section -->
          <div class="mt-8 space-y-1">
            <div class="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-3 px-3">
              Financeiro
            </div>
            
            <router-link 
              to="/financial" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/financial' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
              </svg>
              Controle de Ganhos
              <span class="ml-auto bg-green-100 text-green-800 text-xs px-2 py-0.5 rounded-full">NOVO</span>
            </router-link>
          </div>

          <!-- Analytics Section -->
          <div class="mt-8 space-y-1">
            <div class="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-3 px-3">
              Análises
            </div>
            
            <router-link 
              to="/reports" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/reports' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
              Relatórios
            </router-link>

            <router-link 
              to="/statistics" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/statistics' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 8v8m-4-5v5m-4-2v2m-2 4h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              Estatísticas
            </router-link>
          </div>

          <!-- Configuration Section -->
          <div class="mt-8 space-y-1">
            <div class="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-3 px-3">
              Configurações
            </div>
            
            <router-link 
              to="/preferences" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/preferences' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4" />
              </svg>
              Preferências
            </router-link>

            <router-link 
              to="/bi-integration" 
              class="flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors duration-200"
              :class="$route.path === '/bi-integration' ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-700 hover:text-white'"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
              </svg>
              Integração BI
              <span class="ml-auto bg-purple-100 text-purple-800 text-xs px-2 py-0.5 rounded-full">NOVO</span>
            </router-link>
          </div>
        </nav>

        <!-- Footer in Sidebar -->
        <div class="mt-8 p-4 border-t border-slate-700">
          <div class="text-center">
            <a 
              href="https://www.diegofontedev.com.br" 
              target="_blank" 
              rel="noopener noreferrer"
              class="text-slate-400 hover:text-white text-xs transition-colors"
            >
              © 2025 Diego Fonte Dev
            </a>
            <p class="text-xs text-slate-500 mt-1">Gerador de Orçamento Inteligente</p>
          </div>
        </div>
      </aside>

      <!-- Main Content Area -->
      <main class="flex-1 bg-gray-100">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
// Simplified App component
</script>