<template>
  <v-container>
    <header style="position: relative">
      <h2>Admin blog articles</h2>

      <v-btn
        color="primary"
        icon
        fab
        outlined
        elevation="3"
        style="position: absolute; top: 0; right: 0"
        :to="{ name: 'CreateArticle' }"
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </header>

    <v-list>
      <v-list-item two-line v-for="(article, index) in articles" :key="index">
        <v-list-item-icon>
          <v-icon v-if="article.published">mdi-earth</v-icon>
          <v-icon v-if="!article.published">mdi-eye-off</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>
            {{ article.title }}
          </v-list-item-title>
          <v-list-item-subtitle>
            <v-icon>mdi-update</v-icon>
            {{ article.updated_at }}</v-list-item-subtitle
          >
        </v-list-item-content>

        <v-list-item-action>
          <v-btn
            color="primary"
            icon
            fab
            title="show"
            @click="readArticle(article)"
          >
            <v-icon>mdi-eye</v-icon>
          </v-btn>
          <v-btn
            color="primary"
            icon
            fab
            title="edit"
            @click="editArticle(article)"
          >
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn
            color="primary"
            icon
            fab
            title="publish"
            v-if="!article.published"
          >
            <v-icon>mdi-earth</v-icon>
          </v-btn>
          <v-btn
            color="primary"
            icon
            fab
            title="unpublish"
            v-if="article.published"
          >
            <v-icon>mdi-eye-off</v-icon>
          </v-btn>
          <v-btn
            color="danger"
            icon
            fab
            title="delete"
            @click="deleteArticle(article)"
          >
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
export default {
  data() {
    return { articles: [] };
  },
  mounted() {
    this.refreshArticles();
  },
  methods: {
    refreshArticles() {
      this.$store.dispatch("blog/getArticles").then((articles) => {
        this.articles = articles;
      });
    },
    readArticle(article) {
      this.$router.push({
        name: "ReadArticle",
        params: { articleCode: article.code },
      });
    },
    editArticle(article) {
      this.$router.push({
        name: "EditArticle",
        params: { articleCode: article.code },
      });
    },
    deleteArticle(article) {
      this.$store
        .dispatch("blog/deleteArticle", { code: article.code })
        .then(() => this.refreshArticles());
    },
  },
};
</script>

<style scoped>
.v-list-item__action--stack {
  flex-direction: row;
}
</style>