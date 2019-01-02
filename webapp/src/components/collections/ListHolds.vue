<template>
  <div>
    <b-card v-for="hold in holds" :key="hold.id" class="mb-1">
      <b-card-body>
        <p class="card-text" style="text-align: left">
            <ul>
              <li>Hold id: {{ hold.id }} </li>
              <li>Can id: {{ hold.can_id }} </li>
              <li>Distance from left edge: {{ hold.dist_from_sx}} </li>
              <li>Distance from bottom: {{ hold.dist_from_bot}} </li>
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
    holds: state => state.holds.holds
  }),
  created () {
    this.fetchHolds({})
  },
  methods: {
    ...mapActions({
      fetchHolds: 'holds/fetchHolds'
    })
  }
}
</script>
