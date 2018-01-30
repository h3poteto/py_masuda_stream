import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger'

import Stream from './Stream'

Vue.use(Vuex)

const store = new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  plugins: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : [],
  modules: {
    Stream,
  },
})

export default store
