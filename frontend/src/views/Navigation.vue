<template>
  <v-app-bar
    src="@/assets/navigation-theme.jpg"
    style="position: fixed; z-index: 9999; background-size: cover"
    color="deep-purple accent-4"
    dark
  >
    <v-toolbar-title>
      <h1 style="font-size: 1.25rem">Sylvan LE DEUNFF</h1>
    </v-toolbar-title>

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
      <v-tabs>
        <v-tab :to="{ name: 'Home' }">
          <v-icon>mdi-emoticon-outline</v-icon>
          Presentation
        </v-tab>
        <v-tab :to="{ name: 'Projects' }">
          <v-icon>mdi-presentation</v-icon>
          Projects
        </v-tab>
        <v-tab :to="{ name: 'Curriculum' }">
          <v-icon>mdi-school</v-icon>
          Curriculum
        </v-tab>
        <v-tab :to="{ name: 'Blog' }">
          <v-icon>mdi-file-document-edit</v-icon>
          Blog
        </v-tab>

        <v-spacer />

        <v-tab :to="{ name: 'BlogAdminArticles' }"> Admin </v-tab>
      </v-tabs>
    </template>
  </v-app-bar>
</template>

<style scoped>
.v-icon {
  margin-right: 0.5em;
}

@media screen and (max-width: 800px) {
  .v-tab {
    display: flex;
    flex-direction: column;
    font-size: 0.7em;
  }
  .v-icon {
    margin-right: 0;
  }
}
</style>