const Show = {
  namespaced: true,
  state: {
    entry: {
      title: '',
    },
    entryDetailVisible: true,
  },
  mutations: {
    changeEntryDetailVisible(state, open) {
      state.entryDetailVisible = open
    }
  },
  actions: {
    openEntryDetail({ commit }) {
      commit('changeEntryDetailVisible', true)
    }
  }
}

export default Show
