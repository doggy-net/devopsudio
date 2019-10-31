<template>
  <el-main>
    <el-row>
      <el-col :span="20">
        <el-button type="text" icon="el-icon-plus">
          {{ $t('ui.add') }}
        </el-button>
      </el-col>
      <el-col :span="4">
        <el-input v-model="scheduleSearch" :placeholder="$t('ui.filterTip')"/>
      </el-col>
    </el-row>
    <el-table :data="scheduleData.filter(data => !scheduleSearch || data.name.toLowerCase().includes(scheduleSearch.toLowerCase()))"
      :default-sort="{ prop: 'name', order: 'ascending' }">
      <el-table-column prop="name" :label="$t('ui.name')" sortable width="180"/>
      <el-table-column prop="description" :label="$t('ui.description')"/>
      <el-table-column prop="type" :label="$t('ui.type')"
        :filters="typeFilter"
        :filter-method="filterByType"
      />
      <el-table-column :label="$t('ui.operations')" width="180">
        <template slot-scope="scope">
          <el-button size="mini"
            @click="handleEdit(scope.$index, scope.row)">{{ $t('ui.edit') }}</el-button>
          <el-button size="mini" type="danger"
            @click="handleDelete(scope.$index, scope.row)">{{ $t('ui.delete') }}</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-main>
</template>

<script>
export default {
  name: 'Schedules',
  data() {
    return {
      scheduleData: [],
      scheduleSearch: '',
      typeFilter: []
    }
  },
  methods: {
    filterByType(value, row, column) {
      console.log(value, row, column);
    },
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    }
  }
}
</script>
