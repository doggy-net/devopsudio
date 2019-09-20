import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import store from '@/store'
// import { getToken } from '@/utils/auth'

// create an axios instance
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000 // request timeout
});

// request interceptor
service.interceptors.request.use(
  config => {
    // do something before request is sent

    if (store.getters.token) {
      // let each request carry token
      // ['X-Token'] is a custom headers key
      // please modify it according to the actual situation
      // config.headers['X-Token'] = getToken()
    }
    return config;
  },
  error => {
    // do something with request error
    // eslint-disable-next-line no-console
    console.log(error) // for debug
    return Promise.reject(error);
  }
)

// response interceptor
service.interceptors.response.use(
  response => {
    const data = response.data;

    // if the custom code is not 200, it is judged as an error.
    if (response.status !== 200 && response.status !== 201 && response.status !== 202 && response.status !== 204) {
      Message({
        message: response.message || 'Error',
        type: 'error',
        duration: 5 * 1000
      });

      // 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
      if (response.code === 50008 || response.code === 50012 || response.code === 50014) {
        // to re-login
        MessageBox.confirm('You have been logged out, you can cancel to stay on this page, or log in again', 'Confirm logout', {
          confirmButtonText: 'Re-Login',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          store.dispatch('user/resetToken').then(() => {
            location.reload();
          })
        });
      }
      return Promise.reject(new Error(response.message || 'Error'));
    } else {
      return data;
    }
  },
  error => {
    // eslint-disable-next-line no-console
    console.log(error); // for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error);
  }
)

export default service
