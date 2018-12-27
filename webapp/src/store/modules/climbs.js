import apiclimbs from '@/api/modules/apiclimbs'
import { defaultErrorHandler } from '@/api'

const state = {
  climbs: [],
  climbsMeta: {},
  activeClimb: null
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
  },
  createClimb ({ commit }, payload) {
    // TODO do stuff with response
    apiclimbs.postClimbs(
      (response) => {
        // 1 Mutate state
        commit('setActiveStatus', { activeStatus: true }, { root: true })
        commit('setOngoingClimb', { ongoingClimb: response.data }, { root: true })
        // 2 Call callback
        payload.onResponse(response)
      },
      (error) => defaultErrorHandler(error),
      payload.climb,
      payload.userId,
      payload.wallId
    )
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
