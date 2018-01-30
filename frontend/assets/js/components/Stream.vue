<template>
<div class="margin-container">
  <el-row :gutter="20">
    <el-col :span="18">
      <div class="grid-content main-stream">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>Title</span>
            <el-button class="entry-info" type="text"><i class="el-icon-info"></i></el-button>
          </div>
          <div>
            body
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
export default {
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
