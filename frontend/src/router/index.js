import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home'
import Projects from '@/views/Projects'
import Curriculum from '@/views/Curriculum'
import CreateArticle from '@/views/CreateArticle'
import BlogAdminArticles from '@/views/BlogAdminArticles'
import EditArticle from '@/views/EditArticle'
import ReadArticle from '@/views/ReadArticle'
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
    component: Blog,
    children: [
      {
        path: ':articleCode',
        name: 'ReadArticle',
        component: ReadArticle
      }
    ]
  },
  {
    path: '/blog/article/new',
    name: 'CreateArticle',
    component: CreateArticle
  },
  {
    path: '/blog/article/edit/:articleCode',
    name: 'EditArticle',
    component: EditArticle
  },
  {
    path: '/blog/articles/admin',
    name: 'BlogAdminArticles',
    component: BlogAdminArticles
  },
  {
    path: '*',
    redirect: { name: 'Home' }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 }
  }
})

export default router
