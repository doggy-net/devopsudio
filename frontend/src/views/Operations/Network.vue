<template>
  <el-container>
    <el-aside style="width: auto; padding: 20px; border-right: solid 1px #e6e6e6;">
      <el-select v-model="selectedName" @change="selectedChanged">
        <el-option
          v-for="explorerName in explorerNames"
          :key="explorerName"
          :value="explorerName"
          :allow-drop="function() {return false;}">
        </el-option>
      </el-select>
      <el-tree
        node-key="path"
        :expand-on-click-node="false"
        :data="selectedExplorer.nodes"
      >
        <span slot-scope="{ node, data }" class="explorer-node"
          :draggable="canDrag(node, data)"
          @dragstart="dragstart($event, node, data)"
        >
          <icon :icon-class="getIcon(node, data)" style="margin-right: 6px"/>
          <span>{{ data.name }}</span>
        </span>
      </el-tree>
    </el-aside>
    <el-main style="padding: 0px">
      <router-view/>
    </el-main>
  </el-container>
</template>

<script>
import { getExplorer, getExplorers } from '@/api/explorer'
// import VMap from '@/components/VMap'
// import VMapBrowser from '@/components/VMapBrowser'

export default {
  name: 'Network',
  components: {
    // VMap,
    // VMapBrowser,
  },
  data() {
    return {
      explorerNames: [],
      selectedName: null,
      selectedExplorer: {nodes: []},
    };
  },
  created() {
    this.getExplorers();
  },
  methods: {
    getExplorers() {
      getExplorers()
        .then(response => {
          this.explorerNames = response.explorers;
          this.selectedExplorer = response.default;
          this.selectedName = this.selectedExplorer._id;
        });
    },
    selectedChanged () {
      getExplorer(this.selectedName)
        .then(response => {
          this.selectedExplorer = response;
        });
    },
    getIcon(node, data) {
      if (data.icon) {
        return data.icon;
      }
      if (data.type === 'Folder') {
        if (node.expanded) {
          return 'el-icon-folder-opened';
        } else {
          return 'el-icon-folder';
        }
      } else {
        return 'dot';
      }
    },
    canDrag(node, data) {
      if (data.type === 'Folder') {
        return false;
      } else {
        return true;
      }
    },
    dragstart(event, node, data) {
      event.dataTransfer.setData('text/plain', data.name);
    }
  }
}
</script>

<style scoped>
.explorer-node {
  width: 100%;
  font-size: 14px;
}
</style>
