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
                        <p>Good Job, Matirasa</p>
                        <p><small>You haven,t miss any task this week!</small></p>
                        <div> <a href="#"><i class="ti-panel"></i><small>Settings</small></a> <a href="#"><i class="ti-user"></i><small>Profile</small></a> <a href="#"><i class="ti-power-off"></i><small>Logout</small></a> </div>
                    </div> <img class="bg-user" src="static/img/avatar-bg.png" alt="User Image"> </div>
                <!-- sidebar menu: : style can be found in sidebar.less -->
                <ul class="sidebar-menu">
                    <li class="treeview">
                        <a href="#"> <i class="ti-layout-media-overlay"></i> <span>Demo Page</span> <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span> </a>
                        <ul class="treeview-menu">
                            <li >
                                <router-link to="/demo1">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo1 Page</router-link>
                            </li>
                            <li >
                                <router-link to="/demo2">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo2 Page</router-link>
                            </li>
                            <li >
                                <router-link to="/demo3">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo3 Page</router-link>
                            </li>
                          <li >
                                <router-link to="/demo4">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo4 Page</router-link>
                            </li>
                        </ul>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-dashboard"></i> <span>Dashboard</span></router-link>
                      </li>
                    <li class="header">Network Map</li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-world"></i> <span>Fast Map</span></router-link>
                      </li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-map"></i> <span>Live Map</span></router-link>
                      </li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-heart"></i> <span>Favorite</span></router-link>
                      </li>
                    <li class="header">Network Monitor</li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-video-camera"></i> <span>Live Monitor</span></router-link>
                      </li>
                      <li>
                            <router-link to="/demo1"> <i class="ti-announcement"></i> <span>Alert Setting</span></router-link>
                      </li>
                  <li class="header">App</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-email"></i> <span>Manager</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-email"></i> <span>Editor</span></router-link>
                    </li>
                  <li class="header">Task</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-hummer"></i> <span>Quick Task</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-time"></i> <span>Schedule Task</span></router-link>
                    </li>
                  <li class="header">Analysis</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-file"></i> <span>Analysis Map</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-info-alt"></i> <span>Analysis Document</span></router-link>
                    </li>
                  <li class="header">System</li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-user"></i> <span>User</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-eye"></i> <span>Data Bee</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-panel"></i> <span>Data Setting</span></router-link>
                    </li>
                    <li>
                            <router-link to="/demo1"> <i class="ti-search"></i> <span>Monitor</span></router-link>
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
