<template>
  <div>
    QUI TUTTI I WALLS ATTIVI
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'HomePage',
  computed: mapState({
    walls: state => state.walls.all
  }),
  created () {
    this.$store.dispatch('walls/getWalls')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
