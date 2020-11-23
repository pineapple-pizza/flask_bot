<template>
  <div>
    <v-footer color="grey lighten-4" fixed>
      <v-row justify="center" no-gutters>
        <p class="mt-3">
        <strong>Anouchik Aslanian</strong> —
          </p>
        <v-btn
          v-for="(link, i) in links"
          :key="i"
          light
          text
          rounded
          class="my-2"
        >
        <a :href="link.url" class="link-edit" target="blank">
          {{ link.name }}
        </a>
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
      { name: "Github", url: "https://github.com/pineapple-pizza/flask_bot" },
      { name: "Trello", url: "https://trello.com/b/LcpxO7X5/projet-7" },
    ],
  }),
};
</script>

<style scoped lang="sass">
.link-edit
  text-decoration: none
  color: inherit

</style>
