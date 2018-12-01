<template>
    <div id="result">
        <div class="result-word" 
            v-for="item in result"
            v-bind:key="item.word">
            <p v-if="item.is_node">
            <at-popover trigger="hover" :title="item.word">
                <router-link :to="item.url">{{item.word}}</router-link>
                <template slot="content">
                    <p>{{item.content}}</p>
                </template>
            </at-popover>
            <p v-else>{{item.word}}</p>
        </div>
    </div>
</template>
<style lang="scss">
.result-word {
  display: inline;
  > p {
    display: inline;
  }
}
</style>
<script>
import Vue from "vue";
export default {
  props: ["result"],
  created() {}
};
</script>
