import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'chat',
      component: () => import('@/views/ChatView.vue')
    },
    {
      path: '/detailed',
      name: 'detailed-chat',
      component: () => import('@/views/DetailedChatView.vue')
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
    }
  ]
})

export default router