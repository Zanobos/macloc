import apiclimbs from '@/api/modules/apiclimbs'
import { defaultErrorHandler } from '@/api'

const state = {
  climbs: [],
  climbsMeta: {} // pagination not used any more
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
      payload != null ? payload : {} // It's a query
    )
  },
  initClimbsMeta ({ commit }, payload) {
    commit('storeClimbsMeta', { meta: payload })
  },
  createClimb ({ commit }, payload) {
    apiclimbs.postClimbs(
      (response) => {
        payload.onResponse(response)
      },
      (error) => defaultErrorHandler(error),
      payload.climb,
      { userId: payload.userId, wallId: payload.wallId }
    )
  },
  startClimb ({ commit }, payload) {
    var climb = {}
    climb.id = payload.climbId
    climb.status = 'start'
    apiclimbs.patchClimb(
      (response) => {
        // Mutate state
        commit('realtime/setOngoingClimb', { ongoingClimb: response.data }, { root: true })
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
        commit('realtime/setOngoingClimb', { ongoingClimb: response.data }, { root: true })
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
  getOngoingClimb (context) {
    apiclimbs.getClimbs(
      // Consider only first climb, as there should be only one
      (response) => {
        var climb = response.data.items[0]
        if (climb !== undefined) {
          context.dispatch('walls/getOngoingWall', { wallId: climb.wall_id }, { root: true })
          context.dispatch('holds/getOngoingHolds', { wallId: climb.wall_id }, { root: true })
          context.commit('realtime/setOngoingClimb', { ongoingClimb: climb }, { root: true })
        }
      },
      (error) => defaultErrorHandler(error),
      { not_status: 'end' }
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
