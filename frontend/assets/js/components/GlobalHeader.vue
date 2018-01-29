<template>
<div>
  <el-container>
    <el-header>
      <el-menu
        :default-active="activeIndex"
        class="margin-header-menu"
        mode="horizontal"
        @select="handleSelect">
        <el-menu-item index="1">Stream</el-menu-item>
        <el-menu-item index="2"><a href="https://anond.hatelabo.jp/" target="_blank">Post</a></el-menu-item>
        <el-submenu index="3" class="right-menu">
          <template slot="title">Settings</template>
          <el-menu-item index="3-1">Login</el-menu-item>
          <el-menu-item index="3-2">item two</el-menu-item>
          <el-menu-item index="3-3">item three</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-header>
    <el-main>
      Main
      <router-view></router-view>
    </el-main>
  </el-container>
</div>
</template>

<script>
export default {
  data: {}
}
</script>

<style lang="scss" scoped>
.el-header {
  padding: 0;

  .right-menu {
    float: right;
  }
}
</style>
