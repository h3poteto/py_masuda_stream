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
        <el-menu-item index="2" :route="{path: '/bookmarks'}">Bookmarks</el-menu-item>
        <el-submenu index="3" v-if="isLoggedIn()" class="right-menu">
          <template slot="title"><img class="avatar" :src="user.avatar_url" /></template>
          <el-menu-item index="3-1" :route="{path: '/'}">Logout</el-menu-item>
        </el-submenu>
        <el-menu-item index="4" v-if="!isLoggedIn()" class="right-menu" :route="{path: '/'}">Login</el-menu-item>
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
  computed: {
    ...mapState({
      user: state => state.GlobalHeader.user,
      activeIndex: state => state.GlobalHeader.activeIndex,
    })
  },
  created() {
    this.$store.dispatch('GlobalHeader/fetchUser')
  },
  methods: {
    isLoggedIn() {
      return this.user !== null
    },
    handleSelect(key, keyPath) {
      switch(key) {
      case "3-1":
        // ログアウトにはCSRFTokenが必要になる
        let csrf = this.$cookie.get('csrftoken')
        return this.$store.dispatch('GlobalHeader/logout', csrf)
          .then((res) => {
            this.$message({
              message: 'Logout complete',
              type: 'success',
            })
            this.$store.dispatch('GlobalHeader/changeActiveIndex', '1')
          })
      case "4":
        return window.location.href = '/accounts/login'
      }
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
