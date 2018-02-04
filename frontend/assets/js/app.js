import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'

import router from './router'
import store from './vuex'

Vue.component('icon', Icon)
Vue.use(ElementUI)

new Vue({
  router,
  store
}).$mount('#app')
