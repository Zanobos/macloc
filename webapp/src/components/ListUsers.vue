<template>
  <div>
    <b-card v-for="user in users" :key="user.id" class="mb-1">
      <b-card-body>
        <p class="card-text" style="text-align: left">
            <ul>
              <li>Name: {{ user.name }} </li>
              <li>Nick: {{ user.nickname }} </li>
              <li>Height: {{ user.height}} </li>
              <li>Weight: {{ user.weight}} </li>
            </ul>
          </p>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: mapState({
    users: state => state.users.users,
    usersMeta: state => state.users.usersMeta
  }),
  created () {
    this.$store.dispatch('users/initUsersMeta', {page: 1, per_page: 20}).then(() => {
      this.$store.dispatch('users/fetchUsers', this.usersMeta)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
</style>
