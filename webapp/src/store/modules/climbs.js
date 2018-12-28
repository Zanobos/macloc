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
      payload.per_page,
      payload.userId,
      payload.status
    )
  },
  initClimbsMeta ({ commit }, payload) {
    commit('storeClimbsMeta', { meta: payload })
  },
  createClimb ({ commit }, payload) {
    apiclimbs.postClimbs(
      (response) => {
        // 1 Mutate state
        commit('setOngoingClimb', { ongoingClimb: response.data }, { root: true })
        // 2 Call callback
        payload.onResponse(response)
      },
      (error) => defaultErrorHandler(error),
      payload.climb,
      payload.userId,
      payload.wallId
    )
  },
  startClimb ({ commit }, payload) {
    var climb = {}
    climb.id = payload.climbId
    climb.status = 'start'
    apiclimbs.patchClimb(
      (response) => {
        // Mutate state
        commit('setOngoingClimb', { ongoingClimb: response.data }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      climb
    )
  },
  endClimb ({ commit }, payload) {
    var climb = {}
    climb.id = payload.climbId
    climb.status = 'end'
    apiclimbs.patchClimb(
      (response) => {
        // Mutate state
        commit('setOngoingClimb', { ongoingClimb: response.data }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      climb
    )
  },
  getClimb (context, payload) {
    apiclimbs.getClimb(
      (response) => payload.onResponse(response),
      (error) => defaultErrorHandler(error),
      payload.climbId
    )
  },
  getCurrentClimb ({ commit }) {
    apiclimbs.getClimbs(
      // Consider only first climb, as there should be only one
      (response) => {
        commit('setOngoingClimb', { ongoingClimb: response.data[0] }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      null,
      null,
      null,
      'start'
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
