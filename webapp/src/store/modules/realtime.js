const state = {
  isConnected: false,
  rtholds: [],
  activeStatus: false,
  ongoingClimb: null,
  ongoingWall: null
}

const getters = {}

const actions = {
  socket_connect (context, payload) {
    context.commit('changeConnectionState', { isConnected: true })
  },
  socket_disconnect (context, payload) {
    context.commit('changeConnectionState', { isConnected: false })
  }
}

const mutations = {
  changeConnectionState (state, { isConnected }) {
    state.isConnected = isConnected
  },
  setActiveStatus (state, { activeStatus }) {
    state.activeStatus = activeStatus
  },
  setOngoingClimb (state, { ongoingClimb }) {
    state.ongoingClimb = ongoingClimb
  },
  setOngoingWall (state, { ongoingWall }) {
    state.ongoingWall = ongoingWall
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
