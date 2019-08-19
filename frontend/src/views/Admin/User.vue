<template>
  <el-tabs>
    <el-tab-pane :label="$t('message.users')">
      <el-row>
        <el-col :span="20">
          <el-button type="text" icon="el-icon-plus">
            {{ $t('message.add')}}
          </el-button>
        </el-col>
        <el-col :span="4">
          <el-input v-model="userSearch" :placeholder="$t('message.filterTip')"/>
        </el-col>
      </el-row>
      <!-- <el-button type="text" icon="el-icon-plus" style="float: left">
        {{ $t('message.add')}}
      </el-button>
      <el-input v-model="userSearch" placeholder="Type to search" style="float: right"/> -->
      <el-table :data="userData.filter(data => !userSearch || data.username.toLowerCase().includes(userSearch.toLowerCase()))"
        :default-sort="{prop: 'username', order: 'ascending'}">
        <el-table-column prop="username" :label="$t('message.username')" sortable width="180"/>
        <el-table-column prop="email" :label="$t('message.email')"/>
        <el-table-column prop="groups" :label="$t('message.groups')"
          :filters="groupFilter"
          :filter-method="filterByGroups"
        />
        <el-table-column :label="$t('message.operations')" width="180">
          <template slot-scope="scope">
            <el-button size="mini"
              @click="handleEdit(scope.$index, scope.row)">{{ $t('message.edit') }}</el-button>
            <el-button size="mini" type="danger"
              @click="handleDelete(scope.$index, scope.row)">{{ $t('message.delete') }}</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane :label="$t('message.groups')">
        <el-col :span="20">
          <el-button type="text" icon="el-icon-plus">
            {{ $t('message.add')}}
          </el-button>
        </el-col>
        <el-col :span="4">
          <el-input v-model="groupSearch" placeholder="Type to search"/>
        </el-col>
      <el-table :data="groupData.filter(data => !groupSearch || data.name.toLowerCase().includes(groupSearch.toLowerCase()))"
        :default-sort="{prop: 'name', order: 'ascending'}">
        <el-table-column prop="name" :label="$t('message.name')" sortable width="180"/>
        <el-table-column prop="privileges" :label="$t('message.priviledges')"/>
        <el-table-column :label="$t('message.operations')" width="180">
          <template slot-scopt="scope">
            <el-button size="mini"
              @click="handleEdit(scope.$index, scope.row)">{{ $t('message.edit') }}</el-button>
            <el-button size="mini" type="danger"
              @click="handleDelete(scope.$index, scope.row)">{{ $t('message.delete') }}</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  name: 'User',
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
