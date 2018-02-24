import axios from 'axios'

const GlobalHeader = {
  namespaced: true,
  state: {
    user: null,
  },
  mutations: {
    loadUser(state, data) {
      state.user = data.user
    },
    logoutUser(state) {
      state.user = null
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
    },
    logout({ commit }, csrf) {
      return new Promise((resolve, reject) => {
        axios
          .post('/accounts/logout/', null, {
            headers: {
              'X-CSRFToken': csrf,
            }
          })
          .then((res) => {
            commit('logoutUser', res.data)
            resolve(res)
          })
          .catch((err) => {
            reject(err)
          })
      })
    }
  },
}

export default GlobalHeader
