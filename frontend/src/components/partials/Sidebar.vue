<template>
    <aside class="main-sidebar">
        <!-- sidebar: style can be found in sidebar.less -->
        <div>
            <section class="sidebar">
                <!-- /.search form -->
                <!-- Sidebar user panel -->
                <div class="user-panel">
                    <div class="image"> <img src="static/img/avatar2.png" class="img-circle" alt="User Image"> </div>
                    <div class="info">
                        <p>Hi, Psong</p>
                        <p><small>You haven,t miss any task this week!</small></p>
                        <div> <a href="#"><i class="ti-panel"></i><small>{{ $t("message.mini_bar.settings") }}</small></a> <a href="#"><i class="ti-user"></i><small>{{ $t("message.mini_bar.profile") }}</small></a> <a href="#"><i class="ti-power-off"></i><small>{{ $t("message.mini_bar.logout") }}</small></a> </div>
                    </div> <img class="bg-user" src="static/img/avatar-bg.png" alt="User Image"> </div>
                <!-- sidebar menu: : style can be found in sidebar.less -->
                <ul class="sidebar-menu">
                    <li>
                            <router-link to="/dashboard"> <i class="ti-dashboard"></i> <span>{{ $t("message.dashboard") }}</span></router-link>
                      </li>
                    <li class="header">{{ $t("message.networkMap") }}</li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-world"></i> <span>{{ $t("message.fastMap") }}</span></router-link>
                      </li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-map"></i> <span>{{ $t("message.liveMap") }}</span></router-link>
                      </li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-heart"></i> <span>{{ $t("message.favorite") }}</span></router-link>
                      </li>
                    <li class="header">{{ $t("message.networkMonitor") }}</li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-video-camera"></i> <span>{{ $t("message.liveMonitor") }}</span></router-link>
                      </li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-announcement"></i> <span>{{ $t("message.alertSetting") }}</span></router-link>
                      </li>
                  <li class="header">{{ $t("message.app") }}</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-email"></i> <span>{{ $t("message.manager") }}</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-email"></i> <span>{{ $t("message.editor") }}</span></router-link>
                    </li>
                  <li class="header">{{ $t("message.task") }}</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-hummer"></i> <span>{{ $t("message.quickTask") }}</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-time"></i> <span>{{ $t("message.scheduleTask") }}</span></router-link>
                    </li>
                  <li class="header">{{ $t("message.analysis") }}</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-file"></i> <span>{{ $t("message.analysisMap") }}</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-info-alt"></i> <span>{{ $t("message.analysisDocument") }}</span></router-link>
                    </li>
                  <li class="header">{{ $t("message.system") }}</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-user"></i> <span>{{ $t("message.user") }}</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo2"> <i class="ti-eye"></i> <span>{{ $t("message.dataBee") }}</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo3"> <i class="ti-panel"></i> <span>{{ $t("message.dataSetting") }}</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo4"> <i class="ti-search"></i> <span>{{ $t("message.monitor") }}</span></router-link>
                    </li>
                    <li>
                        <br>
                        <br>
                        <br>
                    </li>
                </ul>
            </section>
            <!-- /.sidebar -->
        </div>
    </aside>
</template>

<script>
import Avatar from 'vue-avatar'
export default {
  name: 'DashboardSidebar',
  mounted: function () {
    $(document).ready(function ($) {
      $('.main-sidebar > div').slimScroll({
        width: '230px',
        position: 'left',
        size: '3px',
        height: '95vh'
      })
    })
  },
  components: {
    Avatar
  }
}
</script>
