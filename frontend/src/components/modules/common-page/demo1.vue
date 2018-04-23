<template>
        <div class='content-wrapper'>
            <!-- Content Header (Page header) -->
            <section class='content-header'>
                <h1>Blank Page<small>It's all start from here <i class='ti-heart'></i><i class='ti-export'></i><i class='ti-printer'></i></small></h1>
                <ol class='breadcrumb'>
                    <li>
                        <router-link to='/'> <i class='ti-home'></i></router-link>
                    </li>
                    <li><a href='#'>Apps</a></li>
                    <li class='active'>Blank Page</li>
                </ol>
            </section>
            <!-- Main content -->
            <section class='content'>
                <div class='box'>
                    <div class='box-header with-border'>
                        <h3 class='box-title'>Basic</h3>
                        <div class='box-tools pull-right'>
                            <button type='button' data-widget='collapse' data-toggle='tooltip' title='Collapse' class='btn btn-box-tool'><i class='ti-minus'></i></button>
                            <button type='button' data-widget='remove' data-toggle='tooltip' title='Remove' class='btn btn-box-tool'><i class='ti-close'></i></button>
                        </div>
                    </div>
                    <div class='box-body'>
                    </div>
                </div>
            </section>
            <!-- /.content -->
        </div>
</template>
<script>
  import * as d3 from 'd3'

  export default {
    name: 'demo1Page',
    mounted: function () {
      var nodes = [{name: 'BGP_A'}, {name: 'BGP_B'},
        {name: 'OSPF_1'}, {name: 'OSPF_2'},
        {name: 'OSPF_1'}, {name: 'OSPF_2'},
        {name: 'OSPF_3'}]

      var links = [{source: 0, target: 1}, {source: 0, target: 2},
        {source: 0, target: 3}, {source: 1, target: 4},
        {source: 1, target: 5}, {source: 1, target: 6}]
      var width = 1800
      var height = 800
      var svg = d3.select('.box-body')
        .append('svg')
        .attr('width', width)
        .attr('height', height)

      // 通过布局来转换数据，然后进行绘制
      var simulation = d3.forceSimulation(nodes)
        .force('link', d3.forceLink(links).distance(100))
        .force('charge', d3.forceManyBody())
        .force('center', d3.forceCenter(width / 2, height / 2))

      simulation
        .nodes(nodes)
        .on('tick', ticked)

      simulation.force('link')
        .links(links)
      var color = d3.scaleOrdinal(d3.schemeCategory20)
      // 绘制
      var svgLinks = svg.selectAll('line')
        .data(links)
        .enter()
        .append('line')
        .style('stroke', '#ccc')
        .style('stroke-width', 3)
        .call(d3.zoom()
          .scaleExtent([-5, 2])
        )

      var svgNodes = svg.selectAll('circle')
        .data(nodes)
        .enter()
        .append('circle')
        .attr('cx', function (d) { return d.x })
        .attr('cy', function (d) { return d.y })
        .attr('r', '20')
        .attr('fill', function (d, i) {
          return color(i)
        }).call(d3.drag().on('start', dragstarted)
          .on('drag', dragged)
          .on('end', dragended))
      console.log(nodes)
      var svgTexts = svg.selectAll('text')
        .data(nodes)
        .enter()
        .append('text')
        .style('fill', 'black')
        .attr('dx', 20)
        .attr('dy', 8)
        .text(function (d) {
          console.log(d)
          return d.name
        })
      function dragstarted (d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart()
        d.fx = d.x
        d.fy = d.y
      }

      function dragged (d) {
        d.fx = d3.event.x
        d.fy = d3.event.y
      }

      function dragended (d) {
        if (!d3.event.active) simulation.alphaTarget(0)
        d.fx = null
        d.fy = null
      }
      function ticked () {
        svgLinks.attr('x1', function (d) { return d.source.x })
          .attr('y1', function (d) { return d.source.y })
          .attr('x2', function (d) { return d.target.x })
          .attr('y2', function (d) { return d.target.y })

        svgNodes.attr('cx', function (d) { return d.x })
          .attr('cy', function (d) { return d.y })

        svgTexts.attr('x', function (d) { return d.x })
          .attr('y', function (d) { return d.y })
      }
    },
    data: function () {
      return {
        nodes: [
          { id: 1, name: 'MySQL-Server-A' },
          { id: 2, name: 'db-center-access-sw-02' },
          { id: 3, name: 'balance-sw-A', _color: 'orange' },
          { id: 4, name: 'Nginx-Server-A' },
          { id: 5, name: 'balance-sw-B' },
          { id: 6, name: 'Nginx-Server-Backup' },
          { id: 7, name: 'ASA-FW-B' },
          { id: 8, name: 'core-sw-J' },
          { id: 9, name: 'Boss-PC' }
        ],
        links: [
          { sid: 1, tid: 2, _color: 'red' },
          { sid: 2, tid: 8, _color: 'f0f' },
          { sid: 3, tid: 4, _color: 'rebeccapurple' },
          { sid: 4, tid: 5 },
          { sid: 5, tid: 6 },
          { sid: 7, tid: 8 },
          { sid: 5, tid: 8 },
          { sid: 3, tid: 8 },
          { sid: 7, tid: 9 }
        ],
        options:
        {
          force: 3000,
          nodeSize: 20,
          nodeLabels: true,
          linkWidth: 5
        }
      }
    }
  }
</script>
