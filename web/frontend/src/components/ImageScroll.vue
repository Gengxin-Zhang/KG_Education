<template>
    <div class="scroll">
        <div class="box"></div>
    </div>
</template>

<style lang="scss">
.scroll {
  background-color: #fff;
  height: 200px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.box {
  height: 200;
}
</style>

<script>
export default {
  props: {
    images: {
      type: Array,
      required: true
    }
  }
};
</script>
