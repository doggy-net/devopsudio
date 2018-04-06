<template>
    <transition name="slice">
        <div class="content-wrapper dashboard-wrapper">
            <!-- Main content -->
            <section class="content">
                <div class="row">
                    <div class="col-md-3">
                        <!--New User-->
                        <div class="box palette-Pink-300 bg">
                            <div class="box-header  palette-Pink-300 bg">
                                <!-- tools box -->
                                <div class="pull-right text-white box-tools"> <span class="text-white box-btn"><i class="circle-nest-medium ti-user"></i>
                                    </span>&nbsp;&nbsp;&nbsp; </div>
                                <h3 class="box-title">
                                    <span class="text-white">&nbsp;&nbsp;&nbsp;NEW USER</span>
                                </h3> </div>
                            <!-- /.box-header -->
                            <div class="box-body no-pad" style="display: block;">
                                <div class="events-nest ">
                                    <div class="wrap-no-pad text-white">
                                        <bars :data="[1, 2, 5, 9, 5, 10, 3, 5, 2, 5, 1, 8, 2, 9, 0]" :gradient="['#ffffff', '#ffffff']"></bars>
                                        <h1 class="text-white"><strong><animate-number
      from="1"
      to="45"
      duration="9000"
      easing="easeOutQuad"
      :formatter="formatter"
    ></animate-number></strong></h1> <span>Active Users</span>
                                        <p>65%</p>
                                        <br> </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                        <!--end of New User-->
                    </div>
                    <div class="col-md-3">
                        <!--facebook-->
                        <div class="box palette-Cyan-400 bg">
                            <div class="box-header  palette-Cyan-400 bg">
                                <!-- tools box -->
                                <div class="pull-right text-white box-tools"> <span class="text-white box-btn"><i class="circle-nest-medium ti-stats-up"></i>
                                    </span>&nbsp;&nbsp;&nbsp; </div>
                                <h3 class="box-title">
                                    <span class="text-white">&nbsp;&nbsp;&nbsp;PAGE VIEWS</span>
                                </h3> </div>
                            <!-- /.box-header -->
                            <div class="box-body no-pad" style="display: block;">
                                <div class="events-nest ">
                                    <div class="wrap-no-pad text-white">
                                        <bars :data="[1, 2, 5, 9, 5, 10, 3, 5, 2, 5, 1, 8, 2, 9, 0]" :gradient="['#ffffff', '#ffffff']"></bars>
                                        <h1 class="text-white"><strong><animate-number
      from="45575"
      to="744"
      duration="9000"
      easing="easeOutQuad"
      :formatter="formatter"
    ></animate-number></strong></h1> <span>PerWeek Views</span>
                                        <p>65%</p>
                                        <br> </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                        <!--end of facebook-->
                    </div>
                    <div class="col-md-3">
                        <!--facebook-->
                        <div class="box palette-Deep-Purple-300 bg">
                            <div class="box-header  palette-Deep-Purple-300 bg">
                                <!-- tools box -->
                                <div class="pull-right text-white box-tools"> <span class="text-white box-btn"><i class="circle-nest-medium dripicons-wallet"></i>
                                    </span>&nbsp;&nbsp;&nbsp; </div>
                                <h3 class="box-title">
                                    <span class="text-white">&nbsp;&nbsp;&nbsp;DAILY SALES</span>
                                </h3> </div>
                            <!-- /.box-header -->
                            <div class="box-body no-pad" style="display: block;">
                                <div class="events-nest ">
                                    <div class="wrap-no-pad text-white">
                                        <bars :data="[1, 2, 5, 9, 5, 10, 3, 5, 2, 5, 1, 8, 2, 9, 0]" :gradient="['#ffffff', '#ffffff']"></bars>
                                        <h1 class="text-white"><strong><animate-number
      from="0"
      to="13"
      duration="9000"
      easing="easeOutQuad"
      :formatter="formatter"
    ></animate-number></strong></h1> <span>Sales</span>
                                        <p>15%</p>
                                        <br> </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                        <!--end of facebook-->
                    </div>
                    <div class="col-md-3">
                        <!--facebook-->
                        <div class="box palette-Indigo-900 bg">
                            <div class="box-header  palette-Indigo-900 bg">
                                <!-- tools box -->
                                <div class="pull-right text-white box-tools"> <span class="text-white box-btn"><i class="circle-nest-medium dripicons-basket"></i>
                                    </span>&nbsp;&nbsp;&nbsp; </div>
                                <h3 class="box-title">
                                    <span class="text-white">&nbsp;&nbsp;&nbsp;TOTAL EARNINGS</span>
                                </h3> </div>
                            <!-- /.box-header -->
                            <div class="box-body no-pad" style="display: block;">
                                <div class="events-nest ">
                                    <div class="wrap-no-pad text-white">
                                        <bars :data="[1, 2, 5, 9, 5, 10, 3, 5, 2, 5, 1, 8, 2, 9, 0]" :gradient="['#ffffff', '#ffffff']"></bars>
                                        <h1 class="text-white"><strong><animate-number
      from="1"
      to="3500"
      duration="9000"
      easing="easeOutQuad"
      :formatter="formatter"
    ></animate-number></strong></h1> <span>Dollars</span>
                                        <p>
                                            <animate-number from="1" to="65" duration="9000" easing="easeOutQuad" :formatter="formatter"></animate-number>%</p>
                                        <br> </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                        <!--end of facebook-->
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="box no-shadow">
                            <!-- /.box-header -->
                            <div class="box-body" style="padding:0">
                                <div class="events-nest">
                                    <div class="text-white lastest-post-nest palette-Blue-800 bg">
                                        <div class="wrap"> <small class="palette-Blue-400 bg"><i class="ti-facebook "></i></small>
                                            <div class="row">
                                                <div class="col-md-2">
                                                    <h1 class="text-white"><img alt="profile" class="img-circle palette-Grey-900 bg" src="http://api.randomuser.me/portraits/thumb/men/46.jpg"></h1> </div>
                                                <div class="col-md-9">
                                                    <h3>D'Agustino Gavin</h3>
                                                    <p>Pink and Blue: Coloring Inside the Lines of Gender</p>
                                                    <p>
                                                        <el-rate v-model="value1"></el-rate>
                                                    </p> <b><i class="ti-eye"></i> 121</b> <b><i class="ti-thumb-up"></i>45</b> <b><i class="ti-comment-alt"></i> 8</b> </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="box no-shadow">
                            <!-- /.box-header -->
                            <div class="box-body" style="padding:0">
                                <div class="events-nest">
                                    <div class="text-white lastest-post-nest-two palette-Deep-Purple-500 bg">
                                        <div class="wrap"> <small class="palette-Blue-800 bg"><i class="ti-twitter-alt "></i></small>
                                            <div class="row">
                                                <div class="col-md-2">
                                                    <h1 class="text-white"><img alt="profile" class="img-circle palette-Grey-900 bg" src="http://api.randomuser.me/portraits/thumb/women/26.jpg"></h1> </div>
                                                <div class="col-md-9">
                                                    <h3>Dewi Saraswati</h3>
                                                    <p>Pink and Blue: Coloring Inside the Lines of Gender</p>
                                                    <p>
                                                        <el-rate v-model="value1"></el-rate>
                                                    </p> <b><i class="ti-eye"></i> 121</b> <b><i class="ti-thumb-up"></i>45</b> <b><i class="ti-comment-alt"></i> 8</b> </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="box box-no-shadow">
                            <!-- /.box-header -->
                            <div class="box-body " style="display: block;">
                                <div style="margin:0" class="row summary-border-top">
                                    <div class="col-md-6">
                                        <div class="summary-nest">
                                            <h2 class="text-black "><span class="counter-up">276.747</span><small class="palette-Orange-700 bg">K</small></h2>
                                            <p>Sales</p>
                                        </div>
                                    </div>
                                    <div class="col-md-6 summary-border-left">
                                        <div class="summary-nest">
                                            <h2 class="text-black"><span class="counter-up">3.219</span><small class="palette-Pink-500 bg">K</small></h2>
                                            <p>Man</p>
                                        </div>
                                    </div>
                                </div>
                                <div style="margin:0" class="row">
                                    <div class="col-md-12">
                                        <div class="summary-nest summary-pad-nest">
                                            <bars :data="[1, 2, 5, 9, 5, 10, 3, 5, 2, 5, 1, 8, 2, 9, 4]" :gradient="['#3b5998', '#3b5998']"></bars>
                                            <h4 class="text-center"><span class="counter-up">5</span>/<span class="counter-up">12</span>/<span class="counter-up">2013</span></h4> </div>
                                    </div>
                                </div>
                                <div style="margin:0" class="row summary-border-bottom">
                                    <div class="col-md-6">
                                        <div class="summary-nest summary-pad-nest">
                                            <h2 class="text-black "><span class="counter-up">82</span><small class="palette-Lime-500 bg ">%</small></h2>
                                            <p>Avarage Sales</p>
                                        </div>
                                    </div>
                                    <div class="col-md-6 summary-border-left">
                                        <div class="summary-nest summary-pad-nest">
                                            <h2 class="text-black"><span class="counter-up">24</span><small class="palette-Teal-500 bg ">th</small></h2>
                                            <p>Overall Rank</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end .timeline -->
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="box box-no-shadow bg-widget-random">
                            <!-- /.box-header -->
                            <div class="box-header bg-transparent">
                                <h3 class="box-title"><i class="text-white ti-rss-alt"></i>
                                    <span class="text-white ">LASTEST REPORT</span>
                                </h3> </div>
                            <div style="margin:15px 0 0" class="box-body">
                                <div class="stats-wrap">
                                    <h2><b class="counter-up text-white">65,800,587</b> <span style="background:#666;">+<b class="counter-up">20</b>%</span></h2>
                                    <p class="text-grey">Total students<small>This Year</small> </p>
                                    <h4><b class="counter-up text-white">1,204</b> <span style="background:#888;">+<b class="counter-up">5</b>%</span></h4>
                                    <p>Graduate <small>This week</small> </p>
                                    <h4 class="text-white"><b class="counter-up">2,690</b> <span>+<b class="counter-up">125</b></span></h4>
                                    <p>New students<small>This Month</small> </p>
                                    <div class="your-account">
                                        <h4>Overall stats of sales and distribution</h4>
                                        <h6>You must <strong>complete</strong> this issues.</h6>
                                        <ul>
                                            <li><i class="text-white palette-Orange-700 bg ti-pie-chart"></i> 2.789</li>
                                            <li><i class="text-white palette-Pink-700 bg ti-stats-down"></i>4.365</li>
                                            <li><i class="palette-Cyan-700 bg text-white ti-bar-chart"></i>9.860 </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <!-- /.box-body -->
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12"> </div>
                </div>
            </section>
            <!-- /.content -->
        </div>
    </transition>
</template>
<script>
  export default {
    name: 'dashboard-first'
  }
</script>
