<template>
<div class="margin-container">
  <el-row :gutter="20">
    <el-col :span="18">
      <div class="grid-content main-stream" v-for="entry in entries" v-bind:key="entry.id">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>{{ entry.title }}</span>
            <el-button class="entry-info" type="text"><i class="el-icon-info"></i></el-button>
          </div>
          <div>
            {{ entry.summary }}
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

  .entry-info {
    float: right;
    padding: 0;
    font-size: 120%;
  }

}
</style>
