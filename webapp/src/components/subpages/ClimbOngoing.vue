<template>
  <b-container>
    <b-row>
      <b-col cols="3">
        <b-button :disabled="prepareButtonDisabled()" class="w-100 mb-1" variant="primary" @click="onPrepare">Prepare</b-button>
        <b-button :disabled="startButtonDisabled()" class="w-100 mb-1" variant="success" @click="onStart">Start</b-button>
        <b-button :disabled="endButtonDisabled()" class="w-100" variant="danger" @click="onEnd">End</b-button>
        <p>Connected?{{connected}}</p>
        <b-card
                v-for="hold in holds"
                :key="hold.id"
                class="mb-1">
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
        <real-time-holds-graph v-if="ongoingClimb(this.wallId)" :wallId="this.wallId"></real-time-holds-graph>
      </b-col>
    </b-row>
    <b-modal ref="modalSubmitRef"
      centered
      hide-footer
      title="Prepare Climb">
      <form-climb :users="users" :wallId="this.wallId" v-on:submit-climb="onSubmitNewClimb"></form-climb>
    </b-modal>
  </b-container>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import { getWallImg } from '@/utils'
import RealTimeHoldsGraph from '@/components/graphs/RealTimeHoldsGraph.vue'
import FormClimb from '@/components/forms/FormClimb.vue'

export default {
  props: {
    wallId: Number
  },
  components: {
    RealTimeHoldsGraph,
    FormClimb
  },
  computed: {
    ...mapState({
      connected: state => state.realtime.isConnected,
      rtholds: state => state.realtime.rtholds
    }),
    ...mapGetters({
      getForceByHoldId: 'realtime/getForceByHoldId',
      ongoingClimb: 'realtime/ongoingClimb',
      users: 'users/getUsersLabelledByName'
    }),
    climb () {
      return this.ongoingClimb(this.wallId)
    },
    holds () {
      return this.ongoingClimb(this.wallId) !== undefined ? this.ongoingClimb(this.wallId).holds : []
    }
  },
  methods: {
    ...mapActions({
      createClimb: 'climbs/createClimb',
      startClimb: 'climbs/startClimb',
      endClimb: 'climbs/endClimb'
    }),
    startButtonDisabled () {
      var dis = this.climb == null
      if (!dis) {
        dis = this.climb.status !== 'ready'
      }
      return dis
    },
    endButtonDisabled () {
      var dis = this.climb == null
      if (!dis) {
        dis = this.climb.status !== 'start'
      }
      return dis
    },
    prepareButtonDisabled () {
      return this.climb != null
    },
    onSubmitNewClimb (climb) {
      var payload = climb
      var modalSubmitRef = this.$refs.modalSubmitRef
      payload.onResponse = function (response) {
        modalSubmitRef.hide()
      }
      this.createClimb(payload)
    },
    onStart (evt) {
      evt.preventDefault()
      var payload = {}
      payload.climbId = this.climb.id
      this.startClimb(payload)
    },
    onEnd (evt) {
      evt.preventDefault()
      var payload = {}
      payload.climbId = this.climb.id
      this.endClimb(payload)
    },
    onPrepare (evt) {
      this.$refs.modalSubmitRef.show()
    },
    getOngoingWallImg () {
      return getWallImg(this.wallId)
    }
  }
}
</script>
