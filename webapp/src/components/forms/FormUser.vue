<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="nameInputGroup"
                    label="Name:"
                    label-for="nameInput">
        <b-form-input id="nameInput"
                      type="text"
                      v-model="form.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="emailInputGroup"
                    label="Email address:"
                    label-for="emailInput"
                    description="We'll never share your email with anyone else.">
        <b-form-input id="emailInput"
                      type="email"
                      v-model="form.email"
                      placeholder="Enter email">
        </b-form-input>
      </b-form-group>
      <b-form-group id="heightInputGroup"
                    label="Height (in cm):"
                    label-for="heightInput">
        <b-form-input id="heightInput"
                      required
                      v-model="form.height">
        </b-form-input>
      </b-form-group>
      <b-form-group id="weightInputGroup"
                    label="Weight (in cm):"
                    label-for="weightInput">
        <b-form-input id="weightInput"
                      required
                      v-model="form.weight">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      form: {
        email: '',
        name: '',
        height: '',
        weight: ''
      },
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      this.createUser(this.form)
    },
    onReset (evt) {
      evt.preventDefault()
      /* Reset our form values */
      this.form.name = ''
      this.form.email = ''
      this.form.height = ''
      this.form.weight = ''
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    },
    ...mapActions({
      createUser: 'users/createUser'
    })
  }
}
</script>
