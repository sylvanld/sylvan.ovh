<template>
  <div id="app">
    <navigation style="position: fixed; z-index: 9999" />
    <v-app>
      <router-view />

      <footer>Sylvan Le Deunff - All right reserved © 2021</footer>
    </v-app>
  </div>
</template>

<script>
import Navigation from "@/views/Navigation";

export default {
  components: { Navigation },
};
</script>

<style>
.v-application--wrap {
  padding-top: 8em;
}

.v-application--wrap footer {
  position: absolute;
  bottom: 0;
}
</style>