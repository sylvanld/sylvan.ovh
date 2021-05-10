<template>
  <v-container>
    <article-editor v-model="article" v-if="article" @save="updateArticle" />
  </v-container>
</template>

<script>
import ArticleEditor from "@/components/ArticleEditor";

export default {
  components: { ArticleEditor },
  data() {
    return {
      article: null,
    };
  },
  mounted() {
    const articleCode = this.$route.params.articleCode;
    this.$store
      .dispatch("blog/getArticle", { code: articleCode })
      .then((article) => (this.article = article));
  },
  methods: {
    updateArticle(articleData) {
      const articleCode = this.$route.params.articleCode;
      this.$store.dispatch("blog/updateArticle", {
        code: articleCode,
        ...articleData,
      });
    },
  },
};
</script>