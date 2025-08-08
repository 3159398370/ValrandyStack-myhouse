<template>
  <div class="about-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <!-- Company Logos in Corners -->
          <div class="corner-logos">
            <div class="corner-logo top-left adobe-brand">
                   <div class="adobe-logo-container">
                     <img src="@/assets/images/Adobe.png" alt="Adobe" class="adobe-logo-img" />
                     <span class="adobe-text">Adobe</span>
                   </div>
                 </div>
            
            <div class="corner-logo top-right jetbrains-brand">
                <svg class="jetbrains-logo-svg" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
                  <!-- JetBrains 2017 Logo Design -->
                  <defs>
                    <linearGradient id="jb-gradient-2017" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#3BEA62"/>
                      <stop offset="16%" stop-color="#087CFA"/>
                      <stop offset="33%" stop-color="#B345F1"/>
                      <stop offset="49%" stop-color="#ED358C"/>
                      <stop offset="66%" stop-color="#F97316"/>
                      <stop offset="82%" stop-color="#FCBA03"/>
                      <stop offset="100%" stop-color="#3BEA62"/>
                    </linearGradient>
                  </defs>
                  <rect width="120" height="120" rx="15" fill="url(#jb-gradient-2017)"/>
                  <rect x="15" y="15" width="90" height="90" rx="8" fill="#000000"/>
                  <text x="60" y="40" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="18" font-weight="bold">JetBrains</text>
                  <rect x="15" y="70" width="90" height="3" fill="white"/>
                  <text x="60" y="88" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="11">DEVELOP WITH</text>
                  <text x="60" y="100" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="11">PLEASURE!</text>
                </svg>
              </div>
          </div>
        
        <!-- Content at Bottom -->
        <div class="hero-content">
          <div class="title-container">
            <h1 class="hero-title animated-title">关于我</h1>
            <div class="hello-world-container">
              <span class="hello-world-text">{{ displayedText }}</span>
              <span class="cursor" :class="{ 'blink': showCursor }">|</span>
            </div>
          </div>
          <p class="hero-subtitle">全栈开发 · 视觉设计 · 3D建模</p>
          <div class="hero-description">
            <p>我是一名全栈开发者，专注于现代Web技术和创新解决方案。</p>
            <p>同时精通视觉设计、3D建模与动画制作，致力于创造完美的数字体验。</p>
            <p>拥有丰富的项目经验，熟练掌握多种编程语言、设计工具和建模软件。</p>
          </div>
          <div class="hero-tags">
            <span class="tag">前端开发</span>
            <span class="tag">后端开发</span>
            <span class="tag">UI/UX设计</span>
            <span class="tag">3D建模</span>
            <span class="tag">视频制作</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">技术栈</h2>
        <div class="skills-grid">
          <div class="skill-category">
            <h3>前端开发</h3>
            <div class="skill-items">
              <div class="skill-item">
                <i class="fab fa-vue"></i>
                <span>Vue.js</span>
              </div>
              <div class="skill-item">
                <i class="fab fa-react"></i>
                <span>React</span>
              </div>
              <div class="skill-item">
                <i class="fab fa-js-square"></i>
                <span>JavaScript</span>
              </div>
              <div class="skill-item">
                <i class="fab fa-html5"></i>
                <span>HTML5</span>
              </div>
              <div class="skill-item">
                <i class="fab fa-css3-alt"></i>
                <span>CSS3</span>
              </div>
            </div>
          </div>
          
          <div class="skill-category">
            <h3>后端开发</h3>
            <div class="skill-items">
              <div class="skill-item">
                <i class="fab fa-python"></i>
                <span>Python</span>
              </div>
              <div class="skill-item">
                <i class="fab fa-node-js"></i>
                <span>Node.js</span>
              </div>
              <div class="skill-item">
                <i class="fas fa-database"></i>
                <span>MySQL</span>
              </div>
              <div class="skill-item">
                <i class="fab fa-docker"></i>
                <span>Docker</span>
              </div>
            </div>
          </div>
          
          <div class="skill-category">
            <h3>视觉设计</h3>
            <div class="skill-items">
              <div class="skill-item">
                <i class="fas fa-palette"></i>
                <span>UI/UX设计</span>
              </div>
              <div class="skill-item">
                <i class="fas fa-image"></i>
                <span>平面设计</span>
              </div>

              <div class="skill-item">
                <i class="fas fa-vector-square"></i>
                <span>矢量插画</span>
              </div>
              <div class="skill-item">
                <i class="fas fa-photo-video"></i>
                <span>视频剪辑</span>
              </div>
            </div>
          </div>
          
          <div class="skill-category">
            <h3>3D建模</h3>
            <div class="skill-items">
              <div class="skill-item">
                <i class="fas fa-cube"></i>
                <span>3D建模</span>
              </div>


              <div class="skill-item">
                <i class="fas fa-running"></i>
                <span>角色动画</span>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tools Section -->
    <section class="tools-section">
      <div class="container">
        <h2 class="section-title">常用工具</h2>
        <p class="section-subtitle">这些是我日常开发中使用的专业工具</p>
        
        <!-- Scrolling Tools Display -->
        <div class="tools-showcase">
          <div class="tools-track">
            <!-- Adobe Suite -->
            <div class="tool-item">
              <div class="tool-logo adobe-pr">
                <!-- Adobe Premiere Pro icon from Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <rect width="256" height="256" rx="60" fill="#9999FF"/>
                  <path d="M90 70h40c30 0 50 20 50 50s-20 50-50 50h-20v36h-20V70zm20 20v60h20c20 0 30-10 30-30s-10-30-30-30h-20z" fill="white"/>
                  <path d="M170 130h20v76h-20v-10c-5 8-15 12-25 12-20 0-35-15-35-35s15-35 35-35c10 0 20 4 25 12v-20zm0 41c0-10-8-18-18-18s-18 8-18 18 8 18 18 18 18-8 18-18z" fill="white"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Adobe Premiere Pro</h4>
                <p>视频编辑</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo adobe-au">
                <!-- Adobe Audition icon from Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <rect width="256" height="256" rx="60" fill="#00E4FF"/>
                  <path d="M128 70l-8 20h-32l-8-20h-20l35 116h18l35-116h-20zm-20 40h24l-12-30-12 30z" fill="white"/>
                  <path d="M170 130v56h-20v-8c-5 6-12 10-20 10-15 0-25-10-25-25v-33h20v28c0 5 3 8 8 8s8-3 8-8v-28h29z" fill="white"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Adobe Audition</h4>
                <p>音频处理</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo adobe-an">
                <!-- Adobe Animate icon from Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <rect width="256" height="256" rx="60" fill="#FF9A00"/>
                  <path d="M128 70l-8 20h-32l-8-20h-20l35 116h18l35-116h-20zm-20 40h24l-12-30-12 30z" fill="white"/>
                  <path d="M170 130v56h-20v-8c-5 6-12 10-20 10-15 0-25-10-25-25v-33h20v28c0 5 3 8 8 8s8-3 8-8v-28h29z" fill="white"/>
                  <circle cx="190" cy="140" r="8" fill="white"/>
                  <circle cx="190" cy="165" r="6" fill="white" opacity="0.7"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Adobe Animate</h4>
                <p>动画制作</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo adobe-ae">
                <!-- Adobe After Effects icon from Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <rect width="256" height="256" rx="60" fill="#9999FF"/>
                  <path d="M128 70l-8 20h-32l-8-20h-20l35 116h18l35-116h-20zm-20 40h24l-12-30-12 30z" fill="white"/>
                  <path d="M170 130h30v15h-30v20h35v15h-55v-76h55v15h-35v11z" fill="white"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Adobe After Effects</h4>
                <p>视觉特效</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo adobe-ps">
                <!-- Adobe Photoshop icon from Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <rect width="256" height="256" rx="60" fill="#31A8FF"/>
                  <path d="M70 70h40c25 0 45 20 45 45s-20 45-45 45h-20v26h-20V70zm20 20v50h20c15 0 25-10 25-25s-10-25-25-25h-20z" fill="white"/>
                  <path d="M170 130c-15 0-25 10-25 25s10 25 25 25c8 0 15-3 20-8l10 12c-8 8-20 12-30 12-25 0-45-20-45-45s20-45 45-45c10 0 22 4 30 12l-10 12c-5-5-12-8-20-8z" fill="white"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Adobe Photoshop</h4>
                <p>图像处理</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo adobe-ai">
                <!-- Adobe Illustrator icon from Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <rect width="256" height="256" rx="60" fill="#FF9A00"/>
                  <path d="M128 70l-8 20h-32l-8-20h-20l35 116h18l35-116h-20zm-20 40h24l-12-30-12 30z" fill="white"/>
                  <path d="M170 130v76h-20v-76h20zm-10-20c-6 0-10-4-10-10s4-10 10-10 10 4 10 10-4 10-10 10z" fill="white"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Adobe Illustrator</h4>
                <p>矢量设计</p>
              </div>
            </div>
            
            <!-- JetBrains Suite -->
            <div class="tool-item">
              <div class="tool-logo jetbrains-idea">
                <!-- IntelliJ IDEA icon from JetBrains official -->
                <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="ideaGradient" x1="14.5%" y1="14.5%" x2="85.5%" y2="85.5%">
                      <stop offset="0%" stop-color="#087CFA"/>
                      <stop offset="8.5%" stop-color="#087CFA"/>
                      <stop offset="19.1%" stop-color="#B85EFF"/>
                      <stop offset="30.6%" stop-color="#FE315D"/>
                      <stop offset="100%" stop-color="#FE315D"/>
                    </linearGradient>
                  </defs>
                  <rect width="70" height="70" rx="6" fill="url(#ideaGradient)"/>
                  <rect x="8" y="50" width="54" height="12" rx="2" fill="#000"/>
                  <text x="35" y="59" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="white">IntelliJ IDEA</text>
                </svg>
              </div>
              <div class="tool-info">
                <h4>IntelliJ IDEA</h4>
                <p>Java开发</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo jetbrains-pycharm">
                <!-- PyCharm icon from JetBrains official -->
                <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="pycharmGradient" x1="14.5%" y1="14.5%" x2="85.5%" y2="85.5%">
                      <stop offset="0%" stop-color="#21D789"/>
                      <stop offset="8.5%" stop-color="#21D789"/>
                      <stop offset="19.1%" stop-color="#07C3F2"/>
                      <stop offset="30.6%" stop-color="#07C3F2"/>
                      <stop offset="100%" stop-color="#07C3F2"/>
                    </linearGradient>
                  </defs>
                  <rect width="70" height="70" rx="6" fill="url(#pycharmGradient)"/>
                  <rect x="8" y="50" width="54" height="12" rx="2" fill="#000"/>
                  <text x="35" y="59" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="white">PyCharm</text>
                </svg>
              </div>
              <div class="tool-info">
                <h4>PyCharm</h4>
                <p>Python开发</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo jetbrains-clion">
                <!-- CLion icon from JetBrains official -->
                <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="clionGradient" x1="14.5%" y1="14.5%" x2="85.5%" y2="85.5%">
                      <stop offset="0%" stop-color="#ED358C"/>
                      <stop offset="8.5%" stop-color="#ED358C"/>
                      <stop offset="19.1%" stop-color="#F9C23C"/>
                      <stop offset="30.6%" stop-color="#F9C23C"/>
                      <stop offset="100%" stop-color="#F9C23C"/>
                    </linearGradient>
                  </defs>
                  <rect width="70" height="70" rx="6" fill="url(#clionGradient)"/>
                  <rect x="8" y="50" width="54" height="12" rx="2" fill="#000"/>
                  <text x="35" y="59" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="white">CLion</text>
                </svg>
              </div>
              <div class="tool-info">
                <h4>CLion</h4>
                <p>C/C++开发</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo jetbrains-datagrip">
                <!-- DataGrip icon from JetBrains official -->
                <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="datagripGradient" x1="14.5%" y1="14.5%" x2="85.5%" y2="85.5%">
                      <stop offset="0%" stop-color="#9775FA"/>
                      <stop offset="8.5%" stop-color="#9775FA"/>
                      <stop offset="19.1%" stop-color="#22D3EE"/>
                      <stop offset="30.6%" stop-color="#22D3EE"/>
                      <stop offset="100%" stop-color="#22D3EE"/>
                    </linearGradient>
                  </defs>
                  <rect width="70" height="70" rx="6" fill="url(#datagripGradient)"/>
                  <rect x="8" y="50" width="54" height="12" rx="2" fill="#000"/>
                  <text x="35" y="59" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="white">DataGrip</text>
                </svg>
              </div>
              <div class="tool-info">
                <h4>DataGrip</h4>
                <p>数据库管理</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo jetbrains-webstorm">
                <!-- WebStorm icon from JetBrains official -->
                <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="webstormGradient" x1="14.5%" y1="14.5%" x2="85.5%" y2="85.5%">
                      <stop offset="0%" stop-color="#07C3F2"/>
                      <stop offset="8.5%" stop-color="#07C3F2"/>
                      <stop offset="19.1%" stop-color="#087CFA"/>
                      <stop offset="30.6%" stop-color="#087CFA"/>
                      <stop offset="100%" stop-color="#087CFA"/>
                    </linearGradient>
                  </defs>
                  <rect width="70" height="70" rx="6" fill="url(#webstormGradient)"/>
                  <rect x="8" y="50" width="54" height="12" rx="2" fill="#000"/>
                  <text x="35" y="59" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="white">WebStorm</text>
                </svg>
              </div>
              <div class="tool-info">
                <h4>WebStorm</h4>
                <p>Web开发</p>
              </div>
            </div>
            
            <!-- Other Tools -->
            <div class="tool-item">
              <div class="tool-logo substance">
                <!-- Substance 3D Painter icon from Adobe/Flaticon -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="substanceGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#FF6B35"/>
                      <stop offset="50%" stop-color="#F7931E"/>
                      <stop offset="100%" stop-color="#FFD23F"/>
                    </linearGradient>
                  </defs>
                  <rect width="256" height="256" rx="60" fill="url(#substanceGradient)"/>
                  <path d="M128 50c-43 0-78 35-78 78s35 78 78 78 78-35 78-78-35-78-78-78zm0 20c32 0 58 26 58 58s-26 58-58 58-58-26-58-58 26-58 58-58z" fill="white"/>
                  <circle cx="128" cy="128" r="25" fill="white"/>
                  <path d="M90 90l76 76M166 90l-76 76" stroke="white" stroke-width="8" stroke-linecap="round"/>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Substance 3D Painter</h4>
                <p>3D纹理绘制</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo blender">
                <i class="fab fa-blender"></i>
              </div>
              <div class="tool-info">
                <h4>Blender</h4>
                <p>3D建模动画</p>
              </div>
            </div>
            
            <div class="tool-item">
              <div class="tool-logo marvelous">
                <!-- Marvelous Designer icon from design resources -->
                <svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="marvelousGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#E91E63"/>
                      <stop offset="50%" stop-color="#9C27B0"/>
                      <stop offset="100%" stop-color="#673AB7"/>
                    </linearGradient>
                  </defs>
                  <rect width="256" height="256" rx="60" fill="url(#marvelousGradient)"/>
                  <path d="M128 50l-30 40h60l-30-40z" fill="white" opacity="0.9"/>
                  <path d="M80 100h96l-20 60H100l-20-60z" fill="white" opacity="0.8"/>
                  <path d="M100 160h56l-8 30h-40l-8-30z" fill="white" opacity="0.7"/>
                  <text x="128" y="220" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="white">MD</text>
                </svg>
              </div>
              <div class="tool-info">
                <h4>Marvelous Designer</h4>
                <p>服装设计</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section">
      <div class="container">
        <h2 class="section-title">联系方式</h2>
        <div class="contact-info">
          <div class="contact-item">
            <i class="fas fa-envelope"></i>
            <span>user_wrjc5857@foxmail.com</span>
          </div>
          <div class="contact-item">
            <i class="fas fa-map-marker-alt"></i>
            <span>陕西，西安</span>
          </div>
        </div>
        
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
    </section>
  </div>
