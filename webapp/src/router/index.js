import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/pages/HomePage'
import ClimbsPage from '@/components/pages/ClimbsPage'
import UsersPage from '@/components/pages/UsersPage'
import HoldsPage from '@/components/pages/HoldsPage'
import WallsPage from '@/components/pages/WallsPage'

import ClimbsHistory from '@/components/subpages/ClimbsHistory'
import ClimbsOngoing from '@/components/subpages/ClimbsOngoing'

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
      label: 'Climbs',
      component: ClimbsPage,
      children: [
        {
          path: 'history',
          name: 'ClimbsHistory',
          label: 'History',
          component: ClimbsHistory
        },
        {
          path: 'ongoing',
          name: 'ClimbsOngoing',
          label: 'Ongoing',
          component: ClimbsOngoing
        },
        {
          path: '',
          redirect: 'history'
        }
      ]
    },
    {
      path: '/users',
      name: 'Users',
      label: 'Users',
      component: UsersPage
    },
    {
      path: '/walls',
      name: 'Walls',
      label: 'Walls',
      component: WallsPage
    },
    {
      path: '/holds',
      name: 'Holds',
      label: 'Holds',
      component: HoldsPage
    },
    {
      path: '',
      redirect: 'walls'
    }
  ]
})
