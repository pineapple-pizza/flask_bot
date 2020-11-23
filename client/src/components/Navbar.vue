<template>
  <div>
    <v-app-bar flat fixed>
        <v-toolbar-title>{{ flaskGreeting }}</v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";

export default {
    name: 'Navbar',
    components: {
    },
    data() {
      return {
        flaskGreeting: ""
      }
    },
    mounted(){
        axios
        .get("/greeting")
        .then((response) => { 
            this.flaskGreeting = response.data.greeting })
        .catch((err) => {
          // Handle Error Here
          console.error(err);
        });
    }
}
</script>

<style scoped lang="sass"></style>
