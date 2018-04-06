<template>
        <div class="content-wrapper">
            <!-- Content Header (Page header) -->
            <section class="content-header">
                <h1>Blank Page<small>It's all start from here <i class="ti-heart"></i><i class="ti-export"></i><i class="ti-printer"></i></small></h1>
                <ol class="breadcrumb">
                    <li>
                        <router-link to="/"> <i class="ti-home"></i></router-link>
                    </li>
                    <li><a href="#">Apps</a></li>
                    <li class="active">Blank Page</li>
                </ol>
            </section>
            <!-- Main content -->
            <section class="content">
                <div class="box">
                    <div class="box-header with-border">
                        <h3 class="box-title">Basic</h3>
                        <div class="box-tools pull-right">
                            <button type="button" data-widget="collapse" data-toggle="tooltip" title="Collapse" class="btn btn-box-tool"><i class="ti-minus"></i></button>
                            <button type="button" data-widget="remove" data-toggle="tooltip" title="Remove" class="btn btn-box-tool"><i class="ti-close"></i></button>
                        </div>
                    </div>
                    <div class="box-body" style="min-height:400px;">
                      <d3-network ref='net' :net-nodes="nodes" :net-links="links" :options="options"  :link-cb="lcb"/>
                    </div>
                </div>
            </section>
            <!-- /.content -->
        </div>
</template>
<script>
  import D3Network from 'vue-d3-network'

  export default {
    name: 'demo3Page',
    components: {
      D3Network
    },
    data: function () {
      return {
        nodes: [
          { id: 1, name: 'my awesome node 1' },
          { id: 2, name: 'my node 2' },
          { id: 3, name: 'orange node', _color: 'orange' },
          { id: 4, name: 'blue node', _color: '#00aaff' },
          { id: 5 },
          { id: 6 },
          { id: 7 },
          { id: 8 },
          { id: 9 },
          { id: 10 },
          { id: 11 },
          { id: 12 },
          { id: 13 },
          { id: 14 }
        ],
        links: [
          { sid: 1, tid: 2, name: 'link 1' },
          { sid: 2, tid: 8, name: ' link from 2 to 8' },
          { sid: 4, tid: 3 },
          { sid: 4, tid: 5 },
          { sid: 4, tid: 9 },
          { sid: 5, tid: 6 },
          { sid: 7, tid: 8 },
          { sid: 5, tid: 8, name: 'another link' },
          { sid: 3, tid: 8 },
          { sid: 7, tid: 9 },
          { sid: 3, tid: 9 },
          { sid: 10, tid: 6 },
          { sid: 11, tid: 6 },
          { sid: 12, tid: 6, name: '12 to center' },
          { sid: 13, tid: 6 },
          { sid: 14, tid: 6 }

        ],
        nodeSize: 10,
        canvas: false

      }
    },
    computed: {
      options () {
        return {
          force: 3000,
          size: { w: 600, h: 600 },
          nodeSize: this.nodeSize,
          nodeLabels: true,
          linkLabels: true,
          canvas: this.canvas,
          linkWidth: 2
        }
      }
    },
    methods: {
      lcb (link) {
        return link
      }
    }
  }
</script>
<style>
  @import url('https://fonts.googleapis.com/css?family=PT+Sans');

  body{
    font-family: 'PT Sans', sans-serif;
    background-color: #eee;
  }
  .title{
    position:absolute;
    text-align: center;
    left: 2em;
  }
  h1,a{
    color: #1aad8d;
    text-decoration: none;
  }

  ul.menu {
    list-style: none;
    position: absolute;
    z-index: 100;
    min-width: 20em;
    text-align: left;
  }
  ul.menu li{
    margin-top: 1em;
    position: relative;
  }

  #m-end path, #m-start{
    fill: rgba(18, 120, 98, 0.8);
  }
  .node-label{
    font-size: .5em;
  }
  .link-label{
    fill: purple;
    transform: translate(0,.5em);
    font-size: .8em;
  }
</style>
