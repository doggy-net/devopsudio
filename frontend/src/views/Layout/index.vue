<template>
  <el-container>
    <el-header height="61px" style="padding: 0px; background-color: white; border-bottom: solid 1px #e6e6e6">
      <navbar/>
    </el-header>
    <el-container>
      <el-aside width="auto">
        <sidebar :routes="permissionRoutes"/>
      </el-aside>
        <router-view></router-view>
    </el-container>
  </el-container>
</template>

<script>
import path from 'path'
import { routes } from '@/router'
import { getBaseRoute } from '@/utils/path'
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'

export default {
  name: 'Operations',
  components: {
    Navbar,
    Sidebar,
  },
  computed: {
    baseRoute() {
      return getBaseRoute(this.$route.path);
    },
    permissionRoutes() {
      const baseRoute = this.baseRoute;
      let curPath = this.$route.path;
      if (curPath.endsWith('/')) {
        curPath = curPath.slice(0, -1);
      }
      for (const route of routes) {
        if (baseRoute === route.path) {
          // redirect to the first child if given url has only main route
          // e.g. '/ops' => 'ops/dashboard'
          if (baseRoute === curPath && route.children.length > 0) {
            this.$router.replace(path.resolve(baseRoute, route.children[0].path));
          }
          return route.children;
        }
      }
      return [];
    }
  }
}
</script>
