<template>
  <div class="blog-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">博客</h1>
        <p class="page-description">分享我的技术心得与学习笔记</p>
      </div>
    </div>
    
    <div class="container">
      <div class="blog-layout">
        <!-- 主内容区 -->
        <div class="blog-main">
          <!-- 过滤器 -->
          <div class="blog-filters">
            <div class="search-box">
              <input 
                type="text" 
                v-model="searchQuery" 
                placeholder="搜索文章..." 
                @input="filterPosts"
              />
              <i class="fas fa-search"></i>
            </div>
            
            <div class="view-options">
              <button 
                class="view-btn" 
                :class="{ active: viewMode === 'grid' }"
                @click="viewMode = 'grid'"
              >
                <i class="fas fa-th-large"></i>
              </button>
              <button 
                class="view-btn" 
                :class="{ active: viewMode === 'list' }"
                @click="viewMode = 'list'"
              >
                <i class="fas fa-list"></i>
              </button>
            </div>
          </div>
          
          <!-- 加载状态 -->
          <div v-if="loading" class="loading">
            <div class="spinner"></div>
            <p>正在加载博客文章...</p>
          </div>
          
          <!-- 错误状态 -->
          <div v-else-if="error" class="error">
            <i class="fas fa-exclamation-circle"></i>
            <h3>获取文章失败</h3>
            <p>{{ error }}</p>
            <button class="btn btn-primary" @click="fetchPosts">重试</button>
          </div>
          
          <!-- 无结果状态 -->
          <div v-else-if="filteredPosts.length === 0" class="no-results">
            <i class="fas fa-file-alt"></i>
            <h3>未找到匹配的文章</h3>
            <p v-if="searchQuery">尝试使用不同的搜索关键词或清除筛选条件</p>
            <p v-else>暂无博客文章，敬请期待</p>
            <button v-if="searchQuery" class="btn btn-primary" @click="resetFilters">清除筛选</button>
          </div>
          
          <!-- 文章列表 - 网格视图 -->
          <div v-else-if="viewMode === 'grid'" class="blog-grid">
            <div 
              v-for="post in filteredPosts" 
              :key="post.id"
              class="blog-card"
              @click="goToPost(post.id)"
            >
              <div class="blog-card-image" v-if="post.featured_image">
                <img :src="post.featured_image" :alt="post.title" />
              </div>
              <div class="blog-card-content">
                <div class="blog-card-meta">
                  <span class="blog-date">
                    <i class="far fa-calendar-alt"></i> {{ formatDate(post.published_date) }}
                  </span>
                  <span class="blog-read-time">
                    <i class="far fa-clock"></i> {{ post.read_time }} 分钟阅读
                  </span>
                </div>
                <h3 class="blog-card-title">{{ post.title }}</h3>
                <p class="blog-card-excerpt">{{ post.excerpt }}</p>
                <div class="blog-card-tags">
                  <span 
                    v-for="tag in post.tags" 
                    :key="tag"
                    class="blog-tag"
                    @click.stop="filterByTag(tag)"
                  >
                    {{ tag }}
                  </span>
                </div>
              </div>
            </div>
          </div>
          
          <!-- 文章列表 - 列表视图 -->
          <div v-else class="blog-list">
            <div 
              v-for="post in filteredPosts" 
              :key="post.id"
              class="blog-list-item"
              @click="goToPost(post.id)"
            >
              <div class="blog-list-image" v-if="post.featured_image">
                <img :src="post.featured_image" :alt="post.title" />
              </div>
              <div class="blog-list-content">
                <h3 class="blog-list-title">{{ post.title }}</h3>
                <div class="blog-list-meta">
                  <span class="blog-date">
                    <i class="far fa-calendar-alt"></i> {{ formatDate(post.published_date) }}
                  </span>
                  <span class="blog-read-time">
                    <i class="far fa-clock"></i> {{ post.read_time }} 分钟阅读
                  </span>
                </div>
                <p class="blog-list-excerpt">{{ post.excerpt }}</p>
                <div class="blog-list-tags">
                  <span 
                    v-for="tag in post.tags" 
                    :key="tag"
                    class="blog-tag"
                    @click.stop="filterByTag(tag)"
                  >
                    {{ tag }}
                  </span>
                </div>
              </div>
            </div>
          </div>
          
          <!-- 分页 -->
          <div v-if="filteredPosts.length > 0" class="pagination">
            <button 
              class="pagination-btn" 
              :disabled="currentPage === 1"
              @click="currentPage--"
            >
              <i class="fas fa-chevron-left"></i> 上一页
            </button>
            
            <div class="pagination-info">
              第 {{ currentPage }} 页，共 {{ totalPages }} 页
            </div>
            
            <button 
              class="pagination-btn" 
              :disabled="currentPage === totalPages"
              @click="currentPage++"
            >
              下一页 <i class="fas fa-chevron-right"></i>
            </button>
          </div>
        </div>
        
        <!-- 侧边栏 -->
        <div class="blog-sidebar">
          <!-- 关于博主 -->
          <div class="sidebar-widget about-author">
            <h3 class="widget-title">关于博主</h3>
            <div class="author-info">
              <div class="author-avatar">
                <img src="../assets/images/avatar.svg" alt="博主头像" />
              </div>
              <div class="author-bio">
                <h4>Valrandy·Joseph</h4>
                <p>全栈开发者，热爱技术分享和开源贡献。专注于Vue、Django和数据可视化领域。</p>
              </div>
            </div>
            <div class="author-social">
              <a href="https://github.com/ValrandyStack" target="_blank" rel="noopener noreferrer">
                <i class="fab fa-github"></i>
              </a>
              <a href="https://twitter.com/ValrandyStack" target="_blank" rel="noopener noreferrer">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="https://linkedin.com/in/ValrandyStack" target="_blank" rel="noopener noreferrer">
                <i class="fab fa-linkedin"></i>
              </a>
            </div>
          </div>
          
          <!-- 标签云 -->
          <div class="sidebar-widget tags-cloud">
            <h3 class="widget-title">文章标签</h3>
            <div class="tags-container">
              <span 
                v-for="tag in tags" 
                :key="tag"
                class="blog-tag"
                :class="{ active: selectedTag === tag }"
                @click="filterByTag(tag)"
              >
                {{ tag }}
              </span>
            </div>
          </div>
          
          <!-- 热门文章 -->
          <div class="sidebar-widget popular-posts">
            <h3 class="widget-title">热门文章</h3>
            <div class="popular-posts-list">
              <div 
                v-for="post in popularPosts" 
                :key="post.id"
                class="popular-post-item"
                @click="goToPost(post.id)"
              >
                <div class="popular-post-image" v-if="post.featured_image">
                  <img :src="post.featured_image" :alt="post.title" />
                </div>
                <div class="popular-post-content">
                  <h4 class="popular-post-title">{{ post.title }}</h4>
                  <div class="popular-post-meta">
                    <span class="blog-date">
                      <i class="far fa-calendar-alt"></i> {{ formatDate(post.published_date) }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- 订阅区域 -->
          <div class="sidebar-widget subscribe">
            <h3 class="widget-title">订阅更新</h3>
            <p>输入您的邮箱地址，获取最新文章通知</p>
            <form class="subscribe-form" @submit.prevent="subscribeNewsletter">
              <input 
                type="email" 
                v-model="subscribeEmail" 
                placeholder="您的邮箱地址" 
                required
              />
              <button type="submit" class="btn btn-primary">
                订阅 <i class="fas fa-paper-plane"></i>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Blog',
  data() {
    return {
      searchQuery: '',
      selectedTag: null,
      viewMode: 'grid',
      currentPage: 1,
      postsPerPage: 6,
      subscribeEmail: '',
      filteredPosts: [],
    };
  },
  computed: {
    ...mapState('blog', ['posts', 'tags', 'loading', 'error']),
    
    paginatedPosts() {
      const startIndex = (this.currentPage - 1) * this.postsPerPage;
      const endIndex = startIndex + this.postsPerPage;
      return this.filteredPosts.slice(startIndex, endIndex);
    },
    
    totalPages() {
      return Math.ceil(this.filteredPosts.length / this.postsPerPage);
    },
    
    popularPosts() {
      // 获取阅读量最高的5篇文章
      return [...this.posts]
        .sort((a, b) => b.view_count - a.view_count)
        .slice(0, 5);
    },
  },
  created() {
    this.fetchPosts();
    this.fetchTags();
  },
  methods: {
    ...mapActions('blog', ['fetchPosts', 'fetchTags']),
    
    filterPosts() {
      let filtered = [...this.posts];
      
      // 按标签筛选
      if (this.selectedTag) {
        filtered = filtered.filter(post => post.tags.includes(this.selectedTag));
      }
      
      // 按搜索关键词筛选
      if (this.searchQuery.trim()) {
        const query = this.searchQuery.toLowerCase().trim();
        filtered = filtered.filter(post => 
          post.title.toLowerCase().includes(query) || 
          post.excerpt.toLowerCase().includes(query) ||
          post.content.toLowerCase().includes(query)
        );
      }
      
      this.filteredPosts = filtered;
      this.currentPage = 1; // 重置到第一页
    },
    
    filterByTag(tag) {
      if (this.selectedTag === tag) {
        this.selectedTag = null; // 再次点击同一标签取消筛选
      } else {
        this.selectedTag = tag;
      }
      this.filterPosts();
    },
    
    resetFilters() {
      this.searchQuery = '';
      this.selectedTag = null;
      this.filterPosts();
    },
    
    goToPost(postId) {
      this.$router.push({ name: 'BlogPost', params: { id: postId } });
    },
    
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('zh-CN', options);
    },
    
    subscribeNewsletter() {
      // 这里可以添加订阅逻辑，例如发送API请求
      alert(`感谢订阅！我们将向 ${this.subscribeEmail} 发送更新通知。`);
      this.subscribeEmail = '';
    },
  },
  watch: {
    posts: {
      immediate: true,
      handler(newPosts) {
        if (newPosts.length > 0) {
          this.filteredPosts = [...newPosts];
        }
      },
    },
  },
};
</script>

