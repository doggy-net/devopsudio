<template>
  <div class="map-parent-container">
    <div :id="mapId" class="map-container"
      @mousewheel.alt.prevent="zoom($event)"
      @keydown.ctrl.65.prevent="selectAllItems($event)"
      @keydown.46.prevent="deleteSelectedItems($event)"
      @keydown.ctrl.90.prevent="undo"
      @dragstart.prevent
      @dragover.prevent
      @drop="drop($event)">
    </div>
    <div :id="minimapId" :class="minimapContainerClasses" v-if="showMinimap"></div>
    <div class="toolbar">
      <el-tooltip class="item" content="Save" placement="top">
        <el-button circle @click="saveToImage">
          <i class="iconfont icon-save-fill"/>
        </el-button>
      </el-tooltip>
      <el-tooltip class="item" content="Menu" placement="top">
        <el-button icon="el-icon-menu" circle @click="toggleMinimap" :disabled="showMinimap? false: true"></el-button>
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
        <el-button icon="el-icon-picture-outline" circle @click="test"></el-button>
      </el-tooltip>
      <el-tooltip class="item" content="Fit View" placement="top">
        <el-button icon="el-icon-picture-outline" circle @click="zoomToFit"></el-button>
      </el-tooltip>
      <el-tooltip class="item" content="Zoom to 100%" placement="top">
        <el-button icon="el-icon-picture-outline" circle @click="zoomTo100"></el-button>
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
      <el-slider v-model="scale" style="width: 348px" :min="40" :max="200" :step="20" :format-tooltip="formatSliderTooltip"></el-slider>
    </div>
  </div>
</template>

<script>
import G6 from '@antv/g6';
// import G6 from '../../../node_modules/@antv/g6/src';
import '@antv/g6/build/plugin.tool.minimap';
import iconPlus from './svg-icons/plus-circle-fill.svg';
import router from './svg-icons/router.svg';

G6.track(false);

const defaultIconSize = 50;
const lineColor = '#666';
const selectedLineColor = '#0af';
const imgPlus = new Image();
imgPlus.src = iconPlus;

