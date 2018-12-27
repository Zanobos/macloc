<template>
  <div>
    <carousel-walls v-bind:carouselFormProp="formClimb"></carousel-walls>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CarouselWalls from '@/components/collections/CarouselWalls.vue'
import FormClimb from '@/components/forms/FormClimb.vue'

export default {
  name: 'WallsPage',
  components: {
    CarouselWalls,
    FormClimb
  },
  computed: mapState({
    walls: state => state.walls.walls,
    active: state => state.activeStatus,
    wallsMeta: state => state.walls.wallsMeta
  }),
  created () {
    this.$store.dispatch('walls/fetchWalls', this.wallsMeta)
  },
  data () {
    return {
      formClimb: FormClimb
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
