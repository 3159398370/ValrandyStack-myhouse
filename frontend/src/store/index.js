import Vue from 'vue';
import Vuex from 'vuex';
import projects from './modules/projects';
import blog from './modules/blog';
import repositories from './modules/repositories';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
    error: null,
  },
  mutations: {
    SET_LOADING(state, status) {
      state.loading = status;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
    CLEAR_ERROR(state) {
      state.error = null;
    },
  },
  actions: {
    setLoading({ commit }, status) {
      commit('SET_LOADING', status);
    },
    setError({ commit }, error) {
      commit('SET_ERROR', error);
    },
    clearError({ commit }) {
      commit('CLEAR_ERROR');
    },
  },
  modules: {
    projects,
    blog,
    repositories,
  },
});