<template>
  <el-menu-item :index="fullPath">
    <icon :icon-class="item.meta.icon"/>
    <span slot="title">{{ generateTitle(item.meta.title) }}</span>
  </el-menu-item>
</template>

<script>
import path from 'path'
import { generateTitle } from '@/utils/i18n'
import FixiOSBug from './FixiOSBug'

export default {
  name: 'SidebarItem',
  mixins: [FixiOSBug],
  props: {
    item: {
      type: Object,
      required: true
    },
    basePath: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      fullPath: this.resolvePath(this.item.path)
    }
  },
  methods: {
    resolvePath(routePath) {
      return path.resolve(this.basePath, routePath)
    },
    generateTitle,
  }
}
</script>
