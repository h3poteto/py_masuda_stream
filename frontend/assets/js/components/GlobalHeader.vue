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
        <el-submenu index="3" v-if="isLoggedIn()" class="right-menu">
          <template slot="title"><img class="avatar" :src="user.avatar_url" /></template>
          <el-menu-item index="3-1"><a href="/accounts/logout">Logout</a></el-menu-item>
          <el-menu-item index="3-2">item two</el-menu-item>
          <el-menu-item index="3-3">item three</el-menu-item>
        </el-submenu>
        <el-menu-item index="4" v-if="!isLoggedIn()" class="right-menu"><a href="/accounts/login">Login</a></el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      activeIndex: "1",
    }
  },
  computed: {
    ...mapState({
      user: state => state.GlobalHeader.user,
    })
  },
  created() {
    this.$store.dispatch('GlobalHeader/fetchUser')
  },
  methods: {
    isLoggedIn() {
      return this.$store.state.GlobalHeader.user !== null
    },
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

  img.avatar {
    width: 28px;
    height: 28px;
    border-radius: 2px;
  }
}
</style>
