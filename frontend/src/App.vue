<template>
  <div id="app">
    <navigation />
    <v-app style="padding-top: 8em">
      <router-view />
    </v-app>
    Sylvan Le Deunff - All right reserved © 2021
  </div>
</template>

<script>
import Navigation from "@/views/Navigation";

export default {
  components: { Navigation },
};
</script>