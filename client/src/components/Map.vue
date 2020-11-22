<template>
  <div>
    <input type="text" placeholder="searching for..." v-model="inputValue">
    <button @click.prevent="getData" type="submit">submit</button>

  <!-- <div class="map-edit"> -->

    <!-- <template>  -->
      <div v-html="map"></div>
      <!-- </template> -->
  <!-- </div> -->

    <div v-html="extract"></div>
  </div>
</template>

<script>
import axios from '@/plugins/axios.js'

export default {
  name: 'Map',
  props: {
  },
  data() {
    return {
      map: null,
      lat: '',
      lon: '',
      address: '',
      inputValue: '',
      extract: ''
    };
  },
  methods: {
    getData(e) {
      e.preventDefault()
      console.log('in some action')
      axios.get("data/", {
        params: {
          query: this.inputValue
        }
      })
      .then(res => {
          this.lat = res.data.lat
          this.lon = res.data.lon
          this.address = res.data.display_name
          this.createMap()
          this.getWiki()
          console.log('res', res.data.display_name)
          console.log('coordinaites', this.lat, this.lon)
        });
    },

    createMap() {
      axios.get("map/", {
        params: {
          lat: this.lat,
          lon: this.lon,
          name: this.address
        }
      })
      .then(res => {
        console.log(res)
        this.map = res.data
        });
    },
    getWiki() {
      axios.get('wiki/', {
        params: {
          query: this.inputValue
        }
      })
      .then(res => {
        console.log('wiki', res)
        this.extract = res.data
        });
    }
  }
}
</script>

<style scoped lang="sass">
h3
  margin: 40px 0 0

ul
  list-style-type: none
  padding: 0

li
  display: inline-block
  margin: 0 10px

a
  color: #42b983

.map-edit
  // height: 30px
</style>
