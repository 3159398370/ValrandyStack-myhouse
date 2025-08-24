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
             <div class="css-showcase-container">
               <div class="showcase-header">
                 <h1 class="title-glitch">CSS动画展示台</h1>
                 <p class="subtitle">视觉展示</p>
               </div>

               <div class="showcase-grid" :class="{ 'expanded': showMoreAnimations }">
                 <!-- 3D旋转卡片 -->
                <div 
                  class="showcase-item" 
                  :class="{ 'selected': selectedAnimation === 'card3d' }"
                  data-animation-type="card3d" 
                  @mouseenter="playAnimation('card3d')" 
                  @mouseleave="pauseAnimation('card3d')" 
                  @click="playAnimation('card3d')"
                >
                  <div class="lily-petals" v-if="selectedAnimation === 'card3d'">
                    <div 
                      v-for="n in 8" 
                      :key="n"
                      class="petal"
                      :style="{
                        '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                        '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                        '--r': `${n * 45}deg`,
                        'animation-delay': `${n * 0.2}s`
                      }"
                    ></div>
                  </div>
                   <div class="card-3d" :class="{ 'playing': animations.card3d }">
                     <div class="card-face front">3D卡片</div>
                     <div class="card-face back">悬停查看</div>
                   </div>
                   <div class="item-info">
                     <h3>3D翻转卡片</h3>
                     <p>鼠标悬停触发3D翻转效果</p>
                   </div>
                 </div>

                 <!-- 粒子系统 -->
                <div 
                  class="showcase-item" 
                  :class="{ 'selected': selectedAnimation === 'particles' }"
                  data-animation-type="particles" 
                  @mouseenter="playAnimation('particles')" 
                  @mouseleave="pauseAnimation('particles')" 
                  @click="playAnimation('particles')"
                >
                  <div class="lily-petals" v-if="selectedAnimation === 'particles'">
                    <div 
                      v-for="n in 8" 
                      :key="n"
                      class="petal"
                      :style="{
                        '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                        '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                        '--r': `${n * 45}deg`,
                        'animation-delay': `${n * 0.2}s`
                      }"
                    ></div>
                  </div>
                   <div class="particle-container" :class="{ 'playing': animations.particles }">
                     <div v-for="n in 50" :key="n" class="particle" :style="getParticleStyle(n)"></div>
                     <div v-for="n in 30" :key="'glow-'+n" class="particle-glow" :style="getParticleStyle(n + 50)"></div>
                   </div>
                   <div class="item-info">
                     <h3>粒子动画</h3>
                     <p>华丽粒子漂浮效果</p>
                   </div>
                 </div>

                 <!-- 霓虹文字 -->
                  <div 
                    class="showcase-item" 
                    :class="{ 'selected': selectedAnimation === 'neon' }"
                    data-animation-type="neon" 
                    @mouseenter="playAnimation('neon')" 
                    @mouseleave="pauseAnimation('neon')" 
                    @click="playAnimation('neon')"
                  >
                    <div class="lily-petals" v-if="selectedAnimation === 'neon'">
                      <div 
                        v-for="n in 8" 
                        :key="n"
                        class="petal"
                        :style="{
                          '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                          '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                          '--r': `${n * 45}deg`,
                          'animation-delay': `${n * 0.2}s`
                        }"
                      ></div>
                    </div>
                   <div class="neon-text" :class="{ 'playing': animations.neon }">
                     <span class="neon-glow">NEON</span>
                   </div>
                   <div class="item-info">
                     <h3>霓虹发光</h3>
                     <p>炫酷的发光文字效果</p>
                   </div>
                 </div>

                 <!-- 可变大小的震撼连点器 -->
                <div class="showcase-item" @click="handleClickCounter">
                  
                  <div class="click-counter-container" :class="{ 'clicked': clickCount > 0 }" :style="{ transform: `scale(${ballSize})`, background: currentColor }">
                    <div class="counter-display">{{ clickCount }}</div>
                  </div>
                  <div class="item-info">
                    <h3>连点器</h3>
                    <p>点击{{ clickCount }}次！{{ getClickMessage() }}</p>
                  </div>
                </div>

                 <!-- 更多效果（默认隐藏） -->
                 <template v-if="showMoreAnimations">
                   <!-- 星空背景 -->
          <div 
            class="showcase-item" 
            :class="{ 'selected': selectedAnimation === 'starry' }"
            data-animation-type="starry" 
            @mouseenter="playAnimation('starry')" 
            @mouseleave="pauseAnimation('starry')" 
            @click="playAnimation('starry')"
          >
            <div class="lily-petals" v-if="selectedAnimation === 'starry'">
              <div 
                v-for="n in 8" 
                :key="n"
                class="petal"
                :style="{
                  '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                  '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                  '--r': `${n * 45}deg`,
                  'animation-delay': `${n * 0.2}s`
                }"
              ></div>
            </div>
            <div class="starry-sky" :class="{ 'playing': animations.starry }">
              <div v-for="star in 120" :key="star" class="star" :style="getStarStyle(star)"></div>
              <div v-for="star in 20" :key="'bright-'+star" class="star bright" :style="getStarStyle(star + 120)"></div>
            </div>
            <div class="item-info">
              <h3>星空动画</h3>
              <p>华丽星空闪烁效果</p>
            </div>
          </div>

                 <!-- 进度环 -->
                 <div 
                   class="showcase-item" 
                   :class="{ 'selected': selectedAnimation === 'progress' }"
                   data-animation-type="progress" 
                   @mouseenter="playAnimation('progress')" 
                   @mouseleave="pauseAnimation('progress')" 
                   @click="playAnimation('progress')"
                 >
                   <div class="lily-petals" v-if="selectedAnimation === 'progress'">
                     <div 
                       v-for="n in 8" 
                       :key="n"
                       class="petal"
                       :style="{
                         '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                         '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                         '--r': `${n * 45}deg`,
                         'animation-delay': `${n * 0.2}s`
                       }"
                     ></div>
                   </div>
                   <div class="progress-ring" :class="{ 'playing': animations.progress }">
                     <svg class="progress-svg" viewBox="0 0 100 100">
                       <circle class="progress-bg" cx="50" cy="50" r="45"></circle>
                       <circle class="progress-bar" cx="50" cy="50" r="45"></circle>
                     </svg>
                     <div class="progress-text">75%</div>
                   </div>
                   <div class="item-info">
                     <h3>环形进度</h3>
                     <p>动态进度指示器</p>
                   </div>
                 </div>

                 <!-- 故障效果 -->
                 <div 
                   class="showcase-item" 
                   :class="{ 'selected': selectedAnimation === 'glitch' }"
                   data-animation-type="glitch" 
                   @mouseenter="playAnimation('glitch')" 
                   @mouseleave="pauseAnimation('glitch')" 
                   @click="playAnimation('glitch')"
                 >
                   <div class="lily-petals" v-if="selectedAnimation === 'glitch'">
                     <div 
                       v-for="n in 8" 
                       :key="n"
                       class="petal"
                       :style="{
                         '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                         '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                         '--r': `${n * 45}deg`,
                         'animation-delay': `${n * 0.2}s`
                       }"
                     ></div>
                   </div>
                   <div class="glitch-text" :class="{ 'playing': animations.glitch }">
                     <span class="glitch-main">GLITCH</span>
                     <span class="glitch-overlay" aria-hidden="true">GLITCH</span>
                     <span class="glitch-overlay-2" aria-hidden="true">GLITCH</span>
                   </div>
                   <div class="item-info">
                     <h3>故障艺术</h3>
                     <p>数字故障视觉效果</p>
                   </div>
                 </div>

                 <!-- 波浪动画 -->
                 <div 
                   class="showcase-item" 
                   :class="{ 'selected': selectedAnimation === 'wave' }"
                   data-animation-type="wave" 
                   @mouseenter="playAnimation('wave')" 
                   @mouseleave="pauseAnimation('wave')" 
                   @click="playAnimation('wave')"
                 >
                   <div class="lily-petals" v-if="selectedAnimation === 'wave'">
                     <div 
                       v-for="n in 8" 
                       :key="n"
                       class="petal"
                       :style="{
                         '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                         '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                         '--r': `${n * 45}deg`,
                         'animation-delay': `${n * 0.2}s`
                       }"
                     ></div>
                   </div>
                   <div class="wave-container" :class="{ 'playing': animations.wave }">
                     <div class="wave wave-1"></div>
                     <div class="wave wave-2"></div>
                     <div class="wave wave-3"></div>
                   </div>
                   <div class="item-info">
                     <h3>波浪动画</h3>
                     <p>流畅的波浪效果</p>
                   </div>
                 </div>

                 <!-- 脉冲按钮 -->
                 <div 
                   class="showcase-item" 
                   :class="{ 'selected': selectedAnimation === 'pulse' }"
                   data-animation-type="pulse" 
                   @mouseenter="playAnimation('pulse')" 
                   @mouseleave="pauseAnimation('pulse')" 
                   @click="playAnimation('pulse')"
                 >
                   <div class="lily-petals" v-if="selectedAnimation === 'pulse'">
                     <div 
                       v-for="n in 8" 
                       :key="n"
                       class="petal"
                       :style="{
                         '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                         '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                         '--r': `${n * 45}deg`,
                         'animation-delay': `${n * 0.2}s`
                       }"
                     ></div>
                   </div>
                   <div class="pulse-button" :class="{ 'playing': animations.pulse }">
                     <div class="pulse-core"></div>
                     <div class="pulse-ring ring-1"></div>
                     <div class="pulse-ring ring-2"></div>
                     <div class="pulse-ring ring-3"></div>
                   </div>
                   <div class="item-info">
                     <h3>脉冲效果</h3>
                     <p>多层脉冲扩散动画</p>
                   </div>
                 </div>

                 <!-- 旋转魔方 -->
                 <div 
                   class="showcase-item" 
                   :class="{ 'selected': selectedAnimation === 'cube' }"
                   data-animation-type="cube" 
                   @mouseenter="playAnimation('cube')" 
                   @mouseleave="pauseAnimation('cube')" 
                   @click="playAnimation('cube')"
                 >
                   <div class="lily-petals" v-if="selectedAnimation === 'cube'">
                     <div 
                       v-for="n in 8" 
                       :key="n"
                       class="petal"
                       :style="{
                         '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                         '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                         '--r': `${n * 45}deg`,
                         'animation-delay': `${n * 0.2}s`
                       }"
                     ></div>
                   </div>
                   <div class="cube-container" :class="{ 'playing': animations.cube }">
                     <div class="cube">
                       <div class="cube-face front">前</div>
                       <div class="cube-face back">后</div>
                       <div class="cube-face left">左</div>
                       <div class="cube-face right">右</div>
                       <div class="cube-face top">上</div>
                       <div class="cube-face bottom">下</div>
                     </div>
                   </div>
                   <div class="item-info">
                     <h3>3D魔方</h3>
                     <p>立体旋转立方体</p>
                   </div>
                 </div>

                 <!-- 打字机效果 -->
                 <div class="showcase-item" data-animation-type="typewriter" @mouseenter="playAnimation('typewriter')" @mouseleave="pauseAnimation('typewriter')" @click="playAnimation('typewriter')">
                   <div class="typewriter-container" :class="{ 'playing': animations.typewriter }">
                     <div class="typewriter-text">Hello World!</div>
                     <div class="typewriter-cursor"></div>
                   </div>
                   <div class="item-info">
                     <h3>打字机</h3>
                     <p>逐字显示动画效果</p>
                   </div>
                 </div>

                 <!-- 渐变边框 -->
                 <div class="showcase-item" data-animation-type="border" @mouseenter="playAnimation('border')" @mouseleave="pauseAnimation('border')" @click="playAnimation('border')">
                   <div class="gradient-border" :class="{ 'playing': animations.border }">
                     <div class="border-content">渐变边框</div>
                   </div>
                   <div class="item-info">
                     <h3>渐变边框</h3>
                     <p>流动的彩虹边框</p>
                   </div>
                 </div>

                 <!-- 粒子爆炸 -->
                 <div class="showcase-item" data-animation-type="explosion" @mouseenter="playAnimation('explosion')" @mouseleave="pauseAnimation('explosion')" @click="playAnimation('explosion')">
                   <div class="explosion-container" :class="{ 'playing': animations.explosion }">
                     <div class="explosion-center"></div>
                     <div v-for="n in 12" :key="n" class="explosion-particle" :style="getExplosionStyle(n)"></div>
                   </div>
                   <div class="item-info">
                     <h3>粒子爆炸</h3>
                     <p>中心爆炸粒子效果</p>
                   </div>
                 </div>

                 <!-- 霓虹跑马灯 -->
                 <div 
                   class="showcase-item" 
                   :class="{ 'selected': selectedAnimation === 'neonMarquee' }"
                   data-animation-type="neonMarquee" 
                   @mouseenter="playAnimation('neonMarquee')" 
                   @mouseleave="pauseAnimation('neonMarquee')" 
                   @click="playAnimation('neonMarquee')"
                 >
                   <div class="lily-petals" v-if="selectedAnimation === 'neonMarquee'">
                     <div 
                       v-for="n in 8" 
                       :key="n"
                       class="petal"
                       :style="{
                         '--x': `${Math.cos((n * 45 * Math.PI) / 180) * 60}px`,
                         '--y': `${Math.sin((n * 45 * Math.PI) / 180) * 60}px`,
                         '--r': `${n * 45}deg`,
                         'animation-delay': `${n * 0.2}s`
                       }"
                     ></div>
                   </div>
                   <div class="neon-marquee-demo" :class="{ 'playing': animations.neonMarquee }">
                     <div class="marquee-content">霓虹跑马灯</div>
                   </div>
                   <div class="item-info">
                     <h3>霓虹跑马灯</h3>
                     <p>赛博朋克流动霓虹边框</p>
                   </div>
                 </div>
                 </template>
               </div>

               <div class="showcase-controls">
                 <button class="show-more-btn" @click="toggleShowMoreAnimations" :class="{ 'expanded': showMoreAnimations }">
                   <span class="btn-text">{{ showMoreAnimations ? '收起项目' : '展开更多项目' }}</span>
                   <span class="btn-icon">
                     <svg class="arrow-icon" :class="{ 'rotated': showMoreAnimations }" viewBox="0 0 24 24">
                       <path d="M7 10l5 5 5-5z"/>
                     </svg>
                   </span>
                 </button>
               </div>
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
      models: [],
      showMoreAnimations: false,
      clickCount: 0,
      ballSize: 1,
      multiplier: 1,
      comboCount: 0,
      currentColor: '#ff6b6b',
      resetTimer: null,
      animations: {
        card3d: false,
        particles: false,
        neon: false,
        ripple: false,
        starry: false,
        progress: false,
        glitch: false,
        wave: false,
        pulse: false,
        cube: false,
        typewriter: false,
        border: false,
        explosion: false,
        neonMarquee: false
      },
      // 性能优化相关
      isPreloaded: false,
      animationStates: {},
      visibleAnimations: new Set(),
      lazyLoadObserver: null,
      performanceMode: true,
      // 彼岸花选中状态
    selectedAnimation: null
    };
  },
  mounted() {
    this.initializePerformanceOptimizations();
    this.startAutoPlay();
  },

  beforeUnmount() {
    this.stopAutoPlay();
    this.cleanupPerformanceOptimizations();
  },

  methods: {
    setActiveCategory(categoryId) {
      this.activeCategory = categoryId;
    },
    
    toggleShowMoreAnimations() {
      this.showMoreAnimations = !this.showMoreAnimations;
      
      // 移除强制滚动，保持用户当前位置
      // 让展开/收回动画在当前视口内自然完成
    },
    
    playAnimation(type) {
      this.playAnimationOptimized(type);
      this.selectAnimation(type);
    },
    
    pauseAnimation(type) {
      this.animations[type] = false;
    },

    startAutoPlay() {
      // 优化后的自动播放，只在可见区域播放
      this.autoPlayInterval = setInterval(() => {
        this.playAllAnimationsOptimized();
      }, 5000); // 延长到5秒，减少频率
      
      // 延迟播放第一次，确保页面完全加载
      setTimeout(() => {
        this.playAllAnimationsOptimized();
      }, 1000);
    },

    stopAutoPlay() {
      if (this.autoPlayInterval) {
        clearInterval(this.autoPlayInterval);
      }
    },

    playAllAnimations() {
      this.playAllAnimationsOptimized();
    },
    
    selectAnimation(type) {
      // 切换选中状态
      if (this.selectedAnimation === type) {
        this.selectedAnimation = null;
      } else {
        this.selectedAnimation = type;
      }
    },

    handleClickCounter() {
      this.clickCount++;
      this.comboCount++;
      this.multiplier = Math.min(Math.floor(this.comboCount / 5) + 1, 10);
      
      // 随机变色
      const colors = [
        '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7',
        '#dda0dd', '#98d8c8', '#f7dc6f', '#bb8fce', '#85c1e9'
      ];
      this.currentColor = colors[Math.floor(Math.random() * colors.length)];
      
      // 温和的变大效果
      this.ballSize = 1.1;
      
      // 150毫秒后回弹到原始大小
      setTimeout(() => {
        this.ballSize = 1;
      }, 150);
      
      // 重置5秒计时器
      if (this.resetTimer) {
        clearTimeout(this.resetTimer);
      }
      this.resetTimer = setTimeout(() => {
        this.comboCount = 0;
        this.multiplier = 1;
        this.currentColor = '#ff6b6b';
      }, 5000);
    },
    
    
    
    getClickMessage() {
      if (this.clickCount === 0) return '点击开始震撼之旅！';
      if (this.clickCount <= 5) return '继续点击，威力在积累！';
      if (this.clickCount <= 15) return '太震撼了！继续！';
      if (this.clickCount <= 30) return '疯狂点击！力量爆发！';
      if (this.clickCount <= 50) return '无敌！你就是点击之王！';
      if (this.clickCount <= 80) return '🔥🔥🔥 传说级点击大师！🔥🔥🔥';
      return `💥💥💥 宇宙级点击霸主！球已变大${this.ballSize.toFixed(1)}倍！💥💥💥`;
    },
    
    getParticleStyle(n) {
      const angle = (n / 80) * Math.PI * 2;
      const radius = 20 + Math.random() * 80;
      const x = 50 + Math.cos(angle) * radius;
      const y = 50 + Math.sin(angle) * radius;
      const delay = Math.random() * 2.5;
      const size = 2 + Math.random() * 4;
      
      return {
        left: `${x}%`,
        top: `${y}%`,
        animationDelay: `${delay}s`,
        width: `${size}px`,
        height: `${size}px`
      };
    },
    
    getStarStyle(star) {
      const x = Math.random() * 100;
      const y = Math.random() * 100;
      const delay = Math.random() * 1.8;
      const duration = 1.5 + Math.random() * 1.5;
      const size = star > 120 ? 3 : 2;
      
      return {
        left: `${x}%`,
        top: `${y}%`,
        animationDelay: `${delay}s`,
        animationDuration: `${duration}s`,
        width: `${size}px`,
        height: `${size}px`
      };
    },
    
    getExplosionStyle(index) {
      const angle = (index * 30) * Math.PI / 180;
      const distance = 50 + Math.random() * 30;
      const delay = Math.random() * 0.5;
      
      return {
        transform: `rotate(${angle}rad) translateX(${distance}px)`,
        animationDelay: `${delay}s`
      };
    },

    // 性能优化方法
    initializePerformanceOptimizations() {
      // 1. 预加载关键CSS
      this.preloadCriticalStyles();
      
      // 2. 设置懒加载观察器
      this.setupLazyLoading();
      
      // 3. 初始化动画状态缓存
      this.initializeAnimationStates();
      
      // 4. 设置性能监控
      this.setupPerformanceMonitoring();
    },

    cleanupPerformanceOptimizations() {
      if (this.lazyLoadObserver) {
        this.lazyLoadObserver.disconnect();
      }
      if (this.performanceObserver) {
        this.performanceObserver.disconnect();
      }
    },

    preloadCriticalStyles() {
      // 预加载关键动画样式
      const criticalAnimations = ['card3d', 'particles', 'neon', 'ripple'];
      criticalAnimations.forEach(type => {
        this.animationStates[type] = { loaded: true, visible: false };
      });
      
      // 延迟加载非关键动画
      setTimeout(() => {
        const lazyAnimations = ['starry', 'progress', 'glitch', 'wave', 'pulse', 'cube', 'typewriter', 'border', 'explosion'];
        lazyAnimations.forEach(type => {
          this.animationStates[type] = { loaded: false, visible: false };
        });
      }, 100);
      
      this.isPreloaded = true;
    },

    setupLazyLoading() {
      if ('IntersectionObserver' in window) {
        this.lazyLoadObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              const animationType = entry.target.dataset.animationType;
              if (animationType) {
                this.loadAnimation(animationType);
                this.lazyLoadObserver.unobserve(entry.target);
              }
            }
          });
        }, {
          rootMargin: '50px 0px',
          threshold: 0.1
        });
        
        // 观察所有动画元素
        this.$nextTick(() => {
          const animationElements = this.$el.querySelectorAll('[data-animation-type]');
          animationElements.forEach(el => {
            this.lazyLoadObserver.observe(el);
          });
        });
      }
    },

    initializeAnimationStates() {
      // 存储动画运行状态，避免重复计算
      Object.keys(this.animations).forEach(key => {
        this.animationStates[key] = {
          lastPlayed: 0,
          playCount: 0,
          cachedStyles: null
        };
      });
    },

    setupPerformanceMonitoring() {
      if ('PerformanceObserver' in window) {
        this.performanceObserver = new PerformanceObserver((list) => {
          const entries = list.getEntries();
          entries.forEach(entry => {
            if (entry.duration > 16.67) { // 超过60fps
              console.warn(`动画性能警告: ${entry.name} 耗时 ${entry.duration}ms`);
            }
          });
        });
        this.performanceObserver.observe({ entryTypes: ['measure'] });
      }
    },

    loadAnimation(type) {
      if (this.animationStates[type] && !this.animationStates[type].loaded) {
        this.animationStates[type].loaded = true;
        this.animationStates[type].visible = true;
      }
    },

    // 优化的动画播放方法
    playAnimationOptimized(type) {
      const now = Date.now();
      const state = this.animationStates[type];
      
      // 节流控制：防止频繁触发
      if (now - state.lastPlayed < 100) {
        return;
      }
      
      state.lastPlayed = now;
      state.playCount++;
      
      // 使用 requestAnimationFrame 优化动画触发
      requestAnimationFrame(() => {
        this.animations[type] = true;
        
        // 自动停止动画，避免资源浪费
        setTimeout(() => {
          this.animations[type] = false;
        }, 2000);
      });
    },

    // 批量动画播放优化
    playAllAnimationsOptimized() {
      const types = ['card3d', 'particles', 'neon', 'ripple', 'starry', 'progress', 'glitch', 'wave'];
      
      // 分批播放，避免同时触发过多动画
      const batchSize = 3;
      const batches = [];
      
      for (let i = 0; i < types.length; i += batchSize) {
        batches.push(types.slice(i, i + batchSize));
      }
      
      batches.forEach((batch, batchIndex) => {
        setTimeout(() => {
          batch.forEach(type => {
            if (this.visibleAnimations.has(type)) {
              this.playAnimationOptimized(type);
            }
          });
        }, batchIndex * 200);
      });
    },

    // 内存清理
    cleanupAnimationMemory(type) {
      if (this.animationStates[type]) {
        this.animationStates[type].cachedStyles = null;
      }
    }

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

