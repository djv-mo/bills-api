import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Register from '@/public/Register.vue'
import Login from '@/public/Login.vue'
import Secure from '@/secure/Secure.vue'
import Dashboard from '@/secure/dashboard/Dashboard.vue'
import BillView from '@/secure/dashboard/BillView.vue'
import Archive from '@/secure/dashboard/Archive.vue'
import Errors from '@/public/Errors.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/',
    component: Secure,
    children: [
      {
        path: '/',
        name: 'Dashboard',
        component: Dashboard
      },
      {
        path: '/bill/:id/',
        name: 'BillView',
        component: BillView,
        props: true
      },
      {
        path: '/archive/',
        name: 'Archive',
        component: Archive,
      }
    ]

  },
  {
    path: '/:catchAll(.*)',
    component: Errors,
    name: 'Errors'
  }

]

const router = createRouter({
  history: createWebHistory(process.env.vue),
  routes
})

export default router
