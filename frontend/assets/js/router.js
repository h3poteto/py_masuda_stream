import Vue from 'vue'
import VueRouter from 'vue-router'
import GlobalHeader from './components/GlobalHeader.vue'
import Stream from './components/Stream.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: GlobalHeader,
    children: [
      {
        path: '',
        component: Stream,
      },
    ],
  },
]

const router = new VueRouter({
  mode: 'history',
  routes: routes,
})


export default router

