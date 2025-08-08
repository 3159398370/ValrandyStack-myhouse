import api from '@/utils/api';

export default {
  namespaced: true,
  state: {
    posts: [],
    post: null,
    tags: [],
    loading: false,
    error: null,
  },
  mutations: {
    SET_POSTS(state, posts) {
      state.posts = posts;
    },
    SET_POST(state, post) {
      state.post = post;
    },
    SET_TAGS(state, tags) {
      state.tags = tags;
    },
    SET_LOADING(state, status) {
      state.loading = status;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    async fetchPosts({ commit }, filters = {}) {
      commit('SET_LOADING', true);
      try {
        const response = await api.get('/api/blog/posts/', { params: filters });
        commit('SET_POSTS', response.data);
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch blog posts');
        throw error;
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchPost({ commit }, id) {
      commit('SET_LOADING', true);
      try {
        const response = await api.get(`/api/blog/posts/${id}/`);
        commit('SET_POST', response.data);
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch blog post');
        throw error;
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchTags({ commit }) {
      try {
        const response = await api.get('/api/blog/tags/');
        commit('SET_TAGS', response.data);
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch tags');
        throw error;
      }
    },
  },
  getters: {
    getPostById: (state) => (id) => {
      return state.posts.find((post) => post.id === parseInt(id, 10));
    },
    getPostsByTag: (state) => (tagId) => {
      if (!tagId) return state.posts;
      return state.posts.filter((post) => post.tags.includes(parseInt(tagId, 10)));
    },
  },
};