<template>
  <div>
    <form action="">
      <v-text-field label="Browse projects..." append-icon="mdi-magnify" />
    </form>

    <div class="panel">
      <github-project-card
        v-for="(project, index) in showcasedRepositories"
        class="panel-card"
        :key="index"
        :project="project"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GithubProjectCard from "@/components/GithubProjectCard";

export default {
  components: { GithubProjectCard },
  data() {
    return {
      projects: [],
    };
  },
  computed: {
    ...mapGetters("github", ["showcasedRepositories"]),
  },
  mounted() {
    // load list of repositories (only if required)
    this.$store.dispatch("github/loadRepositories");
  },
};
</script>

<style scoped>
.panel {
  display: flex !important;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}

.panel-card {
  width: 35em;
  height: 15em;
  margin-bottom: 3em;
}
</style>
