<template>
  <div class="projects-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">作品集</h1>
        <p class="page-description">探索我的项目作品，包括Web应用、数据分析和可视化项目</p>
      </div>
    </div>
    
    <div class="container">
      <!-- 过滤器 -->
      <div class="filters">
        <div class="filter-group">
          <label>分类：</label>
          <div class="filter-options">
            <button 
              class="filter-btn" 
              :class="{ active: selectedCategory === null }"
              @click="selectCategory(null)"
            >
              全部
            </button>
            <button 
              v-for="category in categories" 
              :key="category.id"
              class="filter-btn" 
              :class="{ active: selectedCategory === category.id }"
              @click="selectCategory(category.id)"
            >
              {{ category.name }}
            </button>
          </div>
        </div>
        
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索项目..."
            @input="filterProjects"
          />
          <i class="fas fa-search"></i>
        </div>
      </div>
      
      <!-- 项目列表 -->
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>加载中...</p>
      </div>
      
      <div v-else-if="filteredProjects.length === 0" class="no-results">
        <i class="fas fa-search"></i>
        <h3>未找到匹配的项目</h3>
        <p>尝试使用不同的搜索词或筛选条件</p>
        <button class="btn btn-primary" @click="resetFilters">重置筛选器</button>
      </div>
      
      <div v-else class="projects-grid">
        <div 
          v-for="project in filteredProjects" 
          :key="project.id"
          class="project-card"
        >
          <div class="project-image">
            <img :src="project.thumbnail" :alt="project.title" />
            <div class="project-overlay">
              <router-link :to="`/projects/${project.id}`" class="view-project">
                <i class="fas fa-eye"></i> 查看详情
              </router-link>
              <a v-if="project.demo_url" :href="project.demo_url" target="_blank" rel="noopener noreferrer" class="demo-link">
                <i class="fas fa-external-link-alt"></i> 在线演示
              </a>
            </div>
          </div>
          
          <div class="project-info">
            <div class="project-category" :style="{ backgroundColor: getCategoryColor(project.category) }">
              {{ getCategoryName(project.category) }}
            </div>
            <h3 class="project-title">{{ project.title }}</h3>
            <p class="project-description">{{ project.short_description }}</p>
            
            <div class="project-meta">
              <div class="project-date">
                <i class="far fa-calendar-alt"></i> {{ formatDate(project.created_at) }}
              </div>
              <div class="project-tags">
                <span v-for="(tag, index) in project.tags" :key="index" class="tag">{{ tag }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import project1Image from '@/assets/images/project1.svg';
import project2Image from '@/assets/images/project2.svg';
import project3Image from '@/assets/images/project3.svg';
import project4Image from '@/assets/images/project4.svg';

export default {
  name: 'Projects',
  data() {
    return {
      selectedCategory: null,
      searchQuery: '',
      filteredProjects: [],
      categoryColors: {
        1: '#42b983', // Web开发
        2: '#3498db', // 数据分析
        3: '#9b59b6', // 机器学习
        4: '#e74c3c', // 移动应用
        5: '#f39c12', // 其他
      },
      // 本地项目数据，当后端不可用时使用
      localProjects: [
        {
          id: 1,
          title: '智能数据分析平台',
          short_description: '基于Vue和Django的数据分析平台，支持多种数据源和可视化方式。',
          thumbnail: project1Image,
          tags: ['Vue', 'Django', 'ECharts', 'Pandas'],
          category: 1,
          created_at: '2024-01-15',
          demo_url: '#',
        },
        {
          id: 2,
          title: '个人博客系统',
          short_description: '一个功能完善的博客系统，支持Markdown编辑、标签分类和评论功能。',
          thumbnail: project2Image,
          tags: ['Vue', 'Django REST', 'MySQL', 'Markdown'],
          category: 1,
          created_at: '2024-01-10',
          demo_url: '#',
        },
        {
          id: 3,
          title: '电商数据爬虫',
          short_description: '使用Scrapy开发的电商网站数据采集工具，支持多线程和代理IP。',
          thumbnail: project3Image,
          tags: ['Python', 'Scrapy', 'MongoDB', 'Data Mining'],
          category: 2,
          created_at: '2024-01-05',
          demo_url: '#',
        },
        {
          id: 4,
          title: '小米家具官网复刻',
          short_description: '高度还原小米家具官网的设计和交互，实现响应式布局和现代化UI。',
          thumbnail: project4Image,
          tags: ['Vue', 'Element UI', '响应式设计', 'CSS3'],
          category: 1,
          created_at: '2024-01-01',
          demo_url: '#',
        },
      ],
      localCategories: [
        { id: 1, name: 'Web开发' },
        { id: 2, name: '数据分析' },
        { id: 3, name: '机器学习' },
        { id: 4, name: '移动应用' },
        { id: 5, name: '其他' },
      ],
    };
  },
  computed: {
    ...mapState('projects', ['loading', 'error']),
    // 使用本地数据替代Vuex中的数据
    projects() {
      return this.localProjects;
    },
    categories() {
      return this.localCategories;
    },
  },
  created() {
    // 注释掉API调用，使用本地数据
    // this.fetchProjects();
    // this.fetchCategories();
    this.filterProjects();
  },
  methods: {
    ...mapActions('projects', ['fetchProjects', 'fetchCategories']),
    
    selectCategory(categoryId) {
      this.selectedCategory = categoryId;
      this.filterProjects();
    },
    
    filterProjects() {
      // 先按分类筛选
      let filtered = this.selectedCategory === null
        ? [...this.projects]
        : this.projects.filter(project => project.category === this.selectedCategory);
      
      // 再按搜索词筛选
      if (this.searchQuery.trim() !== '') {
        const query = this.searchQuery.toLowerCase();
        filtered = filtered.filter(project => {
          return (
            project.title.toLowerCase().includes(query) ||
            project.short_description.toLowerCase().includes(query) ||
            project.tags.some(tag => tag.toLowerCase().includes(query))
          );
        });
      }
      
      this.filteredProjects = filtered;
    },
    
    resetFilters() {
      this.selectedCategory = null;
      this.searchQuery = '';
      this.filterProjects();
    },
    
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat.id === categoryId);
      return category ? category.name : '未分类';
    },
    
    getCategoryColor(categoryId) {
      return this.categoryColors[categoryId] || '#6c757d';
    },
    
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      });
    },
  },
  watch: {
    projects: {
      immediate: true,
      handler(newProjects) {
        if (newProjects.length > 0) {
          this.filterProjects();
        }
      },
    },
  },
};
</script>

