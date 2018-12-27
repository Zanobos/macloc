<template>
  <div>
    <h2>Here ongoing climb</h2>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

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
    })
  }
}
</script>
