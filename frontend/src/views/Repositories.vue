<template>
  <div class="repositories-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">代码仓库</h1>
        <p class="page-description">我的GitHub开源项目展示</p>
      </div>
    </div>
    
    <div class="container">
      <!-- 过滤器 -->
      <div class="filters">
        <div class="filter-group">
          <label>编程语言：</label>
          <div class="filter-options">
            <button 
              class="filter-btn" 
              :class="{ active: selectedLanguage === null }"
              @click="filterByLanguage(null)"
            >
              全部
            </button>
            <button 
              v-for="language in languages" 
              :key="language"
              class="filter-btn" 
              :class="{ active: selectedLanguage === language }"
              @click="filterByLanguage(language)"
            >
              {{ language }}
            </button>
          </div>
        </div>
        
        <div class="sort-group">
          <label>排序：</label>
          <select v-model="sortBy" @change="sortRepositories">
            <option value="stars">星标数量</option>
            <option value="updated">最近更新</option>
            <option value="name">名称</option>
            <option value="created">创建时间</option>
          </select>
        </div>
      </div>
      
      <!-- 仓库列表 -->
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>正在从GitHub获取仓库数据...</p>
      </div>
      
      <div v-else-if="error" class="error">
        <i class="fas fa-exclamation-circle"></i>
        <h3>获取仓库失败</h3>
        <p>{{ error }}</p>
        <button class="btn btn-primary" @click="fetchRepositories">重试</button>
      </div>
      
      <div v-else-if="filteredRepositories.length === 0" class="no-results">
        <i class="fab fa-github"></i>
        <h3>未找到匹配的仓库</h3>
        <p>尝试选择不同的编程语言或排序方式</p>
        <button class="btn btn-primary" @click="resetFilters">重置筛选器</button>
      </div>
      
      <div v-else class="repositories-grid">
        <div 
          v-for="repo in filteredRepositories" 
          :key="repo.id"
          class="repository-card"
        >
          <div class="repository-header">
            <h3 class="repository-name">
              <a :href="repo.html_url" target="_blank" rel="noopener noreferrer">
                {{ repo.name }}
              </a>
            </h3>
            <div class="repository-visibility" :class="repo.private ? 'private' : 'public'">
              {{ repo.private ? '私有' : '公开' }}
            </div>
          </div>
          
          <p class="repository-description" v-if="repo.description">
            {{ repo.description }}
          </p>
          <p class="repository-description no-description" v-else>
            暂无描述
          </p>
          
          <div class="repository-meta">
            <div class="meta-item" v-if="repo.language">
              <span class="language-color" :style="{ backgroundColor: getLanguageColor(repo.language) }"></span>
              <span>{{ repo.language }}</span>
            </div>
            
            <div class="meta-item" v-if="repo.stargazers_count > 0">
              <i class="fas fa-star"></i>
              <span>{{ repo.stargazers_count }}</span>
            </div>
            
            <div class="meta-item" v-if="repo.forks_count > 0">
              <i class="fas fa-code-branch"></i>
              <span>{{ repo.forks_count }}</span>
            </div>
            
            <div class="meta-item">
              <i class="far fa-clock"></i>
              <span>{{ formatDate(repo.updated_at) }}</span>
            </div>
          </div>
          
          <div class="repository-footer">
            <a :href="repo.html_url" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
              <i class="fab fa-github"></i> 查看仓库
            </a>
            <a v-if="hasPages(repo)" :href="getPageUrl(repo)" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
              <i class="fas fa-globe"></i> 项目页面
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Repositories',
  data() {
    return {
      selectedLanguage: null,
      sortBy: 'stars',
      filteredRepositories: [],
      languageColors: {
        JavaScript: '#f1e05a',
        TypeScript: '#2b7489',
        Python: '#3572A5',
        Java: '#b07219',
        HTML: '#e34c26',
        CSS: '#563d7c',
        Vue: '#41b883',
        PHP: '#4F5D95',
        Ruby: '#701516',
        Go: '#00ADD8',
        C: '#555555',
        'C++': '#f34b7d',
        'C#': '#178600',
        Swift: '#ffac45',
        Kotlin: '#F18E33',
        Rust: '#dea584',
      },
    };
  },
  computed: {
    ...mapState('repositories', ['repositories', 'loading', 'error']),
    
    languages() {
      // 获取所有仓库中使用的编程语言，去重
      const languages = this.repositories
        .map(repo => repo.language)
        .filter(lang => lang !== null && lang !== undefined);
      
      return [...new Set(languages)].sort();
    },
  },
  created() {
    this.fetchRepositories();
  },
  methods: {
    ...mapActions('repositories', ['fetchRepositories']),
    
    filterByLanguage(language) {
      this.selectedLanguage = language;
      this.applyFilters();
    },
    
    sortRepositories() {
      this.applyFilters();
    },
    
    resetFilters() {
      this.selectedLanguage = null;
      this.sortBy = 'stars';
      this.applyFilters();
    },
    
    applyFilters() {
      // 先按语言筛选
      let filtered = this.selectedLanguage === null
        ? [...this.repositories]
        : this.repositories.filter(repo => repo.language === this.selectedLanguage);
      
      // 再排序
      filtered.sort((a, b) => {
        switch (this.sortBy) {
          case 'stars':
            return b.stargazers_count - a.stargazers_count;
          case 'updated':
            return new Date(b.updated_at) - new Date(a.updated_at);
          case 'name':
            return a.name.localeCompare(b.name);
          case 'created':
            return new Date(b.created_at) - new Date(a.created_at);
          default:
            return 0;
        }
      });
      
      this.filteredRepositories = filtered;
    },
    
    getLanguageColor(language) {
      return this.languageColors[language] || '#6c757d';
    },
    
    formatDate(dateString) {
      const date = new Date(dateString);
      const now = new Date();
      const diffTime = Math.abs(now - date);
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
      
      if (diffDays < 1) {
        return '今天';
      } else if (diffDays < 2) {
        return '昨天';
      } else if (diffDays < 7) {
        return `${diffDays}天前`;
      } else if (diffDays < 30) {
        const weeks = Math.floor(diffDays / 7);
        return `${weeks}周前`;
      } else if (diffDays < 365) {
        const months = Math.floor(diffDays / 30);
        return `${months}个月前`;
      } else {
        const years = Math.floor(diffDays / 365);
        return `${years}年前`;
      }
    },
    
    hasPages(repo) {
      return repo.has_pages || repo.homepage;
    },
    
    getPageUrl(repo) {
      if (repo.homepage) {
        return repo.homepage;
      }
      
      if (repo.has_pages) {
        const username = repo.owner.login;
        return `https://${username}.github.io/${repo.name}`;
      }
      
      return null;
    },
  },
  watch: {
    repositories: {
      immediate: true,
      handler(newRepositories) {
        if (newRepositories.length > 0) {
          this.applyFilters();
        }
      },
    },
  },
};
</script>

