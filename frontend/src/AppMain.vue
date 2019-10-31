<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'AppMain'
}
</script>

<style>
html, body {
  height: 100%;
  min-width: 850px;
  margin: 0px;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
section {
  height: 100%;
}
.el-menu-item .icon {
  width: 20px;
  margin-right: 6px;
}
.el-button .icon {
  height: 14px;
  width: 14px;
}
.float-right {
  float: right;
}
.float-left {
  float: left;
}
</style>
