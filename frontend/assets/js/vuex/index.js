import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger'

import GlobalHeader from './GlobalHeader'
import Stream from './Stream'
import Bookmarks from './Bookmarks'


Vue.use(Vuex)

const store = new Vuex.Store({
  // eslint-disable-next-line no-undef
  strict: process.env.NODE_ENV !== 'production',
  // eslint-disable-next-line no-undef
  plugins: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : [],
  modules: {
    GlobalHeader,
    Stream,
    Bookmarks,
  },
})

export default store
