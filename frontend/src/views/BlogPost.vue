<template>
  <div class="blog-post-page">
    <div class="container">
      <!-- 文章头部 -->
      <div class="post-header">
        <div class="post-meta">
          <span><i class="fas fa-calendar"></i> 2024-01-15</span>
          <span><i class="fas fa-user"></i> Valrandy</span>
          <span><i class="fas fa-eye"></i> 1,234 次阅读</span>
        </div>
        <h1 class="post-title">示例博客文章标题</h1>
        <div class="post-tags">
          <span class="post-tag">Vue.js</span>
          <span class="post-tag">前端开发</span>
          <span class="post-tag">技术分享</span>
        </div>
      </div>

      <!-- 文章内容 -->
      <div class="post-content">
        <div class="post-body">
          <p>这是一篇示例博客文章的内容。在这里可以展示各种格式的文本内容。</p>
          <h2>二级标题</h2>
          <p>这是二级标题下的内容段落。</p>
          <h3>三级标题</h3>
          <p>这是三级标题下的内容段落。</p>
          <blockquote>
            <p>这是一个引用块的示例内容。</p>
          </blockquote>
          <ul>
            <li>列表项目 1</li>
            <li>列表项目 2</li>
            <li>列表项目 3</li>
          </ul>
        </div>
      </div>

      <!-- 作者信息 -->
      <div class="author-box">
        <div class="author-avatar">
          <img src="../assets/images/avatar.svg" alt="作者头像">
        </div>
        <div class="author-details">
          <h3>关于作者</h3>
          <h4>Valrandy</h4>
          <p>全栈开发工程师，专注于现代Web技术栈的研究与实践。</p>
        </div>
      </div>

      <!-- 文章操作 -->
      <div class="post-actions">
        <button class="action-btn">
          <i class="fas fa-heart"></i>
          <span>点赞</span>
        </button>
        <button class="action-btn">
          <i class="fas fa-share"></i>
          <span>分享</span>
        </button>
      </div>

      <!-- 评论区 -->
      <div class="comments-section">
        <h3>评论</h3>
        <div class="comment-form">
          <div class="form-header">
            <div class="user-avatar">
              <img src="../assets/images/default-avatar.svg" alt="用户头像">
            </div>
            <span>发表评论</span>
          </div>
          <textarea placeholder="写下你的评论..."></textarea>
          <button class="submit-btn">发布评论</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogPost',
  data() {
    return {
      // 组件数据
    };
  },
  mounted() {
    // 组件挂载后的逻辑
  },
};
</script>

<style scoped>
.blog-post-page {
  animation: fadeIn 0.5s ease-in-out;
}

/* 文章头部 */
.post-header {
  padding: 40px 0;
  margin-bottom: 40px;
  border-bottom: 1px solid #eee;
}

.post-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  font-size: 0.9rem;
  color: #666;
}

.post-title {
  font-size: 2.5rem;
  margin-bottom: 20px;
  line-height: 1.3;
  color: #333;
}

.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.post-tag {
  padding: 5px 12px;
  border-radius: 20px;
  background-color: #6a11cb;
  color: white;
  font-size: 0.85rem;
}

/* 文章内容 */
.post-content {
  margin-bottom: 40px;
}

.post-body {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #333;
}

.post-body h2 {
  font-size: 1.8rem;
  margin: 40px 0 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.post-body h3 {
  font-size: 1.5rem;
  margin: 30px 0 15px;
}

.post-body p {
  margin-bottom: 20px;
}

.post-body blockquote {
  border-left: 4px solid #6a11cb;
  padding: 15px 20px;
  background-color: #f8f9fa;
  margin: 20px 0;
  font-style: italic;
  color: #555;
}

.post-body ul {
  margin: 20px 0;
  padding-left: 20px;
}

.post-body li {
  margin-bottom: 10px;
}

/* 作者信息框 */
.author-box {
  display: flex;
  gap: 20px;
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 25px;
  margin-bottom: 40px;
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

.author-details {
  flex: 1;
}

.author-details h3 {
  font-size: 1.2rem;
  margin-bottom: 10px;
  color: #6a11cb;
}

.author-details h4 {
  font-size: 1.4rem;
  margin-bottom: 10px;
}

.author-details p {
  color: #6c757d;
  line-height: 1.6;
}

/* 文章操作 */
.post-actions {
  display: flex;
  gap: 15px;
  margin-bottom: 40px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 30px;
  border: 1px solid #ddd;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.action-btn:hover {
  border-color: #6a11cb;
  color: #6a11cb;
}

/* 评论区 */
.comments-section {
  margin-top: 40px;
}

.comments-section h3 {
  font-size: 1.5rem;
  margin-bottom: 25px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.comment-form {
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
}

.form-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.comment-form textarea {
  width: 100%;
  min-height: 100px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  resize: vertical;
  font-family: inherit;
  margin-bottom: 15px;
}

.submit-btn {
  background-color: #6a11cb;
  color: white;
  border: none;
  padding: 10px 25px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #5a0cb6;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .post-title {
    font-size: 2rem;
  }

  .post-meta {
    flex-direction: column;
    gap: 10px;
  }

  .author-box {
    flex-direction: column;
    text-align: center;
  }

  .post-actions {
    justify-content: center;
  }
}

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
</style>