<style scoped>
.blog-page {
  animation: fadeIn 0.5s ease-in-out;
}

.page-header {
  background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
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

/* 布局 */
.blog-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 40px;
  margin-bottom: 60px;
}

/* 过滤器样式 */
.blog-filters {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.search-box {
  position: relative;
  width: 300px;
}

.search-box input {
  width: 100%;
  padding: 12px 20px;
  padding-right: 40px;
  border-radius: 30px;
  border: 1px solid #ddd;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.search-box input:focus {
  outline: none;
  border-color: #6a11cb;
  box-shadow: 0 0 0 2px rgba(106, 17, 203, 0.1);
}

.search-box i {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #6a11cb;
}

.view-options {
  display: flex;
  gap: 10px;
}

.view-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid #ddd;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-btn:hover {
  border-color: #6a11cb;
  color: #6a11cb;
}

.view-btn.active {
  background-color: #6a11cb;
  color: white;
  border-color: #6a11cb;
}

/* 网格视图 */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  margin-bottom: 40px;
}

.blog-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: white;
  cursor: pointer;
}

.blog-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.blog-card-image {
  height: 200px;
  overflow: hidden;
}

.blog-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.blog-card:hover .blog-card-image img {
  transform: scale(1.1);
}

.blog-card-content {
  padding: 20px;
}