<style scoped>
.projects-page {
  animation: fadeIn 0.5s ease-in-out;
}

.page-header {
  background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
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

.filter-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-group label {
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
  border-color: #42b983;
  color: #42b983;
}

.filter-btn.active {
  background-color: #42b983;
  color: white;
  border-color: #42b983;
}

.search-box {
  position: relative;
  width: 100%;
  max-width: 300px;
}

.search-box input {
  width: 100%;
  padding: 10px 15px 10px 40px;
  border-radius: 30px;
  border: 1px solid #ddd;
  font-size: 0.9rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.search-box input:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2);
  outline: none;
}

.search-box i {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #6c757d;
}

/* 项目网格样式 */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.project-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: white;
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.project-image {
  height: 200px;
  position: relative;
  overflow: hidden;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-card:hover .project-image img {
  transform: scale(1.05);
}

.project-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 15px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-card:hover .project-overlay {
  opacity: 1;
}

.view-project, .demo-link {
  padding: 8px 16px;
  border-radius: 4px;
  color: white;
  font-weight: 600;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.view-project {
  background-color: #42b983;
}

.view-project:hover {
  background-color: #3aa876;
}

.demo-link {
  background-color: #3498db;
}

.demo-link:hover {
  background-color: #2980b9;
}

.project-info {
  padding: 20px;
  position: relative;
}

.project-category {
  position: absolute;
  top: -15px;
  left: 20px;
  padding: 5px 15px;
  border-radius: 20px;
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
}

.project-title {
  margin: 15px 0 10px;
  font-size: 1.4rem;
}

.project-description {
  color: #6c757d;
  margin-bottom: 15px;
  line-height: 1.5;
}

.project-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #eee;
  padding-top: 15px;
  flex-wrap: wrap;
  gap: 10px;
}

.project-date {
  color: #6c757d;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 5px;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.tag {
  padding: 3px 8px;
  background-color: #f8f9fa;
  border-radius: 4px;
  font-size: 0.8rem;
  color: #495057;
}

/* 加载和无结果状态 */
.loading, .no-results {
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
  border: 4px solid rgba(66, 185, 131, 0.2);
  border-top-color: #42b983;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.no-results i {
  font-size: 3rem;
  color: #6c757d;
  margin-bottom: 20px;
}

.no-results h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.no-results p {
  color: #6c757d;
  margin-bottom: 20px;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .projects-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
  
  .filters {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .search-box {
    max-width: 100%;
  }
}

@media (max-width: 576px) {
  .page-title {
    font-size: 2rem;
  }
  
  .page-description {
    font-size: 1rem;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>