<template>
  <v-card v-if="displayProject">
    <div class="d-flex flex-no-wrap justify-space-between">
      <div>
        <v-card-title class="headline" v-text="project.name"></v-card-title>

        <v-card-subtitle v-text="project.description"></v-card-subtitle>

        <github-project-topics :topics="project.topics" />

        <v-card-actions>
          <v-btn
            class="ml-2 mt-5"
            outlined
            small
            :href="project.repository_url"
            target="source"
          >
            VIEW SOURCE</v-btn
          >

          <v-btn
            class="ml-2 mt-5"
            color="accent"
            outlined
            small
            v-if="project.showcase_url"
            :href="project.showcase_url"
            target="demo"
          >
            OPEN DEMO</v-btn
          >
        </v-card-actions>
      </div>
    </div>
  </v-card>
</template>

<script>
import GithubProjectTopics from "@/components/GithubProjectTopics";

export default {
  components: { GithubProjectTopics },
  props: {
    project: Object,
  },
  computed: {
    /**
     * Ensure project is not hidden and contains a description before displaying.
     */
    displayProject() {
      return (
        this.project &&
        this.project.name[0] != "." &&
        !!this.project.description &&
        !this.project.forked
      );
    },
  },
};
</script>
