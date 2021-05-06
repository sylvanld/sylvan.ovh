<template>
  <v-app-bar
    src="@/assets/navigation-theme.jpg"
    style="position: fixed; z-index: 9999; background-size: cover"
    color="deep-purple accent-4"
    dark
  >
    <v-toolbar-title>Sylvan LE DEUNFF</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn
      icon
      href="https://stackoverflow.com/users/5970908/sylvan-le-deunff"
      target="stackoverflow"
    >
      <v-icon>mdi-stack-overflow</v-icon>
    </v-btn>

    <v-btn icon href="https://github.com/sylvanld" target="github">
      <v-icon>mdi-github</v-icon>
    </v-btn>

    <v-btn
      icon
      href="https://www.linkedin.com/in/sylvan-le-deunff/"
      target="linkedin"
    >
      <v-icon>mdi-linkedin</v-icon>
    </v-btn>

    <template v-slot:extension>
      <v-tabs align-with-title>
        <v-tab :to="{ name: 'Home' }">Presentation</v-tab>
        <v-tab :to="{ name: 'Projects' }">Personal projects</v-tab>
        <v-tab :to="{ name: 'Curriculum' }">Curriculum</v-tab>
      </v-tabs>
    </template>
  </v-app-bar>
</template>