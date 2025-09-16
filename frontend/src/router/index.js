import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'app',
      component: () => import('@/views/SimpleAppView.vue')
    },
    {
      path: '/app-original',
      name: 'app-original',
      component: () => import('@/views/AppView.vue')
    },
    {
      path: '/chat',
      name: 'chat',
      component: () => import('@/views/ChatView.vue')
    },
    {
      path: '/detailed',
      name: 'detailed-chat',
      component: () => import('@/views/DetailedChatView.vue')
    },
    {
      path: '/detailed-app',
      name: 'detailed-app',
      component: () => import('@/views/DetailedAppView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('@/views/DashboardView.vue')
    },
    {
      path: '/quote/:id',
      name: 'quote',
      component: () => import('@/views/QuoteView.vue'),
      props: true
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('@/views/TestView.vue')
    }
  ]
})

export default router