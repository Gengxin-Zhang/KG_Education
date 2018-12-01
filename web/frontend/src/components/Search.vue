<template>
    <div>
        <div class="kg-container">
            <div class="container-fluid content markdown">
                <div class="search-box ">
                    <h1>查一下</h1>
                    <div class="row at-row no-gutter">
                        <div class="col-md-18 col-lg-20 col-sm-16 col-xs-24" style="padding-left:5px!important; padding-right:5px!important">
                            <at-input v-model="searchKey" size="large" placeholder="不懂就要查一下"></at-input>
                        </div>
                        <div class="col-md-6 col-lg-4 col-sm-8 col-xs-24" style="padding-left:5px!important; padding-right:5px!important">
                            <at-button type="success" v-on:click="searchIt()">搜索</at-button>
                        </div>
                    </div>
                </div>
                <div class="result">
                  <h4 v-if="haveResult">搜索结果: </h4>
                  <h4 v-else>暂无搜索结果</h4>
                  <SearchResult :result="result">暂无搜索结果</SearchResult>
                  <h4 v-if="haveResult">关系图</h4>
                  <div v-if="haveResult"><RelationshipGraph :url="graphDataUrl" graphMethod=2></RelationshipGraph></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from "vue/dist/vue.js";
import SearchResult from "./SearchResult.vue";
import RelationshipGraph from "./RelationshipGraph.vue";
import axios from "axios";

export default {
  components: {
    SearchResult,
    RelationshipGraph
  },
  data() {
    return {
      searchKey: "",
      result: [],
      graphDataUrl: "",
      haveResult: false
    };
  },
  created() {
    const key = this.$route.params.key;
    document.title = "查一下 KG_Education";
    if (key) {
      this.searchkey = key;
    }
  },
  mounted() {},
  methods: {
    searchIt() {
      this.searchKey = this.searchKey.replace(/^\s*|\s*$/g, "");
      if (this.searchKey) {
        this.cleanIt();
        const PATH = `${this.GLOBAL.API_URL}/search`;

        let loading = this.$Message.loading({
          message: "加载中...",
          duration: 0
        });

        axios
          .post(PATH, {
            key: this.searchKey
          })
          .then(res => {
            let data = res.data;
            if (data.code == "1111") {
              this.result = data.data.data;
              this.haveResult = true;
              // this.graphDataUrl = `${this.GLOBAL.API_URL}/graphtest`;
              this.graphDataUrl = `${this.GLOBAL.API_URL}/graph/${this.searchKey}`;
              loading();
            } else {
              loading();
              this.$Message.error(data.msg);
              this.cleanIt();
            }
          })
          .catch(error => {
            loading();
            this.$Message.error("网络错误，请稍后再试");
            this.cleanIt();
          });
      } else {
        this.$Message.warning("请先输入需要查询的关键字");
      }
    },
    cleanIt() {
      this.graphDataUrls = [];
      this.result = [];
      this.haveResult = false;
    }
  }
};
</script>

<style lang="scss">
@import "../assets/style/views.scss";
.search-box {
  margin-bottom: 20px;
  > h1 {
    margin-bottom: 20px;
    margin-left: 20px;
  }
  input {
    margin-top: 10px;
    margin-bottom: 5px;
  }
  button {
    margin-top: 10px;
    margin-bottom: 5px;
    width: 100%;
    transition: all 0.3s;
  }
}
.result {
  margin: 10px;
  min-height: 20px;
  border: 1px #000;
  > h4 {
    margin-top: 20px;
    margin-bottom: 20px;
  }
}
</style>