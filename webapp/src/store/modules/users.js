import apiusers from '@/api/modules/apiusers'
import { defaultErrorHandler } from '@/api'

const state = {
  users: [],
  usersMeta: {}
}

const getters = {}

const actions = {
  fetchUsers ({ commit }, payload) {
    apiusers.getUsers(
      (response) => {
        commit('storeUsers', { users: response.data.items })
        commit('storeUsersMeta', { meta: response.data._meta })
      },
      (error) => defaultErrorHandler(error),
      payload.page,
      payload.per_page
    )
  },
  initUsersMeta ({ commit }, payload) {
    commit('storeUsersMeta', { meta: payload })
  },
  createUser (context, payload) {
    apiusers.postUsers(
      (response) => context.dispatch('fetchUsers', context.state.usersMeta),
      (error) => defaultErrorHandler(error),
      payload
    )
  }
}

const mutations = {
  storeUsers (state, { users }) {
    state.users = users
  },
  storeUsersMeta (state, { meta }) {
    state.usersMeta = meta
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
