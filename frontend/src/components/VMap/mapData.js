import router from "./svg-icons/router.svg";

const mapData = {
  nodes: [
    {
      id: "node1",
      x: 0,
      y: 0,
      pos1: "111",
      pos2: "1111",
      pos3: "555",
      shape: "networkObject",
      icon: router,
      parent: "group1"
    },
    {
      id: "node2",
      x: 400,
      y: 0,
      pos1: "222",
      pos2: "2222",
      shape: "networkObject",
      icon: router,
      parent: "node1"
    },
    {
      id: "node3",
      x: 0,
      y: 500,
      pos1: "111",
      pos2: "1111",
      shape: "networkObject",
      icon: router
      // icon: 'img/router.png'
    },
    {
      id: "node4",
      x: 400,
      y: 500,
      pos1: "222",
      pos2: "2222",
      shape: "networkObject"
    }
  ],
  edges: [
    {
      source: "node1",
      target: "node2",
      shape: "topology"
    },
    {
      source: "node1",
      target: "node2",
      shape: "topology"
    },
    {
      source: "node2",
      target: "node1",
      shape: "topology"
    },
    {
      source: "node2",
      target: "node1",
      shape: "topology"
    },
    {
      source: "node3",
      target: "node4",
      shape: "line"
    }
  ],
  groups: [
    {
      id: "group1", // id 必须唯一
      color: "#f00",
      style: {
        // 关键形样式（优先级高于color）
        stroke: "blue",
        fill: "transparent",
        lineDash: [8, 4]
      },
      label: {
        // 文本标签 || 文本图形配置
        text: "HA Group"
      }
    }
  ]
};

export default mapData;
