import apiwalls from '@/api/modules/apiwalls'
import { defaultErrorHandler } from '@/api'

const state = {
  walls: [],
  wallsMeta: {},
  activeStatus: false
}

const getters = {}

const actions = {
  fetchWalls ({ commit }, payload) {
    apiwalls.getWalls(
      (response) => {
        commit('storeWalls', { walls: response.data.items })
        commit('setActiveStatus', { activeStatus: response.data.active })
        commit('storeWallsMeta', { meta: response.data._meta })
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
  }
}

const mutations = {
  storeWalls (state, { walls }) {
    state.walls = walls
  },
  storeWallsMeta (state, { meta }) {
    state.wallsMeta = meta
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
