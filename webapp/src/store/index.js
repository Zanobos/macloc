import Vue from 'vue'
import Vuex from 'vuex'
import walls from './modules/walls'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    walls
  }
})
