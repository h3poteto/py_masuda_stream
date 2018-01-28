<template>
<div>
  <el-container>
    <el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">Processing Center</el-menu-item>
        <el-submenu index="2">
          <template slot="title">Workspace</template>
          <el-menu-item index="2-1">item one</el-menu-item>
          <el-menu-item index="2-2">item two</el-menu-item>
          <el-menu-item index="2-3">item three</el-menu-item>
        </el-submenu>
        <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">Orders</a></el-menu-item>
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
}
</style>
