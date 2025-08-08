<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section about">
          <h3>关于我</h3>
          <p class="about-text">只是一个小程序员而已<br>Nothing is impossible<br>シンプルが一番</p>
          <div class="social-links">
            <a href="https://github.com/3159398370" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
              <i class="fab fa-github"></i>
            </a>
            <a href="https://space.bilibili.com/" target="_blank" rel="noopener noreferrer" aria-label="Bilibili">
              <i class="fab fa-bilibili"></i>
            </a>
            <a href="https://www.douyin.com/" target="_blank" rel="noopener noreferrer" aria-label="抖音">
              <i class="fab fa-tiktok"></i>
            </a>
          </div>
        </div>

        <div class="footer-section links">
          <h3>快速链接</h3>
          <ul>
            <li v-for="item in navItems" :key="item.path">
              <router-link :to="item.path">{{ item.name }}</router-link>
            </li>
          </ul>
        </div>

        <div class="footer-section contact">
          <h3>联系方式</h3>
          <p><i class="fas fa-envelope"></i> user_wrjc5857@foxmail.com</p>
          <p><i class="fas fa-map-marker-alt"></i> 陕西，西安</p>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-info">
          <span class="copyright">&copy; {{ currentYear }} Valrandy·Joseph. 保留所有权利。</span>
          <span class="separator">|</span>
          <span class="icp-info">
            <i class="fas fa-certificate icp-icon"></i>
            <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">陕ICP备2024055572号-1</a>
          </span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      navItems: [
        {name: '首页', path: '/'},
        {name: '作品集', path: '/projects'},
        {name: '代码仓库', path: '/repositories'},
        {name: '博客', path: '/blog'},
        {name: '关于我', path: '/about'},
      ],
    };
  },
  computed: {
    currentYear() {
      return new Date().getFullYear();
    },
  },
};
</script>

<style scoped>
.footer {
  background-color: #2c3e50;
  color: #fff;
  padding: 50px 0 20px;
  margin-top: auto;
}

.footer-content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-bottom: 30px;
}

.footer-section {
  flex: 1;
  min-width: 250px;
  margin-bottom: 20px;
  padding-right: 20px;
}

.footer-section h3 {
  font-size: 1.2rem;
  margin-bottom: 15px;
  position: relative;
  padding-bottom: 10px;
}

.footer-section h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 2px;
  background-color: #42b983;
}

.about-text {
  line-height: 1.8;
  font-size: 1rem;
  color: #f0f0f0;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3), 0 0 10px rgba(66, 185, 131, 0.3);
  margin-bottom: 20px;
  padding: 15px 20px;
  position: relative;
  border-left: 3px solid #42b983;
  background: linear-gradient(135deg, rgba(66, 185, 131, 0.1) 0%, rgba(66, 185, 131, 0.05) 100%);
  border-radius: 0 8px 8px 0;
  transition: all 0.3s ease;
}

.about-text:hover {
  background: linear-gradient(135deg, rgba(66, 185, 131, 0.15) 0%, rgba(66, 185, 131, 0.08) 100%);
  transform: translateX(5px);
  text-shadow: 0 2px 4px rgba(0,0,0,0.3), 0 0 15px rgba(66, 185, 131, 0.5);
}

.social-links {
  margin-top: 15px;
  display: flex;
  gap: 15px;
}

.social-links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  color: #fff;
  transition: all 0.3s ease;
}

.social-links a:hover {
  background-color: #42b983;
  transform: translateY(-3px);
}

.footer-section.links ul li {
  margin-bottom: 10px;
}

.footer-section.links a {
  color: #fff;
  transition: color 0.3s ease, transform 0.3s ease;
  display: inline-block;
}

.footer-section.links a:hover {
  color: #42b983;
  transform: translateX(5px);
}

.footer-section.contact p {
  margin-bottom: 10px;
  display: flex;
  align-items: center;
}

.footer-section.contact i {
  margin-right: 10px;
  color: #42b983;
}

.footer-bottom {
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-info {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  flex-wrap: wrap;
  font-size: 0.95em;
}

.copyright {
  color: #e8e8e8;
  font-weight: 500;
}

.separator {
  color: rgba(255, 255, 255, 0.4);
  font-weight: 300;
}

.icp-info {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #d0d0d0;
}

.icp-icon {
  color: #ffd700;
  font-size: 1em;
  filter: drop-shadow(0 0 3px rgba(255, 215, 0, 0.3));
}

.icp-info a {
  color: #d0d0d0;
  text-decoration: none;
  transition: all 0.3s ease;
  border-bottom: 1px solid transparent;
}

.icp-info a:hover {
  color: #ffd700;
  border-bottom-color: #ffd700;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
  }

  .footer-info {
    flex-direction: column;
    gap: 8px;
    font-size: 0.9em;
  }

  .separator {
    display: none;
  }

  .footer-section {
    padding-right: 0;
  }
}
</style>