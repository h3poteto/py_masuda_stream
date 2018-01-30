import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import router from './router'
import store from './vuex'

Vue.use(ElementUI)

const app = new Vue({
  router,
  store
}).$mount('#app')
