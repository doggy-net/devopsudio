<template>
  <div style="height: 100%">
    <div class="login-form-container">
    </div>
    <el-card class="login-form">
      <el-form ref="form">
        <h1 style="text-align: center">DevOpStudio</h1>
        <el-form-item>
          <el-input  placeholder="请输入用户名" v-model="credentials.username">
            <template slot="prefix">
              <icon icon-class="user"/>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="password" placeholder="请输入密码" v-model="credentials.password">
            <template slot="prefix">
              <i class="el-icon-info"/>
              <icon icon-class="lock"/>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" style="width: 100%" @click="login">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import auth from '../auth'
import FP from 'fingerprintjs2'

export default {
  name: 'Login',
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
  mounted: function () {
    // FP.get({}, function (result, components) {
    //   console.log(result)
    //   this.credentials.fingerPrint = result
    // })
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
        this.loginLoading = true;
        auth.login(this, credentials, '/');
        this.errors = { username: '', password: '' };
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

<style>
.login-form-container {
  background: url(../assets/bg4.jpg);
  background: #edf0f1;
  background-position: center;
  -webkit-filter: blur(3px);
  -moz-filter: blur(3px);
  -o-filter: blur(3px);
  -ms-filter: blur(3px);
  filter: blur(3px);
  width: 100%;
  height: 100%;
}
.login-form {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  width: 480px;
  height: 306px;
}
</style>
