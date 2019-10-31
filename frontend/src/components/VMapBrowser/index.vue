<template>
  <div class="vmap-container"
      @dragover.prevent
      @drop="drop($event)"
    >
    <el-button icon="el-icon-plus"
      class="create-new-button vmap-image-wrapper"
      @click="createNew"
    ></el-button>
    <span class="el-button vmap-image-wrapper" v-for="vmap in vmaps" :key="vmap.id">
      <img class="vmap-image" :src="vmap.image"/>
      <span class="vmap-name">{{ vmap.name }}}</span>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Hamburger',
  props: {
    isActive: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      vmaps: []
    }
  },
  methods: {
    createNew() {
      this.$router.push({ name: 'map viewer', params: { new: true } });
    },
    open() {

    },
    dragover(event) {
      console.log(event );
    },
    drop(event) {
      console.log(event);
      this.$router.push({
        name: 'map viewer',
        params: {
          new: true,
          mapData: {
            nodes: [
              {
                id: 'node1',
                clientX: event.clientX,
                clientY: event.clientY,
                pos1: '111',
                pos2: '1111',
                pos3: '555',
                shape: 'networkObject',
                icon: '/icons/router.svg',
              },
            ]
          }
        }
      });
      // const nodeId = event.dataTransfer.getData('nodeName');
      event.dataTransfer.clearData();
    }
  }
}
</script>

<style scoped>
.vmap-container {
  padding: 20px;
  /* height: 100%; */
}
.create-new-button {
  width: 222px;
  height: 171px;
  font-size: 36px;
  border-style: dashed;
}
.vmap-image-wrapper {
  padding: 10px;
  margin-bottom: 10px;
  margin-left: 0px;
  margin-right: 10px;
  border-radius: 0px;
  vertical-align: top;
}
.vmap-image {
  width: 200px;
  height: 135px;
  object-fit: contain;
}
.vmap-name {
  font-size: 12px;
  display: block;
}
</style>
