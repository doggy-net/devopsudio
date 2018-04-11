<template>
    <transition name="el-zoom-in-center">
      <div class="content-wrapper">
            <section class="content col-md-6 col-md-offset-2 col-sm-12">
                <div class="box login-box">
                    <div class="box-header">
                      <h4>Doggy Network</h4>
                    </div>
                    <div class="box-body">
                      <form class="form">
                        <div class="form-group">
                          <label for="inputUsername">用户名</label>
                          <el-input id="inputUsername" placeholder="请输入用户名" v-model="credentials.username"></el-input>
                          <p class="field-message" v-if="errors.username">{{ errors.username }}</p>
                        </div>
                        <div class="form-group">
                          <label for="inputpassword">密码</label>
                          <el-input type="password" id="inputpassword" placeholder="请输入用户密码" v-model="credentials.password"></el-input>
                          <p class="field-message" v-if="errors.password">{{ errors.password }}</p>
                        </div>
                        <div class="form-group">
                          <el-button type="primary" :loading="loginLoading" class="btn btn-primary login-btn" @click="login">登录</el-button>
                        </div>
                      </form>
                  </div>
                </div>
            </section>
        </div>
    </transition>
</template>
<script>
  import auth from '../auth'
  import FP from 'fingerprintjs2'

  export default {
    data: function () {
      return {
        loginLoading: false,
        dialogVisible: false,
        credentials: {
          username: '',
          password: '',
          fingerPrint: ''
        },
        error: '',
        errors: Object.assign({}, this.credentials)
      }
    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
      }
      )
    },
    mounted: function () {
      new FP().get(function (result, components) {
        console.log(result)
        this.credentials.fingerPrint = result
      })
    },
    methods: {
      login () {
        this._validateLoginForm()

        const credentials = {
          username: this.credentials.username,
          password: this.credentials.password,
          fingerPrint: this.credentials.fingerPrint
        }

        if (this.credentials.username && this.credentials.password) {
          this.loginLoading = true
          auth.login(this, credentials, '/')
          this.errors = { username: '', password: '' }
        }
      },

      _validateLoginForm () {
        this.error = ''

        if (!this.credentials.username && !this.credentials.password) {
          this.errors = {
            username: '用户名不能为空',
            password: '密码不能为空'
          }
          return
        }

        if (!this.credentials.username) {
          this.errors = {
            username: '用户名不能为空',
            password: ''
          }
          return
        }

        if (!this.credentials.password) {
          this.errors = {
            username: '',
            password: '密码不能为空'
          }
          return
        }
      }
    }
  }
</script>

<style scoped>
  .content-wrapper {
    transform: none;
  }

  .field-message {
    color: red;
    font-weight: bold;
    margin: 5px;
  }

  .login-box {
    opacity: 0.95;
  }

  .login-btn {
    width: 100%;
    margin-top: 20px;
}

  .box-header h4 {
    font-weight: bold;
  }
</style>
