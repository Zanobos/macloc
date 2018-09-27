import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 0,
    inProgress: false
  },
  mutations: {
    increment (state) {
      state.count++
    }
  },
  getters: {
    isInProgress: state => {
      return state.inProgress
    }
  }
})
