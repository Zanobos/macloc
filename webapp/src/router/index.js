import Vue from 'vue'
import Router from 'vue-router'
import WallsPage from '@/components/pages/WallsPage'
import ClimbsPage from '@/components/pages/ClimbsPage'
import UsersPage from '@/components/pages/UsersPage'
import Configuration from '@/components/pages/Configuration'

import ConfigWalls from '@/components/subpages/ConfigWalls'
import ConfigHolds from '@/components/subpages/ConfigHolds'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/walls',
      name: 'Walls',
      label: 'Walls',
      component: WallsPage
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
      path: '/configuration',
      name: 'Configuration',
      label: 'Configuration',
      component: Configuration,
      children: [
        {
          path: 'walls',
          name: 'ConfigWalls',
          label: 'Walls',
          component: ConfigWalls
        },
        {
          path: 'holds',
          name: 'ConfigHolds',
          label: 'Holds',
          component: ConfigHolds
        },
        {
          path: '',
          redirect: 'walls'
        }
      ]
    }
  ]
})
