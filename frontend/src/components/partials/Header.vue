<template>
    <header class="main-header">
        <!-- Logo -->
        <router-link to="/dashboard" class="logo">
            <!-- mini logo for sidebar mini 50x50 pixels --><span class="logo-mini"><b> <img src="static/img/logo.png" alt="User Image"></b></span>
            <!-- logo for regular state and mobile devices --><span class="logo-lg"><img src="/static/img/logo.png" alt="User Image"><b>Devin</b>vue</span> </router-link>
        <!-- Header Navbar: style can be found in header.less -->
        <nav class="navbar navbar-static-top">
            <!-- Sidebar toggle button-->
            <a href="#" class="sidebar-toggle" data-toggle="offcanvas" role="button"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </a>
                                <div class="pull-left-search">
                        <form id="demo-2">
	<input class="devin-search" type="search">
</form>
    
    
    </div>
            <div class="navbar-custom-menu">
                <ul class="nav navbar-nav">
                    <!-- Messages: style can be found in dropdown.less-->

                    <li>
                        <el-dropdown class="header-dropdown-devin" trigger="click"> <span class="el-dropdown-link">
                            <el-badge :value="20" :max="9" class="item">
                            <el-button type="text" size="small"><i class="ti-email"></i></el-button>
                          </el-badge>
                          </span>
                            <el-dropdown-menu slot="dropdown">
                                <ul class="dropdown-menu-devin">
                                    <li class="header">You have 10+ Message</li>
                                    <!-- inner menu: contains the actual data -->
                                    <li>
                                        <ul class="menu">
                                            <li>
                                                <a href="#">
                                                    <h3>Announcements <span>Just Now !</span>
                                                        </h3>
                                                    <p>Pok ame ame belalang kupu kupu</p>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <h3>Complete your profile<span>2 Min Ago</span>
                                                        </h3>
                                                    <p>Siang makan nasi kalo malam minum susu</p>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <h3>New Schedule Realease<span>30 Min ago</span>
                                                        </h3>
                                                    <p>Bintang kecil dilangit yang tinggi</p>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <h3>New Student Data<span>1 Hour ago</span>
                                                        </h3>
                                                    <p>Amat banyak menghias angkasa</p>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="#">
                                                    <h3>Graduate Student List<span>2 Days ago</span>
                                                        </h3>
                                                    <p>Aku ingin terbang dan melayang, jauh tinggi ke tempat kau berada</p>
                                                </a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="footer"><a href="#">View all</a></li>
                                </ul>
                            </el-dropdown-menu>
                        </el-dropdown>
                    </li>
                    <!-- Notifications: style can be found in dropdown.less -->
                    <li>
                        <el-dropdown class="header-dropdown-devin" trigger="click"> <span class="el-dropdown-link">
                            <el-badge is-dot class="item ">
                            <el-button type="text" size="small"><i class="ti-bell"></i></el-button>
                          </el-badge>
                          </span>
                            <el-dropdown-menu slot="dropdown">
                                <ul class="dropdown-menu-devin">
                                    <li class="header">You have 10 notifications</li>
                                    <li>
                                        <!-- inner menu: contains the actual data -->
                                        <ul class="menu">
                                            <li> <i class="ti-announcement"></i>
                                                <a href="#">
                                                    <h3>Announcements <span class="text-green fontello-record"></span>
                                                        </h3>
                                                    <p>Just Now !</p>
                                                </a>
                                            </li>
                                            <li> <i class="ti-user"></i>
                                                <a href="#">
                                                    <h3>Complete your profile<span class="text-yellow fontello-record"></span>
                                                        </h3>
                                                    <p>2 Min Ago</p>
                                                </a>
                                            </li>
                                            <li> <i class="ti-notepad"></i>
                                                <a href="#">
                                                    <h3>New Schedule Realease<span class="text-yellow fontello-record"></span>
                                                        </h3>
                                                    <p>30 Min ago</p>
                                                </a>
                                            </li>
                                            <li> <i class="ti-agenda"></i>
                                                <a href="#">
                                                    <h3>New User Data<span class="text-orange fontello-record"></span>
                                                        </h3>
                                                    <p>1 Hour ago</p>
                                                </a>
                                            </li>
                                            <li> <i class="ti-package"></i>
                                                <a href="#">
                                                    <h3>New User List<span class="fontello-record"></span>
                                                        </h3>
                                                    <p>2 Days ago</p>
                                                </a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="footer"><a href="#">View all</a></li>
                                </ul>
                            </el-dropdown-menu>
                        </el-dropdown>
                    </li>
                    <!-- Control Sidebar Toggle Button -->
                    <li>
                        <el-dropdown class="header-dropdown-devin" trigger="click"> <span class="el-dropdown-link">
                            
                            <el-button data-toggle="control-sidebar" type="text" size="small"><i class="ti-menu-alt"></i></el-button>
                          
                          </span> </el-dropdown>
                    </li>
                  
                </ul>
            </div>
        </nav>
    </header>
</template>
<script>
  export default {
    name: 'DashboardHeader',
    mounted: function () {

    }
  }
</script>