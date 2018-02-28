import axios from 'axios'

const GlobalHeader = {
  namespaced: true,
  state: {
    user: null,
    activeIndex: '1',
  },
  mutations: {
    loadUser(state, data) {
      state.user = data.user
    },
    logoutUser(state) {
      state.user = null
    },
    changeActiveIndex(state, index) {
      state.activeIndex = index
    },
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
    },
    changeActiveIndex({ commit }, index) {
      commit('changeActiveIndex', index)
    },
  },
}

export default GlobalHeader
