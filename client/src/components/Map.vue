<template>
  <v-container>
    <v-row justify="space-around">
      <v-card class="card-edit">
        <v-app-bar flat color="deep-purple lighten-3">
          <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

          <v-toolbar-title class="title white--text pl-0">
            GrandPy Bot
          </v-toolbar-title>

          <v-spacer></v-spacer>

          <v-row align="center" justify="end">
            <span class="white--text" id="temp_slnm">
              {{ temp }}
            </span>
            <div>
              <v-img :src="weather_icon" id="icon_weather"></v-img>
            </div>
          </v-row>
        </v-app-bar>

        <v-card-text class="card-text">
          <div class="font-weight-bold text-center">
            {{ currentDateWithFormat }}
          </div>
          <div v-for="(message, i) in allMessages" :key="i">
            <v-row justify="start" class="mt-3 ml-1">
              <div class="sender-bulle font-italic">
                <p v-text="message.input" id="message_slnm"></p>
              </div>
            </v-row>
            <v-row justify="end" class="mr-1">
              <div class="bot-bulle">
                <v-card flat class="map-edit">
                  <div>{{ message.answer }} {{ message.address }}</div>
                  <div v-html="message.wiki" id="wiki_text"></div>
                  <div v-html="message.map" id="map_widget"></div>
                </v-card>
              </div>
            </v-row>
          </div>
        </v-card-text>
        <v-card-actions>
          <div class="input-field">
            <v-text-field
              label="écris ta question ici"
              rounded
              dense
              filled
              v-model="inputValue"
              name="input_search"
              @keyup.enter="getData"
            ></v-text-field>
          </div>
          <div class="pb-7 pl-5">
            <v-btn
              despressed
              rounded
              color="deep-purple lighten-3"
              dark
              @click="getData"
              type="submit"
              name="submit_search"
              >submit</v-btn
            >
          </div>
        </v-card-actions>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import axios from "@/plugins/axios.js";

export default {
  name: "Map",
  props: {},
  data() {
    return {
      map: null,
      lat: "",
      lon: "",
      address: "",
      inputValue: "",
      extract: "",
      temp: "",
      weather_icon: "",
      newInput: "",
      allMessages: [],
      currentDateWithFormat: new Date()
        .toJSON()
        .slice(0, 10)
        .replace(/-/g, "/"),
      randomSentences: [
        {
          text: "Evidémment, mon petit eucalyptus! La voici : ",
        },
        {
          text:
            "C'est une bonne question laisse-moi chercher mes lunettes et je te dis ça... Ah, les voici. Pour te répondre, c'est : ",
        },
        {
          text:
            "Tu demandes beaucoup de choses dis-donc! Heureusement que je connais tout ahah. ",
        },
        {
          text:
            "Tu devrais ranger ta chambre avant de me demander une adresse. Mais comme je suis gentil, je te la donne : ",
        },
        {
          text: "Pourquoi tu ne cherches pas sur ta brique cellulaire ? ",
        },
        {
          text: "J'ai rencontré ta grand-mère là-bas, héhé.... La voici : ",
        },
        {
          text:
            "Oui, évidemment ! Il devrait y avoir un fleuriste dans le coin, n'oublie pas d'acheter des fleurs pour ta mère. ",
        },
      ],
      selectedSentence: "",
    };
  },
  methods: {
    // method request to get res from /api/data
    getData() {
      axios
        .get("data", {
          params: {
            query: this.inputValue,
          },
        })
        .then((res) => {
          this.lat = res.data.lat;
          this.lon = res.data.lon;
          this.address = res.data.display_name;

          // calling functions that will create the map and the wiki text and displaying results
          this.createMap();
          this.getWiki();
          this.getWeather();

          // to get a random sentence from randomSentences[]
          const idx = Math.floor(Math.random() * this.randomSentences.length);
          this.selectedSentence = this.randomSentences[idx];

          // pushing all in allMessages[] so we can display it dynamically
          this.allMessages.push({
            input: this.inputValue,
            answer: this.selectedSentence.text,
            address: this.address,
          });

          // reseting inputValue to "" so the input won't display the value we just typed
          this.inputValue = "";
        })
        .catch((err) => {
          // Handle Error Here
          console.error(err);
        });
    },

    createMap() {
      // function to create the map from /api/map
      axios
        .get("map", {
          params: {
            lat: this.lat,
            lon: this.lon,
            name: this.address,
          },
        })
        .then((res) => {
          this.map = res.data;
          this.allMessages.push({
            map: this.map,
          });
        })
        .catch((err) => {
          // Handle Error Here
          console.error(err);
        });
    },
    getWiki() {
      // function to get the wiki results from /api/wiki
      axios
        .get("wiki", {
          params: {
            query: this.inputValue,
          },
        })
        .then((res) => {
          this.extract = res.data;
          this.allMessages.push({
            wiki: this.extract,
          });
        })
        .catch((err) => {
          // Handle Error Here
          console.error(err);
        });
    },
    getWeather() {
      // function to get the weather results from /api/weather
      axios
        .get("weather", {
          params: {
            query: this.inputValue,
          },
        })
        .then((res) => {
          this.temp = res.data.temperature + "°C";
          this.weather_icon =
            "http://openweathermap.org/img/wn/" + res.data.icon + ".png";

        })
        .catch((err) => {
          // Handle Error Here
          console.error(err);
        });
    },
  },
};
</script>

<style scoped lang="sass">
.map-edit
  width: 300px
  background-color: transparent

.card-edit
  height: 570px

.card-text
  overflow: scroll
  height: 430px
  text-align: justify

.sender-bulle
  height: 100%
  width: 100%

.input-field
  width: 280px
</style>
