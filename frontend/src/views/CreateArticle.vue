<template>
  <v-container>
    <article-editor v-model="article" @save="createArticle" />
  </v-container>
</template>

<script>
import ArticleEditor from "@/components/ArticleEditor";

export default {
  components: { ArticleEditor },
  data() {
    return { article: { title: null, content: null }, received: null };
  },
  methods: {
    createArticle(articleData) {
      this.$store
        .dispatch("blog/createArticle", articleData)
        .then(() => this.$router.push({ name: "BlogAdminArticles" }));
    },
  },
};
</script>