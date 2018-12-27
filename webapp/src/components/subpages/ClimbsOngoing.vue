<template>
  <b-container>
    <b-row>
      <h2>Here ongoing climb</h2>
    </b-row>
    <b-row>
      <b-col cols="3">
        <p>Climber name: {{ongoingClimb}}</p>
      </b-col>
      <b-col>
        <img  class="d-block img-fluid w-100"
              alt="image slot"
              :src="getImg(ongoingClimb.wall_id)"
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
    getImg: getWallImg
  }
}
</script>
