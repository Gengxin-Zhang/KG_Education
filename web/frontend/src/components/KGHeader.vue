<template>
  <header class="page-header"
    :class="[collapse ? 'collapse': '']"
    id = "KG-page-header">
    <div class="nav-container">
      <div class="nav-left">
        <div class="logo">
          <router-link to="/">
            <img class="logo-img" src="../assets/logo.jpg"/>
            <span>KG_Education</span>
          </router-link>
        </div>
        <i class="icon icon-menu nav-icon" @click="toggleMenu"></i>
      </div>
      <div class="nav-right">
        <ul class="navbar">
          <li><router-link to="/graph">导图</router-link></li>
          <li><router-link to="/search">查一下</router-link></li>
          <li><router-link to="/about">关于</router-link></li>
        </ul>
      </div>
    </div>
  </header>
</template>


<script>
export default {
  props: {
    collapse: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      isOpen: false
    };
  },
  computed: {
    lang() {
      return this.$route.path.split("/")[1] || "zh";
    }
  },
  mounted() {
    if (!this.collapse) {
      window.addEventListener("scroll", this.headerCollapse);
    } else {
      window.removeEventListener("scroll", this.headerCollapse);
    }
  },
  destroyed() {
    window.removeEventListener("scroll", this.headerCollapse);
  },
  methods: {
    toggleMenu() {
      const header = document.getElementById("KG-page-header");

      if (this.isOpen) {
        this.isOpen = false;
        header.classList.remove("open");
      } else {
        this.isOpen = true;
        header.classList.add("open");
      }
    },
    headerCollapse() {
      const header = document.getElementById("KG-page-header");
      const offsetTop = window.scrollY || 0;

      if (offsetTop > 50) {
        header.classList.add("collapse");
      } else {
        header.classList.remove("collapse");
      }
    }
  }
};
</script>

<style lang="scss">
$header-height: 80px;
$screen-sm-max: 800px;
$brand-blue-500: #6190e8;

.page-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: $header-height;
  background-color: transparent;
  transition: all 0.3s;
  z-index: 100;

  &.collapse {
    background-color: #fff;
    box-shadow: 0 10px 60px 0 rgba(29, 29, 31, 0.07);
    opacity: 0.98;
  }
  &.open {
    background-color: #fff;
  }
}

.nav-container {
  margin: 0 auto;
  width: 90%;
  color: #1d1d1f;

  .nav-left {
    float: left;
    .logo {
      position: relative;
      height: $header-height;
      line-height: $header-height;
      transition: all 0.5s;
      img {
        position: absolute;
        top: 50%;
        margin-top: -15px;
        width: 30px;
        height: 30px;
      }
      span {
        margin-left: 40px;
        color: #3473e7;
        font-weight: bold;
        font-size: 16px;
        transition: all 1s;
      }
    }
    .nav-icon {
      display: none;
      position: absolute;
      top: 50%;
      right: 0;
      margin-top: -10px;
      font-size: 20px;
    }
  }
  .nav-right {
    float: right;

    .navbar {
      display: inline-block;
      margin: 0;
      padding: 0;
      height: $header-height;
      font-size: 14px;
      line-height: $header-height;
      list-style-type: none;

      a {
        display: inline-block;
        color: #1d1d1f;

        &::after {
          content: "";
          display: none;
          position: absolute;
          bottom: 0;
          left: 0;
          height: 2px;
          width: 100%;
          background-color: #6190e8;
        }
        &.router-link-active {
          color: $brand-blue-500;

          &::after {
            display: inline-block;
          }
        }
      }
      li {
        position: relative;
        display: inline-block;
        margin: 0 24px;
        cursor: pointer;
        transition: color 0.3s;

        &:hover {
          color: $brand-blue-500;

          a {
            color: $brand-blue-500;
          }
        }
        &.disabled {
          color: #c9c9c9;
          cursor: not-allowed;
        }
      }
    }
    .btn-language {
      display: inline-block;
      margin: 0 24px;
      padding: 2px 12px;
      border: 1px solid #1d1d1f;
      border-radius: 2px;
      cursor: pointer;
      transition: color 0.3s, border 0.3s;

      &:hover {
        color: $brand-blue-500;
        border-color: $brand-blue-500;
      }
    }
  }
}

@media screen and (max-width: $screen-sm-max) {
  .page-header {
    height: 60px;

    &.open {
      .nav-right {
        height: 150px;
      }
    }
  }
  .nav-container {
    width: initial;

    .nav-left {
      position: relative;
      margin: 0 20px;
      float: none;
      text-align: center;

      .logo {
        display: inline-block;
        height: 60px;
        line-height: 60px;
      }
      .nav-icon {
        display: inline-block;
      }
    }
    .nav-right {
      float: none;
      height: 0;
      text-align: center;
      background-color: #fff;
      box-shadow: 0 10px 60px 0 rgba(29, 29, 31, 0.07);
      transition: all 0.3s;
      overflow: hidden;

      .navbar {
        display: block;
        height: initial;
        line-height: 50px;

        li {
          display: block;
        }
        a {
          width: 100%;

          &.router-link-active::after {
            display: none;
          }
        }
      }
      .btn-language {
        margin: 16px;
      }
    }
  }
}
</style>
