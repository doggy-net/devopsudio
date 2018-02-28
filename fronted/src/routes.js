import Dashboard from './components/Dashboard.vue'
import NotFound from './components/modules/dashboard/404.vue'
import BlankPage from './components/modules/common-page/BlankPage.vue'
import Login from './components/Login.vue'
import NotFoundSecond from './components/modules/dashboard/500.vue'

// Routes
const routes = [
  {
    path: '/',
    component: Dashboard,
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      document.body.className += 'skin-light sidebar-mini'
      next()
    },
    activate: function () {
      this.$nextTick(function () {
        // => 'DOM loaded and ready'
        alert('test')
      })
    },
    children: [
      {
        path: '',
        name: 'blank-page',
        component: BlankPage
      }, {
        path: '/login',
        name: 'login',
        component: Login
      }, {
        path: '/blank-page',
        name: 'blank-page',
        component: BlankPage
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