function getContainerSize(containerId) {
  const container = document.getElementById(containerId);
  let containerWidth = parseInt(container.offsetWidth, 10);
  let containerHeight = parseInt(container.offsetHeight, 10);
  containerWidth = containerWidth % 2 === 0 ? containerWidth + 1: containerWidth;
  containerHeight = containerHeight % 2 === 0 ? containerHeight + 1: containerHeight;
  return {width: containerWidth, height: containerHeight};
}
let imageCache;
G6.registerNode('networkObject', {
  draw: function draw(item) {
    const group = item.getGraphicGroup();
    const icon = item.model.icon;
    const selecedShape = this.drawSelected(item);
    if (item.model.selected) {
      selecedShape.show();
    } else {
      selecedShape.hide();
    }
    this.drawExtender(item);
    this.drawText(item);
    const iconSize = {
      width: defaultIconSize,
      height: defaultIconSize
    };
    let keyShape;
    let image = new Image();
    if (icon) {
      if (icon in imageCache) {
        image = imageCache[icon];
      } else {
        const downloadingImage = new Image();
        downloadingImage.onload = function(){
          image.src = this.src;
          // iconSize.height = image.naturalHeight /  image.naturalWidth * defaultIconSize;
          // keyShape.attr('height', iconSize.height);
          item.graph.update(item, {});
        };
        imageCache[icon] = image;
        downloadingImage.src = icon;
      }
      keyShape = group.addShape('image', {
        name: 'keyShape',
        attrs: {
          img: image,
          x: 0,
          y: 0,
          width: iconSize.width,
          height: iconSize.height
        }
      });
    }
    else {
      keyShape = group.addShape('circle', {
        name: 'keyShape',
        attrs: {
          x: defaultIconSize / 2,
          y: defaultIconSize / 2,
          r: defaultIconSize / 2,
          stroke: '#2a71b9',
          fill: 'transparent'
        }
      });
    }
    group.sort();
    return keyShape;
  },
  drawSelected: function (item) {
    const group = item.getGraphicGroup();
    return group.addShape('rect', {
      name: 'selected',
      attrs: {
        x: -10,
        y: -6,
        width: defaultIconSize + 20,
        height: defaultIconSize + 12,
        stroke: '#0af',
        lineDash: [4, 2],
        lineWidth: 1,
        fill: 'rgba(0,170,255,0.04)'
      }
    });
  },
  drawExtender: function (item) {
    const group = item.getGraphicGroup();
    group.addShape('image', {
      name: 'extendNeighbor',
      zIndex: 1,
      attrs: {
        img: imgPlus,
        x: defaultIconSize - 15,
        y: -5,
        width: 20,
        height: 20
      }
    });
  },
  drawText: function (item) {
    const group = item.getGraphicGroup();
    group.addShape('text', {
      name: 'pos0',
      attrs: {
        x: defaultIconSize / 2,
        y: defaultIconSize + 6,
        fill: '#999',
        text: item.id,
        textBaseline: 'top',
        textAlign: 'center'
      }
    });
    group.addShape('text', {
      name: 'pos1',
      attrs: {
        x: defaultIconSize / 2,
        y: defaultIconSize + 18,
        fill: '#999',
        text: item.model.pos2,
        textBaseline: 'top',
        textAlign: 'center'
      }
    });
    group.addShape('text', {
      name: 'pos2',
      attrs: {
        x: defaultIconSize / 2,
        y: defaultIconSize + 30,
        fill: '#999',
        text: item.model.pos2,
        textBaseline: 'top',
        textAlign: 'center'
      }
    });
    group.addShape('text', {
      name: 'pos3',
      attrs: {
        x: defaultIconSize / 2,
        y: defaultIconSize + 42,
        fill: '#999',
        text: item.model.pos3,
        textBaseline: 'top',
        textAlign: 'center'
      }
    });
    group.addShape('text', {
      name: 'pos4',
      attrs: {
        x: defaultIconSize / 2,
        y: defaultIconSize + 54,
        fill: '#999',
        text: item.model.pos4,
        textBaseline: 'top',
        textAlign: 'center'
      }
    });
  }
});
G6.registerEdge('topology', {
  draw: function(item) {
    const group = item.getGraphicGroup();
    const points = item.getPoints();
    const sourceEdges = item.source.getEdges();
    const targetId = item.target.id;
    let curEdgeIndex = 0;
    let edgeCount = 0;
    let findCurEdge = false;
    for (const edgeIndex in sourceEdges) {
      const edge = sourceEdges[edgeIndex];
      if (edge.target.id === targetId || edge.source.id == targetId) {
        if (edge.id !== item.id && !findCurEdge) {
          curEdgeIndex++;
        } else {
          findCurEdge = true;
        }
        edgeCount++;
      }
    }
    const radian = Math.atan((points[1].y - points[0].y) / (points[1].x - points[0].x));
    let offset = 0;
    const defaultOffset = 25;
    if (edgeCount % 2 === 0) {
      const pairIndex = Math.trunc((curEdgeIndex) / 2);
      if (pairIndex === 0) {
        offset = defaultOffset;
      } else {
        offset = pairIndex * defaultOffset * 2 + defaultOffset;
      }
      if ((curEdgeIndex) % 2 === 0) {
        offset = -offset;
      }
    } else {
      const pairIndex = Math.trunc((curEdgeIndex + 1) / 2);
      if (curEdgeIndex === 0) {
        offset = 0;
      } else {
        offset = pairIndex * defaultOffset * 2;
      }
      if ((curEdgeIndex + 1) % 2 === 0) {
        offset = -offset;
      }
    }
    let offsetX = Math.sin(2 * Math.PI - radian) * offset;
    let offsetY = Math.cos(2 * Math.PI - radian) * offset;
    const midControlPoint = {x: (points[0].x + points[1].x) / 2 + offsetX, y: (points[0].y + points[1].y) / 2 + offsetY}
    const textRadian1 = Math.atan((midControlPoint.y - points[0].y) / (midControlPoint.x - points[0].x));
    const textRadian2 = Math.atan((points[1].y - midControlPoint.y) / (points[1].x - midControlPoint.x));
    const textAlign = ['right', 'left'];
    const textBaseline = ['top', 'bottom'];
    let leftStyleIndex = 0;
    let rightStyleIndex = 1;
    if (points[0].x < midControlPoint.x) {
      leftStyleIndex = 1;
    }
    if (points[1].x > midControlPoint.x) {
      rightStyleIndex = 0;
    }
    const text1 = group.addShape('text', {
      attrs: {
        x: points[0].x,
        y: points[0].y,
        fill: '#333',
        text: 'source:' + item.model.source,
        textBaseline: textBaseline[leftStyleIndex],
        textAlign: textAlign[leftStyleIndex]
      }
    });
    const text2 = group.addShape('text', {
      attrs: {
        x: points[1].x,
        y: points[1].y,
        fill: '#333',
        text: 'target:' + item.model.target,
        textBaseline: textBaseline[rightStyleIndex],
        textAlign: textAlign[rightStyleIndex]
      }
    });
    // auxiliaryLine for selecting
    group.addShape('path', {
      attrs: {
        path: 'M' + points[0].x + ',' + points[0].y
          + ' Q ' + midControlPoint.x + ',' + midControlPoint.y
          + ' ' + points[1].x + ',' + points[1].y,
        stroke: 'rgba(0,0,0,0)',
        lineWidth: 9
      }
    });
    const keyShape = group.addShape('path', {
      attrs: {
        path: 'M' + points[0].x + ',' + points[0].y
          + ' Q ' + midControlPoint.x + ',' + midControlPoint.y
          + ' ' + points[1].x + ',' + points[1].y,
        stroke: item.model.selected ? selectedLineColor : lineColor,
        lineWidth: 1,
        lineDash: item.model.selected ? [5, 2] : undefined
      }
    });
    text1.rotateAtStart(textRadian1);
    text2.rotateAtStart(textRadian2);
    return keyShape
  }
});

