<template>
  <div class="creative-lab-page">
    <!-- B站风格头图 -->
    <div class="bilibili-header">
      <div class="header-background">
        <img src="/【哲风壁纸】椿-鸣潮.png" alt="头图背景" class="bg-image" />
        <div class="header-overlay"></div>
      </div>
      <div class="header-content">
        <div class="container">
          <div class="header-info">
            <h1 class="page-title">创意实验室</h1>
            <p class="page-subtitle">Creative Laboratory</p>
            <div class="stats-row">
              <div class="stat-item">
                <span class="stat-number">{{ totalProjects }}</span>
                <span class="stat-label">技术项目</span>
              </div>
              <div class="stat-item">
                <span class="stat-number">{{ totalSkills }}</span>
                <span class="stat-label">掌握技能</span>
              </div>
              <div class="stat-item">
                <span class="stat-number">{{ totalWorks }}</span>
                <span class="stat-label">创意作品</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 技术展示区域 -->
    <div class="container">
      <div class="lab-layout">
        <!-- 分类导航 -->
        <div class="category-nav">
          <div class="nav-container">
            <button 
              v-for="category in categories" 
              :key="category.id"
              class="category-btn"
              :class="{ active: activeCategory === category.id }"
              @click="setActiveCategory(category.id)"
            >
              <i :class="category.icon"></i>
              <span>{{ category.name }}</span>
              <div class="category-count">{{ category.count }}</div>
            </button>
          </div>
        </div>

        <!-- 主展示区域 -->
        <div class="showcase-main">
          <!-- 视频展示区 -->
          <div v-if="activeCategory === 'video'" class="video-showcase">
            <div class="development-notice">
              <div class="notice-icon">
                <i class="fas fa-tools"></i>
              </div>
              <h3 class="notice-title">功能开发中</h3>
              <p class="notice-description">视频作品展示功能正在开发中，敬请期待...</p>
            </div>
          </div>

           <!-- CSS动画展示区 -->
           <div v-if="activeCategory === 'animation'" class="animation-showcase">
             <div class="development-notice">
               <div class="notice-icon">
                 <i class="fas fa-tools"></i>
               </div>
               <h3 class="notice-title">功能开发中</h3>
               <p class="notice-description">CSS动画作品展示功能正在开发中，敬请期待...</p>
             </div>
           </div>

           <!-- 3D建模展示区 -->
           <div v-if="activeCategory === 'modeling'" class="modeling-showcase">
             <div class="development-notice">
               <div class="notice-icon">
                 <i class="fas fa-tools"></i>
               </div>
               <h3 class="notice-title">功能开发中</h3>
               <p class="notice-description">3D建模作品展示功能正在开发中，敬请期待...</p>
             </div>
           </div>

           <!-- 编程项目展示区 -->
           <div v-if="activeCategory === 'coding'" class="coding-showcase">
             <div class="development-notice">
               <div class="notice-icon">
                 <i class="fas fa-tools"></i>
               </div>
               <h3 class="notice-title">功能开发中</h3>
               <p class="notice-description">编程项目展示功能正在开发中，敬请期待...</p>
             </div>
           </div>

           <!-- 设计作品展示区 -->
           <div v-if="activeCategory === 'design'" class="design-showcase">
             <div class="development-notice">
               <div class="notice-icon">
                 <i class="fas fa-tools"></i>
               </div>
               <h3 class="notice-title">功能开发中</h3>
               <p class="notice-description">设计作品展示功能正在开发中，敬请期待...</p>
             </div>
           </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreativeLab',
  data() {
    return {
      activeCategory: 'video',
      totalProjects: 24,
      totalSkills: 15,
      totalWorks: 48,
      categories: [
        { id: 'video', name: '视频剪辑', icon: 'fas fa-video', count: 12 },
        { id: 'animation', name: 'CSS动画', icon: 'fas fa-magic', count: 18 },
        { id: 'modeling', name: '3D建模', icon: 'fas fa-cube', count: 8 },
        { id: 'coding', name: '编程项目', icon: 'fas fa-code', count: 15 },
        { id: 'design', name: '设计作品', icon: 'fas fa-palette', count: 10 }
      ],
      videos: [],
      animations: [],
      models: []
    };
  },
  methods: {

    setActiveCategory(categoryId) {
      this.activeCategory = categoryId;
    },


  },
};
</script>

<style scoped>
.creative-lab-page {
  animation: fadeIn 0.5s ease-in-out;
}

/* B站风格头图 */
.bilibili-header {
  position: relative;
  height: 300px;
  overflow: hidden;
  margin-bottom: 40px;
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.bg-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center bottom;
}

.header-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6));
}

.header-content {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  align-items: flex-end;
  padding-bottom: 40px;
}

