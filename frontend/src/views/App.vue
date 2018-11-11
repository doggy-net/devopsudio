<template>
  <el-container>
    <el-aside width="auto">
      <el-menu router default-active="1" class="el-menu-vertical-demo">
        <el-menu-item index="/app">
          <icon icon-class="app-store-fill"/>
          <span slot="title">App</span>
        </el-menu-item>
        <el-menu-item index="/network">
          <icon icon-class="topo"/>
          <span slot="title">Network</span>
        </el-menu-item>
        <el-menu-item index="/dashboard">
          <icon icon-class="dashboard"/>
          <span slot="title">Dashboard</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main style="padding: 0px">
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'App'
}
</script>
