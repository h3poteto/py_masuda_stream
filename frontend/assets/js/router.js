import Vue from 'vue'
import VueRouter from 'vue-router'
import GlobalHeader from './components/GlobalHeader.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: GlobalHeader,
  },
]

const router = new VueRouter({
  mode: 'history',
  routes: routes,
})


export default router

