import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  token: null,
  isSidebarCollapsed: window.localStorage.getItem('isSidebarCollapsed') === 'yes'
}

const mutations = {
  toggleSidebar (state) {
    state.isSidebarCollapsed = !state.isSidebarCollapsed;
    if (state.isSidebarCollapsed) {
      window.localStorage.setItem('isSidebarCollapsed', 'yes');
    } else {
      window.localStorage.removeItem('isSidebarCollapsed');
    }
  },
  setToken (state, token) {
    state.token = token;
  },
  removeToken (state) {
    window.localStorage.removeItem('token');
    state.token = null;
  }
}

export default new Vuex.Store({
  state,
  mutations
})
