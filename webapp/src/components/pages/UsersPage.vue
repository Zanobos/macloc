<template>
  <div>
    <form-user></form-user>
    <list-users></list-users>
  </div>
</template>

<script>
import ListUsers from '@/components/collections/ListUsers.vue'
import FormUser from '@/components/forms/FormUser.vue'

export default {
  name: 'UsersPage',
  components: {
    ListUsers,
    FormUser
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
