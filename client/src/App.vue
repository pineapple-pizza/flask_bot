<template>
  <v-app>
    <div id="app">
        <home></home>
    </div>
  </v-app>
</template>

<script>
import Home from "@/views/Home.vue";
export default {
  name: "App",
  components: {
    "home": Home
  },
  data() {
    return {};
  },
};
</script>

<style lang="sass">
#app
  font-family: Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #2c3e50
  margin-top: 30px
</style>