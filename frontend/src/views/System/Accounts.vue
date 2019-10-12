<template>
  <el-tabs style="padding: 20px; width: 100%;">
    <el-tab-pane :label="$t('ui.users')">
      <el-row>
        <el-col :span="20">
          <el-button type="text" icon="el-icon-plus">
            {{ $t('ui.add') }}
          </el-button>
        </el-col>
        <el-col :span="4">
          <el-input v-model="userSearch" :placeholder="$t('ui.filterTip')"/>
        </el-col>
      </el-row>
      <el-table :data="userData.filter(data => !userSearch || data.username.toLowerCase().includes(userSearch.toLowerCase()))"
        :default-sort="{ prop: 'username', order: 'ascending' }">
        <el-table-column prop="username" :label="$t('ui.username')" sortable width="180"/>
        <el-table-column prop="email" :label="$t('ui.email')"/>
        <el-table-column prop="groups" :label="$t('ui.groups')"
          :filters="groupFilter"
          :filter-method="filterByGroups"
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
    </el-tab-pane>
    <el-tab-pane :label="$t('ui.groups')">
        <el-col :span="20">
          <el-button type="text" icon="el-icon-plus">
            {{ $t('ui.add')}}
          </el-button>
        </el-col>
        <el-col :span="4">
          <el-input v-model="groupSearch" :placeholder="$t('ui.filterTip')"/>
        </el-col>
      <el-table :data="groupData.filter(data => !groupSearch || data.name.toLowerCase().includes(groupSearch.toLowerCase()))"
        :default-sort="{ prop: 'name', order: 'ascending' }">
        <el-table-column prop="name" :label="$t('ui.name')" sortable width="180"/>
        <el-table-column prop="privileges" :label="$t('ui.priviledges')"/>
        <el-table-column :label="$t('ui.operations')" width="180">
          <template slot-scopt="scope">
            <el-button size="mini"
              @click="handleEdit(scope.$index, scope.row)">{{ $t('ui.edit') }}</el-button>
            <el-button size="mini" type="danger"
              @click="handleDelete(scope.$index, scope.row)">{{ $t('ui.delete') }}</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  name: 'Accounts',
  data() {
    return {
      userData: [],
      groupData: [],
      userSearch: '',
      groupSearch: '',
      groupFilter: []
    }
  },
  methods: {
    filterByGroups(value, row, column) {
    },
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
    }
  }
}
</script>
