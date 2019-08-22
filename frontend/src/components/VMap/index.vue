<template>
  <div class="map-parent-container">
    <div
      :id="mapId"
      tabindex="20"
      class="map-container"
      @mousewheel.alt.prevent="zoom($event)"
      @keydown.ctrl.65.prevent="selectAllItems($event)"
      @keydown.46.prevent.exact="deleteSelectedItems($event)"
      @keydown.ctrl.90.prevent="undo"
      @dragstart.prevent
      @dragover.prevent
      @drop="drop($event)"
    ></div>
    <div :id="minimapId" :class="minimapContainerClasses" v-if="showMinimap"></div>
    <div class="toolbar">
      <el-tooltip class="item" content="Save" placement="top">
        <el-button circle @click="saveImage">
          <icon icon-class="save-fill"/>
        </el-button>
      </el-tooltip>
      <el-tooltip class="item" content="Menu" placement="top">
        <el-button
          icon="el-icon-menu"
          circle
          @click="toggleMinimap"
          :disabled="showMinimap? false: true"
        ></el-button>
      </el-tooltip>
      <el-dropdown placement="top" class="margin-left">
        <el-button icon="el-icon-share" circle></el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>黄金糕</el-dropdown-item>
          <el-dropdown-item>狮子头</el-dropdown-item>
          <el-dropdown-item>螺蛳粉</el-dropdown-item>
          <el-dropdown-item disabled>双皮奶</el-dropdown-item>
          <el-dropdown-item divided>蚵仔煎</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <el-tooltip class="item" content="Test" placement="top">
        <el-button circle @click="test">
          <icon icon-class="pie-chart"/>
        </el-button>
      </el-tooltip>
      <el-tooltip class="item" content="Fit View" placement="top">
        <el-button circle @click="zoomToFit">
          <icon icon-class="fit-to-view"/>
        </el-button>
      </el-tooltip>
      <el-tooltip class="item" content="Zoom to 100%" placement="top">
        <el-button circle @click="zoomTo100">
          <icon icon-class="1to1"/>
        </el-button>
      </el-tooltip>
      <el-dropdown placement="top" class="margin-left">
        <el-button icon="el-icon-more" circle></el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>黄金糕</el-dropdown-item>
          <el-dropdown-item>狮子头</el-dropdown-item>
          <el-dropdown-item>螺蛳粉</el-dropdown-item>
          <el-dropdown-item disabled>双皮奶</el-dropdown-item>
          <el-dropdown-item divided>蚵仔煎</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <el-slider
        v-model="scale"
        style="width: 348px"
        :min="40"
        :max="200"
        :step="20"
        :format-tooltip="formatSliderTooltip"
      ></el-slider>
    </div>
  </div>
</template>

<script>
import G6 from '@antv/g6'
// import G6 from '../../../node_modules/@antv/g6/src'
import Minimap from '@antv/g6/build/minimap'
import mapData from './mapData'
require('./regNode');
require('./regEdge');
require('./regBehavior');

function getContainerSize(container) {
  return { width: container.offsetWidth, height: container.offsetHeight };
}

