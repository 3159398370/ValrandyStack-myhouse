<template>
  <div class="blog-post-container">
    <!-- 加载状态 -->
    <div v-if="loading" class="loading-container">
      <el-skeleton :rows="10" animated/>
    </div>

    <!-- 错误提示 -->
    <el-alert
        v-if="error"
        :title="error"
        type="error"
        :closable="false"
        show-icon
    />

    <!-- 文章内容 -->
    <div v-if="post && !loading" class="post-content">
      <!-- 文章头部信息 -->
      <div class="post-header">
        <h1 class="post-title">{{ post.title }}</h1>

        <div class="post-meta">
          <div class="author-info">
            <el-avatar :src="post.author.avatar || require('@/assets/images/default-avatar.jpg')" :size="40"/>
            <span class="author-name">{{ post.author.full_name || post.author.username }}</span>
          </div>

          <div class="post-info">
            <span class="post-date">
              <i class="el-icon-date"></i>
              {{ formatDate(post.published_at) }}
            </span>
            <span class="post-views">
              <i class="el-icon-view"></i>
              {{ post.views_count }} 阅读
            </span>
            <span class="post-comments">
              <i class="el-icon-chat-dot-round"></i>
              {{ post.comments_count }} 评论
            </span>
            <span class="post-reading-time">
              <i class="el-icon-reading"></i>
              {{ post.reading_time }} 分钟阅读
            </span>
          </div>
        </div>

        <!-- 标签 -->
        <div class="post-tags">
          <el-tag
              v-for="tag in post.tags"
              :key="tag.id"
              size="small"
              effect="plain"
              @click="filterByTag(tag.id)"
          >
            {{ tag.name }}
          </el-tag>
        </div>
      </div>

      <!-- 特色图片 -->
      <div v-if="post.featured_image" class="featured-image">
        <img :src="post.featured_image" :alt="post.title"/>
      </div>

      <!-- 文章内容 -->
      <div class="post-body">
        <div class="markdown-content" v-html="post.content"></div>
      </div>

      <!-- 点赞按钮 -->
      <div class="post-actions">
        <el-button
            type="danger"
            :icon="post.is_liked ? 'el-icon-star-on' : 'el-icon-star-off'"
            :plain="!post.is_liked"
            @click="toggleLike"
        >
          {{ post.is_liked ? '已点赞' : '点赞' }} ({{ post.likes_count }})
        </el-button>

        <el-button
            type="primary"
            icon="el-icon-chat-dot-round"
            plain
            @click="scrollToComments"
        >
          评论 ({{ post.comments_count }})
        </el-button>

        <el-dropdown trigger="click" @command="handleShare">
          <el-button type="info" icon="el-icon-share" plain>
            分享
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="weibo">微博</el-dropdown-item>
            <el-dropdown-item command="wechat">微信</el-dropdown-item>
            <el-dropdown-item command="twitter">Twitter</el-dropdown-item>
            <el-dropdown-item command="facebook">Facebook</el-dropdown-item>
            <el-dropdown-item command="copy">复制链接</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>

      <!-- 作者信息 -->
      <div class="author-card">
        <div class="author-avatar">
          <el-avatar :src="post.author.avatar || require('@/assets/images/default-avatar.jpg')" :size="80"/>
        </div>
        <div class="author-details">
          <h3 class="author-name">{{ post.author.full_name || post.author.username }}</h3>
          <p class="author-bio" v-if="post.author.bio">{{ post.author.bio }}</p>
          <div class="author-social" v-if="post.author">
            <a v-if="post.author.github_username" :href="`https://github.com/${post.author.github_username}`"
               target="_blank">
              <i class="fab fa-github"></i>
            </a>
            <a v-if="post.author.twitter_username" :href="`https://twitter.com/${post.author.twitter_username}`"
               target="_blank">
              <i class="fab fa-twitter"></i>
            </a>
            <a v-if="post.author.linkedin_username" :href="`https://linkedin.com/in/${post.author.linkedin_username}`"
               target="_blank">
              <i class="fab fa-linkedin"></i>
            </a>
            <a v-if="post.author.weibo_username" :href="`https://weibo.com/${post.author.weibo_username}`"
               target="_blank">
              <i class="fab fa-weibo"></i>
            </a>
            <a v-if="post.author.bilibili_username" :href="`https://space.bilibili.com/${post.author.bilibili_username}`"
               target="_blank">
              <i class="fab fa-bilibili"></i>
            </a>
          </div>
        </div>
      </div>

      <!-- 相关文章 -->
      <div class="related-posts" v-if="relatedPosts.length > 0">
        <h3 class="section-title">相关文章</h3>
        <div class="related-posts-grid">
          <div 
              v-for="relatedPost in relatedPosts" 
              :key="relatedPost.id"
              class="related-post-card"
              @click="goToPost(relatedPost.id)"
          >
            <div class="related-post-image" v-if="relatedPost.featured_image">
              <img :src="relatedPost.featured_image" :alt="relatedPost.title"/>
            </div>
            <div class="related-post-info">
              <h4 class="related-post-title">{{ relatedPost.title }}</h4>
              <p class="related-post-excerpt">{{ relatedPost.excerpt }}</p>
              <div class="related-post-meta">
                <span class="related-post-date">{{ formatDate(relatedPost.published_at) }}</span>
                <span class="related-post-reading-time">{{ relatedPost.reading_time }} 分钟阅读</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 评论区 -->
      <div id="comments" class="comments-section">
        <h3 class="section-title">评论 ({{ post.comments_count }})</h3>

        <!-- 评论列表 -->
        <div class="comments-list" v-if="post.comments && post.comments.length > 0">
          <div
              v-for="comment in post.comments"
              :key="comment.id"
              class="comment-item"
          >
            <div class="comment-avatar">
              <el-avatar :src="comment.author.avatar || require('@/assets/images/default-avatar.jpg')" :size="40"/>
            </div>
            <div class="comment-content">
              <div class="comment-header">
                <span class="comment-author">{{ comment.author.full_name || comment.author.username }}</span>
                <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
              </div>
              <div class="comment-body">{{ comment.content }}</div>
              <div class="comment-actions">
                <el-button type="text" size="small" @click="replyToComment(comment)">回复</el-button>
              </div>

              <!-- 回复列表 -->
              <div class="replies-list" v-if="comment.replies && comment.replies.length > 0">
                <div
                    v-for="reply in comment.replies"
                    :key="reply.id"
                    class="reply-item"
                >
                  <div class="reply-avatar">
                    <el-avatar :src="reply.author.avatar || require('@/assets/images/default-avatar.jpg')" :size="30"/>
                  </div>
                  <div class="reply-content">
                    <div class="reply-header">
                      <span class="reply-author">{{ reply.author.full_name || reply.author.username }}</span>
                      <span class="reply-date">{{ formatDate(reply.created_at) }}</span>
                    </div>
                    <div class="reply-body">{{ reply.content }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 无评论提示 -->
        <div class="no-comments" v-else>
          <el-empty description="暂无评论，快来发表第一条评论吧！"/>
        </div>

        <!-- 评论表单 -->
        <div class="comment-form">
          <h4 class="form-title">{{ replyingTo ? `回复 ${replyingTo.author.username}` : '发表评论' }}</h4>

          <!-- 未登录提示 -->
          <div v-if="!isLoggedIn" class="login-notice">
            <p>请先
              <router-link to="/login">登录</router-link>
              后再发表评论
            </p>
          </div>

          <!-- 评论输入框 -->
          <div v-else>
            <el-form :model="commentForm" :rules="commentRules" ref="commentForm">
              <el-form-item prop="content">
                <el-input
                    type="textarea"
                    :rows="4"
                    placeholder="写下你的评论..."
                    v-model="commentForm.content"
                ></el-input>
              </el-form-item>
              <el-form-item>
                <el-button
                    v-if="replyingTo"
                    size="small"
                    @click="cancelReply"
                >
                  取消回复
                </el-button>
                <el-button
                    type="primary"
                    @click="submitComment"
                    :loading="submittingComment"
                >
                  发表评论
                </el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex';
import marked from 'marked';

export default {
  name: 'BlogPost',
  data() {
    return {
      liked: false,
      bookmarked: false,
      showSharePopup: false,
      commentText: '',
      replyText: '',
      replyingTo: null,
      replyingToUser: null,
      subscribeEmail: '',
      tableOfContents: [],
      currentUrl: '',
      submittingComment: false,
      commentForm: {
        content: ''
      },
      commentRules: {
        content: [
          { required: true, message: '请输入评论内容', trigger: 'blur' },
          { min: 3, max: 500, message: '评论长度在 3 到 500 个字符', trigger: 'blur' }
        ]
      }
    };
  },
  computed: {
    ...mapState({
      post: state => state.posts.currentPost,
      loading: state => state.posts.loading,
      error: state => state.posts.error,
      comments: state => state.comments.items,
      commentsLoading: state => state.comments.loading,
      commentsError: state => state.comments.error,
      user: state => state.auth.user,
      relatedPostsData: state => state.posts.relatedPosts,
    }),
    ...mapGetters([
      'isAuthenticated',
    ]),
    postId() {
      return this.$route.params.id;
    },
    isLoggedIn() {
      return this.$store.getters.isAuthenticated;
    },
    headerStyle() {
      if (this.post && this.post.featured_image) {
        return {
          backgroundImage: `url(${this.post.featured_image})`,
        };
      }
      return {};
    },
    relatedPosts() {
      return this.relatedPostsData || [];
    },
    prevPost() {
      return this.post && this.post.prev_post;
    },
    nextPost() {
      return this.post && this.post.next_post;
    },
    formattedContent() {
      if (!this.post || !this.post.content) return '';
      return marked(this.post.content);
    },
    readingTime() {
      if (!this.post || !this.post.content) return '0 分钟';
      const words = this.post.content.trim().split(/\s+/).length;
      const time = Math.ceil(words / 200); // 假设阅读速度为每分钟200字
      return `${time} 分钟`;
    },
  },
  created() {
    this.fetchPost(this.$route.params.id);
    this.fetchComments(this.$route.params.id);
    this.currentUrl = window.location.href;
    
    // 增加浏览量
    this.incrementViews(this.$route.params.id);
    
    // 解析文章内容生成目录
    this.$nextTick(() => {
      this.generateTableOfContents();
    });
  },
  methods: {
    ...mapActions({
      fetchPost: 'posts/fetchPost',
      fetchComments: 'comments/fetchComments',
      addComment: 'comments/addComment',
      incrementViews: 'posts/incrementViews',
    }),
    submitComment() {
      if (!this.isLoggedIn) {
        this.$store.dispatch('showLoginModal');
        return;
      }
      
      if (!this.commentForm.content.trim()) {
        return;
      }
      
      this.submittingComment = true;
      
      const commentData = {
        post_id: this.postId,
        content: this.commentForm.content,
        parent_id: this.replyingTo || null
      };
      
      this.addComment(commentData)
        .then(() => {
          this.commentForm.content = '';
          this.replyingTo = null;
          this.replyingToUser = null;
          this.submittingComment = false;
        })
        .catch(error => {
          console.error('Error submitting comment:', error);
          this.submittingComment = false;
        });
    },
    replyToComment(comment) {
      if (!this.isLoggedIn) {
        this.$store.dispatch('showLoginModal');
        return;
      }
      
      this.replyingTo = comment.id;
      this.replyingToUser = comment.user.name;
      
      // 滚动到评论表单
      this.$nextTick(() => {
        const commentForm = document.querySelector('.comment-form');
        if (commentForm) {
          commentForm.scrollIntoView({ behavior: 'smooth' });
        }
      });
    },
    cancelReply() {
      this.replyingTo = null;
      this.replyingToUser = null;
    },
    
    incrementViews(postId) {
      // 增加文章浏览量
      this.$store.dispatch('posts/incrementViews', postId);
    },
    
    filterByTag(tag) {
      this.$router.push({ name: 'Blog', query: { tag: tag } });
    },
    goToPost(id) {
      this.$router.push({ name: 'BlogPost', params: { id } });
    },
    
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },
    
    toggleLike() {
      if (!this.isLoggedIn) {
        this.$store.dispatch('showLoginModal');
        return;
      }
      this.liked = !this.liked;
    },
    toggleBookmark() {
      if (!this.isLoggedIn) {
        this.$store.dispatch('showLoginModal');
        return;
      }
      this.bookmarked = !this.bookmarked;
    },
    
    toggleSharePopup() {
      this.showSharePopup = !this.showSharePopup;
    },
    
    shareOnSocial(platform) {
      const url = encodeURIComponent(window.location.href);
      const title = encodeURIComponent(this.post.title);
      
      let shareUrl = '';
      
      switch (platform) {
        case 'twitter':
          shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
          break;
        case 'facebook':
          shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
          break;
        case 'linkedin':
          shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${url}`;
          break;
      }
      
      if (shareUrl) {
        window.open(shareUrl, '_blank');
      }
      
      this.showSharePopup = false;
    },
    subscribeNewsletter() {
      // 处理订阅逻辑
      console.log('订阅邮箱:', this.subscribeEmail);
      // 这里可以添加实际的订阅API调用
      this.subscribeEmail = '';
      // 显示成功消息
      this.$message.success('订阅成功！感谢您的关注。');
    },
    
    goToTaggedPosts(tag) {
      this.$router.push({ name: 'Blog', query: { tag } });
    },
    
    scrollToHeading(id) {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    },
    generateTableOfContents() {
      if (!this.post || !this.post.content) return;
      
      // 使用正则表达式匹配所有标题
      const headings = this.post.content.match(/^#{2,3}\s+(.+)$/gm) || [];
      
      this.tableOfContents = headings.map((heading, index) => {
        const level = heading.match(/^(#{2,3})\s+/)[1].length;
        const text = heading.replace(/^#{2,3}\s+/, '');
        const id = `heading-${index}`;
        
        return {
          id,
          text,
          level,
          active: false
        };
      });
    },
    
    // 评论相关方法
    submitComment() {
      if (!this.isLoggedIn) {
        this.$message.warning('请先登录后再发表评论');
        return;
      }
      
      if (!this.post) return;
      
      this.$refs.commentForm.validate(async valid => {
        if (!valid) return;
        
        this.submittingComment = true;
        
        try {
          const payload = {
            content: this.commentForm.content,
            post: this.post.id
          };
          
          if (this.replyingTo) {
            payload.parent = this.replyingTo.id;
          }
          
          // 发送评论到API
          const response = await this.$axios.post('/api/blog/comments/', payload);
          
          // 创建更新后的文章对象
          const updatedPost = { ...this.post };
          
          // 更新评论列表
          if (this.replyingTo) {
            // 如果是回复，添加到回复列表
            const updatedComments = updatedPost.comments.map(comment => {
              if (comment.id === this.replyingTo.id) {
                const updatedComment = { ...comment };
                if (!updatedComment.replies) {
                  updatedComment.replies = [];
                }
                updatedComment.replies = [...updatedComment.replies, response.data];
                return updatedComment;
              }
              return comment;
            });
            updatedPost.comments = updatedComments;
          } else {
            // 如果是新评论，添加到评论列表
            if (!updatedPost.comments) {
              updatedPost.comments = [];
            }
            updatedPost.comments = [...updatedPost.comments, response.data];
          }
          
          // 更新评论计数
          updatedPost.comments_count += 1;
          
          // 更新Vuex中的文章数据
          this.$store.commit('blog/SET_POST', updatedPost);
          
          // 重置表单
          this.commentForm.content = '';
          this.replyingTo = null;
          this.$message.success('评论发表成功');
        } catch (error) {
          console.error('评论发表失败:', error);
          this.$message.error('评论发表失败，请稍后重试');
        } finally {
          this.submittingComment = false;
        }
      });
    },
    
    cancelReply() {
      this.replyingTo = null;
    },
    
    replyToComment(comment) {
      this.replyingTo = comment;
      // 滚动到评论表单
      this.$nextTick(() => {
        const formElement = this.$refs.commentForm.$el;
        formElement.scrollIntoView({ behavior: 'smooth' });
      });
    }
  }
}
</script>

<style lang="scss">
.blog-post {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
  
  .post-container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    
    .post-main {
      flex: 1;
      min-width: 0;
      
      @media (min-width: 992px) {
        flex: 0 0 calc(70% - 1rem);
      }
    }
    
    .post-sidebar {
      width: 100%;
      
      @media (min-width: 992px) {
        flex: 0 0 calc(30% - 1rem);
      }
    }
  }
  
  .post-header {
    margin-bottom: 2rem;
    
    .post-title {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 1rem;
      line-height: 1.2;
    }
    
    .post-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: #666;
      
      .meta-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
      }
    }
  }
}
</style>

</script>

<style scoped>
.blog-post-page {
  animation: fadeIn 0.5s ease-in-out;
}

/* 文章头部 */
.post-header {
  padding: 80px 0;
  color: white;
  margin-bottom: 40px;
  background-size: cover;
  background-position: center;
  position: relative;
}

.post-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  font-size: 0.9rem;
  opacity: 0.9;
}

.post-title {
  font-size: 2.8rem;
  margin-bottom: 20px;
  line-height: 1.3;
}

.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 30px;
}

.post-tag {
  padding: 5px 12px;
  border-radius: 20px;
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  font-size: 0.85rem;
  transition: all 0.3s ease;
  cursor: pointer;
}

.post-tag:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.post-author {
  display: flex;
  align-items: center;
  gap: 15px;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: #f0f0f0;
}

.author-info h4 {
  margin-bottom: 5px;
  font-size: 1.1rem;
}

.author-info p {
  font-size: 0.9rem;
  opacity: 0.9;
}

/* 布局 */
.post-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 40px;
  margin-bottom: 60px;
}

/* 文章主体 */
.post-body {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #333;
  margin-bottom: 40px;
}

.post-body >>> h2 {
  font-size: 1.8rem;
  margin: 40px 0 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.post-body >>> h3 {
  font-size: 1.5rem;
  margin: 30px 0 15px;
}

.post-body >>> p {
  margin-bottom: 20px;
}

.post-body >>> blockquote {
  border-left: 4px solid #6a11cb;
  padding: 15px 20px;
  background-color: #f8f9fa;
  margin: 20px 0;
  font-style: italic;
  color: #555;
}

.post-body >>> pre {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  overflow-x: auto;
  margin: 20px 0;
  font-family: 'Courier New', Courier, monospace;
}

.post-body >>> code {
  background-color: #f8f9fa;
  padding: 2px 5px;
  border-radius: 3px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 0.9em;
}

.post-body >>> img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
  margin: 20px 0;
}

.post-body >>> ul, .post-body >>> ol {
  margin: 20px 0;
  padding-left: 20px;
}

.post-body >>> li {
  margin-bottom: 10px;
}

.post-body >>> a {
  color: #6a11cb;
  text-decoration: none;
  border-bottom: 1px dotted #6a11cb;
  transition: all 0.3s ease;
}

.post-body >>> a:hover {
  color: #2575fc;
  border-bottom-color: #2575fc;
}

.post-body >>> table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.post-body >>> th, .post-body >>> td {
  padding: 12px 15px;
  border: 1px solid #ddd;
  text-align: left;
}

.post-body >>> th {
  background-color: #f8f9fa;
  font-weight: 600;
}

.post-body >>> tr:nth-child(even) {
  background-color: #f8f9fa;
}

/* 文章底部 */
.post-footer {
  margin-top: 40px;
}

.post-actions {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
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

.action-btn.active {
  background-color: #6a11cb;
  color: white;
  border-color: #6a11cb;
}

/* 分享弹窗 */
.share-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  padding: 25px;
  width: 90%;
  max-width: 500px;
  z-index: 1000;
}

.share-popup-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.share-popup-header h4 {
  font-size: 1.3rem;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #6c757d;
  transition: color 0.3s ease;
}

.close-btn:hover {
  color: #dc3545;
}

.share-options {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 20px;
}

.share-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  text-decoration: none;
  color: #333;
  transition: transform 0.3s ease;
}

.share-option:hover {
  transform: translateY(-5px);
}

.share-option i {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
}

.share-option i.fa-weibo {
  background-color: #e6162d;
}

.share-option i.fa-weixin {
  background-color: #07c160;
}

.share-option i.fa-twitter {
  background-color: #1da1f2;
}

.share-option i.fa-facebook {
  background-color: #1877f2;
}

.share-option i.fa-linkedin {
  background-color: #0077b5;
}

.share-option span {
  font-size: 0.9rem;
}

.share-link {
  display: flex;
  margin-top: 20px;
}

.share-link input {
  flex: 1;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-right: none;
  border-radius: 5px 0 0 5px;
  font-size: 0.9rem;
}

.share-link input:focus {
  outline: none;
  border-color: #6a11cb;
}

.copy-btn {
  padding: 10px 15px;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.copy-btn:hover {
  background-color: #5a0cb6;
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

.author-box .author-avatar {
  width: 100px;
  height: 100px;
  border: none;
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
  margin-bottom: 15px;
}

.author-social {
  display: flex;
  gap: 15px;
}

.author-social a {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #e9ecef;
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
  margin-bottom: 30px;
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
  background-color: #f0f0f0;
}

.form-title {
  font-weight: 600;
  font-size: 1.1rem;
}

.comment-form textarea {
  width: 100%;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  resize: vertical;
  font-size: 0.95rem;
  margin-bottom: 15px;
}

.comment-form textarea:focus {
  outline: none;
  border-color: #6a11cb;
  box-shadow: 0 0 0 2px rgba(106, 17, 203, 0.1);
}

.form-footer {
  display: flex;
  justify-content: flex-end;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.comment-item {
  display: flex;
  gap: 20px;
}

.comment-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.comment-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: #f0f0f0;
}

.comment-content {
  flex: 1;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.comment-author {
  font-size: 1.1rem;
  margin: 0;
}

.comment-date {
  font-size: 0.85rem;
  color: #6c757d;
}

.comment-text {
  line-height: 1.6;
  margin-bottom: 15px;
}

.comment-actions {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
}

.comment-action {
  display: flex;
  align-items: center;
  gap: 5px;
  background: none;
  border: none;
  color: #6c757d;
  font-size: 0.9rem;
  cursor: pointer;
  transition: color 0.3s ease;
}

.comment-action:hover {
  color: #6a11cb;
}

.comment-action i.active {
  color: #6a11cb;
}

.replies-list {
  margin-left: 30px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.reply-item {
  display: flex;
  gap: 15px;
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 15px;
}

.reply-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.reply-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: #f0f0f0;
}

.reply-content {
  flex: 1;
}

.reply-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.reply-author {
  font-size: 1rem;
  margin: 0;
}

.reply-date {
  font-size: 0.8rem;
  color: #6c757d;
}

.reply-text {
  line-height: 1.6;
  margin-bottom: 10px;
}

.reply-to {
  color: #6a11cb;
  font-weight: 600;
  margin-right: 5px;
}

.reply-actions {
  display: flex;
  gap: 15px;
}

.reply-action {
  display: flex;
  align-items: center;
  gap: 5px;
  background: none;
  border: none;
  color: #6c757d;
  font-size: 0.85rem;
  cursor: pointer;
  transition: color 0.3s ease;
}

.reply-action:hover {
  color: #6a11cb;
}

.reply-action i.active {
  color: #6a11cb;
}

.reply-form {
  margin-top: 15px;
  background-color: #f8f9fa;
  border-radius: 5px;
  padding: 15px;
}

.reply-form textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  resize: vertical;
  font-size: 0.9rem;
  margin-bottom: 10px;
}

.reply-form textarea:focus {
  outline: none;
  border-color: #6a11cb;
  box-shadow: 0 0 0 2px rgba(106, 17, 203, 0.1);
}

.reply-form .form-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.btn-text {
  background: none;
  border: none;
  color: #6c757d;
  cursor: pointer;
  transition: color 0.3s ease;
}

.btn-text:hover {
  color: #dc3545;
}

.no-comments {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 0;
  text-align: center;
  color: #6c757d;
}

.no-comments i {
  font-size: 3rem;
  margin-bottom: 15px;
  color: #e9ecef;
}

/* 侧边栏 */
.post-sidebar {
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

/* 目录 */
.toc-container {
  max-height: 300px;
  overflow-y: auto;
}

.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-item {
  margin-bottom: 10px;
  padding-left: 0;
  transition: all 0.3s ease;
}

.toc-item a {
  color: #6c757d;
  text-decoration: none;
  display: block;
  padding: 5px 0;
  transition: color 0.3s ease;
  font-size: 0.95rem;
}

.toc-item a:hover {
  color: #6a11cb;
}

.toc-item.active a {
  color: #6a11cb;
  font-weight: 600;
}

.toc-level-2 {
  padding-left: 0;
}

.toc-level-3 {
  padding-left: 15px;
}

.no-toc {
  color: #6c757d;
  font-style: italic;
  text-align: center;
  padding: 20px 0;
}

/* 相关文章 */
.related-posts-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.related-post-item {
  display: flex;
  gap: 15px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.related-post-item:hover {
  transform: translateX(5px);
}

.related-post-image {
  flex: 0 0 70px;
  height: 70px;
  border-radius: 5px;
  overflow: hidden;
}

.related-post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: #f0f0f0;
}

.related-post-content {
  flex: 1;
}

.related-post-title {
  font-size: 1rem;
  margin-bottom: 5px;
  line-height: 1.4;
  transition: color 0.3s ease;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.related-post-item:hover .related-post-title {
  color: #6a11cb;
}

.related-post-meta {
  font-size: 0.8rem;
  color: #6c757d;
}

.no-related-posts {
  color: #6c757d;
  font-style: italic;
  text-align: center;
  padding: 20px 0;
}

/* 标签云 */
.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.sidebar-widget .post-tag {
  background-color: #f0f0f0;
  color: #6c757d;
}

.sidebar-widget .post-tag:hover {
  background-color: #6a11cb;
  color: white;
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

/* 文章导航 */
.post-navigation {
  display: flex;
  justify-content: space-between;
  margin-top: 60px;
  border-top: 1px solid #eee;
  padding-top: 30px;
}

.prev-post, .next-post {
  flex: 0 0 48%;
}

.next-post {
  text-align: right;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 15px;
  text-decoration: none;
  color: #333;
  transition: all 0.3s ease;
  padding: 15px;
  border-radius: 8px;
  background-color: #f8f9fa;
}

.nav-link:hover {
  background-color: #e9ecef;
}

.next-post .nav-link {
  flex-direction: row-reverse;
}

.nav-content {
  flex: 1;
}

.nav-label {
  display: block;
  font-size: 0.85rem;
  color: #6c757d;
  margin-bottom: 5px;
}

.nav-title {
  font-size: 1.1rem;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
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
  border: 4px solid rgba(106, 17, 203, 0.2);
  border-top-color: #6a11cb;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.error i, .not-found i {
  font-size: 3rem;
  color: #dc3545;
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

.error .btn, .not-found .btn {
  margin: 0 10px;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .post-layout {
    grid-template-columns: 1fr;
  }

  .post-sidebar {
    position: static;
    margin-top: 40px;
  }

  .post-navigation {
    flex-direction: column;
    gap: 20px;
  }

  .prev-post, .next-post {
    flex: 0 0 auto;
    width: 100%;
  }
}

@media (max-width: 768px) {
  .post-title {
    font-size: 2.2rem;
  }

  .post-meta {
    flex-wrap: wrap;
  }

  .author-box {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .author-details h3, .author-details h4 {
    text-align: center;
  }

  .author-social {
    justify-content: center;
  }

  .comment-item {
    flex-direction: column;
  }

  .comment-avatar {
    margin-bottom: 10px;
  }

  .replies-list {
    margin-left: 0;
  }
}

@media (max-width: 576px) {
  .post-header {
    padding: 60px 0;
  }

  .post-title {
    font-size: 1.8rem;
  }

  .post-actions {
    flex-wrap: wrap;
  }

  .action-btn {
    flex: 1;
    justify-content: center;
  }

  .share-options {
    justify-content: center;
  }
</style>