import Vue from 'vue'

const state = {
  isConnected: false,
  rtholds: {},
  activeStatus: false,
  ongoingClimb: null,
  ongoingWall: null,
  ongoingHolds: []
}

const getters = {
  getForceByHoldId (state, getters) {
    return (direction, holdId) => {
      console.log(direction + ',' + holdId + ',' + state.rtholds)
      if (state.rtholds[holdId] == null) {
        return null
      }
      return state.rtholds[holdId][direction]
    }
  }
}

const actions = {
  socket_connect (context, payload) {
    context.commit('changeConnectionState', { isConnected: true })
  },
  socket_disconnect (context, payload) {
    context.commit('changeConnectionState', { isConnected: false })
  },
  socket_json (context, payload) {
    context.commit('storeRecord', { record: JSON.parse(payload) })
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
  },
  setOngoingHolds (state, { ongoingHolds }) {
    state.ongoingHolds = ongoingHolds
  },
  storeRecord (state, { record }) {
    Vue.set(state.rtholds, record['hold_id'], { x: record['x'], y: record['y'], z: record['z'] })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
