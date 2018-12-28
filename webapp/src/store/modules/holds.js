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
  },
  getOngoingHolds (context, payload) {
    apiholds.getHolds(
      (response) => {
        context.commit('realtime/setOngoingHolds', { ongoingHolds: response.data.items }, { root: true })
      },
      (error) => defaultErrorHandler(error),
      null,
      null,
      payload.wallId
    )
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
