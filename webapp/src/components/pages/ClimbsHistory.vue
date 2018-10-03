<template>
  <div>
    QUI TUTTE LE SCALATE FATTE
    <ul>
      <li
        v-for="climb in climbs"
        :key="climb.id">
        Climber: {{ climb.climber_name }}
        Date: {{climb.start_time}}
      </li>
    </ul>
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
    this.$store.dispatch('climbs/initClimbsMeta', {page: 1, per_page: 1}).then(() => {
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
