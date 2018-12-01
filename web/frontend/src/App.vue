<template>
  <transition name="fade" mode="out-in" @after-leave="afterLeave">
    <div id="app">
      <KGHeader></KGHeader>
      <div class="page-content">
        <router-view />
      </div>
      <KGFooter></KGFooter>
    </div>
  </transition>
  
</template>

<script>
import KGHeader from "./components/KGHeader.vue";
import KGFooter from "./components/KGFooter.vue";
export default {
  components: {
    KGHeader,
    KGFooter
  },
  name: "App",
  created() {
    this.$Loading.config({
      width: 2
    });
  },
  methods: {
    afterLeave() {
      window.scrollTo(0, 0);
    }
  }
};
</script>

<style>
html,
body {
  height: auto;
}
#app {
  background-color: #f8faff;
  min-height: 100vh;
  height: auto;
  position: relative;
}
.page-content {
  background-color: #f8faff;
  min-height: 100%;
  padding-bottom: 141px;
}
.page-header {
  position: relative !important;
}
.footer {
  position: absolute;
  width: 100%;
  margin-bottom: 0px;
  bottom: 0;
}
</style>
