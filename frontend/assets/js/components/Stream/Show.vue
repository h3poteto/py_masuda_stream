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
    this.$store.dispatch('Stream/Show/load', this.$route.params.id)
  },
  methods: {
    parseDatetime(datetime) {
      // unixtimeでもらったものはutcなのでjstに変換する必要がある
      return moment.unix(datetime).add(9, 'hours').format('YYYY-MM-DD HH:mm')
    },
    handleClose(e) {
      this.$store.dispatch('Stream/Show/cleanup', e)
      this.$router.push({ path: '/' })
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
</style>
