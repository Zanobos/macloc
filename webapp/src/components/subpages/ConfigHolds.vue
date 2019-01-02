<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>
        <config-holds-insert-hold></config-holds-insert-hold>
      </b-col>
      <b-col>
        <list-holds></list-holds>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import ListHolds from '@/components/collections/ListHolds.vue'
import ConfigHoldsInsertHold from '@/components/subpages/ConfigHoldsInsertHold.vue'

export default {
  name: 'ConfigHolds',
  components: {
    ListHolds,
    ConfigHoldsInsertHold
  }
}
</script>
