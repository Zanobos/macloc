import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import HomePage from '@/components/pages/HomePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/homepage',
      name: 'Home Page',
      label: 'Home Page',
      component: HomePage
    },
    {
      path: '/nonhp',
      name: 'Non Home Page',
      label: 'Non Home Page',
      component: HelloWorld
    }
  ]
})
