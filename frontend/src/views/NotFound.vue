<template>
  <div class="not-found-page">
    <div class="not-found-container">
      <div class="error-code">404</div>
      <h1 class="error-title">页面未找到</h1>
      <p class="error-message">抱歉，您访问的页面不存在或已被移除。</p>
      <div class="action-buttons">
        <router-link to="/" class="btn btn-primary">
          <i class="fas fa-home"></i> 返回首页
        </router-link>
        <button @click="goBack" class="btn btn-outline">
          <i class="fas fa-arrow-left"></i> 返回上一页
        </button>
      </div>
      
      <div class="search-section">
        <p>或者您可以尝试搜索：</p>
        <div class="search-form">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索内容..." 
            @keyup.enter="searchSite"
          />
          <button @click="searchSite" class="search-btn">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
    </div>
    
    <div class="suggestions">
      <h2>您可能感兴趣的内容</h2>
      <div class="suggestion-links">
        <router-link to="/projects" class="suggestion-link">
          <i class="fas fa-project-diagram"></i>
          <span>浏览作品集</span>
        </router-link>
        <router-link to="/repositories" class="suggestion-link">
          <i class="fas fa-code-branch"></i>
          <span>查看代码仓库</span>
        </router-link>
        <router-link to="/blog" class="suggestion-link">
          <i class="fas fa-blog"></i>
          <span>阅读博客文章</span>
        </router-link>
        <router-link to="/contact" class="suggestion-link">
          <i class="fas fa-envelope"></i>
          <span>联系我</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  data() {
    return {
      searchQuery: ''
    };
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    searchSite() {
      if (this.searchQuery.trim()) {
        // 这里可以实现站内搜索功能
        // 暂时重定向到博客页面并带上搜索参数
        this.$router.push({
          path: '/blog',
          query: { search: this.searchQuery }
        });
      }
    }
  },
  metaInfo() {
    return {
      title: '404 - 页面未找到 | ValrandyStack个人网站'
    };
  }
};
</script>

<style scoped>
.not-found-page {
  min-height: calc(100vh - 200px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background-color: #f8f9fa;
  animation: fadeIn 0.5s ease-in-out;
}

.not-found-container {
  max-width: 600px;
  width: 100%;
  text-align: center;
  background-color: white;
  border-radius: 10px;
  padding: 40px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  margin-bottom: 40px;
}

.error-code {
  font-size: 8rem;
  font-weight: 700;
  color: #4b6cb7;
  line-height: 1;
  margin-bottom: 20px;
  text-shadow: 2px 2px 0 #182848, 4px 4px 0 rgba(0, 0, 0, 0.1);
  animation: pulse 2s infinite;
}

.error-title {
  font-size: 2rem;
  color: #182848;
  margin-bottom: 15px;
}

.error-message {
  font-size: 1.1rem;
  color: #6c757d;
  margin-bottom: 30px;
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 30px;
}

.btn {
  padding: 12px 25px;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  text-decoration: none;
}

.btn-primary {
  background-color: #4b6cb7;
  color: white;
  border: none;
}

.btn-primary:hover {
  background-color: #3a5a9f;
  transform: translateY(-2px);
}

.btn-outline {
  background-color: transparent;
  color: #4b6cb7;
  border: 2px solid #4b6cb7;
}

.btn-outline:hover {
  background-color: #4b6cb7;
  color: white;
  transform: translateY(-2px);
}

.search-section {
  margin-top: 20px;
}

.search-section p {
  color: #6c757d;
  margin-bottom: 15px;
}

.search-form {
  display: flex;
  max-width: 400px;
  margin: 0 auto;
}

.search-form input {
  flex-grow: 1;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-right: none;
  border-radius: 5px 0 0 5px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.search-form input:focus {
  outline: none;
  border-color: #4b6cb7;
}

.search-btn {
  background-color: #4b6cb7;
  color: white;
  border: none;
  padding: 0 20px;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-btn:hover {
  background-color: #3a5a9f;
}

.suggestions {
  max-width: 800px;
  width: 100%;
}

.suggestions h2 {
  text-align: center;
  font-size: 1.5rem;
  color: #182848;
  margin-bottom: 25px;
}

.suggestion-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.suggestion-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 25px 15px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  text-decoration: none;
  color: #182848;
  transition: all 0.3s ease;
}

.suggestion-link i {
  font-size: 2rem;
  color: #4b6cb7;
  margin-bottom: 15px;
}

.suggestion-link span {
  font-weight: 600;
}

.suggestion-link:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  color: #4b6cb7;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

/* 响应式调整 */
@media (max-width: 768px) {
  .error-code {
    font-size: 6rem;
  }
  
  .error-title {
    font-size: 1.8rem;
  }
  
  .action-buttons {
    flex-direction: column;
    gap: 10px;
  }
  
  .btn {
    width: 100%;
    justify-content: center;
  }
  
  .suggestion-links {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
}

@media (max-width: 480px) {
  .not-found-container {
    padding: 30px 20px;
  }
  
  .error-code {
    font-size: 5rem;
  }
  
  .suggestion-links {
    grid-template-columns: 1fr 1fr;
  }
}
</style>