</template>

<script>
export default {
  name: 'About',
  data() {
    return {
      displayedText: '',
      fullText: 'Hello, World!',
      typewriterIndex: 0,
      showCursor: true,
      typewriterSpeed: 150
    };
  },
  mounted() {
    // 添加滚动动画
    this.initScrollAnimations();
    // 启动打字机效果
    this.startTypewriter();
    // 启动光标闪烁
    this.startCursorBlink();
  },
  methods: {
    startTypewriter() {
      if (this.typewriterIndex < this.fullText.length) {
        this.displayedText += this.fullText.charAt(this.typewriterIndex);
        this.typewriterIndex++;
        setTimeout(() => {
          this.startTypewriter();
        }, this.typewriterSpeed);
      }
    },
    
    startCursorBlink() {
      setInterval(() => {
        this.showCursor = !this.showCursor;
      }, 500);
    },
    
    initScrollAnimations() {
      const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      };
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
          }
        });
      }, observerOptions);
      
      // 观察所有需要动画的元素
      const animateElements = this.$el.querySelectorAll('.skill-category, .tool-item, .contact-item');
      animateElements.forEach(el => observer.observe(el));
    }
  }
};
</script>

<style scoped>
.about-page {
  min-height: 100vh;
}

/* Hero Section */
.hero-section {
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #667eea 100%);
  color: white;
  padding: 60px 0;
  text-align: center;
  position: relative;
  overflow: hidden;
  min-height: 100vh;
  display: flex;
  align-items: center;
}

