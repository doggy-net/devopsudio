<template>
        <div class="content-wrapper">
            <!-- Content Header (Page header) -->
            <section class="content-header">
                <h1>Blank Page<small>It's all start from here <i class="ti-heart"></i><i class="ti-export"></i><i class="ti-printer"></i></small></h1>
                <ol class="breadcrumb">
                    <li>
                        <router-link to="/"> <i class="ti-home"></i></router-link>
                    </li>
                    <li><a href="#">Common Page</a></li>
                    <li class="active">Login Page</li>
                </ol>
            </section>
            <!-- Main content -->
            <section class="content">
                <el-dialog title="Tips" :visible.sync="dialogVisible" size="tiny" visible="false" :before-close="handleClose">
                    <div class="account-box">
                        <form role="form">
                            <div class="form-group"> <a href="#" class="pull-right label-forgot">Forgot email?</a>
                                <label for="inputUsernameEmail">Username or email</label>
                                <input type="text" id="inputUsernameEmail" class="form-control"> </div>
                            <div class="form-group"> <a href="#" class="pull-right label-forgot">Forgot password?</a>
                                <label for="inputPassword">Password</label>
                                <input type="password" id="inputPassword" class="form-control"> </div>
                            <div class="checkbox pull-left">
                                <label>
                                    <input type="checkbox">Remember me</label>
                            </div>
                            <button class="btn btn btn-primary pull-right" type="submit"><router-link style="color:#fff" to="/"> Log In </router-link></button>
                        </form>
                        <a class="forgotLnk" href="#"></a>
                        <div class="or-box">
                            <center><span class="text-center login-with">Login or <b>Sign Up</b></span></center>
                            <div class="row">
                                <div class="col-md-6 row-block">
                                    <a href="#" class="btn btn-facebook btn-block"> <span class="entypo-facebook space-icon"></span>Facebook</a>
                                </div>
                                <div class="col-md-6 row-block">
                                    <a href="#" class="btn btn-twitter btn-block"> <span class="entypo-twitter space-icon"></span>Twitter</a>
                                </div>
                            </div>
                            <div style="margin-top:25px" class="row">
                                <div class="col-md-6 row-block"> <a href="#/profile" class="btn btn-google btn-block"><span class="entypo-gplus space-icon"></span>Google +</a> </div>
                                <div class="col-md-6 row-block"> <a href="#" class="btn btn-instagram btn-block"><span class="entypo-instagrem space-icon"></span>Instagram</a> </div>
                            </div>
                        </div>
                        <hr>
                        <div class="row-block">
                            <div class="row">
                                <div class="col-md-12 row-block"> <a href="#" class="btn btn-primary btn-block">Create New Account</a> </div>
                            </div>
                        </div>
                    </div>
                </el-dialog>
            </section>
            <!-- /.content -->
        </div>
</template>
<script>
  export default {
    data: function () {
      return {
        dialogVisible: false
      }
    },
    methods: {
      handleClose: function (done) {
        this.$confirm('Are you sure to close this dialog?')
          .then(_ => {
            done()
          })
          .catch(_ => {})
      }
    }
  }
</script>
