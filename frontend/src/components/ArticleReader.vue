<template>
  <main v-if="article">
    <header class="article-header">
      <h1>{{ article.title }}</h1>
      <i> <v-icon>mdi-update</v-icon> {{ article.updated_at }}</i>
    </header>

    <div v-html="article.content" class="article-content"></div>
  </main>
</template>

<script>
export default {
  props: {
    article: Object,
  },
};
</script>

<style>
h2 {
  margin-top: 1em;
}
h3 {
  margin-top: 0.5em;
}
h4 {
  margin-top: 0.25em;
}

.article-header {
  margin-bottom: 1em;
  padding-bottom: 1em;
  border-bottom: solid 2px black;
}

.article-content table {
  width: 100%;
  border: solid 2px rgba(0, 0, 0, 0.5);
  border-collapse: collapse;
}

.article-content th {
  text-align: left;
}

.article-content td,
.article-content th {
  padding: 0.5em 1em;
  border: solid 1px rgba(0, 0, 0, 0.2);
}

.article-content tbody > tr:nth-child(2n + 1) {
  background-color: rgba(0, 0, 0, 0.1);
}

.article-content code {
  display: block;
  padding: 0.5em 1em;
  font-family: "Source Code Pro", Menlo, Consolas, monospace;
  counter-reset: line;
}

.article-content code > p:before {
  counter-increment: line;
  content: counter(line);
  display: inline-block;
  border-right: 1px solid #ddd;
  padding: 0 0.5em;
  margin-right: 0.5em;
  color: #888;
}
</style>