/* CSS动画展示台样式 */
.showcase-section {
  margin: 60px 0;
}

.showcase-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 40px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* 重新定义showcase-grid的动画系统 */
.showcase-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform, opacity;
}

/* 优化：避免页面跳动的简洁动画 */
.showcase-grid:not(.expanded) .showcase-item:nth-child(n+11) {
  opacity: 0;
  max-height: 0;
  margin: 0;
  padding: 0;
  overflow: hidden;
  transition: opacity 0.3s ease, max-height 0.3s ease, margin 0.3s ease, padding 0.3s ease;
  /* 移除transform避免重排 */
}

/* 展开状态：简洁淡入 */
.showcase-grid.expanded .showcase-item {
  opacity: 1;
  max-height: 500px;
  margin: 0;
  padding: 30px;
  transition: opacity 0.3s ease, max-height 0.3s ease, margin 0.3s ease, padding 0.3s ease;
}

/* 简化动画，统一过渡时间 */
.showcase-grid.expanded .showcase-item:nth-child(n+11) {
  transition-delay: 0s; /* 移除错开动画，避免跳动 */
}

.showcase-item {
  background: linear-gradient(135deg, #ffffff, #f8f9fa);
  border-radius: 15px;
  padding: 30px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.showcase-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
}

/* 跑马灯流动霓虹边框 - 放在最底层 */
.showcase-item.selected {
  position: relative;
  transform: translateY(-8px);
  border-radius: 15px;
  overflow: visible;
}

.showcase-item.selected::before {
  content: '';
  position: absolute;
  top: -8px;
  left: -8px;
  right: -8px;
  bottom: -8px;
  border-radius: 19px;
  padding: 3px;
  background: linear-gradient(90deg, 
    #00ffff, #0080ff, #8000ff, #ff00ff, 
    #00ffff, #0080ff, #8000ff, #ff00ff);
  background-size: 300% 100%;
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: subtract;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: subtract;
  animation: neon-marquee-flow 3s linear infinite;
  z-index: -10;
}

.showcase-item.selected::after {
  content: '';
  position: absolute;
  top: -12px;
  left: -12px;
  right: -12px;
  bottom: -12px;
  background: linear-gradient(90deg, 
    rgba(0, 255, 255, 0.4), rgba(0, 128, 255, 0.3), 
    rgba(128, 0, 255, 0.4), rgba(255, 0, 255, 0.3), 
    rgba(0, 255, 255, 0.4));
  background-size: 200% 100%;
  border-radius: 23px;
  z-index: -11;
  filter: blur(4px);
  animation: neon-marquee-glow 3s linear infinite;
}

@keyframes neon-marquee-flow {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: 300% 50%;
  }
}

@keyframes neon-marquee-glow {
  0% {
    background-position: -200% 50%;
  }
  100% {
    background-position: 200% 50%;
  }
}

/* 霓虹流动动画 */
@keyframes neon-glow-flow {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: 400% 50%;
  }
}

