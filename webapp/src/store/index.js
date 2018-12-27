import Vue from 'vue'
import Vuex from 'vuex'
import walls from './modules/walls'
import climbs from './modules/climbs'
import users from './modules/users'
import holds from './modules/holds'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    walls,
    climbs,
    users,
    holds
  },
  state: {
    activeStatus: false,
    ongoingClimb: null
  },
  mutations: {
    setActiveStatus (state, { activeStatus }) {
      state.activeStatus = activeStatus
    },
    setOngoingClimb (state, { ongoingClimb }) {
      state.ongoingClimb = ongoingClimb
    }
  }
})
