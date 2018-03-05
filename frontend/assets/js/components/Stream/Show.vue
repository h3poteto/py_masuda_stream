<template>
<div>
  <el-dialog :title="entry.title" :visible.sync="entryDetailVisible" @close="handleClose">
    <a v-bind:href="entry.link"><el-button class="entry-info" type="text"><i class="el-icon-info"></i></el-button></a>
    <div v-html="entry.anond_content_html" class="anond-content" v-loading="loading"></div>
    <div class="line"></div>
    <div class="tool-box">
      <div class="comment">
        <icon name="comment"></icon>
        <span>{{ entry.hatena_bookmarkcount }}</span>
      </div>
      <div class="date">
        {{ parseDatetime(entry.posted_at) }}
      </div>
      <div class="clearfix"></div>
    </div>
    <div class="my-bookmark">
      <div class="my-comment" v-if="isLoggedIn() && userAlreadyBookmarked">
        <div class="bookmark">
          <div class="icon"><img :src="user.avatar_url" /></div>
          <div class="head-wrapper">
            <div class="user">{{ user.uid }}</div>
            <div class="bookmarked_at">{{ cutJSTDatetime(userBookmarked.created_datetime) }}</div>
          </div>
          <div class="comment">{{ userBookmarked.comment }}</div>
          <div class="clearfix"></div>
        </div>
      </div>
      <div class="add-bookmark" v-if="isLoggedIn() && !userAlreadyBookmarked">
        <el-form :model="bookmarkForm" :rules="bookmarkRules" ref="bookmarkForm" class="add-bookmark-form">
          <el-form-item prop="comment">
            <el-input type="textarea" v-model="bookmarkForm.comment"></el-input>
          </el-form-item>
          <el-form-item class="submit">
            <el-button type="primary" @click="submitBookmark">ブックマークする</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="login-required" v-if="!isLoggedIn()">
        <el-button type="primary" @click="goToLoginPage">ログインしてブックマークする</el-button>
      </div>
    </div>
    <div class="bookmark-comment">
      <div class="bookmark" v-for="bookmark in bookmarks" v-bind:key="bookmark.id">
        <div class="icon"><img :src="icon(bookmark.user)" /></div>
        <div class="head-wrapper">
          <div class="user">{{ bookmark.user }}</div>
          <div class="bookmarked_at">{{ parseDatetime(bookmark.bookmarked_at) }}</div>
        </div>
        <div class="comment">{{ bookmark.comment }}</div>
        <div class="clearfix"></div>
        <div class="fill-line"></div>
      </div>
    </div>
  </el-dialog>
</div>
</template>

<script>
import { mapState } from 'vuex'
import moment from 'moment'

export default {
  data() {
    return {
      bookmarkForm: {
        comment: '',
      },
      bookmarkRules: {
        comment: [
          { min: 0, max: 100, message: 'Length should be 0 to 100', trigger: 'blur' }
        ],
      },
    }
  },
  computed: {
    ...mapState({
      entry: state => state.Stream.Show.entry,
      loading: state => state.Stream.Show.loading,
      bookmarks: state => state.Stream.Show.bookmarks,
      user: state => state.GlobalHeader.user,
      userAlreadyBookmarked: state => state.Stream.Show.userAlreadyBookmarked,
      userBookmarked: state => state.Stream.Show.userBookmarked,
    }),
    entryDetailVisible: {
      get() {
        return this.$store.state.Stream.Show.entryDetailVisible
      },
      set(value) {
        this.$store.commit('Stream/Show/changeEntryDetailVisible', value)
      }
    }
  },
  created() {
    this.$store.dispatch('Stream/Show/startLoading', this.$store.state.Stream.Show.loading)
    this.$store.dispatch('Stream/Show/loadEntry', this.$route.params.id)
      .then((res) => {
        let url = res.data.entry.link
        this.$store.dispatch('Stream/Show/fetchUserBookmark', url)
      })
    this.$store.dispatch('Stream/Show/loadBookmarks', this.$route.params.id)
  },
  methods: {
    parseDatetime(datetime) {
      // unixtimeでもらったものはutcなのでjstに変換する必要がある
      return moment.unix(datetime).add(9, 'hours').format('YYYY-MM-DD HH:mm')
    },
    cutJSTDatetime(datetime) {
      // JSTでもらった時刻を適切な形に整形
      return moment(datetime).format('YYYY-MM-DD HH:mm')
    },
    handleClose(e) {
      this.$store.dispatch('Stream/Show/cleanup', e)
      this.$router.push({ path: '/' })
    },
    icon(user) {
      return `http://cdn1.www.st-hatena.com/users/${user.slice(0,2)}/${user}/profile.gif`
    },
    isLoggedIn() {
      return this.$store.state.GlobalHeader.user !== null
    },
    goToLoginPage() {
      window.location.href = '/accounts/login'
    },
    submitBookmark() {
      this.$refs["bookmarkForm"].validate((valid) => {
        if (valid) {
          let csrf = this.$cookie.get('csrftoken')
          this.$store.dispatch('Stream/Show/addBookmark',
                               Object.assign({}, this.bookmarkForm,{
                                 csrf: csrf,
                                 url: this.entry.link,
                               }))
            .then((res) => {
              this.$message({
                message: 'Bookmarked',
                type: 'success',
              })
            })
            .catch((err) => {
              this.$message({
                message: 'Can not add bookmark',
                type: 'error',
              })
            })
        } else {
          this.$message({
            message: 'Validation error',
            type: 'error',
          })
        }
      })
    },
  }
}
</script>

<style lang="scss" scoped>
.entry-info {
  float: right;
  padding: 0;
}

.line {
  height: 1px;
  background-color: #f2f6fc;
  margin: 1.5em 0 0.5em;
}

.fill-line {
  height: 1px;
  background-color: #f2f6fc;
  margin: 1.0em 0 0.5em;
}

.tool-box {
  padding: 0 1.0em;
  color: #c0c4cc;

  .comment {
    float: left;
  }

  .date {
    float: right;
  }
}

.my-bookmark {
  background-color: #e4e7ed;
  padding: 1em 1em;
  margin: 1.5em 0 1.0em 0;
  border-radius: 4px;

  .add-bookmark {
    .el-form-item {
      margin-bottom: 4px;
    }

    .submit {
      text-align: right;
    }
  }

  .login-required {
    text-align: center;
  }
}

.bookmark {
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
</style>