/* 移除内部扫描线效果，保持纯粹外围发光 */

.item-info h3 {
  margin-bottom: 15px;
  color: #2d3748;
  font-size: 1.3rem;
  font-weight: 600;
}

.item-info p {
  color: #718096;
  font-size: 0.9rem;
  line-height: 1.5;
}

/* 3D旋转卡片 */
.card-3d {
  width: 100px;
  height: 100px;
  position: relative;
  perspective: 1000px;
  margin: 20px auto;
}

.card-face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1rem;
  transition: transform 0.6s;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.card-face.front {
  background: linear-gradient(135deg, #74b9ff, #0984e3);
  color: white;
}

.card-face.back {
  background: linear-gradient(135deg, #00cec9, #55a3ff);
  color: white;
  transform: rotateY(180deg);
}

.card-3d.playing .card-face.front {
  animation: card-rotate 2s infinite ease-in-out;
}

.card-3d.playing .card-face.back {
  animation: card-rotate-back 2s infinite ease-in-out;
}

@keyframes card-rotate {
  0% { transform: rotateY(0deg); }
  25% { transform: rotateY(180deg); }
  50% { transform: rotateY(0deg); }
  75% { transform: rotateY(-180deg); }
  100% { transform: rotateY(0deg); }
}

@keyframes card-rotate-back {
  0% { transform: rotateY(180deg); }
  25% { transform: rotateY(0deg); }
  50% { transform: rotateY(180deg); }
  75% { transform: rotateY(360deg); }
  100% { transform: rotateY(180deg); }
}

/* 粒子动画 */
.particle-container {
  width: 100%;
  height: 120px;
  position: relative;
  background: radial-gradient(circle, rgba(102, 126, 234, 0.15), rgba(74, 144, 226, 0.1), transparent);
  border-radius: 10px;
  overflow: hidden;
}

.particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: #667eea;
  border-radius: 50%;
  opacity: 0;
  box-shadow: 0 0 8px rgba(102, 126, 234, 0.8);
}

.particle-glow {
  position: absolute;
  width: 6px;
  height: 6px;
  background: linear-gradient(45deg, #74b9ff, #0984e3);
  border-radius: 50%;
  opacity: 0;
  box-shadow: 0 0 12px rgba(116, 185, 255, 1);
}

.particle-container.playing .particle {
  animation: particle-float 2s infinite ease-in-out;
}

.particle-container.playing .particle-glow {
  animation: particle-float 2s infinite ease-in-out;
}

@keyframes particle-float {
  0% { transform: translateY(120px) translateX(0px) scale(0.5); opacity: 0; }
  20% { opacity: 1; transform: scale(1); }
  80% { opacity: 1; transform: scale(1); }
  100% { transform: translateY(-30px) translateX(60px) scale(0.3); opacity: 0; }
}

/* 霓虹文字 */
.neon-text {
  font-size: 2.5rem;
  font-weight: bold;
  color: #667eea;
  text-align: center;
  padding: 30px;
  background: #0a0a0a;
  border-radius: 10px;
  position: relative;
  overflow: hidden;
  text-shadow: 0 0 10px rgba(102, 126, 234, 0.5);
}

.neon-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle, rgba(102, 126, 234, 0.3), rgba(116, 185, 255, 0.2), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.neon-text.playing .neon-glow {
  animation: neon-pulse 6s infinite ease-in-out;
}

.neon-text.playing {
  animation: neon-text-glow 6s infinite ease-in-out;
}

@keyframes neon-pulse {
  0%, 100% { opacity: 0.3; }
  15% { opacity: 0.6; }
  30% { opacity: 0.9; }
  45% { opacity: 1; }
  60% { opacity: 0.8; }
  75% { opacity: 0.7; }
  90% { opacity: 0.5; }
}

@keyframes neon-text-glow {
  0%, 100% { text-shadow: 0 0 10px rgba(102, 126, 234, 0.5); }
  15% { text-shadow: 0 0 12px rgba(102, 126, 234, 0.7), 0 0 15px rgba(116, 185, 255, 0.5); }
  30% { text-shadow: 0 0 15px rgba(102, 126, 234, 0.9), 0 0 20px rgba(116, 185, 255, 0.7); }
  45% { text-shadow: 0 0 20px rgba(102, 126, 234, 1), 0 0 30px rgba(116, 185, 255, 0.8), 0 0 40px rgba(102, 126, 234, 0.6); }
  60% { text-shadow: 0 0 25px rgba(102, 126, 234, 0.9), 0 0 35px rgba(116, 185, 255, 0.7); }
  75% { text-shadow: 0 0 20px rgba(102, 126, 234, 0.8), 0 0 30px rgba(116, 185, 255, 0.6); }
  90% { text-shadow: 0 0 15px rgba(102, 126, 234, 0.7), 0 0 20px rgba(116, 185, 255, 0.5); }
}

/* 连点器效果 */


.score-item {
  display: flex;
  align-items: center;
  gap: 4px;
}

.score-label {
  opacity: 0.8;
}

.score-value {
  color: #ffd700;
  font-size: 16px;
}

@keyframes score-pop {
  0% { transform: scale(0.6); opacity: 0; }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); opacity: 1; }
}

