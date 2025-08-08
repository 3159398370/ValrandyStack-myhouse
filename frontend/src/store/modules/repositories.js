import api from '@/utils/api';

export default {
  namespaced: true,
  state: {
    repositories: [],
    loading: false,
    error: null,
  },
  mutations: {
    SET_REPOSITORIES(state, repositories) {
      state.repositories = repositories;
    },
    SET_LOADING(state, status) {
      state.loading = status;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    async fetchRepositories({ commit }) {
      commit('SET_LOADING', true);
      try {
        // 直接调用GitHub API获取用户仓库
        const headers = {
          'Accept': 'application/vnd.github.v3+json',
          'User-Agent': 'ValrandyStack-Portfolio'
        };
        
        const response = await fetch('https://api.github.com/users/3159398370/repos?sort=updated&per_page=100&type=public', {
          headers
        });
        
        if (!response.ok) {
          if (response.status === 403) {
            const resetTime = response.headers.get('X-RateLimit-Reset');
            const resetDate = resetTime ? new Date(resetTime * 1000).toLocaleTimeString() : '未知';
            throw new Error(`GitHub API速率限制，请在 ${resetDate} 后重试`);
          }
          throw new Error(`GitHub API请求失败: ${response.status}`);
        }
        
        const data = await response.json();
        commit('SET_REPOSITORIES', data);
        return data;
      } catch (error) {
        commit('SET_ERROR', error.message || 'Failed to fetch repositories');
        throw error;
      } finally {
        commit('SET_LOADING', false);
      }
    },
  },
  getters: {
    getRepositoriesByLanguage: (state) => (language) => {
      if (!language) return state.repositories;
      return state.repositories.filter((repo) => repo.language === language);
    },
    getTopRepositories: (state) => (count = 5) => {
      return [...state.repositories]
        .sort((a, b) => b.stargazers_count - a.stargazers_count)
        .slice(0, count);
    },
  },
};