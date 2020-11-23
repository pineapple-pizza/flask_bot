<template>
<v-app>
  <div id="app">
      <navbar></navbar>
      <my-map></my-map>
      <my-footer></my-footer>
  </div>
</v-app>
</template>

<script>
import Map from '@/components/Map.vue'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: 'App',
    components: {
      "my-map": Map,
      "navbar": Navbar,
      "my-footer": Footer,
    },
    data() {
      return {
      }
    },
}
</script>

<style lang="sass">
#app 
  font-family: Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #2c3e50
  margin-top: 60px
</style>