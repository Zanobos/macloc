<template>
  <div class="col">
    <b-carousel id="carousel1"
      style="text-shadow: 1px 1px 2px #333;"
      class="d-block"
      controls
      indicators
      background="#ababab"
      :interval="0"
      v-model="slide"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >

      <b-carousel-slide v-for="wall in walls" :key="wall.id">
        <img  slot="img"
              class="d-block img-fluid w-100"
              alt="image slot"
              :src="getImg(wall.id)"
        >
        <b-button v-if="carouselFormProp" v-b-toggle.collapse1>Start climbing wall #{{wall.id}}</b-button>
        <b-collapse id="collapse1">
          <component :is="carouselFormProp" v-bind:wallId="wall.id"/>
        </b-collapse>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: {
    carouselFormProp: { type: Object, required: false }
  },
  data () {
    return {
      slide: 0,
      sliding: null
    }
  },
  computed: mapState({
    walls: state => state.walls.walls,
    wallsMeta: state => state.walls.wallsMeta
  }),
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    getImg (id) {
      var images = require.context('@/assets/img/walls/', false, /\.png$/)
      return images('./wall' + id + '.png')
    }
  },
  created () {
    // I fetch all the possible walls, and I put all of them in a carousel
    this.$store.dispatch('walls/initWallsMeta', {page: 1, per_page: 20}).then(() => {
      this.$store.dispatch('walls/fetchWalls', this.wallsMeta)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
</style>
