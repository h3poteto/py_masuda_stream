<template>
<div>
  <el-dialog :title="entry.title" :visible.sync="entryDetailVisible">
    <span>hoge</span>
  </el-dialog>
</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState({
      entry: state => state.Stream.Show.entry,
    }),
    entryDetailVisible: {
      get() {
        return this.$store.state.Stream.Show.entryDetailVisible
      },
      set(value) {
        this.$store.commit('Stream/Show/changeEntryDetailVisible', value)
      }
    }
  }
}
</script>
