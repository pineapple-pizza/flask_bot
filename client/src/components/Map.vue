<template>
  <v-container>
    <v-row justify="space-around">
      <v-card width="400" class="card-edit">
        <v-app-bar flat color="deep-purple lighten-3">
          <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

          <v-toolbar-title class="title white--text pl-0">
            GrandPy Bot
          </v-toolbar-title>

          <v-spacer></v-spacer>

          <v-btn color="white" icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </v-app-bar>

        <v-card-text class="card-text">
          <div class="font-weight-bold ml-8 mb-2">
            {{ currentDateWithFormat }}
          </div>
          <div v-for="(message, i) in allMessages" :key="i">
            <v-row justify="start" class="mt-3">
              <div class="sender-bulle font-italic">
                <p v-text="message.input"></p>
              </div>
            </v-row>
            <v-row justify="end">
              <div class="bot-bulle">
                <v-card flat class="map-edit">

                  <div>{{message.answer}} {{message.address}}</div>
                  <div v-html="message.wiki"></div>
                  <div v-html="message.map"></div>
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
      newInput: "",
      allMessages: [],
      currentDateWithFormat: new Date()
        .toJSON()
        .slice(0, 10)
        .replace(/-/g, "/"),
      randomSentences: [
        {
          text: 'Evidémment, mon petit eucalyptus! La voici : '
        },
        {
          text: "C'est une bonne question laisse-moi chercher mes lunettes et je te dis ça... Ah, les voici. Pour te répondre, c'est : "
        },
        {
          text: 'Tu demandes beaucoup de choses dis-donc! Heureusement que je connais tout ahah. '
        },
        {
          text: 'Tu devrais ranger ta chambre avant de me demander une adresse. Mais comme je suis gentil, je te la donne : '
        },
        {
          text: 'Pourquoi tu ne cherches pas sur ta brique cellulaire ? '
        },
        {
          text: "J'ai rencontré ta grand-mère là-bas, héhé.... La voici : "
        },
        {
          text: "Oui, évidemment ! Il devrait y avoir un fleuriste dans le coin, n'oublie pas d'acheter des fleurs pour ta mère. "
        },
      ],
      selectedSentence: ''
    };
  },
  methods: {
    getData() {
      axios
        .get("data/", {
          params: {
            query: this.inputValue,
          },
        })
        .then((res) => {
          this.lat = res.data.lat;
          this.lon = res.data.lon;
          this.address = res.data.display_name;
          this.createMap();
          this.getWiki();

          const idx = Math.floor(Math.random() * this.randomSentences.length);
          this.selectedSentence = this.randomSentences[idx]

          console.log("selected senntence", this.selectedSentence)

          this.allMessages.push({
            input: this.inputValue,
            answer: this.selectedSentence.text,
            address: this.address
          });
          console.log("all messages", this.allMessages);

          this.inputValue = "";
          console.log("res", res.data.display_name);
          console.log("coordinaites", this.lat, this.lon);
        })
        .catch((err) => {
          // Handle Error Here
          console.error(err);
        });
    },

    createMap() {
      axios
        .get("map/", {
          params: {
            lat: this.lat,
            lon: this.lon,
            name: this.address,
          },
        })
        .then((res) => {
          console.log(res);
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
      axios
        .get("wiki/", {
          params: {
            query: this.inputValue,
          },
        })
        .then((res) => {
          console.log("wiki", res);
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

.bot-bulle

.input-field
  width: 280px
</style>