<style scoped>
.repositories-page {
  animation: fadeIn 0.5s ease-in-out;
}

.page-header {
  background: linear-gradient(135deg, #24292e 0%, #1a1e22 100%);
  color: white;
  padding: 60px 0;
  margin-bottom: 40px;
}

.page-title {
  font-size: 2.5rem;
  margin-bottom: 15px;
}

.page-description {
  font-size: 1.2rem;
  max-width: 700px;
  opacity: 0.9;
}

/* 过滤器样式 */
.filters {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 20px;
}

.filter-group, .sort-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-group label, .sort-group label {
  font-weight: 600;
  margin-right: 10px;
}

.filter-options {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 8px 16px;
  border-radius: 30px;
  border: 1px solid #ddd;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.filter-btn:hover {
  border-color: #24292e;
  color: #24292e;
}

.filter-btn.active {
  background-color: #24292e;
  color: white;
  border-color: #24292e;
}

.sort-group select {
  padding: 8px 16px;
  border-radius: 30px;
  border: 1px solid #ddd;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23333' d='M6 8.825L1.175 4 2.05 3.125 6 7.075 9.95 3.125 10.825 4 6 8.825z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  padding-right: 40px;
}

.sort-group select:focus {
  outline: none;
  border-color: #24292e;
}

/* 仓库网格样式 */
.repositories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.repository-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: white;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.repository-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.repository-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 15px;
}

.repository-name {
  margin: 0;
  font-size: 1.4rem;
  line-height: 1.3;
}

.repository-name a {
  color: #24292e;
  transition: color 0.3s ease;
}

.repository-name a:hover {
  color: #0366d6;
}

.repository-visibility {
  padding: 3px 8px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.repository-visibility.public {
  background-color: #e6f6e6;
  color: #28a745;
}

.repository-visibility.private {
  background-color: #ffeef0;
  color: #d73a49;
}

.repository-description {
  margin-bottom: 20px;
  color: #586069;
  line-height: 1.5;
  flex-grow: 1;
}

.repository-description.no-description {
  color: #a0a0a0;
  font-style: italic;
}

.repository-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 20px;
  color: #586069;
  font-size: 0.9rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 5px;
}

.language-color {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
}

.repository-footer {
  display: flex;
  gap: 10px;
}

/* 加载和错误状态 */
.loading, .error, .no-results {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 0;
  text-align: center;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(36, 41, 46, 0.2);
  border-top-color: #24292e;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error i, .no-results i {
  font-size: 3rem;
  color: #d73a49;
  margin-bottom: 20px;
}

.no-results i {
  color: #24292e;
}

.error h3, .no-results h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.error p, .no-results p {
  color: #586069;
  margin-bottom: 20px;
  max-width: 500px;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .repositories-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
  
  .filters {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .sort-group {
    width: 100%;
  }
  
  .sort-group select {
    width: 100%;
  }
}

@media (max-width: 576px) {
  .page-title {
    font-size: 2rem;
  }
  
  .page-description {
    font-size: 1rem;
  }
  
  .repositories-grid {
    grid-template-columns: 1fr;
  }
  
  .repository-footer {
    flex-direction: column;
  }
  
  .repository-footer a {
    width: 100%;
    text-align: center;
  }
}
</style>