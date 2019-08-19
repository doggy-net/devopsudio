import Vue from 'vue'
import VueI18n from 'vue-i18n'
import elementEnLocale from 'element-ui/lib/locale/lang/en'
import elementZhLocale from 'element-ui/lib/locale/lang/zh-CN'
import enLang from './i18n/en'
import zhChsLang from './i18n/zh-chs'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import AppMain from './AppMain.vue'
import Icon from './components/Icon/index.vue'
import router from './router'
import store from './store'
import auth from './auth'

Vue.config.productionTip = false

// Check local storage to handle refreshes
if (window.localStorage) {
    if (store.state.token !== window.localStorage.getItem('token')) {
        store.commit('setToken', window.localStorage.getItem('token'))
    }
}

// i18n
Vue.use(VueI18n);
const i18n = new VueI18n({
  locale: 'en',
  messages: {
    'en': {
      ...enLang,
      ...elementEnLocale,
    },
    'zh-chs': {
      ...zhChsLang,
      ...elementZhLocale,
    }
  }
});

Vue.use(ElementUI, {
  i18n: (key, value) => i18n.t(key, value)
});
Vue.component(Icon.name, Icon);

new Vue({
  el: '#app',
  i18n,
  router,
  store,
  render: h => h(AppMain)
})
