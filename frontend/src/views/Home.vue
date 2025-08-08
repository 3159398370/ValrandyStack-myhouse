<template>
  <div class="home">
    <!-- 英雄区域 -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <div class="title-container">
            <h1 class="hero-title animated-title">你好，我是 <span class="highlight">Valrandy·Joseph</span></h1>
            <div class="hello-world-container">
              <span class="hello-world-text">{{ displayedText }}</span>
              <span class="cursor" :class="{ 'blink': showCursor }">|</span>
            </div>
          </div>
          <h2 class="hero-subtitle">全栈开发者 & 数据工程师</h2>
          <p class="hero-description">
            我专注于使用Vue和Django创建现代化的Web应用程序，同时擅长数据分析和可视化。
            让我们一起将您的想法转化为现实！
          </p>
          <div class="hero-buttons">
            <router-link to="/projects" class="btn btn-primary">查看作品集</router-link>
            <router-link to="/about" class="btn btn-outline ml-3">联系我</router-link>
          </div>
        </div>
        <div class="hero-image">
          <img src="@/assets/styles/images/vj.jpg" alt="Profile Image" />
        </div>
      </div>
    </section>

    <!-- 技能区域 -->
    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">我的技能</h2>
        <p class="section-description">我擅长的技术栈和专业领域</p>

        <div class="skills-content">
          <div class="skills-radar">
            <div ref="radarChart" class="radar-chart"></div>
          </div>

          <div class="skills-details">
            <div v-for="(skill, index) in skills" :key="index" class="skill-card">
              <div class="skill-icon" :style="{ backgroundColor: skill.color }">
                <i :class="skill.icon"></i>
              </div>
              <div class="skill-info">
                <h3>{{ skill.name }}</h3>
                <p>{{ skill.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 技术栈标签云 -->
    <section class="awards-section">
      <div class="container">
        <h2 class="section-title">获奖证书</h2>
        <div class="awards-cloud">
          <div v-for="(award, index) in awards" :key="index" class="award-tag" :style="getFixedStyle(index)">
            {{ award }}
          </div>
        </div>
      </div>
    </section>

    <!-- 项目预览 -->
    <section class="projects-preview">
      <div class="container">
        <h2 class="section-title">精选项目</h2>
        <p class="section-description">我最近完成的一些项目</p>

        <div class="projects-grid">
          <div v-for="(project, index) in featuredProjects" :key="index" class="project-card">
            <div class="project-image">
              <img :src="project.image" :alt="project.title" />
            </div>
            <div class="project-info">
              <h3>{{ project.title }}</h3>
              <p>{{ project.description }}</p>
              <div class="project-tags">
                <span v-for="(tag, tagIndex) in project.tags" :key="tagIndex" class="tag">{{ tag }}</span>
              </div>
              <router-link :to="`/projects/${project.id}`" class="btn btn-outline">查看详情</router-link>
            </div>
          </div>
        </div>

        <div class="text-center mt-4">
          <router-link to="/projects" class="btn btn-primary">查看所有项目</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import project1Image from '@/assets/images/project1.svg';
import project2Image from '@/assets/images/project2.svg';
import project3Image from '@/assets/images/project3.svg';
import project4Image from '@/assets/images/project4.svg';

export default {
  name: 'Home',
  data() {
    return {
      displayedText: '',
      fullText: 'Hello, World!',
      typewriterIndex: 0,
      showCursor: true,
      typewriterSpeed: 150,
      skills: [
        {
          name: '前端开发',
          description: '精通Vue.js、HTML5、CSS3和JavaScript，构建响应式和用户友好的界面。',
          icon: 'fas fa-code',
          color: '#42b983',
          value: 90,
        },
        {
          name: '后端开发',
          description: '使用Django和Python创建可扩展的API和Web应用程序。',
          icon: 'fas fa-server',
          color: '#2c3e50',
          value: 85,
        },
        {
          name: '数据工程',
          description: '使用ALGC算法和机器学习技术进行智能数据处理。',
          icon: 'fas fa-database',
          color: '#e74c3c',
          value: 80,
        },
        {
          name: '数据分析',
          description: '使用Pandas和NumPy进行数据清洗、转换和分析。',
          icon: 'fas fa-chart-bar',
          color: '#3498db',
          value: 85,
        },
        {
          name: 'Python爬虫',
          description: '使用Scrapy和BeautifulSoup进行网络数据采集和处理。',
          icon: 'fas fa-spider',
          color: '#9b59b6',
          value: 75,
        },
        {
          name: '数据可视化',
          description: '使用ECharts创建交互式和信息丰富的数据可视化。',
          icon: 'fas fa-chart-pie',
          color: '#f39c12',
          value: 90,
        },
        {
          name: '运维部署',
          description: '在阿里云服务器上部署宝塔面板，实现项目上线、服务器运维和应用程序管理。',
          icon: 'fas fa-cloud',
          color: '#1abc9c',
          value: 70,
        },
      ],
      awards: [
        '数据分析科普竞赛一等奖',
        '大数据省赛铜奖',
        'Agent认证',
        '大模型开发工程师',
      ],
      featuredProjects: [
        {
          id: 1,
          title: '智能数据分析平台',
          description: '基于Vue和Django的数据分析平台，支持多种数据源和可视化方式。',
          image: project1Image,
          tags: ['Vue', 'Django', 'ECharts', 'Pandas'],
        },
        {
          id: 2,
          title: '个人网站开发',
          description: '基于Vue.js和Django的全栈个人网站，包含作品展示、博客系统、代码仓库和联系功能的完整解决方案。',
          image: project2Image,
          tags: ['Vue.js', 'Django', 'MySQL', 'Vite', 'ECharts'],
        },
        {
          id: 3,
          title: '电商数据爬虫',
          description: '使用Scrapy开发的电商网站数据采集工具，支持多线程和代理IP。',
          image: project3Image,
          tags: ['Python', 'Scrapy', 'MongoDB', 'Data Mining'],
        },
        {
          id: 4,
          title: '小米家具官网复刻',
          description: '高度还原小米家具官网的设计和交互，实现响应式布局和现代化UI。',
          image: project4Image,
          tags: ['Vue', 'Element UI', '响应式设计', 'CSS3'],
        },
      ],
      radarChart: null,
    };
  },
  mounted() {
    this.initRadarChart();
    window.addEventListener('resize', this.resizeRadarChart);
    // 启动打字机效果
    this.startTypewriter();
    // 启动光标闪烁
    this.startCursorBlink();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.resizeRadarChart);
    if (this.radarChart) {
      this.radarChart.dispose();
    }
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

    initRadarChart() {
      this.radarChart = echarts.init(this.$refs.radarChart);

      const option = {
        backgroundColor: 'transparent',
        tooltip: {
          trigger: 'item',
        },
        radar: {
          indicator: this.skills.map((skill) => ({
            name: skill.name,
            max: 100,
          })),
          radius: '65%',
          splitNumber: 5,
          axisName: {
            color: '#333',
            fontSize: 12,
          },
          splitArea: {
            areaStyle: {
              color: ['rgba(255, 255, 255, 0.5)'],
              shadowColor: 'rgba(0, 0, 0, 0.05)',
              shadowBlur: 10,
            },
          },
          axisLine: {
            lineStyle: {
              color: 'rgba(44, 62, 80, 0.3)',
            },
          },
          splitLine: {
            lineStyle: {
              color: 'rgba(44, 62, 80, 0.3)',
            },
          },
        },
        series: [{
          name: '技能水平',
          type: 'radar',
          data: [{
            value: this.skills.map((skill) => skill.value),
            name: '技能水平',
            areaStyle: {
              color: 'rgba(66, 185, 131, 0.6)',
            },
            lineStyle: {
              color: '#42b983',
              width: 2,
            },
            itemStyle: {
              color: '#42b983',
            },
          }],
        }],
      };

      this.radarChart.setOption(option);
    },
    resizeRadarChart() {
      if (this.radarChart) {
        this.radarChart.resize();
      }
    },
    getFixedStyle(index) {
      const colors = ['#42b983', '#2c3e50', '#e74c3c', '#3498db', '#9b59b6', '#f39c12', '#1abc9c'];
      const sizes = ['1rem', '1.1rem', '1.2rem'];
      const rotations = ['-1deg', '0deg', '1deg'];

      return {
        backgroundColor: colors[index % colors.length],
        fontSize: sizes[index % sizes.length],
        transform: `rotate(${rotations[index % rotations.length]})`,
      };
    },
  },
};
</script>

<style scoped>
.home {
  animation: fadeIn 0.5s ease-in-out;
}

/* 英雄区域 */
.hero {
  padding: 80px 0;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.hero .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.hero-content {
  flex: 1;
  max-width: 600px;
}

/* Title Container */
.title-container {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 15px;
  flex-wrap: wrap;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.2;
}

/* Title Animation */
.animated-title {
  animation: slideInFromLeft 1s ease-out, glow 3s ease-in-out infinite alternate 1.5s;
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
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
  50% {
    text-shadow: 0 2px 10px rgba(0,0,0,0.1), 0 0 15px rgba(66, 185, 131, 0.4);
  }
  100% {
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
}

/* Hello World Container */
.hello-world-container {
  display: flex;
  align-items: center;
  font-family: 'Courier New', monospace;
  font-size: 1.2rem;
  color: #00ff41;
  text-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
  background: rgba(0, 0, 0, 0.8);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 1px solid rgba(0, 255, 65, 0.3);
  backdrop-filter: blur(5px);
  animation: slideInFromRight 1.2s ease-out 1s both;
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
  font-size: 1.5rem;
  color: #6c757d;
  margin-bottom: 20px;
}

.highlight {
  color: #42b983;
}

.hero-description {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 30px;
  color: #495057;
}

.hero-buttons {
  display: flex;
}

.hero-image {
  flex: 1;
  max-width: 500px;
  display: flex;
  justify-content: center;
}

.hero-image img {
  max-width: 300px;
  height: 300px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* 技能区域 */
.skills-section {
  padding: 80px 0;
  background-color: #fff;
}

.section-title {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 10px;
  color: #2c3e50;
}

.section-description {
  text-align: center;
  font-size: 1.2rem;
  color: #6c757d;
  margin-bottom: 50px;
}

.skills-content {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
}

.skills-radar {
  flex: 1;
  min-width: 300px;
}

.radar-chart {
  width: 100%;
  height: 400px;
}

.skills-details {
  flex: 1;
  min-width: 300px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.skill-card {
  display: flex;
  align-items: center;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.skill-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.skill-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  color: white;
  font-size: 1.5rem;
  flex-shrink: 0;
  min-width: 50px;
  min-height: 50px;
}

.skill-icon i {
  font-size: 1.5rem !important;
  line-height: 1;
}

.skill-info h3 {
  margin: 0 0 5px;
  font-size: 1.2rem;
}

.skill-info p {
  margin: 0;
  font-size: 0.9rem;
  color: #6c757d;
}

/* 获奖证书 */
.awards-section {
  padding: 80px 0;
  background-color: #f8f9fa;
}

.awards-cloud {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 30px;
}

.award-tag {
  padding: 10px 20px;
  border-radius: 30px;
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.award-tag:hover {
  transform: translateY(-5px) scale(1.05);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}

/* 项目预览 */
.projects-preview {
  padding: 80px 0;
  background-color: #fff;
}

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
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.project-image {
  height: 250px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.5s ease;
}

.project-card:hover .project-image img {
  transform: scale(1.05);
}

.project-info {
  padding: 20px;
}

.project-info h3 {
  margin: 0 0 10px;
  font-size: 1.4rem;
}

.project-info p {
  margin: 0 0 15px;
  color: #6c757d;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 15px;
}

.tag {
  padding: 5px 10px;
  background-color: #e9ecef;
  border-radius: 4px;
  font-size: 0.8rem;
  color: #495057;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .hero .container {
    flex-direction: column;
    text-align: center;
  }

  .hero-content {
    max-width: 100%;
    margin-bottom: 40px;
  }

  .title-container {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .hero-buttons {
    justify-content: center;
  }

  .skills-content {
    flex-direction: column;
  }

  .projects-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
}

@media (max-width: 576px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hello-world-container {
    font-size: 1rem;
    padding: 0.4rem 0.8rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
