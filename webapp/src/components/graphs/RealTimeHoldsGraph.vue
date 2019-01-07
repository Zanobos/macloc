
<template>
  <div id="wall"
      :style="{ 'background-image': 'url(\'' + getOngoingWallImg()+ '\')' }">

  </div>
</template>

<script>
/* globals window, requestAnimationFrame */
import * as d3 from 'd3'
import { mapState, mapGetters } from 'vuex'
import { getWallImg } from '@/utils'

export default {
  data () {
    return {
      svgContainer: {}
    }
  },
  computed: {
    ...mapState({
      ongoingClimb: state => state.realtime.ongoingClimb,
      ongoingWall: state => state.realtime.ongoingWall,
      ongoingHolds: state => state.realtime.ongoingHolds,
      rtholds: state => state.realtime.rtholds
    }),
    ...mapGetters({
      getForceByHoldId: 'realtime/getForceByHoldId'
    })
  },
  methods: {
    getOngoingWallImg () {
      var id = this.ongoingClimb.wall_id
      return getWallImg(id)
    },
    drawWall () {
      // same height and width of the wall
      this.svgContainer = d3.select('#wall')
        .append('svg')
        .attr('width', '100%')
        .attr('height', '100%')
      // Adding the definition of the arrowhead
      var defs = this.svgContainer.append('defs')
      var marker = defs.append('marker')
        .attr('id', 'arrow')
        .attr('viewBox', '0 -5 10 10')
        .attr('refX', 5)
        .attr('refY', 0)
        .attr('markerWidth', 6)
        .attr('markerHeight', 6)
        .attr('orient', 'auto')
      marker.append('path')
        .attr('d', 'M0,-5L10,0L0,5')
        .attr('class', 'arrowHead')
    },
    drawHolds () {
      // Joining data
      var circle = this.svgContainer.selectAll('circle')
        .data(this.ongoingHolds)
      // Removing old data
      circle.exit().remove()
      // New data and update of existing
      circle.enter()
        .append('circle')
        .merge(circle)
        .attr('cx', 100)
        .attr('cy', 100)
        .attr('r', 100)
        .style('fill', 'green')
    }
  },
  mounted () {
    this.drawWall()
    this.drawHolds()
  }
}
</script>

<style>
  #wall {
    width: 100%;
    height: 100%;
  }
</style>
