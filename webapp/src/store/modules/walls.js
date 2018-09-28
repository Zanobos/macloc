import apiwalls from '@/api/modules/apiwalls'

const state = {
  walls: [],
  inProgress: false
}

const getters = {
  isInProgress: state => {
    return state.inProgress
  }
}

const actions = {
  getWalls ({ commit }) {
    apiwalls.getWalls(
      (response) => commit('storeWalls', { walls: response.data }),
      () => {} // Default error handler?
    )
  }
}

const mutations = {
  storeWalls (state, { walls }) {
    state.walls = walls
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
