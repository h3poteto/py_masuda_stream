import axios from 'axios'

const Stream = {
  namespaced: true,
  state: {
    entries: [
      {
        id: 0,
        title: "",
        summary: "",
        content: "",
        hatena_bookmarkcount: 0,
        posted_at: "",
      }
    ],
    lazyloading: false,
  },
  mutations: {
    loadEntries(state, data) {
      state.entries = data.entries
    },
    changeLazyloading(state, flag) {
      state.lazyloading = flag
    },
    appendEntries(state, data) {
      state.entries = state.entries.concat(data.entries)
    }
  },
  actions: {
    fetchEntries({ commit }) {
      axios
        .get('/api/masuda/entries')
        .then((res) => {
          commit('loadEntries', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    lazyFetchEntries({ commit, state }, before) {
      if (state.lazyloading) {
        return
      }
      commit('changeLazyloading', true)
      axios
        .get(`/api/masuda/entries?before=${before}`)
        .then((res) => {
          commit('appendEntries', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
        .then(() => {
          commit('changeLazyloading', false)
        })
    },

  },
}
export default Stream
