import Vue from 'vue'
import ElementUI from 'element-ui'
import Resource from 'vue-resource'
import VueRouter from 'vue-router'
import routes from './routes'
import store from './store'
// fade/zoom 等
import 'element-ui/lib/theme-chalk/base.css'
// collapse 展开折叠
import CollapseTransition from 'element-ui/lib/transitions/collapse-transition'
import vbclass from 'vue-body-class'
import VueI18n from 'vue-i18n'
import enLang from './i18n/en'
import zhChsLang from './i18n/zh-chs'
import zhChtLang from './i18n/zh-cht'

// Resource logic
Vue.use(Resource)
Vue.http.options.emulateJSON = true
Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.component(CollapseTransition.name, CollapseTransition)

// Import top level component
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
//  for element 1.9.9 below
// import 'element-ui/lib/theme-default/index.css'
import 'element-ui/lib/theme-chalk/index.css'

// Routing logic
var router = new VueRouter({
  routes: routes,
  mode: 'hash',
  linkActiveClass: 'open active',
  scrollBehavior: function (to, from, savedPosition) {
    return savedPosition || { x: 0, y: 0 }
  }
})

// vue-body-class(动态修改body的class)
Vue.use(vbclass, router)

// Check local storage to handle refreshes
if (window.localStorage) {
  if (store.state.token !== window.localStorage.getItem('token')) {
    store.commit('SET_TOKEN', window.localStorage.getItem('token'))
  }
}
// i18n
Vue.use(VueI18n)
const i18n = new VueI18n({
  locale: 'en',
  messages: {
    'en': enLang,
    'zh-chs': zhChsLang,
    'zh-cht': zhChtLang
  }
})

// Some middleware to help us ensure the user is authenticated.

// Start out app!
// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  router: router,
  i18n,
  store: store,
  render: h => h(App)
})

require('bootstrap')
// require('admin-lte')
require('../node_modules/admin-lte/plugins/slimScroll/jquery.slimscroll.js')
require('../node_modules/admin-lte/dist/js/app.js')
// require('../node_modules/admin-lte/dist/js/demo.js')