.hero-section .container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 80vh;
  width: 100%;
}

/* Corner Logos */
.corner-logos {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.corner-logo {
  position: absolute;
  width: 120px;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  cursor: pointer;
  pointer-events: auto;
}

.corner-logo.top-left {
  top: 2rem;
  left: 2rem;
}

.corner-logo.top-right {
  top: 2rem;
  right: 2rem;
}

.corner-logo:hover {
  transform: scale(1.15);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
}

.adobe-logo-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
  }

.adobe-logo-img {
  width: 60px;
  height: 60px;
  object-fit: contain;
}

.adobe-text {
  font-family: 'Arial', sans-serif;
  font-size: 18px;
  font-weight: bold;
  color: #2C2C2C;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.jetbrains-logo-svg {
  width: 100px;
  height: 100px;
  filter: drop-shadow(0 10px 20px rgba(0,0,0,0.3));
}

/* Content at Bottom */
.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
  margin: 0 auto;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Title Container */
.title-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.hero-title {
  font-size: 4rem;
  font-weight: 700;
  background: linear-gradient(45deg, #fff, #f0f0f0);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* Title Animation */
.animated-title {
  /* animation removed */
}

@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100px);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes glow {
  0% {
    text-shadow: 0 4px 20px rgba(0,0,0,0.3), 0 0 10px rgba(255,255,255,0.2);
  }
  100% {
    text-shadow: 0 4px 20px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.4), 0 0 30px rgba(255,255,255,0.2);
  }
}

