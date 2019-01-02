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
import { mapActions, mapState } from 'vuex'

export default {
  computed: mapState({
    users: state => state.users.users
  }),
  methods: {
    ...mapActions({
      fetchUsers: 'users/fetchUsers'
    })
  },
  created () {
    this.fetchUsers()
  }
}
</script>
