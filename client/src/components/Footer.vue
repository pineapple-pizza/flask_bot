<template>
  <div>
    <v-footer color="grey lighten-4" fixed>
      <v-row justify="center" no-gutters>
        <v-btn
          v-for="(link, i) in links"
          :key="i"
          light
          text
          rounded
          class="my-2"
          :to="link.url"
        >
          {{ link.name }}
        </v-btn>
      </v-row>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data: () => ({
    links: [
      { name: "Github", url: "url github" },
      { name: "Trello", url: "url trello" },
    ],
  }),
};
</script>

<style scoped lang="sass"></style>