.blog-card-meta {
  display: flex;
  gap: 15px;
  color: #6c757d;
  font-size: 0.85rem;
  margin-bottom: 10px;
}

.blog-card-title {
  font-size: 1.3rem;
  margin-bottom: 10px;
  line-height: 1.4;
  color: #333;
  transition: color 0.3s ease;
}

.blog-card:hover .blog-card-title {
  color: #6a11cb;
}

.blog-card-excerpt {
  color: #6c757d;
  margin-bottom: 15px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.blog-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.blog-tag {
  padding: 4px 10px;
  border-radius: 20px;
  background-color: #f0f0f0;
  color: #6c757d;
  font-size: 0.8rem;
  transition: all 0.3s ease;
  cursor: pointer;
}

.blog-tag:hover, .blog-tag.active {
  background-color: #6a11cb;
  color: white;
}

/* 列表视图 */
.blog-list {
  display: flex;
  flex-direction: column;
  gap: 30px;
  margin-bottom: 40px;
}

.blog-list-item {
  display: flex;
  gap: 30px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: white;
  cursor: pointer;
}

.blog-list-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.blog-list-image {
  flex: 0 0 250px;
  height: 200px;
  overflow: hidden;
}

.blog-list-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.blog-list-item:hover .blog-list-image img {
  transform: scale(1.1);
}

.blog-list-content {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.blog-list-title {
  font-size: 1.5rem;
  margin-bottom: 10px;
  line-height: 1.4;
  color: #333;
  transition: color 0.3s ease;
}

.blog-list-item:hover .blog-list-title {
  color: #6a11cb;
}

.blog-list-meta {
  display: flex;
  gap: 15px;
  color: #6c757d;
  font-size: 0.85rem;
  margin-bottom: 10px;
}

.blog-list-excerpt {
  color: #6c757d;
  margin-bottom: 15px;
  line-height: 1.5;
  flex-grow: 1;
}

.blog-list-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 40px;
}

.pagination-btn {
  padding: 10px 20px;
  border-radius: 30px;
  border: 1px solid #ddd;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.pagination-btn:hover:not(:disabled) {
  border-color: #6a11cb;
  color: #6a11cb;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-info {
  font-size: 0.9rem;
  color: #6c757d;
}

/* 侧边栏 */
.blog-sidebar {
  position: sticky;
  top: 20px;
  align-self: flex-start;
}

.sidebar-widget {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  padding: 25px;
  margin-bottom: 30px;
}

.widget-title {
  font-size: 1.3rem;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #f0f0f0;
  position: relative;
}

.widget-title::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 50px;
  height: 2px;
  background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
}

