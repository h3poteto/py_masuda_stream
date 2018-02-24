import Vue from 'vue'
import VueCookie from 'vue-cookie'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css'
import router from './router'
import store from './vuex'


loadProgressBar()

Vue.component('icon', Icon)
Vue.use(VueCookie)
Vue.use(ElementUI)

new Vue({
  router,
  store
}).$mount('#app')
