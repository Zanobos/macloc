<template>
  <div>
    <b-card no-body class="mb-1" v-for="climb in climbs"
        :key="climb.id">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-btn block href="#" v-b-toggle.accordion2 variant="info">Climb #{{climb.id}}</b-btn>
      </b-card-header>
      <b-collapse id="accordion2" accordion="my-accordion" role="tabpanel">
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

    <b-pagination v-on:change="onPageChange" align="center" :total-rows="this.climbsMeta.total_items" v-model="climbsMeta.page" :per-page="climbsMeta.per_page">
    </b-pagination>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ClimbsHistory',
  computed: mapState({
    climbs: state => state.climbs.climbs,
    climbsMeta: state => state.climbs.climbsMeta
  }),
  methods: {
    onPageChange: function (page) {
      this.climbsMeta.page = page
      this.$store.dispatch('climbs/fetchClimbs', this.climbsMeta)
    }
  },
  created () {
    this.$store.dispatch('climbs/initClimbsMeta', {page: 1, per_page: 2}).then(() => {
      this.$store.dispatch('climbs/fetchClimbs', this.climbsMeta)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
