import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/pages/HomePage'
import ClimbsHistory from '@/components/pages/ClimbsHistory'
import Users from '@/components/pages/Users'
import Configuration from '@/components/pages/Configuration'

import ConfigWalls from '@/components/subpages/ConfigWalls'
import ConfigHolds from '@/components/subpages/ConfigHolds'

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
      path: '/climbsHistory',
      name: 'Climbs History',
      label: 'Climbs History',
      component: ClimbsHistory
    },
    {
      path: '/users',
      name: 'Users',
      label: 'Users',
      component: Users
    },
    {
      path: '/configuration',
      name: 'Configuration',
      label: 'Configuration',
      component: Configuration,
      children: [
        {
          path: 'walls',
          name: 'Walls',
          label: 'Walls',
          component: ConfigWalls
        },
        {
          path: 'holds',
          name: 'Holds',
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
