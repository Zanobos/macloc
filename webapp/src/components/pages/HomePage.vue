<template>
  <active-walls v-bind:carouselFormProp="formClimb"></active-walls>
</template>

<script>
import ActiveWalls from '@/components/collections/ActiveWalls.vue'
import FormClimb from '@/components/forms/FormClimb.vue'

export default {
  name: 'HomePage',
  components: {
    ActiveWalls,
    FormClimb
  },
  data () {
    return {
      formClimb: FormClimb
    }
  }
}
</script>
