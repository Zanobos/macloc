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
      </b-col>
      <b-col>
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
    ongoingClimb: state => state.ongoingClimb
  }),
  created () {
    // If the climb is in state "ready", it's local state, and the obj is not null
    if (this.ongoingClimb == null) {
      // If no local climb in status "ready", then check if it exist in server
      this.getCurrentClimb()
    }
  },
  methods: {
    ...mapActions([
      'climbs/startClimb',
      'climbs/endClimb',
      'climbs/getCurrentClimb'
    ]),
    ...mapActions({
      startClimb: 'climbs/startClimb',
      endClimb: 'climbs/endClimb',
      getCurrentClimb: 'climbs/getCurrentClimb'
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
