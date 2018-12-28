import apiwalls from '@/api/modules/apiwalls'
import { defaultErrorHandler } from '@/api'

const state = {
  walls: [],
  wallsMeta: {}
}

const getters = {}

const actions = {
  fetchWalls ({ commit }, payload) {
    apiwalls.getWalls(
      (response) => {
        commit('storeWalls', { walls: response.data.items })
        commit('storeWallsMeta', { meta: response.data._meta })
        commit('realtime/setActiveStatus', { activeStatus: response.data.active }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      payload.page,
      payload.per_page
    )
  },
  initWallsMeta ({ commit }, payload) {
    commit('storeWallsMeta', { meta: payload })
  },
  addWall ({ commit }, wall) {
    apiwalls.postWalls(
      (response) => {
        this.fetchWalls({ commit: commit })
      },
      (error) => defaultErrorHandler(error),
      wall
    )
  },
  getOngoingWall (context, payload) {
    apiwalls.getWall(
      (response) => {
        context.commit('realtime/setOngoingWall', response.data, { root: true })
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
