<template>
  <div class="kg-container">
    <div class="content markdown">
      <h1>{{name}}</h1>
      <hr>
      <div v-html="content"></div>
    </div>
  </div>
</template>

<script>
import marked from "marked";
import axios from "axios";

export default {
  data() {
    return {
      name: "",
      content: ""
    };
  },
  methods: {
    compiledMarkdown(text) {
      return marked(text, { sanitize: true });
    }
  },
  created() {
    const PATH = `${this.GLOBAL.API_URL}/wiki/${this.$route.params.key}`;
    document.title = `${this.$route.params.key} -- Wiki of KG_Education`;
    axios.get(PATH).then(res => {
      const _data = res.data;
      if (_data.code == "1111") {
        this.name = _data.data.name;
        this.content = this.compiledMarkdown(_data.data.content);
      } else if (_data.code == "0001") {
        this.$Message.error(_data.msg);
      }
    });
  }
};
</script>

<style lang="scss">
@import "../assets/style/views.scss";
</style>
