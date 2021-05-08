<template>
  <main class="layout">
    <aside class="navigation">
      <blog-navigation :posts="blogPosts" />
    </aside>

    <main class="content">
      <h2>Article title</h2>
      <router-view />
    </main>
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

main.content {
  flex: 3;
}

aside.navigation {
  flex: 1;
}
</style>