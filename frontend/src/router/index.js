import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home'
import Projects from '@/views/Projects'
import Curriculum from '@/views/Curriculum'
import Blog from '@/views/Blog'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/curriculum',
    name: 'Curriculum',
    component: Curriculum
  },
  {
    path: '/blog',
    name: 'Blog',
    component: Blog
  },
  {
    path: '*',
    redirect: { name: 'Home' }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
