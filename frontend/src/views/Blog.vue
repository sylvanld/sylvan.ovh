<template>
  <main class="layout">
    <main class="content">
      <router-view />
    </main>

    <aside class="navigation">
      <blog-navigation :posts="blogPosts" />
    </aside>
  </main>
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

<style scoped>
main.layout {
  display: flex;
}

@media screen and (max-width: 600px) {
  main.layout {
    flex-direction: column;
  }
}

main.content {
  flex: 3;
  padding-left: 2em;
}

aside.navigation {
  flex: 1;
}
</style>