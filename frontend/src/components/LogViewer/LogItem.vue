<template>
    <el-alert
      :type="item.level"
      :description="item.msg"
      :closable="false"
      show-icon
    />
</template>

<script>
export default {
  name: 'LogItem',
  props: {
    item: {
      type: Object,
      required: true
    }
  }
}
</script>
