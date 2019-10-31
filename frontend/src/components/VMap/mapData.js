const mapData = {
  nodes: [
    {
      id: 'node1',
      x: 50,
      y: 50,
      pos1: '111',
      pos2: '1111',
      pos3: '555',
      shape: 'networkObject',
      icon: '/icons/router.svg',
    },
    {
      id: 'node2',
      x: 400,
      y: 50,
      pos1: '222',
      pos2: '2222',
      shape: 'networkObject',
      icon: '/icons/router.svg',
    },
    {
      id: 'node3',
      x: 50,
      y: 500,
      pos1: '111',
      pos2: '1111',
      shape: 'networkObject',
      icon: '/icons/router.svg',
      // icon: 'img/'/icons/router.svg',.png'
    },
    {
      id: 'node4',
      x: 400,
      y: 500,
      pos1: '222',
      pos2: '2222',
      shape: 'networkObject',
      icon: '/icons/l2_switch.svg',
    }
  ],
  edges: [
    {
      source: 'node1',
      target: 'node2',
      shape: 'topology'
    },
    {
      source: 'node1',
      target: 'node2',
      shape: 'topology'
    },
    {
      source: 'node1',
      target: 'node2',
      shape: 'topology'
    },
    {
      source: 'node3',
      target: 'node4',
      shape: 'topology'
    }
  ],
  groups: [
    {
      id: 'group1', // id 必须唯一
      color: '#f00',
      style: {
        // 关键形样式（优先级高于color）
        stroke: 'blue',
        fill: 'transparent',
        lineDash: [8, 4]
      },
      label: {
        // 文本标签 || 文本图形配置
        text: 'HA Group'
      }
    }
  ]
};

export default mapData;
