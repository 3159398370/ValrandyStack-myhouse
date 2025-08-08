import api from '@/utils/api';

export default {
  namespaced: true,
  state: {
    projects: [],
    project: null,
    categories: [],
    loading: false,
    error: null,
  },
  mutations: {
    SET_PROJECTS(state, projects) {
      state.projects = projects;
    },
    SET_PROJECT(state, project) {
      state.project = project;
    },
    SET_CATEGORIES(state, categories) {
      state.categories = categories;
    },
    SET_LOADING(state, status) {
      state.loading = status;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    async fetchProjects({ commit }, filters = {}) {
      commit('SET_LOADING', true);
      try {
        const response = await api.get('/api/projects/', { params: filters });
        commit('SET_PROJECTS', response.data);
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch projects');
        throw error;
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchProject({ commit }, id) {
      commit('SET_LOADING', true);
      try {
        const response = await api.get(`/api/projects/${id}/`);
        commit('SET_PROJECT', response.data);
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch project');
        throw error;
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchCategories({ commit }) {
      try {
        const response = await api.get('/api/projects/categories/');
        commit('SET_CATEGORIES', response.data);
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch categories');
        throw error;
      }
    },
  },
  getters: {
    getProjectById: (state) => (id) => state.projects.find((project) => project.id === parseInt(id, 10)),
    getProjectsByCategory: (state) => (categoryId) => {
      if (!categoryId) return state.projects;
      return state.projects.filter((project) => project.category === parseInt(categoryId, 10));
    },
  },
};
