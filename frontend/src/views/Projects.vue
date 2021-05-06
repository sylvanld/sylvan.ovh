<template>
  <div class="home">
    <v-container>
      <h2>Personal projects</h2>
      <GithubProjectsPanel />
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import GithubProjectsPanel from "@/components/GithubProjectsPanel.vue";

export default {
  name: "Home",
  components: {
    GithubProjectsPanel,
  },
};
</script>