/* 关于博主 */
.author-info {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
}

.author-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.author-bio h4 {
  margin-bottom: 8px;
  font-size: 1.1rem;
}

.author-bio p {
  color: #6c757d;
  line-height: 1.5;
  font-size: 0.9rem;
}

.author-social {
  display: flex;
  gap: 15px;
  margin-top: 15px;
}

.author-social a {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6c757d;
  transition: all 0.3s ease;
}

.author-social a:hover {
  background-color: #6a11cb;
  color: white;
}

/* 标签云 */
.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

/* 热门文章 */
.popular-posts-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.popular-post-item {
  display: flex;
  gap: 15px;
  cursor: pointer;
}

.popular-post-image {
  flex: 0 0 70px;
  height: 70px;
  border-radius: 5px;
  overflow: hidden;
}

.popular-post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.popular-post-content {
  flex: 1;
}

.popular-post-title {
  font-size: 1rem;
  margin-bottom: 5px;
  line-height: 1.4;
  transition: color 0.3s ease;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.popular-post-item:hover .popular-post-title {
  color: #6a11cb;
}

.popular-post-meta {
  font-size: 0.8rem;
  color: #6c757d;
}

/* 订阅区域 */
.subscribe p {
  color: #6c757d;
  margin-bottom: 15px;
  font-size: 0.9rem;
}

.subscribe-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.subscribe-form input {
  padding: 12px 15px;
  border-radius: 5px;
  border: 1px solid #ddd;
  font-size: 0.9rem;
}

.subscribe-form input:focus {
  outline: none;
  border-color: #6a11cb;
  box-shadow: 0 0 0 2px rgba(106, 17, 203, 0.1);
}

.subscribe-form button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
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
  border: 4px solid rgba(106, 17, 203, 0.2);
  border-top-color: #6a11cb;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error i, .no-results i {
  font-size: 3rem;
  color: #dc3545;
  margin-bottom: 20px;
}

.no-results i {
  color: #6a11cb;
}

.error h3, .no-results h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.error p, .no-results p {
  color: #6c757d;
  margin-bottom: 20px;
  max-width: 500px;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .blog-layout {
    grid-template-columns: 1fr;
  }
  
  .blog-sidebar {
    position: static;
    margin-top: 40px;
  }
  
  .blog-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .blog-grid {
    grid-template-columns: 1fr;
  }
  
  .blog-list-item {
    flex-direction: column;
  }
  
  .blog-list-image {
    flex: 0 0 auto;
    height: 200px;
  }
  
  .search-box {
    width: 100%;
  }
  
  .blog-filters {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }
  
  .view-options {
    align-self: flex-end;
  }
}

@media (max-width: 576px) {
  .page-title {
    font-size: 2rem;
  }
  
  .page-description {
    font-size: 1rem;
  }
  
  .pagination {
    flex-direction: column;
    gap: 15px;
  }
  
  .pagination-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>