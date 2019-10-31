<template>
  <el-main style="background-color: #eef0f3">
    <el-row :gutter="20">
      <el-col :span="6">
        <el-card shadow="hover" class="widget">
          <span class="strong-text">1</span>
          <span>Devices</span>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" class="widget">
          <span class="strong-text">1</span>
          <span>Monitors</span>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" class="widget">
          <span class="strong-text">1</span>
          <span>Monitors</span>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" class="widget">
          <span class="strong-text">1</span>
          <span>Monitors</span>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col>
        <el-card shadow="hover" class="widget">
          <span class="strong-text">1</span>
          <span>Monitors</span>
        </el-card>
      </el-col>
    </el-row>
  </el-main>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>

<style>
.widget {
  margin-bottom: 20px;
}
.strong-text {
  font-size: 50px;
  color: #409eff;
  padding: 10px;
}
</style>
