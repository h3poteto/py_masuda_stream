<template>
<div class="margin-container">
  <el-row :gutter="20">
    <el-col :span="18">
      <div class="gird-content not-login" v-if="!isLoggedIn()">
        <el-button type="primary" @click="login">Please login</el-button>
      </div>
      <div class="grid-content feed" v-if="isLoggedIn()">
        <el-card class="box-card bookmark-card" v-for="bookmark in bookmarks" v-bind:key="bookmark.id">
          <div class="title"><h4><a :href="bookmark.link[0]['@href']" target="_blank">{{ bookmark.title }}</a></h4></div>
          <div class="link"><a :href="bookmark.link[0]['@href']" target="_blank">{{ bookmark.link[0]['@href'] }}</a></div>
          <div class="bookmark">
            <div class="icon"><img :src="user.avatar_url" /></div>
            <div class="head-wrapper">
              <div class="user">{{ user.uid }}</div>
              <div class="bookmarked_at">{{ fixDatetime(bookmark.issued) }}</div>
            </div>
            <div class="comment">{{ bookmark.summary }}</div>
            <div class="clearfix"></div>
          </div>
        </el-card>
      </div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content">
        <el-card class="box-card">
          <div class="side-menu">
            <p>MasudaStreamについて</p>
            <p>&copy; 2018 <a href="https://twitter.com/h3_poteto" target="_blank">@h3_poteto</a></p>
          </div>
        </el-card>
      </div>
    </el-col>
  </el-row>
</div>
</template>

<script>
import { mapState } from 'vuex'
import moment from 'moment'

export default {
  computed: {
    ...mapState({
      user: state => state.GlobalHeader.user,
      bookmarks: state => state.Bookmarks.Index.bookmarks,
    })
  },
  created() {
    this.$store.dispatch('GlobalHeader/changeActiveIndex', '2')
    this.$store.dispatch('Bookmarks/Index/fetchBookmarks')
  },
  methods: {
    isLoggedIn() {
      return this.user !== null
    },
    login() {
      return window.location.href = '/accounts/login'
    },
    fixDatetime(datetime) {
      // YYYY-MM-DDTHH:mm:ssをYYYY-MM-DD HH:mmにしたい
      return moment(datetime).format('YYYY-MM-DD HH:mm')
    }
  }
}
</script>

<style lang="scss" scoped>
.not-login {
  text-align: center;
}

.feed {

  .title {
    a:link,
    a:visited,
    a:hover,
    a:active,
    a:focus {
      color: #303133;
      text-decoration: none;
    }
  }

  .link {
    font-size: 12px;
  }

  .bookmark {
    background-color: #e4e7ed;
    padding: 1em 1em;
    margin: 1em 0 0 0;
    border-radius: 4px;
    font-size: 14px;
    line-height: 24px;
    color: #606266;

    .icon {
      float: left;
      margin-right: 0.8em;
      margin-top: 0.6em;

      img {
        width: 36px;
        height: 36px;
        border-radius: 4px;
      }
    }

    .head-wrapper {
      .user {
        float: left;
        color: #409EFF;
      }

      .bookmarked_at {
        width: 100%;
        text-align: right;
        color: #C0C4CC;
      }
    }
  }

  .line {
    height: 1px;
    background-color: #f2f6fc;
    margin: 1.5em 0 0.5em;
  }
  .side-menu {
    font-size: 14px;
    color: #606366;

    a:link,
    a:visited,
    a:hover,
    a:active,
    a:focus {
      color: #606366;
    }
  }
}
</style>
