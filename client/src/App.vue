<template>
<div id="app">
    <p>{{ greeting }}</p>
    <p>{{ flaskGreeting }}</p>
    <my-map></my-map>
</div>
</template>

<script>
import Map from '@/components/Map.vue'

export default {
    name: 'App',
    components: {
      "my-map": Map
    },
    data() {
      return {
        greeting: 'Hello, Vue!',
        flaskGreeting: ""
      }
    },
    created: async function(){
        const gResponse = await fetch("http://localhost:5000/greeting");
        const gObject = await gResponse.json();
        this.flaskGreeting = gObject.greeting;
    }
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
