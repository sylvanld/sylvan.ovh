<template>
  <v-card v-if="displayProject">
    <div class="d-flex flex-no-wrap justify-space-between">
      <div>
        <v-card-title class="headline" v-text="project.name"></v-card-title>

        <v-card-subtitle v-text="project.description"></v-card-subtitle>

        <v-card-actions>
          <v-btn
            class="ml-2 mt-5"
            outlined
            rounded
            small
            :href="project.repository_url"
            target="blank"
          >
            VIEW SOURCE</v-btn
          >

          <v-btn
            class="ml-2 mt-5"
            outlined
            rounded
            small
            v-if="project.showcase_url"
            :href="project.showcase_url"
          >
            OPEN DEMO</v-btn
          >
        </v-card-actions>
      </div>
    </div>
  </v-card>
</template>

<script>
export default {
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
