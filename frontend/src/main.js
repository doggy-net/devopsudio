import Vue from 'vue'
import VueRouter from 'vue-router'
import VueI18n from 'vue-i18n'
import enLang from './i18n/en'
import zhChsLang from './i18n/zh-chs'
import zhChtLang from './i18n/zh-cht'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import AppMain from './AppMain.vue'
import Icon from './components/Icon/index.vue'
import routes from './routes'
import store from './store'
import auth from './auth'

Vue.use(ElementUI);
Vue.component(Icon.name, Icon);

Vue.config.productionTip = false

// Check local storage to handle refreshes
if (window.localStorage) {
    if (store.state.token !== window.localStorage.getItem('token')) {
        store.commit('setToken', window.localStorage.getItem('token'))
    }
}

// router
Vue.use(VueRouter);
const router = new VueRouter({
  routes,
  mode: 'history',
  linkActiveClass: 'open active',
  scrollBehavior: function (to, from, savedPosition) {
      return savedPosition || { x: 0, y: 0 }
  }
});
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!auth.user.authenticated) {
      next({
        path: '/login',
        params: {
          redirect: to.fullPath
        }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})
Vue.use(router);

// i18n
Vue.use(VueI18n);
const i18n = new VueI18n({
  locale: 'en',
  messages: {
    'en': enLang,
    'zh-chs': zhChsLang,
    'zh-cht': zhChtLang
  }
});

new Vue({
  el: '#app',
  i18n,
  router,
  store,
  render: h => h(AppMain)
})
