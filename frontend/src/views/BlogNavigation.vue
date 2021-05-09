<template>
  <main>
    <v-list two-line>
      <v-subheader class="primary--text"><h3>Other articles</h3></v-subheader>

      <v-subheader>
        <h4 class="accent--text">Most recents posts</h4>
      </v-subheader>

      <v-list-item-group active-class="pink--text" multiple>
        <template v-for="post in posts">
          <v-list-item :key="post.title">
            <template v-slot:default>
              <v-list-item-content>
                <v-list-item-title v-text="post.title"></v-list-item-title>

                <v-list-item-subtitle
                  v-text="humanReadableDate(post.date)"
                ></v-list-item-subtitle>
              </v-list-item-content>
            </template>
          </v-list-item>
        </template>
      </v-list-item-group>

      <v-subheader class="accent--text">
        <h4>Suggested articles</h4>
      </v-subheader>

      <v-list-item-group active-class="pink--text" multiple>
        <template v-for="post in posts">
          <v-list-item :key="post.title">
            <template v-slot:default>
              <v-list-item-content>
                <v-list-item-title v-text="post.title"></v-list-item-title>

                <v-list-item-subtitle
                  v-text="humanReadableDate(post.date)"
                ></v-list-item-subtitle>
              </v-list-item-content>
            </template>
          </v-list-item>
        </template>
      </v-list-item-group>
    </v-list>
  </main>
</template>

<script>
export default {
  props: {
    posts: Array,
  },
  methods: {
    humanReadableDate(date) {
      return date.toLocaleString();
    },
  },
};
</script>