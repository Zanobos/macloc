import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/pages/HomePage'
import ClimbsPage from '@/components/pages/ClimbsPage'
import UsersPage from '@/components/pages/UsersPage'
import HoldsPage from '@/components/pages/HoldsPage'
import WallsPage from '@/components/pages/WallsPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/homepage',
      name: 'HomePage',
      label: 'HomePage',
      component: HomePage
    },
    {
      path: '/climbs',
      name: 'Climbs',
      label: 'Climbs',
      component: ClimbsPage
    },
    {
      path: '/users',
      name: 'Users',
      label: 'Users',
      component: UsersPage
    },
    {
      path: '/holds',
      name: 'Holds',
      label: 'Holds',
      component: HoldsPage
    },
    {
      path: '/walls',
      name: 'Walls',
      label: 'Walls',
      component: WallsPage
    },
    {
      path: '',
      redirect: 'homepage'
    }
  ]
})
