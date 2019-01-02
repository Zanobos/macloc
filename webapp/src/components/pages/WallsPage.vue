<template>
  <div>
    <carousel-walls v-bind:carouselFormProp="formClimb"></carousel-walls>
  </div>
</template>

<script>
import CarouselWalls from '@/components/collections/CarouselWalls.vue'
import FormClimb from '@/components/forms/FormClimb.vue'

export default {
  name: 'WallsPage',
  components: {
    CarouselWalls,
    FormClimb
  },
  data () {
    return {
      formClimb: FormClimb
    }
  }
}
</script>
