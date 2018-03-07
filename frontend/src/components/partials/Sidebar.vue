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
                        <a href="#"> <i class="ti-layout-media-overlay"></i> <span>Common Page</span> <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span> </a>
                        <ul class="treeview-menu">
                            <li class="active">
                                <router-link to="/demo1">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo1 Page</router-link>
                            </li>
                            <li class="active">
                                <router-link to="/demo2">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo2 Page</router-link>
                            </li>
                            <li class="active">
                                <router-link to="/demo3">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo3 Page</router-link>
                            </li>
                          <li class="active">
                                <router-link to="/demo4">
                                    <avatar username="Blank Page" :size='20' color="#fff"></avatar> Demo4 Page</router-link>
                            </li>
                        </ul>
                    </li>
                    <li class="header">DEVIN VUE 1.0.0</li>
                    <li> <a href="http://ndesaintheme.com/devin/doc"><span>Documentation</span>
                  <span class="pull-right-container">
                  <i class="fa ti-agenda pull-right version"></i>
                </span>
                    </a></li>
                    <li> <a href="#"><span>About</span>
                  <span class="pull-right-container">
                  <i class="fa ti-info-alt pull-right version"></i>
                </span>
                    </a></li>
                    <li> <a href="#"><span>Feedback</span>
                  <span class="pull-right-container">
                  <i class="version fa ti-package pull-right"></i>
                </span>
                    </a></li>
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
