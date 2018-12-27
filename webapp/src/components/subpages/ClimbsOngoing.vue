<template>
  <div>
    <list-climbs></list-climbs>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ListClimbs from '@/components/collections/ListClimbs.vue'

export default {
  name: 'ClimbsOngoing',
  components: {
    ListClimbs
  },
  created () {
    // I fetch all the possible walls, and I put all of them in a carousel
    this.$store.dispatch('walls/initWallsMeta', {page: 1, per_page: 20}).then(() => {
      this.$store.dispatch('walls/fetchWalls', this.wallsMeta)
    })
  },
  ...mapActions([
    'climbs/getClimb',
    'climbs/updateClimb'
  ]),
  ...mapActions({
    getClimb: 'climbs/getClimb',
    updateClimb: 'climbs/updateClimb'
  })
}
</script>
