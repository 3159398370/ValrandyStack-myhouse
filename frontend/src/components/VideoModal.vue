<template>
  <div v-if="show" class="video-modal-overlay" @click.self="close">
    <div class="video-modal">
      <div class="video-modal-header">
        <h3 class="modal-title">{{ video ? video.title : '' }}</h3>
        <button class="close-btn" @click="close">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <div class="video-modal-content">
        <div class="video-player-container">
          <!-- 视频占位符，点击后切换到播放器 -->
          <div v-if="!isPlaying && video" class="video-placeholder" @click="startPlaying">
            <img :src="video.cover" :alt="video.title" class="modal-video-cover" />
            <div class="play-icon-overlay">
              <i class="fas fa-play"></i>
            </div>
            <div class="video-duration-badge">{{ formatDuration(video.duration) }}</div>
          </div>
          
          <!-- Bilibili 视频播放器 -->
          <div v-else-if="isPlaying && video" class="bilibili-player">
            <iframe 
              :src="getBilibiliEmbedUrl(video.bvid)" 
              scrolling="no" 
              border="0" 
              frameborder="no" 
              framespacing="0" 
              allowfullscreen="true"
              width="100%"
              height="100%"
              style="aspect-ratio: 16 / 9;"
            ></iframe>
          </div>
          
          <div class="video-description">
            {{ video ? video.description : '' }}
          </div>
          <div class="video-meta-info">
            <span>{{ video ? video.viewCount : '' }} 播放</span>
            <span>{{ video ? formatDate(video.publishDate) : '' }}</span>
          </div>
        </div>
      </div>
      <div class="video-modal-footer">
        <button class="view-original-btn" @click="viewOriginal">
          <i class="fas fa-external-link-alt"></i>
          查看原视频
        </button>
        <button class="close-modal-btn" @click="close">
          <i class="fas fa-times"></i>
          关闭
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoModal',
  props: {
    show: {
      type: Boolean,
      default: false
    },
    video: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      // 控制视频是否正在播放
      isPlaying: false
    };
  },
  methods: {
    close() {
      // 重置播放状态
      this.isPlaying = false;
      // 关闭背景滚动
      document.body.style.overflow = '';
      // 通知父组件关闭弹窗
      this.$emit('close');
    },
    viewOriginal() {
      if (this.video && this.video.bvid) {
        const url = `https://www.bilibili.com/video/${this.video.bvid}`;
        window.open(url, '_blank');
      }
    },
    formatDuration(duration) {
      // 格式化时长
      if (!duration || duration < 0) return '00:00';
      const minutes = Math.floor(duration / 60);
      const seconds = duration % 60;
      return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    },
    formatDate(dateString) {
      // 格式化日期
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleDateString('zh-CN');
    },
    // 开始播放视频
    startPlaying() {
      this.isPlaying = true;
    },
    // 获取Bilibili视频嵌入链接
    getBilibiliEmbedUrl(bvid) {
      if (!bvid) return '';
      // Bilibili嵌入播放器的URL格式
      return `https://player.bilibili.com/player.html?aid=&cid=&bvid=${bvid}&page=1&as_wide=1&high_quality=1&danmaku=1`;
    }
  },
  watch: {
    show(newVal) {
      if (newVal) {
        // 阻止背景滚动
        document.body.style.overflow = 'hidden';
      } else {
        // 恢复背景滚动
        document.body.style.overflow = '';
        // 重置播放状态
        this.isPlaying = false;
      }
    },
    // 当视频信息变化时，重置播放状态
    video: {
      handler() {
        this.isPlaying = false;
      },
      deep: true
    }
  }
};
</script>

<style scoped>
.video-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.video-modal {
  background: #fff;
  border-radius: 8px;
  max-width: 900px;
  width: 90%;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
  animation: slideIn 0.3s ease;
  overflow: hidden;
}

@keyframes slideIn {
  from {
    transform: translateY(-20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.video-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid #eee;
  background: #f8f9fa;
}

.modal-title {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #333;
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding-right: 20px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #999;
  cursor: pointer;
  padding: 5px;
  transition: color 0.3s ease;
}

.close-btn:hover {
  color: #333;
}

.video-modal-content {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.video-player-container {
  display: flex;
  flex-direction: column;
}

.video-placeholder {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  margin-bottom: 16px;
  background-color: #000;
  border-radius: 4px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.video-placeholder:hover {
  transform: scale(1.01);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.modal-video-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.3s ease;
}

.video-placeholder:hover .modal-video-cover {
  opacity: 0.9;
}

.play-icon-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.6);
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  opacity: 0.8;
}

.video-placeholder:hover .play-icon-overlay {
  transform: translate(-50%, -50%) scale(1.1);
  opacity: 1;
  background: rgba(255, 107, 107, 0.8);
}

.play-icon-overlay i {
  color: #fff;
  font-size: 32px;
  margin-left: 4px;
}

.video-duration-badge {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

/* Bilibili播放器样式 */
.bilibili-player {
  width: 100%;
  background-color: #000;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 16px;
  transition: all 0.3s ease;
}

.bilibili-player iframe {
  border: none;
}

.video-description {
  margin-bottom: 12px;
  color: #666;
  line-height: 1.6;
  font-size: 14px;
}

.video-meta-info {
  display: flex;
  gap: 20px;
  color: #999;
  font-size: 12px;
  margin-bottom: 16px;
}

.video-modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding: 16px 20px;
  border-top: 1px solid #eee;
  background: #f8f9fa;
}

.view-original-btn,
.close-modal-btn {
  padding: 8px 20px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}

.view-original-btn {
  background: #ff6b6b;
  color: #fff;
}

.view-original-btn:hover {
  background: #ff5252;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(255, 107, 107, 0.3);
}

.close-modal-btn {
  background: #e9ecef;
  color: #495057;
}

.close-modal-btn:hover {
  background: #dee2e6;
  transform: translateY(-1px);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .video-modal {
    width: 95%;
    max-height: 95vh;
  }
  
  .video-modal-header,
  .video-modal-content,
  .video-modal-footer {
    padding: 12px 16px;
  }
  
  .modal-title {
    font-size: 16px;
  }
  
  .video-modal-footer {
    flex-direction: column;
  }
  
  .view-original-btn,
  .close-modal-btn {
    width: 100%;
    justify-content: center;
  }
  
  .play-icon-overlay {
    width: 60px;
    height: 60px;
  }
  
  .play-icon-overlay i {
    font-size: 24px;
  }
}
</style>