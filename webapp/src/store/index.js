import Vue from 'vue'
import Vuex from 'vuex'
import walls from './modules/walls'
import climbs from './modules/climbs'
import users from './modules/users'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    walls,
    climbs,
    users
  }
})
