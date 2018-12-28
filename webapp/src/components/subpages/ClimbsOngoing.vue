<template>
  <b-container>
    <b-row>
      <h2>Here ongoing climb</h2>
    </b-row>
    <b-row>
      <b-col cols="3">
        <p>Climber name: {{ongoingClimb}}</p>
        <b-button :disabled="startButtonDisabled()" class="w-100 mb-1" variant="primary" @click="onStart">Start</b-button>
        <b-button :disabled="endButtonDisabled()" class="w-100" variant="danger" @click="onEnd">End</b-button>
        Connected? <p>{{connected}}</p>
      </b-col>
      <b-col v-if="ongoingClimb">
        <img  class="d-block img-fluid w-100"
              alt="image slot"
              :src="getOngoingWallImg()"
        >
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { getWallImg } from '@/utils'

export default {
  name: 'ClimbsOngoing',
  computed: mapState({
    connected: state => state.realtime.isConnected,
    ongoingClimb: state => state.realtime.ongoingClimb,
    ongoingWall: state => state.realtime.ongoingWall,
    ongoingHolds: state => state.realtime.ongoingHolds
  }),
  created () {
    // TODO change the flow using some more general if

    // If the climb is in state "ready", it's local state, and the obj is not null
    if (this.ongoingClimb == null) {
      // If no local climb in status "ready", then check if it exist in server
      this.getOngoingClimb()
    }
    if (this.ongoingClimb != null) {
      this.getOngoingWall({ wallId: this.ongoingClimb.wall_id })
      this.getOngoingHolds({ wallId: this.ongoingClimb.wall_id })
    }
  },
  methods: {
    ...mapActions([
      'climbs/startClimb',
      'climbs/endClimb',
      'climbs/getOngoingClimb',
      'walls/getOngoingWall',
      'holds/getOngoingHolds'
    ]),
    ...mapActions({
      startClimb: 'climbs/startClimb',
      endClimb: 'climbs/endClimb',
      getOngoingClimb: 'climbs/getOngoingClimb',
      getOngoingWall: 'walls/getOngoingWall',
      getOngoingHolds: 'holds/getOngoingHolds'
    }),
    getOngoingWallImg () {
      var id = this.ongoingClimb.wall_id
      return getWallImg(id)
    },
    startButtonDisabled () {
      var dis = this.ongoingClimb == null
      if (!dis) {
        dis = this.ongoingClimb.status !== 'ready'
      }
      return dis
    },
    endButtonDisabled () {
      var dis = this.ongoingClimb == null
      if (!dis) {
        dis = this.ongoingClimb.status !== 'start'
      }
      return dis
    },
    onStart (evt) {
      evt.preventDefault()
      var payload = {}
      payload.climbId = this.ongoingClimb.id
      this.startClimb(payload)
    },
    onEnd (evt) {
      evt.preventDefault()
      var payload = {}
      payload.climbId = this.ongoingClimb.id
      this.endClimb(payload)
    }
  }
}
</script>
