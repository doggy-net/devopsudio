import G6 from '@antv/g6'
// import G6 from '../../../node_modules/@antv/g6/src'

import iconPlus from './svg-icons/plus-circle-fill.svg'
const defaultIconSize = 60;
const imgPlus = new Image();
imgPlus.src = iconPlus;

let imageCache = {};
G6.registerNode('networkObject', {
  draw(cfg, group) {
    this.drawSelected(group);
    // this.drawExtender(cfg, group);
    this.drawText(cfg, group);
    const iconSize = {
      width: defaultIconSize,
      height: defaultIconSize
    };
    let keyShape;
    let image = new Image();
    if (cfg.icon) {
      if (cfg.icon in imageCache) {
        image = imageCache[cfg.icon];
      } else {
        const downloadingImage = new Image();
        downloadingImage.onload = function() {
          image.src = this.src;
          // graph.refresh();
        };
        imageCache[cfg.icon] = image;
        downloadingImage.src = cfg.icon;
      }
      keyShape = group.addShape('image', {
        name: 'keyShape',
        attrs: {
          img: cfg.icon,
          x: -defaultIconSize / 2,
          y: -defaultIconSize / 2,
          width: iconSize.width,
          height: iconSize.height
        }
      });
    } else {
      keyShape = group.addShape('circle', {
        name: 'keyShape',
        attrs: {
          x: -defaultIconSize / 2,
          y: -defaultIconSize / 2,
          r: defaultIconSize / 2,
          stroke: '#409eff',
          fill: 'transparent'
        }
      });
    }
    group.sort();
    return keyShape;
  },
  drawSelected(group) {
    return group.addShape('rect', {
      name: 'selected',
      attrs: {
        x: -defaultIconSize / 2 - 10,
        y: -defaultIconSize / 2 - 6,
        width: defaultIconSize + 20,
        height: defaultIconSize + 12,
        stroke: '#0af',
        lineDash: [4, 2],
        lineWidth: 1,
        fill: 'rgba(0, 170, 255, 0.04)'
      },
      visible: false
    });
  },
  drawExtender(cfg, group) {
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
  addText(pos, cfg, group) {
    let text;
    if (pos === 0) {
      text = cfg.id;
    } else {
      text = cfg['pos' + pos];
    }
    group.addShape('text', {
      name: 'pos' + pos,
      attrs: {
        x: 0,
        y: defaultIconSize / 2 + 6 + 14 * pos,
        fill: '#999',
        text: text,
        textBaseline: 'top',
        textAlign: 'center',
        cursor: 'pointer'
      }
    });
  },
  drawText(cfg, group) {
    this.addText(0, cfg, group);
    this.addText(1, cfg, group);
    this.addText(2, cfg, group);
    this.addText(3, cfg, group);
    this.addText(4, cfg, group);
  },
  setState(name, value, item) {
    const group = item.getContainer();
    if (name === 'selected') {
      const selectedShape = group.get('children')[0];
      if (value) {
        selectedShape.show();
      } else {
        selectedShape.hide();
      }
    }
  }
});
