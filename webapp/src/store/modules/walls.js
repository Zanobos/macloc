import apiwalls from '@/api/modules/apiwalls'

const state = {
  walls: [],
  activeStatus: false
}

const getters = {}

const actions = {
  fetchWalls ({ commit }) {
    apiwalls.getWalls(
      (response) => {
        commit('storeWalls', { walls: response.data.items })
        commit('setActiveStatus', { activeStatus: response.data.active })
      },
      () => {} // Default error handler?
    )
  }
}

const mutations = {
  storeWalls (state, { walls }) {
    state.walls = walls
  },
  setActiveStatus (state, { activeStatus }) {
    state.activeStatus = activeStatus
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
