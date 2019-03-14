<template>
  <el-tabs style="background: white; padding: 20px">
    <el-tab-pane :label="$t('message.user')">{{ $t('message.user') }}</el-tab-pane>
    <el-tab-pane :label="$t('message.role')">{{ $t('message.role') }}</el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  name: 'Admin'
}
</script>
