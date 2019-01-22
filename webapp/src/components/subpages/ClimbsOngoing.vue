<template>
  <b-container>
    <b-row>
      <b-col cols="3">
        <p>Climber name: {{ongoingClimb(this.wallId)}}</p>
        <b-button :disabled="startButtonDisabled()" class="w-100 mb-1" variant="primary" @click="onStart">Start</b-button>
        <b-button :disabled="endButtonDisabled()" class="w-100" variant="danger" @click="onEnd">End</b-button>
        <p>Connected?{{connected}}</p>
        <b-card v-for="hold in ongoingClimb(this.wallId).holds" :key="hold.id" class="mb-1">
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
        <real-time-holds-graph :wallId="this.wallId"></real-time-holds-graph>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import { getWallImg } from '@/utils'
import RealTimeHoldsGraph from '@/components/graphs/RealTimeHoldsGraph.vue'

export default {
  props: {
    wallId: Number
  },
  components: {
    RealTimeHoldsGraph
  },
  computed: {
    ...mapState({
      connected: state => state.realtime.isConnected,
      rtholds: state => state.realtime.rtholds
    }),
    ...mapGetters({
      getForceByHoldId: 'realtime/getForceByHoldId',
      ongoingClimb: 'realtime/ongoingClimb'
    })
  },
  methods: {
    ...mapActions({
      startClimb: 'climbs/startClimb',
      endClimb: 'climbs/endClimb'
    }),
    startButtonDisabled () {
      var dis = this.ongoingClimb(this.wallId) == null
      if (!dis) {
        dis = this.ongoingClimb(this.wallId).status !== 'ready'
      }
      return dis
    },
    endButtonDisabled () {
      var dis = this.ongoingClimb(this.wallId) == null
      if (!dis) {
        dis = this.ongoingClimb(this.wallId).status !== 'start'
      }
      return dis
    },
    onStart (evt) {
      evt.preventDefault()
      var payload = {}
      payload.climbId = this.ongoingClimb(this.wallId).id
      this.startClimb(payload)
    },
    onEnd (evt) {
      evt.preventDefault()
      var payload = {}
      payload.climbId = this.ongoingClimb(this.wallId).id
      this.endClimb(payload)
    },
    getOngoingWallImg () {
      return getWallImg(this.wallId)
    }
  }
}
</script>
