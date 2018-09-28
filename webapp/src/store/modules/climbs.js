import apiclimbs from '@/api/modules/apiclimbs'

const state = {
  climbs: []
}

const getters = {}

const actions = {
  fetchClimbs ({ commit }) {
    apiclimbs.getClimbs(
      (response) => {
        commit('storeClimbs', { climbs: response.data.items })
      },
      () => {} // Default error handler?
    )
  }
}

const mutations = {
  storeClimbs (state, { climbs }) {
    state.climbs = climbs
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
