import apiclimbs from '@/api/modules/apiclimbs'
import { defaultErrorHandler } from '@/api'

const state = {
  climbs: [],
  climbsMeta: {}
}

const getters = {}

const actions = {
  fetchClimbs ({ commit }, payload) {
    apiclimbs.getClimbs(
      (response) => {
        commit('storeClimbs', { climbs: response.data.items })
        commit('storeClimbsMeta', { meta: response.data._meta })
      },
      (error) => defaultErrorHandler(error),
      payload.page,
      payload.per_page
    )
  },
  initClimbsMeta ({ commit }, payload) {
    commit('storeClimbsMeta', { meta: payload })
  }
}

const mutations = {
  storeClimbs (state, { climbs }) {
    state.climbs = climbs
  },
  storeClimbsMeta (state, { meta }) {
    state.climbsMeta = meta
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
