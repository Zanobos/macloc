<template>
  <b-container>
    <b-row class="mt-2">
      <b-col>
        <form-user></form-user>
      </b-col>
      <b-col>
        <list-users></list-users>
      </b-col>
    </b-row>
  </b-container>
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
