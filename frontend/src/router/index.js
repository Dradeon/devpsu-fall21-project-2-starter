import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ToDoList from '../views/ToDoList.vue'
import Journal from '../views/Journal.vue'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/todolist',
      name: 'todolist',
      component: ToDoList
    },
    {
      path: '/journal',
      name: 'journal',
      component: Journal
    },
    {
      path: '*',
      redirect: '/'
    }
  ],
  linkActiveClass: 'active',
})