export default {
  name: 'vmap',
  props: {
    showMinimap: {
      type: Boolean,
      default: true
    },
    mapId: String
  },
  data: function() {
    return {
      minimapId: this.mapId + '-minimap',
      minimapVisiable: this.showMinimap,
      scale: 100,
      graph: undefined,
      mapData: {
        nodes: [{
          id: 'node1',
          x: 0,
          y: 0,
          pos1: '111',
          pos2: '1111',
          shape: 'networkObject',
          icon: router,
          parent: 'group1'
        }, {
          id: 'node2',
          x: 400,
          y: 0,
          pos1: '222',
          pos2: '2222',
          shape: 'networkObject',
          icon: router,
          parent: 'node1'
        }, {
          id: 'node3',
          x: 0,
          y: 500,
          pos1: '111',
          pos2: '1111',
          shape: 'networkObject',
          icon: router
          // icon: 'img/router.png'
        }, {
          id: 'node4',
          x: 400,
          y: 500,
          pos1: '222',
          pos2: '2222',
          shape: 'networkObject',
        }],
        edges: [{
          source: 'node1',
          target: 'node2',
          shape: 'topology'
        }, {
          source: 'node1',
          target: 'node2',
          shape: 'topology'
        }, {
          source: 'node2',
          target: 'node1',
          shape: 'topology'
        }, {
          source: 'node2',
          target: 'node1',
          shape: 'topology'
        }, {
          source: 'node3',
          target: 'node4',
          shape: 'topology'
        }, {
          source: 'node3',
          target: 'node4',
          shape: 'topology'
        }, {
          source: 'node4',
          target: 'node3',
          shape: 'topology'
        }, {
          source: 'node4',
          target: 'node3',
          shape: 'topology'
        }, {
          source: 'node3',
          target: 'group1',
          shape: 'topology'
        }, {
          source: 'node4',
          target: 'node2',
          shape: 'topology'
        }],
        groups: [{
          id: 'group1',       // id 必须唯一
          color: '#f00',
          style: {         // 关键形样式（优先级高于color）
            stroke: 'blue',
            fill: 'transparent',
            lineDash: [8, 4]
          },
          label: {   // 文本标签 || 文本图形配置
            text: 'HA Group'
          }
        }]
      }
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
      this.graph.zoom(this.scale / 100);
    }
  },
  methods: {
    test: function() {
      this.graph.update('node1', {parent: 'group1'});
      this.graph.update('node2', {parent: 'group1'});
      this.graph.update('group1', {});
      this.graph.find('node1').updateCollapsedParent(true);
    },
    test2: function() {
      // console.log(this.graph.save());
    },
    saveToImage: function() {
      // console.log(this.graph.saveImage().toDataURL());
    },
    toggleMinimap: function() {
      this.minimapVisiable = !this.minimapVisiable;
    },
    zoomToFit: function() {
      this.graph.setFitView('autoZoom');
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
      const nodeId = event.dataTransfer.getData("text");
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
        if (node.model.selected) {
          const nodeParent = node.getParent();
          this.graph.remove(node);
          this.graph.update(nodeParent, {});
          nodeIndex--;
        }
      }
      const edges = this.graph.getEdges();
      for (let edgeIndex = 0; edgeIndex < edges.length; edgeIndex++) {
        const edge = edges[edgeIndex];
        const source = edge.source;
        if (edge.model.selected) {
          this.graph.remove(edge);
          if (source) {
            this.graph.update(source, {});
          }
          edgeIndex--;
        }
      }
      const groups = this.graph.getGroups();
      for (let groupIndex = 0; groupIndex < groups.length; groupIndex++) {
        const group = groups[groupIndex];
        if (group.getChildren().length === 0) {
          this.graph.remove(group);
          groupIndex--;
        }
      }
      // this.graph.draw();
    },
    undo: function() {
      // console.log('undo');
    },
    selectAllItems: function(event) {
      event.preventDefault();
      for (let item of this.graph.getItems()) {
        this.graph.update(item, {selected: true});
      }
    },
  },
  mounted: function() {
    imageCache = {};
    const plugins = [];
    if (this.showMinimap) {
      const minimap = new G6.Plugins['tool.minimap']({
        container: this.minimapId,
        width: 200,
        height: 120
      });
      plugins.push(minimap);
    }
    const containerSize = getContainerSize(this.mapId);
    this.graph = new G6.Graph({
      container: this.mapId,
      width: containerSize.width,
      height: containerSize.height,
      fitView: 'cc',
      plugins: plugins
    });
    const graph = this.graph;
    this.graph.read(this.mapData);
    this.graph.getNodes().forEach(
      node => {
        this.graph.update(node, {});
      }
    );
    this.graph.css({
      cursor: '-webkit-grab'
    });
    this.graph.on('contextmenu', event => {
      event.domEvent.preventDefault();
      const item = event.item;
      const div = document.createElement('div');
      div.innerHTML = `<el-button>${item.id}</el-button>`;
      this.graph.getGraphContainer().appendChild(div);
    });
    this.graph.on('click', event => {
      if (!event.item) {
        for (let item of graph.getItems()) {
          if (item.model.selected) {
            graph.update(item, {selected: false});
          }
        }
      } else {
        graph.update(event.item, {selected: true});
      }
    });
    let mouseOffset;
    this.graph.on('dragstart', function(event) {
      if (event.currentItem && event.currentItem.isNode) {
        if (event.currentItem.isNode) {
          mouseOffset = {
            x: event.currentItem.model.x - event.x,
            y: event.currentItem.model.y - event.y
          };
          graph.update(event.currentItem, {selected: true});
        }
      }
    });
    this.graph.on('drag', event => {
      const movementX = event.domEvent.movementX;
      const movementY = event.domEvent.movementY;
      if (event.currentItem) {
        if (event.currentItem.isNode) {
          for (let node of graph.getNodes()) {
            if (node.model.selected && node.id !== event.currentItem.id) {
              graph.update(node, {
                x: node.model.x + movementX,
                y: node.model.y + movementY
              });
              const nodeParent = node.getParent();
              if (nodeParent) {
                graph.update(nodeParent, {});
              }
            }
          }
          graph.update(event.currentItem, {
            x: event.x + mouseOffset.x,
            y: event.y + mouseOffset.y
          });
          graph.update(event.currentItem.getParent(), {});
        } else if (event.currentItem.isGroup) {
          for (let child of event.currentItem.getChildren()) {
            graph.update(child, {
              x: child.model.x + movementX,
              y: child.model.y + movementY
            });
          }
          graph.update(event.currentItem, {});
        }
      } else {
        this.graph.translate(movementX, movementY);
      }
    });
    this.graph.on('dragend', () => {
      mouseOffset = undefined;
    });
    this.graph.on('mouseenter', event => {
      if (event.item) {
        this.graph.css({
          cursor: 'default'
        });
      }
    });
    this.graph.on('mouseleave', event => {
      if (event.item) {
        this.graph.css({
          cursor: '-webkit-grab'
        });
      }
    });
    window.onresize = () => {
      const containerSize = getContainerSize(this.graph.get('container'));
      this.graph.changeSize(containerSize.width, containerSize.height);
    }
  }
}
</script>

<style scoped>
.map-parent-container {
  background: #fff;
  height: 100%;
  overflow: hidden;
  position: relative;
  -webkit-user-drag: none;
}
.map-container {
  height: 100%;
  image-rendering: pixelated;
}
.minimap-container {
  border: 1px solid #999;
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
