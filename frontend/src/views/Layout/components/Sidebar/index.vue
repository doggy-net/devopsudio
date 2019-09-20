<template>
  <el-menu router :default-active="$route.path" class="el-menu-vertical-demo" :collapse="isSidebarCollapsed">
    <sidebar-item v-for="route in routes" :key="route.name" :item="route" :base-path="baseRoute"/>
  </el-menu>
</template>

<script>
import { mapState } from 'vuex'
import { getBaseRoute } from '@/utils/path'
import SidebarItem from './SidebarItem'

export default {
  name: 'Sidebar',
  components: { SidebarItem },
  props: {
    routes: {
      type: Array,
      required: true
    },
  },
  computed: {
    ...mapState({
      isSidebarCollapsed: state => state.isSidebarCollapsed
    }),
    baseRoute() {
      return getBaseRoute(this.$route.path);
    }
  }
}
</script>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  height: 100%;
}
.el-menu--collapse {
  height: 100%;
  width: 64px;
}
</style>
