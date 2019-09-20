<template>
  <el-table :data="taskData" style="margin: 20px">
    <el-table-column prop="id" :label="$t('ui.id')" width="180"/>
    <el-table-column prop="progress" :label="$t('ui.progress')"/>
    <el-table-column :label="$t('ui.operations')" width="180">
      <template slot-scopt="scope">
        <el-button size="mini"
          @click="handleViewLog(scope.$index, scope.row)">
          {{ $t('ui.viewLog') }}
        </el-button>
        <el-button size="mini" type="danger"
          @click="handleStop(scope.$index, scope.row)">
          {{ $t('ui.stop') }}
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  name: 'Task',
  data() {
    return {
      taskData: [],
    }
  },
  methods: {
    handleViewLog(index, row) {
      console.log(index, row);
    },
    handleStop(index, row) {
      console.log(index, row);
    }
  }
}
</script>
