<template>
  <div>
    <sub-navbar parentRouteLabel="Climbs" />
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
