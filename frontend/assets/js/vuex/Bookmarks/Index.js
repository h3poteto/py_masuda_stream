import axios from 'axios'

const Index = {
  namespaced: true,
  state: {
    bookmarks: []
  },
  mutations: {
    loadBookmarks(state, data) {
      state.bookmarks = data['feed']['entry']
    }
  },
  actions: {
    fetchBookmarks({ commit }) {
      axios
        .get('/api/user/bookmark/feed')
        .then((res) => {
          commit('loadBookmarks', res.data)
        })
        .catch((err) => {
          // eslint-disable-next-line no-console
          console.log(err)
        })
    }
  },
}

export default Index