.header-info {
  color: white;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 8px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.page-subtitle {
  font-size: 1.1rem;
  font-weight: 300;
  opacity: 0.9;
  margin-bottom: 20px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

.stats-row {
  display: flex;
  gap: 30px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  display: block;
  font-size: 1.8rem;
  font-weight: 700;
  color: #00aeec;
  margin-bottom: 4px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

.stat-label {
  font-size: 0.85rem;
  opacity: 0.9;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

/* 技术展示区域布局 */
.lab-layout {
  margin-top: 80px;
  margin-bottom: 80px;
}

/* 分类导航样式 */
.category-nav {
  background: white;
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  margin-bottom: 40px;
}

.nav-container {
  display: flex;
  justify-content: center;
  gap: 15px;
  flex-wrap: wrap;
}

.category-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 15px 25px;
  border: 2px solid #e2e8f0;
  background: white;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 16px;
  font-weight: 500;
  color: #4a5568;
  position: relative;
  overflow: hidden;
}

.category-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  transition: left 0.5s;
}

.category-btn:hover::before {
  left: 100%;
}

.category-btn:hover {
  border-color: #667eea;
  color: #667eea;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
}

.category-btn.active {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-color: #667eea;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.category-btn i {
  font-size: 18px;
}

.category-count {
  background: rgba(255, 255, 255, 0.2);
  color: inherit;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.category-btn.active .category-count {
  background: rgba(255, 255, 255, 0.3);
}

/* 视频展示区域 */
.video-showcase {
  margin-bottom: 60px;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: #2d3748;
  margin-bottom: 30px;
  text-align: center;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #667eea, #764ba2);
  border-radius: 2px;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
}

.video-card {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  position: relative;
}

.video-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
}

.video-thumbnail {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.video-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.video-card:hover .video-thumbnail img {
  transform: scale(1.1);
}

.play-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8));
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  cursor: pointer;
}

.video-card:hover .play-overlay {
  opacity: 1;
}

.play-overlay i {
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: #667eea;
  transition: all 0.3s ease;
}

.play-overlay i:hover {
  background: white;
  transform: scale(1.1);
}

.video-duration {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.video-info {
  padding: 25px;
}

.video-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 10px;
}

.video-description {
  color: #718096;
  line-height: 1.6;
  margin-bottom: 15px;
}

.video-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #a0aec0;
  font-size: 0.9rem;
}

/* 动画展示区域 */
.animation-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
}

.animation-card {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.animation-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
}

.animation-preview {
  position: relative;
  height: 200px;
  background: #f7fafc;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.animation-demo {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.animation-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgba(102, 126, 234, 0.9), rgba(118, 75, 162, 0.9));
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.animation-card:hover .animation-overlay {
  opacity: 1;
}

.preview-btn, .code-btn {
  padding: 10px 20px;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  color: #4a5568;
}

.preview-btn:hover, .code-btn:hover {
  background: white;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.animation-info {
  padding: 25px;
}

.animation-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 10px;
}

.animation-description {
  color: #718096;
  line-height: 1.6;
  margin-bottom: 15px;
}

.animation-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 500;
}

/* 3D建模展示区域 */
.modeling-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
}

.model-card {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.model-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
}

.model-preview {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.model-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.model-card:hover .model-preview img {
  transform: scale(1.1);
}

.model-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8));
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.model-card:hover .model-overlay {
  opacity: 1;
}

.view-3d-btn {
  padding: 12px 24px;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  color: #4a5568;
  font-size: 16px;
}

.view-3d-btn:hover {
  background: white;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.model-category {
  position: absolute;
  top: 15px;
  left: 15px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  padding: 6px 12px;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 500;
}

.model-info {
  padding: 25px;
}

.model-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 10px;
}

.model-description {
  color: #718096;
  line-height: 1.6;
  margin-bottom: 15px;
}

.model-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #a0aec0;
  font-size: 0.9rem;
}

.model-software {
  background: #edf2f7;
  color: #4a5568;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
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

/* 响应式设计 */
@media (max-width: 1200px) {
  .hero-content .container {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 40px;
  }
  
  .character-container {
    width: 300px;
    height: 300px;
  }
}

@media (max-width: 768px) {
  .anime-hero-section {
    min-height: 80vh;
  }
  
  .title-main {
    font-size: 2.5rem;
  }
  
  .hero-description {
    font-size: 1.1rem;
  }
  
  .hero-stats {
    justify-content: center;
    gap: 30px;
  }
  
  .category-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .category-btn {
    width: 100%;
    max-width: 300px;
    justify-content: center;
  }
  
  .works-grid,
  .video-grid,
  .animation-grid,
  .modeling-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .anime-hero-section {
    min-height: 70vh;
  }
  
  .title-main {
    font-size: 2rem;
  }
  
  .hero-stats {
    flex-direction: column;
    gap: 20px;
  }
  
  .category-nav,
  .work-card,
  .video-card,
  .animation-card,
  .model-card {
    margin: 0 15px;
  }
  
  .work-info,
  .video-info,
  .animation-info,
  .model-info {
    padding: 20px;
  }
}

/* 开发中提示样式 */
.development-notice {
  text-align: center;
  padding: 80px 20px;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
  border-radius: 15px;
  margin: 40px 0;
}

.notice-icon {
  margin-bottom: 20px;
}

.notice-icon i {
  font-size: 4rem;
  color: #6c757d;
  animation: pulse 2s infinite;
}

.notice-title {
  font-size: 1.8rem;
  color: #495057;
  margin-bottom: 15px;
  font-weight: 600;
}

.notice-description {
  font-size: 1.1rem;
  color: #6c757d;
  line-height: 1.6;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

/* 加载和错误状态 */
.loading-state,
.error-state,
.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.loading-state i,
.error-state i,
.empty-state i {
  font-size: 4rem;
  color: #cbd5e0;
  margin-bottom: 20px;
  display: block;
}

.loading-state h3,
.error-state h3,
.empty-state h3 {
  font-size: 1.5rem;
  color: #4a5568;
  margin-bottom: 10px;
}

.loading-state p,
.error-state p,
.empty-state p {
  color: #718096;
  font-size: 1.1rem;
}

/* 动画效果 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.work-card,
.video-card,
.animation-card,
.model-card {
  animation: fadeIn 0.6s ease-out;
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #5a67d8, #6b46c1);
}

/* 通用工具类 */
.text-gradient {
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.btn-gradient {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.btn-gradient:hover {
  background: linear-gradient(135deg, #5a67d8, #6b46c1);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}
</style>
