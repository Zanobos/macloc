<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <!-- At the moment not used, only id to be faster -->
      <b-form-group id="userNameInputGroup"
                    label="User name:"
                    label-for="userNameInput">
        <b-form-input id="userNameInput"
                      type="text"
                      v-model="form.userName"
                      placeholder="Enter user name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="userIdInputGroup"
                    label="User Id:"
                    label-for="userIdInput">
        <b-form-input id="userIdInput"
                      type="number"
                      v-model="form.userId"
                      placeholder="Enter user id">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      form: {
        wallId: this.wallId,
        userId: '',
        name: ''
      },
      show: true
    }
  },
  props: {
    wallId: Number
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      var router = this.$router
      this.form.onResponse = function (response) {
        router.push('climbs/ongoing')
      }
      this.createClimb(this.form)
    },
    onReset (evt) {
      evt.preventDefault()
      /* Reset our form values */
      this.form.wallId = ''
      this.form.userId = ''
      this.form.name = ''
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    },
    ...mapActions([
      'climbs/createClimb'
    ]),
    ...mapActions({
      createClimb: 'climbs/createClimb'
    })
  }
}
</script>
