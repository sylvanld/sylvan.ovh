<template>
  <form @submit.prevent="submitArticle()">
    <div style="display: flex; align-items: baseline">
      <v-text-field label="Article title" v-model="articleTitle" required />
      <v-btn color="primary" style="margin-left: 1em" type="submit">
        <v-icon>mdi-content-save</v-icon>
        Enregistrer
      </v-btn>
    </div>

    <main class="editor-content">
      <aside style="width: 20%">
        <i>
          <strong>Table of contents</strong>
        </i>

        <ul style="list-style-type: none; padding-left: 0">
          <li
            v-for="(heading, index) in tableOfContents"
            :key="index"
            :style="{
              paddingLeft: heading.level - 1 + 'em',
            }"
          >
            {{ heading.title }}
          </li>
        </ul>
      </aside>

      <ckeditor
        v-model="articleContent"
        :editor="editor"
        :config="editorConfig"
      ></ckeditor>
    </main>
  </form>
</template>


<script>
// NOTE: We don't use @ckeditor/ckeditor5-build-classic any more!
// Since we're building CKEditor from source, we use the source version of ClassicEditor.
import ClassicEditor from "@ckeditor/ckeditor5-editor-classic/src/classiceditor";

import HeadingPlugin from "@ckeditor/ckeditor5-heading/src/heading";
import EssentialsPlugin from "@ckeditor/ckeditor5-essentials/src/essentials";
import BoldPlugin from "@ckeditor/ckeditor5-basic-styles/src/bold";
import ItalicPlugin from "@ckeditor/ckeditor5-basic-styles/src/italic";
import LinkPlugin from "@ckeditor/ckeditor5-link/src/link";
import ListPlugin from "@ckeditor/ckeditor5-list/src/list";
import Underline from "@ckeditor/ckeditor5-basic-styles/src/underline";
import Strikethrough from "@ckeditor/ckeditor5-basic-styles/src/strikethrough";
import ParagraphPlugin from "@ckeditor/ckeditor5-paragraph/src/paragraph";
import Autoformat from "@ckeditor/ckeditor5-autoformat/src/autoformat";
import CodeBlock from "@ckeditor/ckeditor5-code-block/src/codeblock";
import Table from "@ckeditor/ckeditor5-table/src/table";
import TableToolbar from "@ckeditor/ckeditor5-table/src/tabletoolbar";
import TableProperties from "@ckeditor/ckeditor5-table/src/tableproperties";
import TableCellProperties from "@ckeditor/ckeditor5-table/src/tablecellproperties";

function parseTableOfContents(content, maxLevelOrDefault) {
  const maxLevel = maxLevelOrDefault ? maxLevelOrDefault : 3;
  const dom = new DOMParser().parseFromString(content, "text/html");
  const levels = [...Array(maxLevel).keys()]
    .map((level) => `h${level + 1}`)
    .join(",");
  console.log(levels);
  return [...dom.querySelectorAll(levels)].map((heading) => ({
    title: heading.innerText,
    level: parseInt(heading.tagName.substr(1)),
  }));
}

export default {
  name: "app",
  data() {
    return {
      articleTitle: null,
      articleContent: null,
      tableOfContents: [],

      editor: ClassicEditor,
      editorData: "<p>Content of the editor.</p>",
      editorConfig: {
        plugins: [
          HeadingPlugin,
          EssentialsPlugin,
          BoldPlugin,
          ItalicPlugin,
          LinkPlugin,
          ListPlugin,
          ParagraphPlugin,
          Table,
          TableToolbar,
          TableProperties,
          TableCellProperties,
          Underline,
          Strikethrough,
          Autoformat,
          CodeBlock,
        ],

        toolbar: {
          items: [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "|",
            "bulletedList",
            "numberedList",
            "codeBlock",
            "insertTable",
            "|",
            "link",
          ],
        },

        table: {
          contentToolbar: [
            "tableColumn",
            "tableRow",
            "mergeTableCells",
            "tableProperties",
            "tableCellProperties",
          ],
        },
      },
    };
  },
  props: {
    value: Object,
  },
  watch: {
    articleContent(content) {
      this.tableOfContents = parseTableOfContents(content, 4);
    },
    value: {
      immediate: true,
      handler(articleInfo) {
        if (articleInfo) {
          this.articleTitle = articleInfo.title;
          this.articleContent = articleInfo.content;
        }
      },
    },
  },
  methods: {
    submitArticle() {
      this.$emit("save", {
        title: this.articleTitle,
        content: this.articleContent,
      });
    },
  },
};
</script>


<style>
.editor-content {
  display: flex;
}

@media screen and (max-width: 1264px) {
  .editor-content {
    flex-direction: column;
  }
}

.ck-editor {
  flex: 1;
}

.ck-editor__editable {
  min-height: 30em;
}

.ck-content .table {
  margin: 1.3em 0;
}
</style>