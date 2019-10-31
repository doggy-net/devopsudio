<template>
  <i v-if="iconType === 'el-icon'" :class="iconClass"/>
  <svg v-else class="el-icon-svg" aria-hidden="true">
    <image v-if="iconType === 'img-url'" :xlink:href="iconClass" style="height: 1em; width: 1em"/>
    <use v-else :xlink:href="iconName"/>
  </svg>
</template>

<script>
const req = require.context('./svg-icons', false, /\.svg$/);
const requireAll = requireContext => requireContext.keys().map(requireContext);
requireAll(req);

export default {
  name: 'Icon',
  props: {
    iconClass: {
      type: String,
      required: true,
    }
  },
  computed: {
    iconType() {
      if (this.iconClass.startsWith('el-')) {
        return 'el-icon';
      } else if (this.iconClass.startsWith('http') || this.iconClass.startsWith('/')) {
        return 'img-url';
      } else {
        return 'icon-class';
      }
    },
    iconName() {
      return `#icon-${this.iconClass}`
    }
  }
}
</script>

<style>
.el-icon-svg {
  width: 1em;
  height: 1em;
  /* font-style: normal;
  font-weight: 400;
  font-variant: normal;
  vertical-align: middle;
  text-transform: none;
  text-align: center;
  display: inline-block;
  line-height: 1; */
  fill: currentColor;
  /* overflow: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
}
</style>
