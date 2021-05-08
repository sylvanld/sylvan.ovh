<template>
  <div>
    <form action="">
      <v-text-field
        label="Browse projects..."
        v-model="search"
        append-icon="mdi-magnify"
      />
    </form>

    <div class="panel">
      <github-project-card
        v-for="(project, index) in filteredProjects"
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

function computePertinence(project, search) {
  const projectName = project.name.toLowerCase();
  const projectDescription = (project.description || "").toLowerCase();
  const projectTopics = project.topics.join(" ").toLowerCase();
  const searchTerms = search.toLowerCase().split(" ");

  // try to find them in project
  let score = 0;
  for (let term of searchTerms) {
    if (projectName.includes(term)) {
      score += 3;
    }
    if (projectDescription.includes(term)) {
      score += 1;
    }
    if (projectTopics.includes(term)) {
      score += 2;
    }
  }
  return score;
}

export default {
  components: { GithubProjectCard },
  data() {
    return {
      search: null,
    };
  },
  computed: {
    filteredProjects() {
      if (!this.showcasedRepositories) {
        return [];
      }

      if (this.search) {
        // if search is provided, apply search algorithm to filter/sort results
        const projectsPertinences = this.showcasedRepositories.map(
          (project) => [computePertinence(project, this.search), project]
        );
        return projectsPertinences
          .filter((pp) => pp[0] > 0)
          .sort((ppA, ppB) => ppA[0] < ppB[0])
          .map((pp) => pp[1]);
      } else {
        // if no search is provided, take most pertinent project based on their content
        return this.showcasedRepositories;
      }
    },
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