.click-counter-container {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ff6b6b, #ee5a24);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  position: relative;
  margin: 0 auto;
  cursor: pointer;
  user-select: none;
  box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
  transition: transform 0.15s ease-out, background 0.2s ease;
  transform-origin: center center;
  transform: scale(1);
}

.click-counter-container:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 35px rgba(255, 107, 107, 0.4);
}

.click-counter-container.clicked {
  animation: counter-bounce 0.3s ease;
  background: linear-gradient(135deg, #ff4757, #c44569);
}

.counter-display {
  font-size: 2rem;
  font-weight: bold;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  transition: all 0.2s ease;
}

@keyframes counter-bounce {
  0% { transform: scale(1); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

/* 星空背景 */
.starry-sky {
  width: 100%;
  height: 120px;
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
  border-radius: 10px;
  position: relative;
  overflow: hidden;
}

.star {
  position: absolute;
  width: 2px;
  height: 2px;
  background: white;
  border-radius: 50%;
  opacity: 0;
}

.star.bright {
  width: 3px;
  height: 3px;
  background: linear-gradient(45deg, #fff, #74b9ff);
  box-shadow: 0 0 6px rgba(255, 255, 255, 0.8);
}

.starry-sky.playing .star {
  animation: star-twinkle 2s infinite ease-in-out;
}

.starry-sky.playing .star.bright {
  animation: star-twinkle-bright 2.5s infinite ease-in-out;
}

@keyframes star-twinkle {
  0%, 100% { opacity: 0.2; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.5); }
}

@keyframes star-twinkle-bright {
  0%, 100% { opacity: 0.5; transform: scale(1) rotate(0deg); }
  50% { opacity: 1; transform: scale(2.5) rotate(180deg); }
}

/* 进度环 */
.progress-ring {
  width: 100px;
  height: 100px;
  position: relative;
  margin: 0 auto;
}

.progress-svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.progress-bg {
  fill: none;
  stroke: #e2e8f0;
  stroke-width: 8;
}

.progress-bar {
  fill: none;
  stroke: #667eea;
  stroke-width: 8;
  stroke-linecap: round;
  stroke-dasharray: 283;
  stroke-dashoffset: 283;
  transition: stroke-dashoffset 1s ease;
}

.progress-ring.playing .progress-bar {
  animation: progress-fill 3s infinite;
}

@keyframes progress-fill {
  0% { stroke-dashoffset: 283; }
  50% { stroke-dashoffset: 70; }
  100% { stroke-dashoffset: 283; }
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.2rem;
  font-weight: bold;
  color: #667eea;
}

/* 故障效果 */
.glitch-text {
  font-size: 2rem;
  font-weight: bold;
  color: #667eea;
  position: relative;
  display: inline-block;
}

.glitch-main {
  position: relative;
  display: inline-block;
}

.glitch-overlay,
.glitch-overlay-2 {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
}

.glitch-text.playing .glitch-overlay {
  animation: glitch-1 0.3s infinite;
  color: #ff006e;
  clip-path: polygon(0 0, 100% 0, 100% 45%, 0 45%);
}

.glitch-text.playing .glitch-overlay-2 {
  animation: glitch-2 0.3s infinite;
  color: #00ff88;
  clip-path: polygon(0 55%, 100% 55%, 100% 100%, 0 100%);
}

@keyframes glitch-1 {
  0%, 100% { transform: translate(0); opacity: 0; }
  20% { transform: translate(-2px, 2px); opacity: 1; }
  40% { transform: translate(-2px, -2px); opacity: 1; }
  60% { transform: translate(2px, 2px); opacity: 1; }
  80% { transform: translate(2px, -2px); opacity: 1; }
}

@keyframes glitch-2 {
  0%, 100% { transform: translate(0); opacity: 0; }
  20% { transform: translate(2px, -2px); opacity: 1; }
  40% { transform: translate(-2px, 2px); opacity: 1; }
  60% { transform: translate(2px, 2px); opacity: 1; }
  80% { transform: translate(-2px, -2px); opacity: 1; }
}

/* 波浪动画 */
.wave-container {
  width: 100%;
  height: 120px;
  position: relative;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 10px;
  overflow: hidden;
}

.wave {
  position: absolute;
  width: 200%;
  height: 200%;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 43%;
}

.wave-1 {
  animation: wave-move 7s infinite linear;
  opacity: 0.7;
}

.wave-2 {
  animation: wave-move 9s infinite linear;
  animation-delay: -2s;
  opacity: 0.5;
}

.wave-3 {
  animation: wave-move 11s infinite linear;
  animation-delay: -4s;
  opacity: 0.3;
}

.wave-container.playing .wave {
  animation-play-state: running;
}

@keyframes wave-move {
  0% { transform: translate(-50%, 0) rotateZ(0deg); }
  100% { transform: translate(-50%, -50%) rotateZ(360deg); }
}

.showcase-controls {
  text-align: center;
  margin-top: 40px;
}

.show-more-btn {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 50px;
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: 600;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); /* 使用更平滑的缓动 */
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
  transform: translateY(0);
}

.show-more-btn:hover {
  background: linear-gradient(135deg, #5a67d8, #6b46c1);
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
}

.show-more-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.6s ease;
}

.show-more-btn:hover::before {
  left: 100%;
}

.show-more-btn:active {
  transform: translateY(-1px) scale(0.98);
  transition: all 0.1s ease;
}

.btn-icon {
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

.btn-icon.rotated {
  transform: rotate(180deg);
}

.btn-text {
  transition: all 0.3s ease;
  will-change: transform;
}

/* 按钮展开状态的额外样式 */
.show-more-btn.expanded {
  background: linear-gradient(135deg, #764ba2, #667eea);
  transform: translateY(-2px);
}

.show-more-btn.expanded:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 35px rgba(102, 126, 234, 0.5);
}

.showcase-item.fadeInUp {
  animation: fadeInUp 0.6s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .showcase-title {
    font-size: 2rem;
  }
  
  .showcase-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .showcase-item {
    padding: 20px;
  }
  
  .animation-container {
    height: 150px;
  }
  
  .show-more-btn {
    padding: 12px 24px;
    font-size: 1rem;
  }
}

/* 添加优雅的加载指示器 */
.showcase-controls {
  position: relative;
  text-align: center;
  margin-top: 40px;
  padding-bottom: 20px;
}

.showcase-controls::before {
  content: '';
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, transparent, #667eea, transparent);
  opacity: 0.6;
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% { opacity: 0.3; transform: translateX(-50%) scaleX(0.3); }
  50% { opacity: 1; transform: translateX(-50%) scaleX(1); }
  100% { opacity: 0.3; transform: translateX(-50%) scaleX(0.3); }
}

/* 为按钮添加点击波纹效果 */
.show-more-btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  transition: width 0.4s ease, height 0.4s ease;
  z-index: 1;
}

.show-more-btn:active::after {
  width: 200px;
  height: 200px;
}

.show-more-btn > * {
  position: relative;
  z-index: 2;
}

/* 新增5个CSS动画样式 */

/* 脉冲效果 */
.pulse-button {
  position: relative;
  width: 60px;
  height: 60px;
  margin: 20px auto;
}

.pulse-core {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 50%;
  position: relative;
  z-index: 3;
}

.pulse-ring {
  position: absolute;
  border: 2px solid #667eea;
  border-radius: 50%;
  opacity: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.ring-1 {
  width: 80px;
  height: 80px;
}

.ring-2 {
  width: 100px;
  height: 100px;
}

.ring-3 {
  width: 120px;
  height: 120px;
}

.pulse-button.playing .pulse-ring {
  animation: pulse-expand 2s infinite ease-out;
}

.pulse-button.playing .ring-1 { animation-delay: 0s; }
.pulse-button.playing .ring-2 { animation-delay: 0.2s; }
.pulse-button.playing .ring-3 { animation-delay: 0.4s; }

@keyframes pulse-expand {
  0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; }
  100% { transform: translate(-50%, -50%) scale(2); opacity: 0; }
}

/* 3D魔方 */
.cube-container {
  width: 100px;
  height: 100px;
  margin: 20px auto;
  perspective: 400px;
}

.cube {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transform: rotateX(-15deg) rotateY(15deg);
  transition: transform 0.5s ease;
}

.cube-face {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: bold;
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.cube-face.front { transform: translateZ(50px); }
.cube-face.back { transform: rotateY(180deg) translateZ(50px); }
.cube-face.left { transform: rotateY(-90deg) translateZ(50px); }
.cube-face.right { transform: rotateY(90deg) translateZ(50px); }
.cube-face.top { transform: rotateX(90deg) translateZ(50px); }
.cube-face.bottom { transform: rotateX(-90deg) translateZ(50px); }

.cube-container.playing .cube {
  animation: cube-rotate 3s infinite linear;
}

@keyframes cube-rotate {
  0% { transform: rotateX(-15deg) rotateY(15deg); }
  100% { transform: rotateX(-15deg) rotateY(375deg); }
}

/* 打字机效果 */
.typewriter-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 60px;
  margin: 20px auto;
  font-family: 'Courier New', monospace;
}

.typewriter-text {
  font-size: 1.2rem;
  font-weight: bold;
  color: #667eea;
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  border-right: 2px solid #667eea;
}

.typewriter-cursor {
  width: 2px;
  height: 1.2rem;
  background: #667eea;
  animation: blink 1s infinite;
}

.typewriter-container.playing .typewriter-text {
  animation: typing 2s steps(12, end) forwards;
}

@keyframes typing {
  0% { width: 0; }
  100% { width: 120px; }
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* 渐变边框 */
.gradient-border {
  position: relative;
  width: 120px;
  height: 60px;
  margin: 20px auto;
  border-radius: 10px;
  overflow: hidden;
  padding: 2px;
  background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7);
  background-size: 300% 300%;
}

.gradient-border::before {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  right: 2px;
  bottom: 2px;
  background: white;
  border-radius: 8px;
  z-index: 1;
}

.border-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  font-weight: bold;
  color: #667eea;
}

.gradient-border.playing {
  animation: gradient-shift 2s infinite linear;
}

@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* 粒子爆炸 */
.explosion-container {
  position: relative;
  width: 100px;
  height: 100px;
  margin: 20px auto;
}

.explosion-center {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 10px;
  height: 10px;
  background: #ff6b6b;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  opacity: 0;
}

.explosion-particle {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 4px;
  height: 4px;
  background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
  border-radius: 50%;
  opacity: 0;
  transform-origin: center;
}

.explosion-container.playing .explosion-center {
  animation: center-explode 0.5s ease-out forwards;
}

.explosion-container.playing .explosion-particle {
  animation: particle-explode 1s ease-out forwards;
}

@keyframes center-explode {
  0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
  100% { transform: translate(-50%, -50%) scale(1); opacity: 0; }
}

@keyframes particle-explode {
  0% { 
    transform: rotate(0deg) translateX(0px) scale(1); 
    opacity: 1; 
  }
  100% { 
    transform: rotate(var(--angle, 0deg)) translateX(80px) scale(0); 
    opacity: 0; 
  }
}

/* 霓虹跑马灯展示 */
.neon-marquee-demo {
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0a0a0a, #1a1a2e);
  border-radius: 10px;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(0, 255, 255, 0.2);
}

.neon-marquee-demo::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(0, 255, 255, 0.1) 25%, 
    rgba(0, 128, 255, 0.2) 50%, 
    rgba(255, 0, 255, 0.1) 75%, 
    transparent 100%
  );
  background-size: 200% 100%;
  animation: neon-marquee-flow 3s linear infinite;
}

.neon-marquee-demo.playing::before {
  opacity: 1;
}

.marquee-content {
  color: #fff;
  font-size: 1.2rem;
  font-weight: bold;
  text-shadow: 
    0 0 5px rgba(0, 255, 255, 0.8),
    0 0 10px rgba(0, 255, 255, 0.6),
    0 0 15px rgba(0, 255, 255, 0.4);
  z-index: 1;
  position: relative;
  letter-spacing: 2px;
}

.neon-marquee-demo.playing .marquee-content {
  animation: neon-text-glow 2s infinite ease-in-out;
}

.neon-marquee-demo::after {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  background: linear-gradient(90deg, 
    #00ffff, #0080ff, #8000ff, #ff00ff, 
    #00ffff, #0080ff, #8000ff, #ff00ff
  );
  background-size: 300% 100%;
  border-radius: 12px;
  z-index: -1;
  animation: neon-marquee-flow 4s linear infinite;
  opacity: 0.7;
}

.neon-marquee-demo.playing::after {
  opacity: 1;
}
</style>
