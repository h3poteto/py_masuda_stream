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
    bookmarks: [],
    entryDetailVisible: true,
    loading: true,
    userAlreadyBookmarked: false,
  },
  mutations: {
    changeEntryDetailVisible(state, open) {
      state.entryDetailVisible = open
    },
    setEntry(state, response) {
      state.entry = response.entry
    },
    setBookmarks(state, response) {
      state.bookmarks = response.bookmarks
    },
    cleanEntry(state) {
      state.entry = {
        title: '',
        anond_content_html: '',
        hatena_bookmarkcount: 0,
        posted_at: '',
      }
    },
    cleanBookmarks(state) {
      state.bookmarks = []
    },
    changeLoading(state, loading) {
      state.loading = loading
    },
    changeBookmarked(state, bookmarked) {
      state.bookmarked = bookmarked
    }
  },
  actions: {
    openEntryDetail({ commit }) {
      commit('changeEntryDetailVisible', true)
    },
    loadEntry({ commit }, id) {
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
    loadBookmarks({ commit }, id) {
      axios
        .get(`/api/masuda/entries/${id}/bookmarks`)
        .then((res) => {
          commit('setBookmarks', res.data)
        })
        .catch((err) => {
          // eslint-disable-next-line no-console
          console.log(err)
        })
    },
    cleanup({ commit }) {
      commit('cleanEntry', {})
      commit('cleanBookmarks', {})
    },
    startLoading({ commit }) {
      commit('changeLoading', true)
    },
    stopLoading({ commit }) {
      commit('changeLoading', false)
    },
    addBookmark({ commit }, comment) {
      return new Promise((resolve, reject) => {
        axios
          .post('/api/user/bookmark', {
            comment: comment,
          })
          .then((res) => {
            commit('changeBookmakred', true)
            resolve(res)
          })
          .catch((err) => {
            reject(err)
          })
      })
    }
  }
}

export default Show
