<template>
  <div class="map-parent-container">
    <div
      :id="'map-' + mapId"
      tabindex="20"
      class="map-container"
      @mousewheel.alt.prevent="zoom($event)"
      @keydown.ctrl.65.prevent="selectAllItems"
      @keydown.46.prevent.exact="deleteSelectedItems"
      @dragstart.prevent
      @dragover.prevent
      @drop="drop($event)"
    ></div>
    <div :id="'minimap-' + mapId" class="minimap-container" v-show="showMinimap"></div>
    <div class="toolbar">
      <el-tooltip :content="$t('ui.save')" placement="top">
        <el-button circle @click="save">
          <icon icon-class="save-fill"/>
        </el-button>
      </el-tooltip>
      <el-tooltip :content="$t('ui.toggelMiniMap')" placement="top">
        <el-button
          icon="el-icon-menu"
          circle
          @click="toggleMinimap"
        ></el-button>
      </el-tooltip>
      <el-tooltip :content="$t('ui.fitView')" placement="top">
        <el-button circle @click="zoomToFit">
          <icon icon-class="fit-to-view"/>
        </el-button>
      </el-tooltip>
      <el-tooltip :content="$t('ui.zoomTo100')" placement="top">
        <el-button circle @click="zoomTo100">
          <icon icon-class="1to1"/>
        </el-button>
      </el-tooltip>
      <el-tooltip :content="$t('ui.close')" placement="top">
        <el-button circle @click="close">
          <icon icon-class="el-icon-close"/>
        </el-button>
      </el-tooltip>
      <el-slider
        v-model="scale"
        :min="40"
        :max="200"
        :step="20"
        :format-tooltip="formatSliderTooltip"
      ></el-slider>
    </div>
    <el-dialog
      title="$t('ui.save')"
      :visible.sync="showSaveDialog"
      width="30%">
      <span>这是一段信息</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import G6 from '@antv/g6'
import Minimap from '@antv/g6/build/minimap'
// import { getMap, saveMap } from '@/api/vmap'
import './regNode'
import './regEdge'
import './regBehavior'

function getContainerSize(container) {
  return { width: container.offsetWidth, height: container.offsetHeight };
}

export default {
  name: 'VMap',
  props: {
    minimap: {
      type: Boolean,
      default: true,
    },
    mapId: {
      type: String,
    }
  },
  data() {
    return {
      scale: 100,
      graph: null,
      mapData: {},
      showMinimap: this.minimap,
      showSaveDialog: false,
    };
  },
  watch: {
    scale(val) {
      if (!val && val !== 0) {
        return;
      }
      this.graph.zoomTo(this.scale / 100);
    }
  },
  created() {
  },
  mounted() {
    const minimap = new Minimap({
      container: 'minimap-' + this.mapId
    });
    const plugins = [minimap];
    const containerSize = getContainerSize(document.getElementById('map-' + this.mapId));
    this.graph = new G6.Graph({
      container: 'map-' + this.mapId,
      width: containerSize.width,
      height: containerSize.height - 4,
      plugins: plugins,
      modes: {
        default: ['drag-canvas', { type: 'drag-node', delegate: true }, 'select'],
        edit: ['brush-select']
      }
    });
    const graph = this.graph;

    if (this.$route.params.new) {
      if (this.$route.params.mapData) {
        for (const node of this.$route.params.mapData.nodes) {
          const points = this.graph.getPointByClient(node.clientX, node.clientY);
          node.x = points.x;
          node.y = points.y;
          delete node.clientX;
          delete node.clientY;
        }
        this.mapData = this.$route.params.mapData;
      }
    }
    this.graph.read(this.mapData);

    this.graph.on('node:mouseleave', () => {
      graph.get('canvas').get('el').style.cursor = '-webkit-grab';
    });
    this.graph.on('edge:mouseleave', () => {
      graph.get('canvas').get('el').style.cursor = '-webkit-grab';
    });

    window.onresize = () => {
      const mapContainer = document.getElementById('map-' + this.mapId);
      if (!mapContainer){
        return
      }
      const containerSize = getContainerSize(mapContainer);
      this.graph.changeSize(containerSize.width, containerSize.height - 4);
    };
  },
  methods: {
    downloadImage() {
      this.graph.downloadImage(this.mapId);
    },
    save() {
      const points = this.graph.getPointByClient(500, 89);
      console.log(points);
      console.log(this.graph.getNodes());
      // const mapData = {
      //   name: th
      //   data: this.graph.save(),
      //   image: this.graph.toDataURL(),
      // }
    },
    close() {
      this.$router.push({ name: 'map browser'});
    },
    toggleMinimap() {
      this.showMinimap = !this.showMinimap;
    },
    zoomToFit() {
      this.graph.fitView(0);
      this.scale = this.graph.getZoom() * 100;
    },
    zoomTo100() {
      this.scale = 100;
    },
    zoom(event) {
      if (event.wheelDelta > 0) {
        this.scale += 20;
      } else {
        this.scale -= 20;
      }
    },
    formatSliderTooltip(value) {
      return value + '%';
    },
    drop(event) {
      const nodeId = event.dataTransfer.getData('text');
      console.log(nodeId);
      if (!nodeId) {
        return;
      }
      if (this.graph.find(nodeId) === undefined) {
        const points = this.graph.getPointByClient(event.clientX, event.clientY);
        const nodeModel = {
          id: nodeId,
          x: points.x,
          y: points.y,
          pos1: '333',
          pos2: '333',
          shape: 'networkObject',
          icon: '/icons/router.svg',
        };
        this.graph.add('node', nodeModel);
      } else {
        this.graph.focus(nodeId);
      }
      event.dataTransfer.clearData();
    },
    deleteSelectedItems() {
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
        if (edge.hasState('selected')) {
          this.graph.remove(edge);
          edgeIndex--;
        }
      }
    },
    selectAllItems() {
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
