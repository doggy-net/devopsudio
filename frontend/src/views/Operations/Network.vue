<template>
  <el-container>
    <el-aside style="width: 312px; padding: 20px; border-right: solid 1px #e6e6e6;">
      <el-select v-model="value">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button style="padding: 12px; margin-left: 10px;" icon="el-icon-setting"></el-button>
      <el-tree>
      </el-tree>
    </el-aside>
    <el-main>
      <v-map mapId="111"/>
    </el-main>
  </el-container>
</template>

<script>
import VMap from '@/components/VMap'

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
