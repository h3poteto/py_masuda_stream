<template>
<div>
  <el-dialog :title="entry.title" :visible.sync="entryDetailVisible" @close="handleClose">
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
    <div class="line"></div>
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
  computed: {
    ...mapState({
      entry: state => state.Stream.Show.entry,
      loading: state => state.Stream.Show.loading,
      bookmarks: state => state.Stream.Show.bookmarks,
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
    this.$store.dispatch('Stream/Show/loadBookmarks', this.$route.params.id)
  },
  methods: {
    parseDatetime(datetime) {
      // unixtimeでもらったものはutcなのでjstに変換する必要がある
      return moment.unix(datetime).add(9, 'hours').format('YYYY-MM-DD HH:mm')
    },
    handleClose(e) {
      this.$store.dispatch('Stream/Show/cleanup', e)
      this.$router.push({ path: '/' })
    },
    icon(user) {
      return `http://cdn1.www.st-hatena.com/users/${user.slice(0,2)}/${user}/profile.gif`
    }
  }
}
</script>

<style lang="scss" scoped>

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
