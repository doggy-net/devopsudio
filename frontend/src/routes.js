import Dashboard from './components/Dashboard.vue'
import NotFound from './components/modules/error/404.vue'
import demo1Page from './components/modules/common-page/demo1.vue'
import demo2Page from './components/modules/common-page/demo2.vue'
import demo3Page from './components/modules/common-page/demo3.vue'
import demo4Page from './components/modules/common-page/demo4.vue'
import Login from './components/Login.vue'
import NotFoundSecond from './components/modules/error/500.vue'
import Index from './components/modules/dashboard/Index.vue'
import auth from './auth'

const requireAuth = (to, from, next) => {
  if (!auth.user.authenticated) {
    next({
      path: '/login',
      query: { redirect: to.fullPath }
    })
  } else {
    document.body.className += 'skin-dark sidebar-mini'
    next()
  }
}

const afterAuth = (_to, from, next) => {
  if (auth.user.authenticated) {
    next(from.path)
  } else {
    next()
  }
}

// Routes
const routes = [
  {
    path: '/login',
    name: 'login',
    meta: { bodyClass: 'login-page' },
    component: Login,
    beforeEnter: afterAuth
  },
  {
    path: '/',
    component: Dashboard,
    meta: { requiresAuth: true, bodyClass: ' skin-dark sidebar-mini' },
    activate: function () {
      this.$nextTick(function () {
        // => 'DOM loaded and ready'
        alert('test')
      })
    },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: Index,
        beforeEnter: requireAuth
      }, {
        path: 'dashboard',
        name: 'dashboard',
        component: Index,
        beforeEnter: requireAuth
      }, {
        path: '/demo1',
        name: 'demo1',
        component: demo1Page
      }, {
        path: '/demo2',
        name: 'demo2',
        component: demo2Page
      }, {
        path: '/demo3',
        name: 'demo3',
        component: demo3Page
      }, {
        path: '/demo4',
        name: 'demo4',
        component: demo4Page
      }, {
        path: '/login',
        name: 'login',
        component: Login
      }, {
        path: '/404',
        name: '404',
        component: NotFound
      }, {
        path: '/500',
        name: '500',
        component: NotFoundSecond
      },
      {
        path: '*',
        name: '404',
        component: NotFound
      }
    ]
  }, {
    // not found handler
    path: '*',
    redirect: '/login'
  }
]

export default routes
