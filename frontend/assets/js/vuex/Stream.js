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
      }
    ],
  },
  mutations: {
    loadEntries(state, data) {
      state.entries = data.entries
    }
  },
  actions: {
    fetchEntries({ commit }) {
      axios
        .get("/api/masuda/entries")
        .then((res) => {
          commit('loadEntries', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
}
export default Stream
