<template>
  <div>
    <sub-navbar parentRouteLabel="Configuration" />
    <b-container>
      <router-view/>
    </b-container>
  </div>
</template>

<script>
import SubNavbar from '@/components/SubNavbar.vue'

export default {
  name: 'Configuration',
  components: {
    SubNavbar
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
