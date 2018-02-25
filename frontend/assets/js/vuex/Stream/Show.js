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
    userBookmarked: {},
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
    changeAlreadyBookmarked(state, bookmarked) {
      state.userAlreadyBookmarked = bookmarked
    },
    setUserBookmarked(state, response) {
      state.userBookmarked = response
    }
  },
  actions: {
    openEntryDetail({ commit }) {
      commit('changeEntryDetailVisible', true)
    },
    loadEntry({ commit }, id) {
      return new Promise((resolve, reject) => {
        axios
          .get(`/api/masuda/entries/${id}`)
          .then((res) => {
            commit('setEntry', res.data)
            commit('changeLoading', false)
            resolve(res)
          })
          .catch((err) => {
            // eslint-disable-next-line no-console
            console.log(err)
            commit('changeLoading', false)
            reject(err)
          })
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
    addBookmark({ commit }, form) {
      return new Promise((resolve, reject) => {
        axios
          .post('/api/user/bookmark', {
            comment: form.comment,
            url: form.url,
          }, {
            headers: {
              'X-CSRFToken': form.csrf,
            }
          })
          .then((res) => {
            commit('changeAlreadyBookmarked', true)
            commit('setUserBookmarked', res.data)
            resolve(res)
          })
          .catch((err) => {
            reject(err)
          })
      })
    },
    fetchUserBookmark({ commit }, url) {
      axios
        .get(`/api/user/bookmark?url=${url}`)
        .then((res) => {
          commit('changeAlreadyBookmarked', true)
          commit('setUserBookmarked', res.data)
        })
        .catch(() => {
          commit('changeAlreadyBookmarked', false)
        })
    }
  }
}

export default Show
