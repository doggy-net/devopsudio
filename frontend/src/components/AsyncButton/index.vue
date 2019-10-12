<template>
  <el-button :type="type" :loading="loading" :state="state" @click="click">
    {{ $t(text) }}
  </el-button>
</template>

<script>
export default {
  name: 'AsyncButton',
  props: {
    normalText: {
      required: true,
    },
    normalLoadingText: {
      required: true,
    },
    dangerText: {
      required: true,
    },
    dangerLoadingText: {
      required: true,
    },
  },
  data() {
    return {
      loading: true,
      running: false,
      state: 'init',
    };
  },
  computed:{
    type() {
      return this.state !== 'running' ? 'primary' : 'danger';
    },
    text() {
      if (this.state === 'init') {
        return 'ui.loading';
      } else if (this.state === 'normal') {
        if (this.loading) {
          return this.normalLoadingText;
        } else {
          return this.normalText;
        }
      } else {
        if (this.loading) {
          return this.dangerLoadingText;
        } else {
          return this.dangerText;
        }
      }
    }
  },
  created() {
    this.$emit('init-state');
  },
  methods: {
    click() {
      if (this.loading) {
        return;
      }
      if (this.state === 'normal') {
        this.$emit('normal-click');
        this.loading = true;
      } else {
        this.$emit('danger-click');
        this.loading = true;
      }
    },
  }
};
</script>
