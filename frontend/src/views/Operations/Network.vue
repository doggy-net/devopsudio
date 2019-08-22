<template>
  <el-container style="height: 100%; width: 100%;">
    <el-aside style="width: 324px; padding: 20px; border-right: solid 1px #e6e6e6;">
      <el-select v-model="value" placeholder="请选择" style="display: inline-block;">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button style="margin-left: 10px; display: inline-block;" icon="el-icon-refresh"></el-button>
      <el-tree
        lazy
        show-checkbox>
      </el-tree>
    </el-aside>
    <el-main>
      <v-map mapId="111"/>
    </el-main>
  </el-container>
</template>

<script>
import VMap from '@/components/VMap/index.vue'
export default {
  name: 'Network',
  components: {
    VMap
  },
  data() {
    return {
      options: [
        {
          'label': 'Site',
          'value': 'site'
        },
        {
          'label': 'Routing Protocol',
          'value': 'routingProtocol'
        }
      ],
      value: 'site'
    };
  }
}
</script>