export default {
  name: 'vmap',
  props: {
    showMinimap: {
      type: Boolean,
      default: true
    },
    mapId: String
  },
  data() {
    return {
      minimapId: this.mapId + '-minimap',
      minimapVisiable: this.showMinimap,
      scale: 100,
      graph: undefined,
      mapData: mapData
    };
  },
  computed: {
    minimapContainerClasses() {
      if (this.minimapVisiable) {
        return ['minimap-container'];
      }
      return ['minimap-container', 'hide'];
    }
  },
  watch: {
    scale: function(val) {
      if (!val && val !== 0) {
        return;
      }
      this.graph.zoomTo(this.scale / 100);
    }
  },
  mounted() {
    const plugins = [];
    if (this.showMinimap) {
      const minimap = new Minimap({
        container: this.minimapId
      });
      plugins.push(minimap);
    }
    const containerSize = getContainerSize(document.getElementById(this.mapId));
    this.graph = new G6.Graph({
      container: this.mapId,
      width: containerSize.width,
      height: containerSize.height,
      // fitView: 'cc',
      plugins: plugins,
      modes: {
        default: [ 'drag-canvas', {type: 'drag-node', delegate: true}, 'select'],
        edit: ['brush-select']
      }
    });
    const graph = this.graph;
    this.graph.read(this.mapData);
    this.graph.refresh();

    this.graph.on('node:mouseleave', () => {
      graph.get('canvas').get('el').style.cursor = '-webkit-grab';
    });
    this.graph.on('edge:mouseleave', () => {
      graph.get('canvas').get('el').style.cursor = '-webkit-grab';
    });

    window.onresize = () => {
      const mapContainer = document.getElementById(this.mapId);
      if (!mapContainer){
        return
      }
      const containerSize = getContainerSize(mapContainer);
      this.graph.changeSize(containerSize.width, containerSize.height);
    };
  },
  methods: {
    test: function() {
      const firstNode = this.graph.getNodes()[0];
      console.log(firstNode);
      // this.graph.update(firstNode, {pos2: 987});
      firstNode.update({pos2: '888'});
      // firstNode.refresh();
    },
    undo() {
    },
    saveImage: function() {
      this.graph.downloadImage(this.mapId);
    },
    toggleMinimap: function() {
      this.minimapVisiable = !this.minimapVisiable;
    },
    zoomToFit: function() {
      this.graph.fitView(0);
      this.scale = this.graph.getZoom() * 100;
    },
    zoomTo100: function() {
      this.scale = 100;
    },
    zoom: function(event) {
      if (event.wheelDelta > 0) {
        this.scale += 20;
      } else {
        this.scale -= 20;
      }
    },
    formatSliderTooltip: function(value) {
      return value + '%';
    },
    drop: function(event) {
      const nodeId = event.dataTransfer.getData('text');
      if (nodeId === 'undefined') {
        return;
      }
      if (this.graph.find(nodeId) === undefined) {
        let points = this.graph.getPointByClient({
          x: event.clientX,
          y: event.clientY
        });
        const nodeModel = {
          id: nodeId,
          x: points.x,
          y: points.y,
          pos1: '333',
          pos2: '333',
          shape: 'networkObject'
        };
        this.graph.add('node', nodeModel);
      } else {
        this.graph.focus(nodeId);
      }
      event.dataTransfer.clearData();
    },
    deleteSelectedItems: function(event) {
      event.preventDefault();
      const nodes = this.graph.getNodes();
      for (let nodeIndex = 0; nodeIndex < nodes.length; nodeIndex++) {
        const node = nodes[nodeIndex];
        if (node.hasState('selected')) {
          this.graph.remove(node);
          nodeIndex--;
        }
      }
      const edges = this.graph.getEdges();
      for (let edgeIndex = 0; edgeIndex < edges.length; edgeIndex++) {
        const edge = edges[edgeIndex];
        // const source = edge.source;
        if (edge.hasState('selected')) {
          this.graph.remove(edge);
          // if (source) {
          //   this.graph.update(source, {});
          // }
          edgeIndex--;
        }
      }
    },
    selectAllItems(event) {
      event.preventDefault();
      const autoPaint = this.graph.get('autoPaint');
      this.graph.setAutoPaint(false);
      for (let node of this.graph.getNodes()) {
        node.setState('selected', true);
      }
      for (let edge of this.graph.getEdges()) {
        edge.setState('selected', true);
      }
      this.graph.paint();
      this.graph.setAutoPaint(autoPaint);
    }
  }
};
</script>

<style scoped>
.map-parent-container {
  background: #fff;
  height: 100%;
  overflow: hidden;
  position: relative;
  /* -webkit-user-drag: none; */
}
.map-container {
  height: 100%;
  image-rendering: pixelated;
  overflow: hidden;
  outline: none;
  cursor: -webkit-grab;
}
.minimap-container {
  border: 1px solid #999;
  background-color: #fff;
  position: absolute;
  bottom: 0px;
  right: 0px;
  margin: 20px;
}
.hide {
  display: none;
}
.toolbar {
  position: absolute;
  bottom: 0px;
  left: 0px;
  margin: 20px;
}
.margin-left {
  margin: 0px 11px;
}
</style>
