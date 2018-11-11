<template>
  <el-container>
    <el-aside width="auto">
      <el-menu router :default-active="$route.path" class="el-menu-vertical-demo" :collapse="isSidebarCollapsed">
        <el-menu-item index="/app">
          <icon icon-class="app-store-fill"/>
          <span slot="title">App1</span>
        </el-menu-item>
        <el-menu-item index="/admin/network">
          <icon icon-class="topo"/>
          <span slot="title">Network1</span>
        </el-menu-item>
        <el-menu-item index="/dashboard">
          <icon icon-class="dashboard"/>
          <span slot="title">Dashboard1</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main style="padding: 0px">
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Admin',
  computed: {
    ...mapState({
      isSidebarCollapsed: state => state.isSidebarCollapsed
    })
  }
}
</script>
