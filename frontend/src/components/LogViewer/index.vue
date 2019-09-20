<template>
  <div>
    <log-item v-for="log in logs" :key="log.index" :item="log"/>
  </div>
</template>

<script>
import LogItem from './LogItem'

export default {
  name: 'LogViewer',
  components: {
    LogItem
  },
  props: {
    logs: {
      type: Array,
      required: true
    },
  }
}
</script>
