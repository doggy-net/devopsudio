<template>
  <svg class="icon" aria-hidden="true">
    <use :xlink:href="iconName"></use>
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
    iconName() {
      return `#icon-${this.iconClass}`
    }
  }
}
</script>

<style>
.icon {
  width: 1em;
  height: 1em;
  font-size: 18px;
  font-style: normal;
  font-weight: 400;
  font-variant: normal;
  vertical-align: middle;
  text-transform: none;
  text-align: center;
  display: inline-block;
  line-height: 1;
  fill: currentColor;
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