/* Hello World Container */
.hello-world-container {
  display: flex;
  align-items: center;
  font-family: 'Courier New', monospace;
  font-size: 1.5rem;
  color: #00ff41;
  text-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
  background: rgba(0, 0, 0, 0.3);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 1px solid rgba(0, 255, 65, 0.3);
  backdrop-filter: blur(5px);
  animation: slideInFromRight 1s ease-out 0.5s both;
}

@keyframes slideInFromRight {
  0% {
    transform: translateX(100px);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

.hello-world-text {
  margin-right: 2px;
}

.cursor {
  font-weight: bold;
  color: #00ff41;
  animation: none;
}

.cursor.blink {
  opacity: 1;
}

.cursor:not(.blink) {
  opacity: 0;
}

.hero-subtitle {
  font-size: 1.8rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  font-weight: 300;
  letter-spacing: 1px;
}

.hero-description {
  max-width: 700px;
  margin: 0 auto 2rem;
  font-size: 1.2rem;
  line-height: 1.8;
  opacity: 0.85;
}

.hero-tags {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.tag {
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.3);
  padding: 0.5rem 1.5rem;
  border-radius: 25px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
  cursor: default;
}

.tag:hover {
  background: rgba(255,255,255,0.3);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

/* Skills Section */
.skills-section {
  padding: 80px 0;
  background: #f8f9fa;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.section-subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: #6c757d;
  margin-bottom: 3rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.skill-category {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  opacity: 0;
  transform: translateY(30px);
}

.skill-category.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.skill-category:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.skill-category h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: #2c3e50;
  text-align: center;
}

.skill-items {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.skill-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 10px;
  transition: all 0.3s ease;
  min-width: 80px;
}

.skill-item:hover {
  background: #e9ecef;
  transform: translateY(-2px);
}

.skill-item i {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #42b983;
}

.skill-item span {
  font-size: 0.9rem;
  font-weight: 500;
  color: #2c3e50;
}

/* Tools Section */
.tools-section {
  padding: 80px 0;
  background: white;
  overflow: hidden;
}

.tools-showcase {
  margin-top: 3rem;
  position: relative;
  overflow: hidden;
  padding: 2rem 0;
}

.tools-track {
  display: flex;
  gap: 2rem;
  animation: scroll 30s linear infinite;
  width: calc(300px * 14 + 2rem * 13); /* 14个工具项 */
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(-300px * 7 - 2rem * 6)); /* 滚动一半的距离 */
  }
}

.tools-track:hover {
  animation-play-state: paused;
}

.tool-item {
  flex: 0 0 280px;
  background: white;
  border-radius: 15px;
  padding: 1.5rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 1rem;
  opacity: 0;
  transform: translateY(30px);
}

.tool-item.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.tool-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.tool-logo {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
  color: white;
  flex-shrink: 0;
}

.tool-logo svg {
  width: 100%;
  height: 100%;
  border-radius: 12px;
}

/* Tool logo containers - no background needed for SVG icons */
.adobe-pr, .adobe-au, .adobe-an, .adobe-ae, .adobe-ps, .adobe-ai,
.jetbrains-idea, .jetbrains-pycharm, .jetbrains-clion, .jetbrains-datagrip, .jetbrains-webstorm,
.substance, .marvelous {
  background: transparent;
}

/* Keep background for tools that still use FontAwesome icons */
.blender { background: linear-gradient(45deg, #ff6b35, #f7931e); }

.tool-logo i {
  font-size: 1.8rem;
}

.tool-info h4 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: #2c3e50;
}

.tool-info p {
  font-size: 0.9rem;
  color: #6c757d;
  margin: 0;
}

/* Contact Section */
.contact-section {
  padding: 80px 0;
  background: #f8f9fa;
  text-align: center;
}

.contact-info {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.1rem;
  color: #2c3e50;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.5s ease;
}

.contact-item.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.contact-item i {
  color: #42b983;
  font-size: 1.2rem;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

.social-links a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background: #42b983;
  color: white;
  border-radius: 50%;
  transition: all 0.3s ease;
  text-decoration: none;
}

.social-links a:hover {
  background: #369870;
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(66, 185, 131, 0.3);
}

.social-links i {
  font-size: 1.2rem;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-section {
    min-height: 100vh;
    padding: 40px 0;
  }
  
  .hero-section .container {
    min-height: 90vh;
  }
  
  .corner-logo {
    width: 90px;
    height: 90px;
  }
  
  .corner-logo.top-left {
    top: 1rem;
    left: 1rem;
  }
  
  .corner-logo.top-right {
    top: 1rem;
    right: 1rem;
  }
  
  .adobe-logo-img {
    width: 45px;
    height: 45px;
  }
  
  .adobe-text {
    font-size: 14px;
  }
  
  .jetbrains-logo-svg {
    width: 70px;
    height: 70px;
  }
  
  .title-container {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hello-world-container {
    font-size: 1.2rem;
    padding: 0.4rem 0.8rem;
  }
  
  .hero-subtitle {
    font-size: 1.3rem;
  }
  
  .hero-description {
    font-size: 1rem;
  }
  
  .hero-tags {
    gap: 0.5rem;
  }
  
  .tag {
    font-size: 0.8rem;
    padding: 0.4rem 1rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .skills-grid {
    grid-template-columns: 1fr;
  }
  
  .contact-info {
    flex-direction: column;
    gap: 1rem;
  }
  
  .tools-track {
    gap: 1rem;
  }
  
  .tool-item {
    flex: 0 0 250px;
  }
  
  .container {
    padding: 0 1rem;
  }
}

@media (max-width: 480px) {
  .hero-section {
    padding: 100px 0 60px;
  }
  
  .skills-section,
  .tools-section,
  .contact-section {
    padding: 60px 0;
  }
  
  .tool-item {
    flex-direction: column;
    text-align: center;
    flex: 0 0 200px;
  }
  
  .tool-logo {
    margin-bottom: 1rem;
  }
}
</style>