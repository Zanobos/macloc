<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>
        <form-hold></form-hold>
      </b-col>
      <b-col>
        <list-holds></list-holds>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import ListHolds from '@/components/collections/ListHolds.vue'
import FormHold from '@/components/forms/FormHold.vue'

export default {
  name: 'ConfigHolds',
  components: {
    ListHolds,
    FormHold
  }
}
</script>
