<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-logo"></div>
      <div class="footer-desc">
        <div class="footer-copyright">© 2018 Created by<a href="//" target="_blank"> 儿女情长</a></div>
      </div>
      <div class="github-logo"><a href="//https://github.com/Gengxin-Zhang/KG_Education" target="_blank">Github</a></div>
    </div>
  </footer>
</template>

<style lang="scss">
@import "../assets/style/mixin";
$screen-sm-max: 800px;
.footer {
  padding: 30px 0 30px;
  color: #6190e8;
  text-align: center;
  background-color: #fff;
  box-shadow: 0 10px 60px 0 rgba(29, 29, 31, 0.07);
  opacity: 0.98;
  transition: all 0.3s;
  .container {
    position: relative;
    width: 90%;
  }
  &-logo {
    margin: 10px 0 14px;
    width: 198px;
    height: 40px;
    // @include image2x-background('o2logo');
    background-size: 100% auto;
  }
  &-desc {
    text-align: left;
    font-size: 12px;
    color: #6190e8;
  }
  &-copyright {
    letter-spacing: 1px;
    font-weight: 300;

    a {
      color: #6190e8;
      text-decoration: none;
    }
  }
  .github-logo {
    position: absolute;
    right: 20px;
    top: 20px;
    width: 42px;
    height: 42px;
    @include image2x-background("github");
    transition: transform 0.3s;

    &:hover {
      transform: scale(1.1);
    }
    a {
      display: inline-block;
      width: 100%;
      height: 100%;
      text-indent: -9999px;
    }
  }
}

@media screen and (max-width: $screen-sm-max) {
  .footer {
    padding: 20px 0;
    height: 141;
    &-logo {
      margin: 8px 0;
      height: 20px;
      width: 100px;
    }
    &-desc {
      font-size: 10px;
    }
    .github-logo {
      top: 0;
      right: 0;
    }
  }
}
</style>

<script>
export default {};
</script>
