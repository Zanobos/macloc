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
      <b-col>
        <real-time-holds-graph></real-time-holds-graph>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import { getWallImg } from '@/utils'
import RealTimeHoldsGraph from '@/components/graphs/RealTimeHoldsGraph.vue'

export default {
  name: 'ClimbsOngoing',
  components: {
    RealTimeHoldsGraph
  },
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
    this.getOngoingClimb()
  },
  methods: {
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
