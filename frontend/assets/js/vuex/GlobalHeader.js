import axios from 'axios'

const GlobalHeader = {
  namespaced: true,
  state: {
    user: null,
  },
  mutations: {
    loadUser(state, data) {
      state.user = data.user
    }
  },
  actions: {
    fetchUser({ commit }) {
      axios
        .get('/api/user/my')
        .then((res) => {
          commit('loadUser', res.data)
        })
        .catch((err) => {
          // eslint-disable-next-line no-console
          console.log(err)
        })
    }
  },
}

export default GlobalHeader
