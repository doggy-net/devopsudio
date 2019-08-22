import G6 from '@antv/g6'
// import G6 from '../../../node_modules/@antv/g6/src'

const lineColor = '#666';
const selectedLineColor = '#0af';

G6.registerEdge('topology', {
  draw(cfg, group) {
    const sourceEdges = cfg.sourceNode.getEdges();
    const targetId = cfg.targetNode.id;
    let curEdgeIndex = 0;
    let edgeCount = 0;
    let findCurEdge = false;
    for (const edgeIndex in sourceEdges) {
      const edge = sourceEdges[edgeIndex];
      if (edge.getTarget().id === targetId || edge.getSource().id == targetId) {
        if (edge.id !== cfg.id && !findCurEdge) {
          curEdgeIndex++;
        } else {
          findCurEdge = true;
        }
        edgeCount++;
      }
    }
    const radian = Math.atan(
      (cfg.endPoint.y - cfg.startPoint.y) / (cfg.endPoint.x - cfg.startPoint.x)
    );
    let offset = 0;
    const defaultOffset = 25;
    if (edgeCount % 2 === 0) {
      const pairIndex = Math.trunc(curEdgeIndex / 2);
      if (pairIndex === 0) {
        offset = defaultOffset;
      } else {
        offset = pairIndex * defaultOffset * 2 + defaultOffset;
      }
      if (curEdgeIndex % 2 === 0) {
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
    const midControlPoint = {
      x: (cfg.startPoint.x + cfg.endPoint.x) / 2 + offsetX,
      y: (cfg.startPoint.y + cfg.endPoint.y) / 2 + offsetY
    };
    const textRadian1 = Math.atan(
      (midControlPoint.y - cfg.startPoint.y) / (midControlPoint.x - cfg.startPoint.x)
    );
    const textRadian2 = Math.atan(
      (cfg.endPoint.y - midControlPoint.y) / (cfg.endPoint.x - midControlPoint.x)
    );
    const textAlign = ['right', 'left'];
    const textBaseline = ['top', 'bottom'];
    let leftStyleIndex = 0;
    let rightStyleIndex = 1;
    if (cfg.startPoint.x < midControlPoint.x) {
      leftStyleIndex = 1;
    }
    if (cfg.endPoint.x > midControlPoint.x) {
      rightStyleIndex = 0;
    }
    const text1 = group.addShape('text', {
      attrs: {
        x: cfg.startPoint.x,
        y: cfg.startPoint.y,
        fill: '#333',
        text: 'source:' + cfg.source,
        textBaseline: textBaseline[leftStyleIndex],
        textAlign: textAlign[leftStyleIndex]
      }
    });
    const text2 = group.addShape('text', {
      attrs: {
        x: cfg.endPoint.x,
        y: cfg.endPoint.y,
        fill: '#333',
        text: 'target:' + cfg.target,
        textBaseline: textBaseline[rightStyleIndex],
        textAlign: textAlign[rightStyleIndex]
      }
    });
    // auxiliary line for selecting
    group.addShape('path', {
      attrs: {
        path:
          'M' +
          cfg.startPoint.x +
          ',' +
          cfg.startPoint.y +
          ' Q ' +
          midControlPoint.x +
          ',' +
          midControlPoint.y +
          ' ' +
          cfg.endPoint.x +
          ',' +
          cfg.endPoint.y,
        stroke: 'rgba(0,0,0,0)',
        lineWidth: 14
      }
    });
    const keyShape = group.addShape('path', {
      attrs: {
        path:
          'M' +
          cfg.startPoint.x +
          ',' +
          cfg.startPoint.y +
          ' Q ' +
          midControlPoint.x +
          ',' +
          midControlPoint.y +
          ' ' +
          cfg.endPoint.x +
          ',' +
          cfg.endPoint.y,
        stroke: lineColor,
        lineWidth: 1
      }
    });
    text1.rotateAtStart(textRadian1);
    text2.rotateAtStart(textRadian2);
    return keyShape;
  },
  setState(name, value, item) {
    if (name === 'selected') {
      const keyShape = item.getKeyShape();
      if (value) {
        keyShape.attr({stroke: selectedLineColor, lineDash: [5, 2]});
      } else {
        keyShape.attr({stroke: lineColor, lineDash: []});
      }
    }
  }
});
