import APIURI from '../service/api'

export default {
  user: {
    authenticated: !!window.localStorage.getItem('token')
  },

  login (context, creds, redirect) {
    // context.$http.post(APIURI.SESSION_URL, creds)
    //   .then(resp => {
    //     window.localStorage.setItem('token', resp.body.token)
    //
    //     this.user.authenticated = true
    //
    //     if (redirect) {
    //       context.loginLoading = false
    //       context.$router.push({path: redirect})
    //     }
    //   }, resp => {
    //     context.loginLoading = false
    //     context.error = resp.body.message
    //     context.$notify.error({
    //       title: '登录失败',
    //       message: '请输入正确的用户名与密码'
    //     })
    //   })
    if (creds.username === 'demo' && creds.password === 'demo') {
      window.localStorage.setItem('token', 'demo')
      this.user.authenticated = true
      if (redirect) {
        context.loginLoading = false
        context.$router.push({path: redirect})
      }
    }
  },

  currentUser (context) {
    context.$http.get(APIURI.CURRENT_USER_URL, {headers: this.getAuthHeader()})
      .then(resp => {
        context.user = resp.body.username
      }, _ => {
        window.localStorage.removeItem('token')
        this.user.authenticated = false
        context.$router.push({
          path: '/login',
          query: {redirect: context.$route.fullPath}
        })
      })
  },

  signup (context, creds, redirect) {
    context.$http.post(APIURI.REGISTRATION_URL, creds)
      .then(resp => {
        window.localStorage.setItem('token', resp.body.jwt)
        this.user.authenticated = true

        if (redirect) {
          context.$router.push({path: redirect})
        }
      }, resp => {
        console.log(resp.body.errors)
        context.errors = resp.body.errors
      })
  },

  logout (context, options) {
    window.localStorage.removeItem('token')
    this.user.authenticated = false
    context.$router.push({path: '/login'})
  },

  checkAuth () {
    const jwt = window.localStorage.getItem('token')
    this.user.authenticated = !!jwt
  },

  getAuthHeader () {
    return {
      'Authorization': 'JWT ' + window.localStorage.getItem('token')
    }
  }
}
