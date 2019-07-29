<template>
  <v-map mapId="111"/>
</template>

<script>
import VMap from '@/components/VMap/index.vue'
export default {
  name: 'Network',
  components: {
    VMap
  },
  data() {
    return {
      isCollapse: true
    };
  },
  computed: {
    logoClasses() {
      if (this.isCollapse) {
        return ['logo', 'logo--collapse'];
      }
      return ['logo'];
    }
  },
  methods: {
    collapse() {
      this.isCollapse = !this.isCollapse;
    }
  }
}
</script>
