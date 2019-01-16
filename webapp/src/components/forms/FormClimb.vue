<template>
  <div>
    <b-form @submit="onSubmit" v-if="show">
      <!-- At the moment not used, only id to be faster -->
      <b-form-group id="userInputGroup"
                    label="User:"
                    label-for="userInput">
        <b-form-select id="userInput"
          :options="users"
          v-model="selectedUser">
        <template slot="first">
          <option :value="null" disabled>-- Select a user --</option>
        </template>
        </b-form-select>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  data () {
    return {
      show: true,
      selectedUser: null
    }
  },
  computed: {
    ...mapGetters({
      users: 'users/getUsersLabelledByName'
    })
  },
  props: {
    wallId: Number
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      var router = this.$router
      var form = {}
      form.onResponse = function (response) {
        router.push('climbs/ongoing')
      }
      form.wallId = this.wallId
      form.userId = this.selectedUser.id
      this.createClimb(form)
    },
    ...mapActions({
      createClimb: 'climbs/createClimb',
      fetchUsers: 'users/fetchUsers'
    })
  },
  created () {
    this.fetchUsers()
  }
}
</script>
