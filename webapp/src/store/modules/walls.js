import apiwalls from '@/api/modules/apiwalls'
import { defaultErrorHandler } from '@/api'

const state = {
  walls: [],
  wallsMeta: {} // not used anymore
}

const getters = {
  wallIds (state) {
    return state.walls.map(wall => wall.id)
  }
}

const actions = {
  fetchWalls ({ commit }, payload) {
    apiwalls.getWalls(
      (response) => {
        commit('storeWalls', { walls: response.data.items })
        commit('storeWallsMeta', { meta: response.data._meta })
        commit('realtime/setActiveStatus', { activeStatus: response.data.active }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      payload != null ? payload : {}
    )
  },
  initWallsMeta ({ commit }, payload) {
    commit('storeWallsMeta', { meta: payload })
  },
  createWall (context, wall) {
    apiwalls.postWalls(
      (response) => context.dispatch('fetchWalls'),
      (error) => defaultErrorHandler(error),
      wall
    )
  },
  getOngoingWall (context, payload) {
    apiwalls.getWall(
      (response) => {
        context.commit('realtime/setOngoingWall', { ongoingWall: response.data }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      payload.wallId
    )
  }
}

const mutations = {
  storeWalls (state, { walls }) {
    state.walls = walls
  },
  storeWallsMeta (state, { meta }) {
    state.wallsMeta = meta
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
