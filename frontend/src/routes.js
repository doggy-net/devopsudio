import Login from './views/Login.vue'
import Navbar from './views/Navbar.vue'
import Admin from './views/Admin.vue'
import Development from './views/Development.vue'
import Operations from './views/Operations.vue'
import Network from './views/Network.vue'
import App from './views/App.vue'
import auth from './auth'

// const afterAuth = (_to, from, next) => {
//   console.log(from, _to);
//   if (auth.user.authenticated) {
//     next(from.path)
//   } else {
//     next()
//   }
// }

// Routes
const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
    // beforeEnter: afterAuth
  },
  {
    path: '/',
    name: 'root',
    component: Navbar,
    meta: { requiresAuth: true },
    activate: function () {
      this.$nextTick(function () {
        // => 'DOM loaded and ready'
        alert('test')
      })
    },
    children: [
      {
        path: '',
        name: 'operations',
        component: Operations,
        meta: { requiresAuth: true },
        activate: function () {
          this.$nextTick(function () {
            // => 'DOM loaded and ready'
            alert('test')
          })
        },
        children: [{
            path: 'network',
            name: 'network',
            component: Network,
          },
          {
            path: 'app',
            name: 'app',
            component: App,
          }
        ]
      },
      {
        path: '/ops',
        redirect: { name: 'operations' }
      },
      {
        path: '/dev',
        name: 'development',
        component: Development,
        meta: { requiresAuth: true },
        activate: function () {
          this.$nextTick(function () {
            // => 'DOM loaded and ready'
            alert('test')
          })
        },
        children: [{
            path: 'network',
            name: 'network',
            component: Network,
          },
          {
            path: 'app',
            name: 'app',
            component: App,
          }
        ]
      },
      {
        path: '/admin',
        name: 'admin',
        component: Admin,
        meta: { requiresAuth: true },
        activate: function () {
          this.$nextTick(function () {
            // => 'DOM loaded and ready'
            alert('test')
          })
        },
        children: [{
          path: 'network',
          name: 'network',
          component: Network,
          },
          {
            path: 'app',
            name: 'app',
            component: App
          }
        ]
      }
    ]
  },
  {
    // not found handler
    path: '*',
    redirect: '/'
  }
]

export default routes
