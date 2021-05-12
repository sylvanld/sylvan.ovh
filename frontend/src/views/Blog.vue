<template>
  <v-container>
    <v-row>
      <v-col cols="auto" md="8" sm="12">
        <router-view />
      </v-col>

      <v-col cols="auto" md="4" sm="12">
        <blog-navigation :posts="blogPosts" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import BlogNavigation from "@/views/BlogNavigation";

export default {
  components: { BlogNavigation },
  data() {
    return {
      blogPosts: [
        {
          title: "Build a Kubernetes cluster with raspberry",
          date: new Date(),
        },
        {
          title: "New features of Python 3",
          date: new Date(),
        },
        {
          title: "Implement new stuff",
          date: new Date(),
        },
      ],
    };
  },
};
</script>
