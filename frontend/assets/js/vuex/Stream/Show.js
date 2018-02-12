import axios from 'axios'

const Show = {
  namespaced: true,
  state: {
    entry: {
      title: '',
      anond_content_html: '',
      hatena_bookmarkcount: 0,
      posted_at: '',
    },
    entryDetailVisible: true,
    loading: true,
  },
  mutations: {
    changeEntryDetailVisible(state, open) {
      state.entryDetailVisible = open
    },
    setEntry(state, response) {
      state.entry = response.entry
    },
    cleanEntry(state) {
      state.entry = {
        title: '',
        anond_content_html: '',
        hatena_bookmarkcount: 0,
        posted_at: '',
      }
    },
    changeLoading(state, loading) {
      state.loading = loading
    }
  },
  actions: {
    openEntryDetail({ commit }) {
      commit('changeEntryDetailVisible', true)
    },
    load({ commit }, id) {
      axios
        .get(`/api/masuda/entries/${id}`)
        .then((res) => {
          commit('setEntry', res.data)
          commit('changeLoading', false)
        })
        .catch((err) => {
          // eslint-disable-next-line no-console
          console.log(err)
          commit('changeLoading', false)
        })
    },
    cleanup({ commit }) {
      commit('cleanEntry', {})
    },
    startLoading({ commit }) {
      commit('changeLoading', true)
    },
    stopLoading({ commit }) {
      commit('changeLoading', false)
    }
  }
}

export default Show
