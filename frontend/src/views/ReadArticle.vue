<template>
  <v-container>
    <article-reader :article="article"></article-reader>
  </v-container>
</template>

<script>
import ArticleReader from "@/components/ArticleReader";

export default {
  components: { ArticleReader },
  data() {
    return { article: null };
  },

  watch: {
    "$route.params.articleCode": function (code) {
      this.updateArticle(code);
    },
  },

  methods: {
    updateArticle(code) {
      this.$store
        .dispatch("blog/getArticle", { code })
        .then((article) => (this.article = article));
    },
  },

  mounted() {
    const code = this.$route.params.articleCode;
    this.updateArticle(code);
  },
};
</script>