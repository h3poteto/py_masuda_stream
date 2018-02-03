<template>
<div class="margin-container">
  <el-row :gutter="20">
    <el-col :span="18">
      <div class="grid-content main-stream" v-for="entry in entries" v-bind:key="entry.id">
        <el-card class="box-card entry-card">
          <div slot="header" class="clearfix">
            <span>{{ entry.title }}</span>
            <a v-bind:href="entry.link"><el-button class="entry-info" type="text"><i class="el-icon-info"></i></el-button></a>
          </div>
          <div>
            {{ entry.summary }}
          </div>
          <div class="line"></div>
          <div class="tool-box">
            <icon name="comment"></icon>
            <span>{{ entry.hatena_bookmarkcount }}</span>
          </div>
        </el-card>
      </div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content">
        <el-card class="box-card">
          sidemenu
        </el-card>
      </div>
    </el-col>
  </el-row>
</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState({
      entries: state => state.Stream.entries
    })
  },
  created() {
    this.$store.dispatch('Stream/fetchEntries', this.$store.state.Stream.entries)
  }
}
</script>

<style lang="scss" scoped>
.margin-container {

  .entry-card {
    cursor: pointer;
    margin-bottom: 0.5em;

    .entry-info {
      float: right;
      padding: 0;
    }

    .line {
      height: 1px;
      background-color: #f2f6fc;
      margin: 1.5em 0 0.5em;
    }

    .tool-box {
      padding: 0 1.0em;
      color: #c0c4cc;
    }
  }

}
</style>
