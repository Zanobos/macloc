<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>
        <insert-wall></insert-wall>
      </b-col>
      <b-col>
        <carousel-walls></carousel-walls>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import CarouselWalls from '@/components/collections/CarouselWalls.vue'
import InsertWall from '@/components/subpages/InsertWall.vue'

export default {
  name: 'WallsPage',
  components: {
    CarouselWalls,
    InsertWall
  }
}
</script>
