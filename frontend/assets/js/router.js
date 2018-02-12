import Vue from 'vue'
import VueRouter from 'vue-router'
import GlobalHeader from './components/GlobalHeader.vue'
import StreamIndex from './components/Stream/Index.vue'
import StreamShow from './components/Stream/Show.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: GlobalHeader,
    children: [
      {
        path: '',
        component: StreamIndex,
        children: [
          {
            path: 'entries/:id',
            component: StreamShow,
          }
        ],
      },
    ],
  },
]

const router = new VueRouter({
  mode: 'history',
  routes: routes,
})


export default router

