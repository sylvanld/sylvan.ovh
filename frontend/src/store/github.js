import http from '@/plugins/http'

export default {
    namespaced: true,

    state: {
        allRepositories: null
    },

    getters: {
        showcasedRepositories(state) {
            if (!state.allRepositories) {
                return [];
            }
            return state.allRepositories;
        }
    },

    mutations: {
        setRepositories(state, repositories) {
            state.allRepositories = repositories;
        }
    },

    actions: {
        loadRepositories({ state, commit }) {
            if (!state.allRepositories) {
                http.get('/github/my/repositories')
                    .then(response => commit('setRepositories', response.data));
            }
        }
    }
}