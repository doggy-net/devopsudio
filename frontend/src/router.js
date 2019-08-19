import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './views/Login.vue'
import Layout from './views/Layout'
import User from './views/Admin/User.vue'
import Email from './views/Admin/Email.vue'
import DevApp from './views/Development/App.vue'
import Network from './views/Operations/Network.vue'
import Discovery from './views/Operations/Discovery.vue'
import Dashboard from './views/Operations/Dashboard.vue'
import auth from './auth'


Vue.use(VueRouter);

// Routes
export const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
    // beforeEnter: afterAuth
  },
  {
    path: '',
    redirect: {name: 'operations'},
  },
  {
    path: '/admin',
    name: 'admin',
    component: Layout,
    meta: { requiresAuth: true, permission: 'admin' },
    children: [
      {
        path: 'user',
        name: 'user',
        component: User,
        meta: { requiresAuth: true, permission: 'admin.user', title: 'userAccounts', icon: 'user'},
      },
      {
        path: 'email',
        name: 'email',
        component: Email,
        meta: { requiresAuth: true, permission: 'admin.email', title: 'emailSettings', icon: 'email'},
      }
    ]
  },
  {
    path: '/dev',
    name: 'development',
    component: Layout,
    meta: { requiresAuth: true, permission: 'development', title: 'development', icon: 'development' },
    children: [
      {
        path: 'app',
        name: 'devapp',
        component: DevApp,
        meta: { requiresAuth: true, permission: 'development.app', title: 'app', icon: 'app-store-fill' },
      }
    ]
  },
  {
    path: '/ops',
    name: 'operations',
    component: Layout,
    meta: { requiresAuth: true, permission: 'operations', title: 'operations', icon: 'operations' },
    children: [{
        path: 'dashboard',
        name: 'dashboard',
        component: Dashboard,
        meta: { requiresAuth: true, permission: 'operations.dashboard', title: 'dashboard', icon: 'dashboard' },
      },
      {
        path: 'network',
        name: 'network',
        component: Network,
        meta: { requiresAuth: true, permission: 'operations.network', title: 'network', icon: 'topo' },
      },
      {
        path: 'discovery',
        name: 'discovery',
        component: Discovery,
        meta: { requiresAuth: true, permission: 'operations.discovery', title: 'discovery', icon: 'discovery' },
      }
    ]
  },
  {
    // not found handler
    path: '*',
    redirect: '/'
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
  linkActiveClass: 'open active',
  scrollBehavior: function (to, from, savedPosition) {
      return savedPosition || { x: 0, y: 0 }
  }
});

const permissions = {
  'admin': ['user', 'email'],
  'development': ['app'],
  'operations': ['discovery', 'network', 'dashboard'],
}

function hasPermission(reqiredPermission, permissions) {
  if (!reqiredPermission) {
    return true;
  }
  let requiredPermissionList = reqiredPermission.split('.');
  if (!requiredPermissionList) {
    return true;
  }
  if (!(requiredPermissionList[0] in permissions)) {
    return false;
  }
  for (let requiredPermission of requiredPermissionList.slice(1)) {
    if (permissions[requiredPermissionList[0]].indexOf(requiredPermission) < 0) {
      return false;
    }
  }
  return true;
}

const whiteList = ['/login', '/auth-redirect']// no redirect whitelist

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

router.beforeEach((to, from, next) => {
  // NProgress.start() // start progress bar
  if (auth.user.authenticated) { // determine if there has token
    /* has token*/
    if (to.path === '/login') {
      next({ path: '/' })
      // NProgress.done() // if current page is dashboard will not trigger	afterEach hook, so manually handle it
    } else {
      // if (store.getters.roles.length === 0) { // 判断当前用户是否已拉取完user_info信息
      if (false) {
        // store.dispatch('GetUserInfo').then(res => { // 拉取user_info
        //   const roles = res.data.roles // note: roles must be a array! such as: ['editor','develop']
        //   store.dispatch('GenerateRoutes', { roles }).then(() => { // 根据roles权限生成可访问的路由表
        //     router.addRoutes(store.getters.addRouters) // 动态添加可访问路由表
        //     next({ ...to, replace: true }) // hack方法 确保addRoutes已完成 ,set the replace: true so the navigation will not leave a history record
        //   })
        // }).catch((err) => {
        //   store.dispatch('FedLogOut').then(() => {
        //     Message.error(err || 'Verification failed, please login again')
        //     next({ path: '/' })
        //   })
        // })
      } else {
        // 没有动态改变权限的需求可直接next() 删除下方权限判断 ↓
        if (hasPermission(to.meta.permission, permissions)) {
          next()
        } else {
          next({ path: '/401', replace: true, query: { noGoBack: true }})
        }
        // 可删 ↑
      }
    }
  } else {
    /* has no token*/
    if (whiteList.indexOf(to.path) !== -1) { // 在免登录白名单，直接进入
      next()
    } else {
      next(`/login?redirect=${to.path}`) // 否则全部重定向到登录页
      // NProgress.done() // if current page is login will not trigger afterEach hook, so manually handle it
    }
  }
})

router.afterEach(() => {
  // NProgress.done() // finish progress bar
})

export default router
