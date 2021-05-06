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
  margin: 1%;
  min-height: 12em;
}

@media screen and (max-width: 875px) {
  .panel-card {
    width: 98%;
  }
}

@media screen and (min-width: 875px) and (max-width: 1264px) {
  .panel-card {
    width: 48%;
  }
}

@media screen and (min-width: 1264px) and (max-width: 10000px) {
  .panel-card {
    width: 31.33%;
  }
}
</style>
