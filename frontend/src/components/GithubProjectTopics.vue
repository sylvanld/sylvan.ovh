<template>
  <div class="chip-panel">
    <v-chip class="chip" label v-for="topic in topics" :key="topic">
      {{ topic }}
    </v-chip>
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
  flex-wrap: wrap;
  padding: 0 1em;
}

.chip {
  margin: 0.5em;
}
</style>