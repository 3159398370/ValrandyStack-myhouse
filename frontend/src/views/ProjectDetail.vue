<template>
  <div class="project-detail">
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>加载中...</p>
    </div>
    
    <div v-else-if="error" class="error">
      <i class="fas fa-exclamation-circle"></i>
      <h3>加载失败</h3>
      <p>{{ error }}</p>
      <router-link to="/projects" class="btn btn-primary">返回项目列表</router-link>
    </div>
    
    <div v-else-if="!project" class="not-found">
      <i class="fas fa-search"></i>
      <h3>项目未找到</h3>
      <p>您请求的项目不存在或已被删除</p>
      <router-link to="/projects" class="btn btn-primary">返回项目列表</router-link>
    </div>
    
    <div v-else class="project-content">
      <!-- 项目头部 -->
      <div class="project-header" :style="{ backgroundImage: `url(${project.banner_image})` }">
        <div class="overlay"></div>
        <div class="container">
          <div class="project-header-content">
            <div class="project-category" :style="{ backgroundColor: getCategoryColor(project.category) }">
              {{ getCategoryName(project.category) }}
            </div>
            <h1 class="project-title">{{ project.title }}</h1>
            <p class="project-description">{{ project.short_description }}</p>
            
            <div class="project-meta">
              <div class="meta-item">
                <i class="far fa-calendar-alt"></i>
                <span>{{ formatDate(project.created_at) }}</span>
              </div>
              <div class="meta-item" v-if="project.client">
                <i class="far fa-building"></i>
                <span>{{ project.client }}</span>
              </div>
              <div class="meta-item" v-if="project.duration">
                <i class="far fa-clock"></i>
                <span>{{ project.duration }}</span>
              </div>
            </div>
            
            <div class="project-actions">
              <a v-if="project.demo_url" :href="project.demo_url" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                <i class="fas fa-external-link-alt"></i> 在线演示
              </a>
              <a v-if="project.github_url" :href="project.github_url" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                <i class="fab fa-github"></i> 查看源码
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 项目内容 -->
      <div class="container">
        <div class="project-body">
          <!-- 项目概览 -->
          <section class="project-section">
            <h2 class="section-title">项目概览</h2>
            <div class="project-overview">
              <div class="overview-text">
                <div v-html="project.description"></div>
              </div>
              
              <div class="overview-details">
                <div class="detail-card">
                  <h3>技术栈</h3>
                  <div class="tags-list">
                    <span v-for="(tag, index) in project.tags" :key="index" class="tag">{{ tag }}</span>
                  </div>
                </div>
                
                <div class="detail-card" v-if="project.features && project.features.length > 0">
                  <h3>主要功能</h3>
                  <ul class="features-list">
                    <li v-for="(feature, index) in project.features" :key="index">
                      {{ feature }}
                    </li>
                  </ul>
                </div>
                
                <div class="detail-card" v-if="project.challenges && project.challenges.length > 0">
                  <h3>项目挑战</h3>
                  <ul class="challenges-list">
                    <li v-for="(challenge, index) in project.challenges" :key="index">
                      {{ challenge }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </section>
          
          <!-- 项目图片 -->
          <section class="project-section" v-if="project.images && project.images.length > 0">
            <h2 class="section-title">项目展示</h2>
            <div class="project-gallery">
              <div 
                v-for="(image, index) in project.images" 
                :key="index"
                class="gallery-item"
                @click="openLightbox(index)"
              >
                <img :src="image.thumbnail" :alt="image.caption || `项目图片 ${index + 1}`" />
                <div class="gallery-caption" v-if="image.caption">{{ image.caption }}</div>
              </div>
            </div>
          </section>
          
          <!-- 项目视频 -->
          <section class="project-section" v-if="project.video_url">
            <h2 class="section-title">项目演示</h2>
            <div class="project-video">
              <div class="video-container">
                <iframe 
                  :src="getEmbedUrl(project.video_url)" 
                  frameborder="0" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen
                ></iframe>
              </div>
            </div>
          </section>
          
          <!-- 相关项目 -->
          <section class="project-section" v-if="relatedProjects.length > 0">
            <h2 class="section-title">相关项目</h2>
            <div class="related-projects">
              <div 
                v-for="relatedProject in relatedProjects" 
                :key="relatedProject.id"
                class="related-project-card"
              >
                <div class="related-project-image">
                  <img :src="relatedProject.thumbnail" :alt="relatedProject.title" />
                </div>
                <div class="related-project-info">
                  <h3>{{ relatedProject.title }}</h3>
                  <p>{{ relatedProject.short_description }}</p>
                  <router-link :to="`/projects/${relatedProject.id}`" class="btn btn-outline">
                    查看详情
                  </router-link>
                </div>
              </div>
            </div>
          </section>
        </div>
        
        <!-- 项目导航 -->
        <div class="project-navigation">
          <router-link 
            v-if="prevProject" 
            :to="`/projects/${prevProject.id}`" 
            class="nav-link prev-link"
          >
            <i class="fas fa-arrow-left"></i>
            <div class="nav-content">
              <span>上一个项目</span>
              <h4>{{ prevProject.title }}</h4>
            </div>
          </router-link>
          
          <router-link to="/projects" class="nav-link all-link">
            <i class="fas fa-th-large"></i>
            <span>所有项目</span>
          </router-link>
          
          <router-link 
            v-if="nextProject" 
            :to="`/projects/${nextProject.id}`" 
            class="nav-link next-link"
          >
            <div class="nav-content">
              <span>下一个项目</span>
              <h4>{{ nextProject.title }}</h4>
            </div>
            <i class="fas fa-arrow-right"></i>
          </router-link>
        </div>
      </div>
    </div>
    
    <!-- 图片灯箱 -->
    <div class="lightbox" v-if="lightboxOpen" @click="closeLightbox">
      <div class="lightbox-content" @click.stop>
        <button class="lightbox-close" @click="closeLightbox">
          <i class="fas fa-times"></i>
        </button>
        <button class="lightbox-prev" @click.stop="prevImage" v-if="project.images.length > 1">
          <i class="fas fa-chevron-left"></i>
        </button>
        <div class="lightbox-image-container">
          <img :src="project.images[currentImageIndex].full" :alt="project.images[currentImageIndex].caption || ''" />
          <div class="lightbox-caption" v-if="project.images[currentImageIndex].caption">
            {{ project.images[currentImageIndex].caption }}
          </div>
        </div>
        <button class="lightbox-next" @click.stop="nextImage" v-if="project.images.length > 1">
          <i class="fas fa-chevron-right"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'ProjectDetail',
  data() {
    return {
      categoryColors: {
        1: '#42b983', // Web开发
        2: '#3498db', // 数据分析
        3: '#9b59b6', // 机器学习
        4: '#e74c3c', // 移动应用
        5: '#f39c12', // 其他
      },
      lightboxOpen: false,
      currentImageIndex: 0,
    };
  },
  computed: {
    ...mapState('projects', ['project', 'projects', 'categories', 'loading', 'error']),
    
    projectId() {
      return parseInt(this.$route.params.id, 10);
    },
    
    relatedProjects() {
      if (!this.project || !this.projects.length) return [];
      
      // 获取同类别的项目，排除当前项目
      return this.projects
        .filter(p => p.category === this.project.category && p.id !== this.project.id)
        .slice(0, 3); // 最多显示3个相关项目
    },
    
    prevProject() {
      if (!this.project || !this.projects.length) return null;
      
      const currentIndex = this.projects.findIndex(p => p.id === this.project.id);
      if (currentIndex <= 0) return null;
      
      return this.projects[currentIndex - 1];
    },
    
    nextProject() {
      if (!this.project || !this.projects.length) return null;
      
      const currentIndex = this.projects.findIndex(p => p.id === this.project.id);
      if (currentIndex === -1 || currentIndex === this.projects.length - 1) return null;
      
      return this.projects[currentIndex + 1];
    },
  },
  created() {
    this.loadProjectData();
  },
  methods: {
    ...mapActions('projects', ['fetchProject', 'fetchProjects', 'fetchCategories']),
    
    async loadProjectData() {
      try {
        // 确保有项目列表数据
        if (this.projects.length === 0) {
          await this.fetchProjects();
        }
        
        // 确保有分类数据
        if (this.categories.length === 0) {
          await this.fetchCategories();
        }
        
        // 获取当前项目详情
        await this.fetchProject(this.projectId);
      } catch (error) {
        console.error('Failed to load project data:', error);
      }
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
    
    getEmbedUrl(url) {
      // 处理YouTube链接
      if (url.includes('youtube.com') || url.includes('youtu.be')) {
        let videoId = '';
        
        if (url.includes('youtube.com/watch')) {
          const urlParams = new URLSearchParams(new URL(url).search);
          videoId = urlParams.get('v');
        } else if (url.includes('youtu.be/')) {
          videoId = url.split('youtu.be/')[1].split('?')[0];
        }
        
        if (videoId) {
          return `https://www.youtube.com/embed/${videoId}`;
        }
      }
      
      // 处理Vimeo链接
      if (url.includes('vimeo.com')) {
        const vimeoId = url.split('vimeo.com/')[1].split('?')[0];
        if (vimeoId) {
          return `https://player.vimeo.com/video/${vimeoId}`;
        }
      }
      
      // 处理Bilibili链接
      if (url.includes('bilibili.com')) {
        let bvid = '';
        
        if (url.includes('video/')) {
          bvid = url.split('video/')[1].split('?')[0];
          return `https://player.bilibili.com/player.html?bvid=${bvid}&high_quality=1&danmaku=0`;
        }
      }
      
      // 默认返回原始URL
      return url;
    },
    
    openLightbox(index) {
      this.currentImageIndex = index;
      this.lightboxOpen = true;
      document.body.style.overflow = 'hidden'; // 防止背景滚动
    },
    
    closeLightbox() {
      this.lightboxOpen = false;
      document.body.style.overflow = ''; // 恢复背景滚动
    },
    
    prevImage() {
      if (this.currentImageIndex > 0) {
        this.currentImageIndex--;
      } else {
        this.currentImageIndex = this.project.images.length - 1; // 循环到最后一张
      }
    },
    
    nextImage() {
      if (this.currentImageIndex < this.project.images.length - 1) {
        this.currentImageIndex++;
      } else {
        this.currentImageIndex = 0; // 循环到第一张
      }
    },
  },
  watch: {
    '$route.params.id'() {
      // 路由参数变化时重新加载数据
      this.loadProjectData();
      // 滚动到页面顶部
      window.scrollTo(0, 0);
    },
  },
  beforeDestroy() {
    // 确保在组件销毁时恢复body的overflow
    if (this.lightboxOpen) {
      document.body.style.overflow = '';
    }
  },
};
</script>

<style scoped>
.project-detail {
  animation: fadeIn 0.5s ease-in-out;
}

/* 加载和错误状态 */
.loading, .error, .not-found {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100px 0;
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

.error i, .not-found i {
  font-size: 3rem;
  color: #e74c3c;
  margin-bottom: 20px;
}

.not-found i {
  color: #6c757d;
}

.error h3, .not-found h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.error p, .not-found p {
  color: #6c757d;
  margin-bottom: 20px;
  max-width: 500px;
}

/* 项目头部 */
.project-header {
  position: relative;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 500px;
  display: flex;
  align-items: center;
  color: white;
  margin-bottom: 50px;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.5) 100%);
}

