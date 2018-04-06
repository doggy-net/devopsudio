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
                      <d3-network :net-nodes="nodes" :net-links="links" :options="options" />
                    </div>
                </div>
            </section>
            <!-- /.content -->
        </div>
</template>
<script>
  import D3Network from 'vue-d3-network'

  export default {
    name: 'demo1Page',
    components: {
      D3Network
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
