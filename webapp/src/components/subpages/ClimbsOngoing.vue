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
        <p>Connected?{{connected}}</p>
        <b-card v-for="hold in ongoingHolds" :key="hold.id" class="mb-1">
          <b-card-body>
          <p class="card-text" style="text-align: left">
            <ul>
              <li>Id: {{ hold.id }} </li>
              <li>Type: {{ hold.hold_type }} </li>
              <li>Force 1: {{getForceByHoldId('x', hold.id)}}</li>
              <li>Force 2: {{getForceByHoldId('y', hold.id)}}</li>
              <li>Force 3: {{getForceByHoldId('z', hold.id)}}</li>
            </ul>
          </p>
        </b-card-body>
        </b-card>
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
import { mapActions, mapState, mapGetters } from 'vuex'
import { getWallImg } from '@/utils'

export default {
  name: 'ClimbsOngoing',
  computed: {
    ...mapState({
      connected: state => state.realtime.isConnected,
      ongoingClimb: state => state.realtime.ongoingClimb,
      ongoingWall: state => state.realtime.ongoingWall,
      ongoingHolds: state => state.realtime.ongoingHolds,
      rtholds: state => state.realtime.rtholds
    }),
    ...mapGetters({
      getForceByHoldId: 'realtime/getForceByHoldId'
    })
  },
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
    },
    getOngoingWallImg () {
      var id = this.ongoingClimb.wall_id
      return getWallImg(id)
    }
  }
}
</script>
