<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="canIdInputGroup"
                    label="Can ID:"
                    label-for="canIdInput"
                    horizontal>
        <b-form-input id="canIdInput"
                      type="text"
                      v-model="form.can_id"
                      required
                      placeholder="Enter can ID">
        </b-form-input>
      </b-form-group>
      <b-form-group id="distFromSxInputGroup"
                    label="Dist from left:"
                    label-for="distFromSxInput"
                    horizontal>
        <b-form-input id="distFromSxInput"
                      type="number"
                      v-model="form.dist_from_sx"
                      required
                      placeholder="Enter distance from left edge (in cm)">
        </b-form-input>
      </b-form-group>
      <b-form-group id="distFromBotInputGroup"
                    label="Dist from bottom:"
                    label-for="distFromBotInput"
                    horizontal>
        <b-form-input id="distFromBotInput"
                      type="number"
                      v-model="form.dist_from_bot"
                      required
                      placeholder="Enter distance from bottom (in cm)">
        </b-form-input>
      </b-form-group>
      <b-form-group id="holdTypeInputGroup"
                    label="Hold type:"
                    label-for="holdTypeInput"
                    horizontal>
        <b-form-input id="holdTypeInput"
                      type="text"
                      v-model="form.hold_type">
        </b-form-input>
      </b-form-group>
      <b-form-group id="wallIdInputGroup"
                    label="Wall ID:"
                    label-for="wallIdInput"
                    horizontal>
        <b-form-select id="wallIdInput"
                      :options="wallIds"
                      v-model="form.wall_id">
          <template slot="first">
            <option :value="null">-- No wall --</option>
          </template>
        </b-form-select>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  data () {
    return {
      form: {
        can_id: '',
        dist_from_sx: '',
        dist_from_bot: '',
        hold_type: null,
        wall_id: null
      },
      show: true
    }
  },
  computed: {
    ...mapGetters({
      wallIds: 'walls/wallIds'
    })
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      this.createHold(this.form)
    },
    onReset (evt) {
      evt.preventDefault()
      /* Reset our form values */
      this.form.can_id = ''
      this.form.dist_from_sx = ''
      this.form.dist_from_bot = ''
      this.form.hold_type = ''
      this.wall_id = null
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    },
    ...mapActions({
      createHold: 'holds/createHold',
      fetchWalls: 'walls/fetchWalls'
    })
  },
  created () {
    this.fetchWalls()
  }
}
</script>
