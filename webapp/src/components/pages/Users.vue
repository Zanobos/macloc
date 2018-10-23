<template>
  <div>
    <list-users></list-users>
  </div>
</template>

<script>
import ListUsers from '@/components/ListUsers.vue'

export default {
  name: 'Users',
  components: {
    ListUsers
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
