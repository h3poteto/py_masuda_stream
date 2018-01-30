<template>
<div>
  <el-container>
    <el-header>
      <el-menu
        :default-active="activeIndex"
        class="header-menu"
        mode="horizontal"
        active-text-color="#409EFF"
        :router="true"
        @select="handleSelect">
        <span class="title-logo">MasudaStream</span>
        <el-menu-item index="1" :route="{path: '/'}">Stream</el-menu-item>
        <el-menu-item index="2">Bookmarks</el-menu-item>
        <el-submenu index="3" class="right-menu">
          <template slot="title">Settings</template>
          <el-menu-item index="3-1">Login</el-menu-item>
          <el-menu-item index="3-2">item two</el-menu-item>
          <el-menu-item index="3-3">item three</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "1",
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style lang="scss" scoped>
.el-header {
  padding: 0;

  .title-logo {
    float: left;
    height: 60px;
    line-height: 60px;
    padding-right: 1.5em;
  }

  .header-menu {
    padding-left: 3.5em;
    padding-right: 3.5em;
  }

  .right-menu {
    float: right;
  }
}
</style>
