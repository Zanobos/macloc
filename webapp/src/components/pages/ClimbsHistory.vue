<template>
  <div>
    QUI TUTTE LE SCALATE FATTE
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ClimbsHistory',
  computed: mapState({
    climbs: state => state.climbs.all
  }),
  created () {
    this.$store.dispatch('walls/fetchClimbs')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
