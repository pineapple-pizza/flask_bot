<template>
  <div class="home">
      <my-navbar></my-navbar>
      <my-map></my-map>
      <my-footer></my-footer>
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: 'Home',
  components: {
    "my-map": Map,
    "my-navbar": Navbar,
    "my-footer": Footer,
  }
}
</script>