import Vue from 'vue'
import Vuex from 'vuex'
import walls from './modules/walls'
import climbs from './modules/climbs'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    walls,
    climbs
  }
})
