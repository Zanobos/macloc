import apiholds from '@/api/modules/apiholds'
import { defaultErrorHandler } from '@/api'

const state = {
  holds: [],
  holdsMeta: {}
}

const getters = {}

const actions = {
  fetchHolds ({ commit }, payload) {
    apiholds.getHolds(
      (response) => {
        commit('storeHolds', { holds: response.data.items })
        commit('storeHoldsMeta', { meta: response.data._meta })
      },
      (error) => defaultErrorHandler(error),
      payload.page,
      payload.per_page,
      payload.wall_id
    )
  },
  initHoldsMeta ({ commit }, payload) {
    commit('storeHoldsMeta', { meta: payload })
  }
}

const mutations = {
  storeHolds (state, { holds }) {
    state.holds = holds
  },
  storeHoldsMeta (state, { meta }) {
    state.holdsMeta = meta
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
