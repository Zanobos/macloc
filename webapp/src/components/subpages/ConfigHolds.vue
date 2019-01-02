<template>
  <div>
    <form-hold></form-hold>
    <list-holds></list-holds>
  </div>
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
