<template>
  <div>
    <b-card v-for="climb in climbs" :key="climb.id" no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-btn block href="#" v-b-toggle.accordion variant="info">Climb #{{climb.id}}</b-btn>
      </b-card-header>
      <b-collapse id="accordion" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <p class="card-text" style="text-align: left">
            <ul>
              <li>Climber: {{ climb.climber_name }} </li>
              <li>Date: {{climb.start_time}} </li>
              <li>Wall grade: {{climb.wall_grade}} </li>
            </ul>
          </p>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ListClimbs',
  computed: mapState({
    climbs: state => state.climbs.climbs
  }),
  methods: {
    ...mapActions({
      fetchClimbs: 'climbs/fetchClimbs'
    })
  },
  created () {
    this.fetchClimbs({ status: 'end' })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
