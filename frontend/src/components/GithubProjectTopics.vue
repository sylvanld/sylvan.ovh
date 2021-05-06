<template>
  <div class="chip-panel">
    <v-chip class="chip" label v-for="topic in topics" :key="topic">{{
      topic
    }}</v-chip>
  </div>
</template>

<script>
export default {
  props: {
    topics: Array,
  },
};
</script>

<style scoped>
.chip-panel {
  display: flex;
}

.chip {
  margin-left: 1em;
}
</style>