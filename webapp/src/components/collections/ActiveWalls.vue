<template>
  <b-carousel id="carousel1"
    style="text-shadow: 1px 1px 2px #333; max-height: inherit;"
    class="d-block"
    controls
    indicators
    background="#ababab"
    :interval="0"
    v-model="slide"
    @sliding-start="onSlideStart"
    @sliding-end="onSlideEnd"
  >
    <b-carousel-slide v-for="wall in walls" :key="wall.id" img-blank
      :style="{ 'background-image': 'url(\'' + getImg(wall.id)+ '\')' }">

      <climbs-ongoing :wallId="wall.id" v-if="ongoingClimb(wall.id)"></climbs-ongoing>

      <b-button v-if="carouselFormProp" v-b-toggle.collapse1>Start climbing wall #{{wall.id}}</b-button>
      <b-collapse id="collapse1">
        <component :is="carouselFormProp" v-bind:wallId="wall.id"/>
      </b-collapse>
    </b-carousel-slide>
  </b-carousel>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import { getWallImg } from '@/utils'
import ClimbsOngoing from '@/components/subpages/ClimbsOngoing'

export default {
  props: {
    carouselFormProp: { type: Object, required: false }
  },
  components: {
    ClimbsOngoing
  },
  data () {
    return {
      slide: 0,
      sliding: null
    }
  },
  computed: {
    ...mapState({
      walls: state => state.walls.walls,
      climbs: state => state.realtime.ongoingClimbs
    }),
    ...mapGetters({
      ongoingClimb: 'realtime/ongoingClimb'
    })
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    getImg: getWallImg,
    ...mapActions({
      fetchWalls: 'walls/fetchWalls',
      getOngoingClimbs: 'realtime/getOngoingClimbs'
    })
  },
  created () {
    this.fetchWalls()
    this.getOngoingClimbs()
  }
}
</script>

<style>
.carousel-inner {
  max-height: inherit;
}
.carousel-item {
  max-height: inherit;
}
</style>