.project-header-content {
  position: relative;
  z-index: 1;
  max-width: 800px;
}

.project-category {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 20px;
}

.project-title {
  font-size: 3rem;
  margin-bottom: 15px;
  line-height: 1.2;
}

.project-description {
  font-size: 1.2rem;
  margin-bottom: 30px;
  opacity: 0.9;
  line-height: 1.6;
}

.project-meta {
  display: flex;
  gap: 30px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.meta-item i {
  font-size: 1.2rem;
}

.project-actions {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

/* 项目内容 */
.project-body {
  margin-bottom: 50px;
}

.project-section {
  margin-bottom: 60px;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 30px;
  position: relative;
  padding-bottom: 10px;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 3px;
  background-color: #42b983;
}

/* 项目概览 */
.project-overview {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 40px;
}

.overview-text {
  line-height: 1.8;
  color: #333;
}

.overview-text :deep(h3) {
  margin: 25px 0 15px;
  font-size: 1.5rem;
}

.overview-text :deep(p) {
  margin-bottom: 20px;
}

.overview-text :deep(ul), .overview-text :deep(ol) {
  margin-bottom: 20px;
  padding-left: 20px;
}

.overview-text :deep(li) {
  margin-bottom: 10px;
}

.overview-text :deep(img) {
  max-width: 100%;
  border-radius: 8px;
  margin: 20px 0;
}

.overview-text :deep(blockquote) {
  border-left: 4px solid #42b983;
  padding-left: 20px;
  margin: 20px 0;
  font-style: italic;
  color: #6c757d;
}

.overview-text :deep(code) {
  background-color: #f8f9fa;
  padding: 2px 5px;
  border-radius: 4px;
  font-family: monospace;
}

.overview-text :deep(pre) {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 20px 0;
}

.overview-text :deep(pre code) {
  background-color: transparent;
  padding: 0;
}

.overview-details {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.detail-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.detail-card h3 {
  margin-top: 0;
  margin-bottom: 15px;
  font-size: 1.2rem;
  color: #2c3e50;
}

.tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 5px 10px;
  background-color: white;
  border-radius: 4px;
  font-size: 0.9rem;
  color: #495057;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.features-list, .challenges-list {
  padding-left: 20px;
}

.features-list li, .challenges-list li {
  margin-bottom: 10px;
  position: relative;
}

.features-list li::before {
  content: '✓';
  color: #42b983;
  position: absolute;
  left: -20px;
  font-weight: bold;
}

.challenges-list li::before {
  content: '!';
  color: #f39c12;
  position: absolute;
  left: -20px;
  font-weight: bold;
}

/* 项目图片 */
.project-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.gallery-item {
  border-radius: 8px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.gallery-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.gallery-item:hover img {
  transform: scale(1.05);
}

.gallery-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  font-size: 0.9rem;
}

/* 项目视频 */
.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 比例 */
  height: 0;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* 相关项目 */
.related-projects {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
}

.related-project-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: white;
}

.related-project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.related-project-image {
  height: 150px;
  overflow: hidden;
}

.related-project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.related-project-card:hover .related-project-image img {
  transform: scale(1.05);
}

.related-project-info {
  padding: 15px;
}

.related-project-info h3 {
  margin: 0 0 10px;
  font-size: 1.2rem;
}

.related-project-info p {
  margin: 0 0 15px;
  color: #6c757d;
  font-size: 0.9rem;
  line-height: 1.5;
}

/* 项目导航 */
.project-navigation {
  display: flex;
  justify-content: space-between;
  margin-top: 50px;
  padding-top: 30px;
  border-top: 1px solid #eee;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: 15px;
  border-radius: 8px;
  background-color: #f8f9fa;
  transition: all 0.3s ease;
  max-width: 250px;
}

.nav-link:hover {
  background-color: #e9ecef;
  transform: translateY(-3px);
}

.prev-link, .next-link {
  flex: 1;
}

.prev-link {
  margin-right: 10px;
}

.next-link {
  margin-left: 10px;
  justify-content: flex-end;
}

.all-link {
  padding: 15px 20px;
  justify-content: center;
  background-color: #2c3e50;
  color: white;
}

.all-link:hover {
  background-color: #1e2b38;
}

.nav-link i {
  font-size: 1.2rem;
}

.prev-link i {
  margin-right: 10px;
}

.next-link i {
  margin-left: 10px;
}

.nav-content {
  overflow: hidden;
}

.nav-content span {
  display: block;
  font-size: 0.8rem;
  color: #6c757d;
  margin-bottom: 5px;
}

.nav-content h4 {
  margin: 0;
  font-size: 1rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 图片灯箱 */
.lightbox {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
}

.lightbox-image-container {
  position: relative;
}

.lightbox-image-container img {
  max-width: 100%;
  max-height: 80vh;
  display: block;
  border-radius: 4px;
}

.lightbox-caption {
  position: absolute;
  bottom: -40px;
  left: 0;
  width: 100%;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  text-align: center;
  border-radius: 0 0 4px 4px;
}

.lightbox-close, .lightbox-prev, .lightbox-next {
  background-color: transparent;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  transition: color 0.3s ease;
  position: absolute;
}

.lightbox-close:hover, .lightbox-prev:hover, .lightbox-next:hover {
  color: #42b983;
}

.lightbox-close {
  top: -40px;
  right: 0;
}

.lightbox-prev {
  left: -60px;
  top: 50%;
  transform: translateY(-50%);
}

.lightbox-next {
  right: -60px;
  top: 50%;
  transform: translateY(-50%);
}

/* 响应式调整 */
@media (max-width: 992px) {
  .project-overview {
    grid-template-columns: 1fr;
  }
  
  .project-title {
    font-size: 2.5rem;
  }
  
  .project-navigation {
    flex-wrap: wrap;
    gap: 10px;
  }
  
  .nav-link {
    flex: 1 1 100%;
    max-width: none;
    margin: 0;
  }
  
  .all-link {
    order: -1;
    margin-bottom: 10px;
  }
  
  .lightbox-prev {
    left: 10px;
  }
  
  .lightbox-next {
    right: 10px;
  }
}

@media (max-width: 768px) {
  .project-header {
    height: auto;
    padding: 60px 0;
  }
  
  .project-title {
    font-size: 2rem;
  }
  
  .project-meta {
    gap: 15px;
  }
  
  .section-title {
    font-size: 1.8rem;
  }
  
  .related-projects {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 576px) {
  .project-gallery {
    grid-template-columns: 1fr;
  }
  
  .project-actions {
    flex-direction: column;
    width: 100%;
  }
  
  .project-actions a {
    width: 100%;
    text-align: center;
  }
}
</style>