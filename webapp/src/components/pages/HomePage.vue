<template>
  <div>
    <carousel-walls></carousel-walls>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CarouselWalls from '@/components/CarouselWalls.vue'

export default {
  name: 'HomePage',
  components: {
    CarouselWalls
  },
  computed: mapState({
    walls: state => state.walls.walls,
    active: state => state.activeStatus,
    wallsMeta: state => state.walls.wallsMeta
  }),
  created () {
    this.$store.dispatch('walls/fetchWalls', this.wallsMeta)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
