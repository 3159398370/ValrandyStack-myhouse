<template>
  <div class="footer-container">
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
              <a href="https://space.bilibili.com/505984286?spm_id_from=333.1007.0.0" target="_blank" rel="noopener noreferrer" aria-label="Bilibili">
                <i class="fab fa-bilibili"></i>
              </a>
              <a @click="showDouyinQRCode" aria-label="抖音">
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

        <!-- 贪吃蛇游戏区域 -->
        <div class="snake-area" v-if="isGameActive">
          <div class="game-info">
            <span class="game-score">分数: {{ score }}</span>
            <button class="restart-btn" @click="initGame">重新开始</button>
            <button class="close-btn" @click="stopGame">×</button>
          </div>
          <!-- 作弊码输入框 -->
          <div class="cheat-code-container">
            <input
              type="text" 
              class="cheat-code-input" 
              placeholder="输入作弊码..." 
              @input="onCheatCodeInput"
              @keyup.enter="applyCheatCode"
            />
            <button class="apply-cheat-btn" @click="applyCheatCode">应用</button>
          </div>
          <canvas ref="snakeCanvas" class="game-canvas"></canvas>
          <div class="game-controls">
            <div class="control-buttons-container">
              <div class="direction-controls">
                <button class="control-btn" @click="changeDirection('up')">↑</button>
                <div class="control-row">
                  <button class="control-btn" @click="changeDirection('left')">←</button>
                  <button class="control-btn" @click="changeDirection('down')">↓</button>
                  <button class="control-btn" @click="changeDirection('right')">→</button>
                </div>
              </div>
              <button class="control-btn pause-resume-btn" @click="togglePauseResume" v-if="!isGameOver">
                {{ isPaused ? '继续' : '暂停' }}
              </button>
            </div>
          </div>
          <!-- 游戏结束覆盖层 -->
          <div class="game-over-overlay" v-if="isGameOver">
            <div class="game-over-content">
              <h3>游戏结束</h3>
              <p>您的分数: {{ score }}</p>
              <div class="game-over-buttons">
                <button class="restart-btn" @click="initGame">再玩一次</button>
                <button class="close-btn" @click="stopGame">关闭游戏</button>
              </div>
            </div>
          </div>
        </div>

        <div class="footer-bottom">
          <div class="footer-info">
            <span class="copyright">&copy; {{ currentYear }} Valrandy·Joseph. 保留所有权利。</span>
            <span class="separator">|</span>
            <span class="icp-info">
              <img src="/备案图标.png" alt="备案图标" class="icp-icon" />
              <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">陕ICP备2024055572号-1</a>
              <span class="separator">|</span>
              <a href="https://beian.mps.gov.cn/#/query/webSearch?code=61043102610496" rel="noreferrer" target="_blank">陕公网安备61043102610496号</a>
            </span>
            <!-- 隐蔽的游戏触发点 -->
            <span class="secret-trigger" @click="toggleGame" title="点击试试">🐍</span>
          </div>
        </div>
      </div>
    </footer>
  
    <!-- 抖音二维码弹窗 -->
    <div v-if="showDouyinQR" class="qr-code-overlay" @click="closeDouyinQR">
      <div class="qr-code-modal" @click.stop>
        <div class="qr-code-content">
          <h3>我的抖音二维码</h3>
          <img src="/src/assets/images/tx.png" alt="抖音二维码" class="qr-code-image" />
          <p>扫码关注我的抖音</p>
          <button class="close-btn" @click="closeDouyinQR">关闭</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      navItems: [
        { name: '首页', path: '/' },
        { name: '作品集', path: '/projects' },
        { name: '代码仓库', path: '/repositories' },
        { name: '创意实验室', path: '/creative-lab' },
        { name: '关于我', path: '/about' },
      ],
      // 游戏相关数据
      snake: [],
      food: {},
      direction: 'right',
      nextDirection: 'right',
      score: 0,
      gameInterval: null,
      lastTimestamp: null, // 用于requestAnimationFrame的时间戳
      gridSize: 15,
      speed: 180,
      isGameActive: false,
      isGameOver: false,
      isPaused: false, // 标记游戏是否暂停
      gridDrawn: false, // 标记网格是否已绘制
      needsGridRedraw: false, // 标记是否需要重新绘制网格
      isInvincible: false, // 无敌模式标志
      cheatCode: '', // 用于跟踪作弊码输入
      cheatCodeInput: '' ,// 存储输入框中的作弊码
      showDouyinQR: false // 抖音二维码显示状态
    };
  },
  computed: {
    currentYear() {
      return new Date().getFullYear();
    },
  },
  mounted() {
    // 设置canvas尺寸
    this.resizeCanvas();
    // 监听窗口大小变化
    window.addEventListener('resize', this.resizeCanvas);
  },
  beforeUnmount() {
    this.stopGame();
    window.removeEventListener('resize', this.resizeCanvas);
    document.removeEventListener('keydown', this.handleKeyDown);
  },
  methods: {
    // 显示抖音二维码
    showDouyinQRCode() {
      this.showDouyinQR = true;
    },
    
    // 关闭抖音二维码
    closeDouyinQR() {
      this.showDouyinQR = false;
    },
    
    // 切换游戏状态
    toggleGame() {
      if (this.isGameActive) {
        this.stopGame();
      } else {
        this.initGame();
        this.setupKeyboardControls();
        // 默认暂停游戏，等待用户手动开始
        this.pauseGame();
      }
    },
    
    // 初始化游戏
    initGame() {
      this.isGameActive = true;
      this.isGameOver = false;
      // 等待DOM更新后再调整canvas尺寸
      this.$nextTick(() => {
        this.resizeCanvas();
      });
      // 初始化蛇的位置
      this.snake = [
        { x: 5, y: 3 },
        { x: 4, y: 3 },
        { x: 3, y: 3 }
      ];
      this.direction = 'right';
      this.nextDirection = 'right';
      this.score = 0;
      this.speed = 180;
      this.generateFood();
      this.draw();
      this.startGame();
    },
    
    // 开始游戏循环
    startGame() {
      if (this.gameInterval) {
        cancelAnimationFrame(this.gameInterval);
      }
      
      // 使用requestAnimationFrame代替setInterval以获得更流畅的动画
      const gameLoop = (timestamp) => {
        // 游戏暂停时不更新状态，但仍然绘制画面（包含暂停提示）
        if (!this.isPaused && (!this.lastTimestamp || timestamp - this.lastTimestamp >= this.speed)) {
          this.update();
          this.lastTimestamp = timestamp;
        }
        this.draw();
        this.gameInterval = requestAnimationFrame(gameLoop);
      };
      
      // 如果是从暂停状态恢复，保留原有的lastTimestamp以保持连续性
      if (!this.isPaused) {
        this.lastTimestamp = 0;
      }
      this.gameInterval = requestAnimationFrame(gameLoop);
    },
    
    // 停止游戏
    stopGame() {
      if (this.gameInterval) {
        cancelAnimationFrame(this.gameInterval);
        this.gameInterval = null;
      }
      this.isGameActive = false;
      this.isGameOver = false;
      this.isPaused = false;
      this.lastTimestamp = null;
      // 在游戏窗口关闭时关闭无敌模式
      if (this.isInvincible) {
        this.isInvincible = false;
        console.log('无敌模式已关闭！');
      }
    },
    
    // 暂停游戏
    pauseGame() {
      if (this.gameInterval && !this.isGameOver) {
        cancelAnimationFrame(this.gameInterval);
        this.gameInterval = null;
        this.isPaused = true;
        // 确保暂停后立即显示暂停提示
        this.draw();
      }
    },
    
    // 继续游戏
    resumeGame() {
      if (this.isGameActive && this.isPaused && !this.isGameOver) {
        this.startGame();
        this.isPaused = false;
      }
    },
    
    // 切换暂停/继续状态
    togglePauseResume() {
      if (this.isPaused) {
        this.resumeGame();
      } else {
        this.pauseGame();
      }
    },
    
    // 更新游戏状态
    update() {
      this.direction = this.nextDirection;
      const head = { ...this.snake[0] };
      
      // 根据方向移动蛇头
      switch (this.direction) {
        case 'up':
          head.y--;
          break;
        case 'down':
          head.y++;
          break;
        case 'left':
          head.x--;
          break;
        case 'right':
          head.x++;
          break;
      }
      
      // 检查是否撞到墙壁
      const canvas = this.$refs.snakeCanvas;
      const cols = Math.floor(canvas.width / this.gridSize);
      const rows = Math.floor(canvas.height / this.gridSize);
      
      // 在无敌模式下，让蛇可以穿墙而过
      if (!this.isInvincible) {
        if (head.x < 0 || head.x >= cols || head.y < 0 || head.y >= rows) {
          this.gameOver();
          return;
        }
        
        // 检查是否撞到自己
        for (let i = 0; i < this.snake.length; i++) {
          if (this.snake[i].x === head.x && this.snake[i].y === head.y) {
            this.gameOver();
            return;
          }
        }
      } else {
        // 无敌模式下穿墙逻辑：从另一边出来
        if (head.x < 0) head.x = cols - 1;
        else if (head.x >= cols) head.x = 0;
        if (head.y < 0) head.y = rows - 1;
        else if (head.y >= rows) head.y = 0;
      }
      
      // 添加新的头部
      this.snake.unshift(head);
      
      // 检查是否吃到食物
      if (this.food && head.x === this.food.x && head.y === this.food.y) {
        this.score += 10;
        this.generateFood();
        // 随着分数增加，游戏速度加快
        if (this.score % 50 === 0 && this.speed > 80) {
          this.speed -= 10;
          // 保存当前食物状态后重启游戏循环
          const currentFood = this.food;
          this.startGame();
          this.food = currentFood;
        }
      } else {
        // 移除尾部
        this.snake.pop();
      }
    },
    
    // 绘制游戏画面 - 使用优化的渲染方法
    draw() {
      const canvas = this.$refs.snakeCanvas;
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      const cols = Math.floor(canvas.width / this.gridSize);
      const rows = Math.floor(canvas.height / this.gridSize);
      
      // 清空画布
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // 优化网格绘制 - 只在必要时绘制，减少绘制次数
      if (!this.gridDrawn || this.needsGridRedraw) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        ctx.lineWidth = 1;
        // 使用路径批量绘制，减少渲染调用
        ctx.beginPath();
        for (let x = 0; x <= cols; x++) {
          ctx.moveTo(x * this.gridSize, 0);
          ctx.lineTo(x * this.gridSize, canvas.height);
        }
        for (let y = 0; y <= rows; y++) {
          ctx.moveTo(0, y * this.gridSize);
          ctx.lineTo(canvas.width, y * this.gridSize);
        }
        ctx.stroke();
        this.gridDrawn = true;
        this.needsGridRedraw = false;
      }
      
      // 绘制蛇
      this.snake.forEach((segment, index) => {
        // 在无敌模式下改变蛇头颜色
        if (index === 0 && this.isInvincible) {
          ctx.fillStyle = '#ffd700'; // 金色
        } else if (index === 0) {
          ctx.fillStyle = '#42b983'; // 正常绿色
        } else {
          ctx.fillStyle = '#35495e'; // 蛇身颜色
        }
        ctx.fillRect(
          segment.x * this.gridSize,
          segment.y * this.gridSize,
          this.gridSize - 1,
          this.gridSize - 1
        );
        // 绘制蛇头眼睛
        if (index === 0) {
          ctx.fillStyle = 'white';
          const eyeSize = this.gridSize / 5;
          const eyeOffset = this.gridSize / 3;
          
          if (this.direction === 'right') {
            ctx.beginPath();
            ctx.arc(
              segment.x * this.gridSize + this.gridSize - eyeOffset,
              segment.y * this.gridSize + eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.arc(
              segment.x * this.gridSize + this.gridSize - eyeOffset,
              segment.y * this.gridSize + this.gridSize - eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.fill();
          } else if (this.direction === 'left') {
            ctx.beginPath();
            ctx.arc(
              segment.x * this.gridSize + eyeOffset,
              segment.y * this.gridSize + eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.arc(
              segment.x * this.gridSize + eyeOffset,
              segment.y * this.gridSize + this.gridSize - eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.fill();
          } else if (this.direction === 'up') {
            ctx.beginPath();
            ctx.arc(
              segment.x * this.gridSize + eyeOffset,
              segment.y * this.gridSize + eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.arc(
              segment.x * this.gridSize + this.gridSize - eyeOffset,
              segment.y * this.gridSize + eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.fill();
          } else if (this.direction === 'down') {
            ctx.beginPath();
            ctx.arc(
              segment.x * this.gridSize + eyeOffset,
              segment.y * this.gridSize + this.gridSize - eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.arc(
              segment.x * this.gridSize + this.gridSize - eyeOffset,
              segment.y * this.gridSize + this.gridSize - eyeOffset,
              eyeSize,
              0,
              2 * Math.PI
            );
            ctx.fill();
          }
        }
      });
      
      // 绘制食物 - 添加存在性检查
      if (this.food && this.food.x !== undefined && this.food.y !== undefined) {
        ctx.fillStyle = '#ff6b6b';
        ctx.beginPath();
        ctx.arc(
          this.food.x * this.gridSize + this.gridSize / 2,
          this.food.y * this.gridSize + this.gridSize / 2,
          this.gridSize / 2 - 1,
          0,
          2 * Math.PI
        );
        ctx.fill();
      } else {
        // 如果食物不存在，重新生成
        this.generateFood();
      }
      
      // 如果游戏暂停，显示暂停提示
      if (this.isPaused) {
        // 使用半透明黑色背景确保文字清晰可见
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // 大标题文字 - 使用更醒目的颜色和更大的字体
        ctx.fillStyle = '#42b983';
        ctx.font = 'bold 24px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('游戏暂停', canvas.width / 2, canvas.height / 2 - 30);
        
        // 副标题文字 - 同样使用更大的字体确保清晰
        ctx.fillStyle = '#ffffff';
        ctx.font = '18px Arial';
        ctx.fillText('点击继续按钮或按空格键继续', canvas.width / 2, canvas.height / 2 + 20);
      }
    },
    
    // 生成食物 - 优化以确保总能生成食物
    generateFood() {
      const canvas = this.$refs.snakeCanvas;
      if (!canvas) return;
      
      const cols = Math.floor(canvas.width / this.gridSize);
      const rows = Math.floor(canvas.height / this.gridSize);
      const totalCells = cols * rows;
      
      // 如果蛇身已经占据了大部分空间，使用备用策略
      if (this.snake.length >= totalCells * 0.9) {
        // 简单策略：寻找第一个可用的格子
        for (let y = 0; y < rows; y++) {
          for (let x = 0; x < cols; x++) {
            let isAvailable = true;
            for (let i = 0; i < this.snake.length; i++) {
              if (this.snake[i].x === x && this.snake[i].y === y) {
                isAvailable = false;
                break;
              }
            }
            if (isAvailable) {
              this.food = { x, y };
              return;
            }
          }
        }
        // 极端情况：如果没有可用格子，就放在蛇头旁边
        this.food = { x: this.snake[0].x + 1, y: this.snake[0].y };
        return;
      }
      
      // 正常情况下的随机生成
      let newFood;
      let onSnake;
      let attempts = 0;
      const maxAttempts = 100;
      
      do {
        onSnake = false;
        newFood = {
          x: Math.floor(Math.random() * cols),
          y: Math.floor(Math.random() * rows)
        };
        
        for (let i = 0; i < this.snake.length; i++) {
          if (this.snake[i].x === newFood.x && this.snake[i].y === newFood.y) {
            onSnake = true;
            break;
          }
        }
        attempts++;
      } while (onSnake && attempts < maxAttempts);
      
      // 如果尝试次数过多，使用备用位置
      if (attempts >= maxAttempts) {
        // 放在蛇尾后面（如果可能）
        const tail = this.snake[this.snake.length - 1];
        let tailX = tail.x;
        let tailY = tail.y;
        
        // 根据蛇的移动方向，尝试在蛇尾后面生成食物
        if (this.direction === 'right' && tailX > 0) tailX--;
        else if (this.direction === 'left' && tailX < cols - 1) tailX++;
        else if (this.direction === 'up' && tailY < rows - 1) tailY++;
        else if (this.direction === 'down' && tailY > 0) tailY--;
        
        newFood = { x: tailX, y: tailY };
      }
      
      this.food = newFood;
    },
    
    // 改变方向
    changeDirection(newDirection) {
      // 防止蛇直接反向移动
      if (
        (newDirection === 'up' && this.direction !== 'down') ||
        (newDirection === 'down' && this.direction !== 'up') ||
        (newDirection === 'left' && this.direction !== 'right') ||
        (newDirection === 'right' && this.direction !== 'left')
      ) {
        this.nextDirection = newDirection;
      }
    },
    
    // 游戏结束
    gameOver() {
      // 停止游戏循环但保持游戏界面显示
      if (this.gameInterval) {
        cancelAnimationFrame(this.gameInterval);
        this.gameInterval = null;
      }
      this.isGameOver = true;
    },
    
    // 设置键盘控制
    setupKeyboardControls() {
      // 先移除可能存在的旧监听器
      document.removeEventListener('keydown', this.handleKeyDown);
      
      // 定义处理函数并绑定this
      this.handleKeyDown = (e) => {
        if (!this.isGameActive) return;
        
        // 如果游戏结束，只响应重新开始或关闭
        if (this.isGameOver) {
          if (e.key === 'Enter' || e.key === ' ') {
            this.initGame();
            e.preventDefault();
          } else if (e.key === 'Escape') {
            this.stopGame();
            e.preventDefault();
          }
          // 在游戏结束状态下也处理作弊码输入
          this.checkCheatCode(e.key);
          return;
        }
        
        // 处理方向控制键
        switch (e.key) {
          case 'ArrowUp':
            this.changeDirection('up');
            e.preventDefault();
            break;
          case 'ArrowDown':
            this.changeDirection('down');
            e.preventDefault();
            break;
          case 'ArrowLeft':
            this.changeDirection('left');
            e.preventDefault();
            break;
          case 'ArrowRight':
            this.changeDirection('right');
            e.preventDefault();
            break;
          case ' ':
            // 空格键暂停/继续游戏
            if (this.isPaused) {
              this.resumeGame();
            } else if (!this.isGameOver) {
              this.pauseGame();
            }
            e.preventDefault();
            break;
          default:
            // 其他按键可能是作弊码的一部分
            this.checkCheatCode(e.key);
            break;
        }
      };
      
      // 添加新的事件监听器
    document.addEventListener('keydown', this.handleKeyDown);
  },
  
  // 检查作弊码输入
  checkCheatCode(key) {
    // 重置作弊码如果输入特殊键
    if (key.length > 1) return;
    
    // 更新作弊码
    this.cheatCode += key;
    
    // 只保留最近的15个字符，防止内存占用过大
    if (this.cheatCode.length > 15) {
      this.cheatCode = this.cheatCode.slice(-15);
    }
    
    // 检查是否输入了作弊码
    if (this.cheatCode.includes('Valrandy·Joseph')) {
      this.toggleInvincibleMode();
      // 重置作弊码
      this.cheatCode = '';
    }
  },
  
  // 切换无敌模式
  toggleInvincibleMode() {
    this.isInvincible = !this.isInvincible;
    // 添加视觉反馈
    if (this.isInvincible) {
      // 在控制台输出提示
      console.log('无敌模式已开启！');
      // 添加分数奖励
      this.score += 100;
      // 显示视觉提示
      this.showCheatCodeMessage('无敌模式已开启！获得100分奖励！', 'success');
    } else {
      console.log('无敌模式已关闭！');
      // 显示视觉提示
      this.showCheatCodeMessage('无敌模式已关闭！', 'info');
    }
    // 强制重绘以显示无敌模式状态变化
    this.needsGridRedraw = true;
    this.draw();
  },
    
    // 处理作弊码输入框的输入事件
    onCheatCodeInput(e) {
      this.cheatCodeInput = e.target.value;
    },
    
    // 应用作弊码
    applyCheatCode() {
      if (this.cheatCodeInput === 'Valrandy·Joseph') {
        this.toggleInvincibleMode();
        // 清空输入框
        this.cheatCodeInput = '';
      } else if (this.cheatCodeInput.trim() !== '') {
        this.showCheatCodeMessage('无效的作弊码！', 'error');
      }
    },
    
    // 显示作弊码提示信息
    showCheatCodeMessage(message, type) {
      // 创建临时提示元素
      const messageElement = document.createElement('div');
      messageElement.className = `cheat-message cheat-message-${type}`;
      messageElement.textContent = message;
      messageElement.style.position = 'fixed';
      messageElement.style.top = '50%';
      messageElement.style.left = '50%';
      messageElement.style.transform = 'translate(-50%, -50%)';
      messageElement.style.padding = '15px 25px';
      messageElement.style.backgroundColor = type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#17a2b8';
      messageElement.style.color = 'white';
      messageElement.style.borderRadius = '5px';
      messageElement.style.zIndex = '10000';
      messageElement.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
      messageElement.style.animation = 'fadeInOut 2s ease-in-out';
      
      // 添加到文档
      document.body.appendChild(messageElement);
      
      // 2秒后移除
      setTimeout(() => {
        document.body.removeChild(messageElement);
      }, 2000);
    },
    
    // 调整canvas尺寸
    resizeCanvas() {
      const canvas = this.$refs.snakeCanvas;
      if (!canvas) return;
      
      // 获取父容器宽度
      const container = canvas.parentElement;
      const containerWidth = container.clientWidth;
      
      // 设置canvas尺寸为容器宽度的80%，保持正方形
      const size = Math.min(containerWidth * 0.8, 300);
      
      // 只有当尺寸变化时才重设canvas大小，避免不必要的重绘
      if (canvas.width !== size) {
        canvas.width = size;
        canvas.height = size;
        this.gridDrawn = false;
        this.needsGridRedraw = true;
        
        // 如果游戏正在进行，重新绘制
        if (this.isGameActive) {
          this.draw();
        }
      }
    }
  }
};
</script>

<style scoped>
.footer-container {
  display: flex;
  flex-direction: column;
}

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

/* 贪吃蛇游戏样式 */
.snake-area {
  margin: 20px auto;
  padding: 15px;
  background-color: rgba(34, 49, 63, 0.5);
  border-radius: 10px;
  max-width: 400px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  position: relative;
}

.game-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  padding: 5px 10px;
  background-color: rgba(66, 185, 131, 0.1);
  border-radius: 5px;
}

.game-score {
  font-size: 1rem;
  font-weight: bold;
  color: #42b983;
}

.restart-btn {
  padding: 5px 15px;
  font-size: 0.9rem;
  font-weight: 600;
  background-color: #ff6b6b;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.restart-btn:hover {
  background-color: #ff5252;
  transform: translateY(-1px);
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #999;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background-color: #f0f0f0;
  color: #666;
}

/* 游戏结束覆盖层样式 */
.game-over-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  z-index: 10;
}

.game-over-content {
  text-align: center;
  padding: 30px;
  background-color: #2c3e50;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  min-width: 250px;
}

.game-over-content h3 {
  color: #ff6b6b;
  margin-bottom: 15px;
  font-size: 1.5rem;
}

.game-over-content p {
  color: #f0f0f0;
  margin-bottom: 20px;
  font-size: 1.1rem;
}

.game-over-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
}

.game-over-buttons .restart-btn,
.game-over-buttons .close-btn {
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
  font-weight: 600;
}

.game-over-buttons .restart-btn {
  background-color: #42b983;
  color: white;
}

.game-over-buttons .restart-btn:hover {
  background-color: #35495e;
  transform: translateY(-2px);
}

.game-over-buttons .close-btn {
  background-color: #ff6b6b;
  color: white;
  width: auto;
  height: auto;
}

.game-over-buttons .close-btn:hover {
  background-color: #ff5252;
  transform: translateY(-2px);
}

.game-canvas {
  display: block;
  margin: 0 auto;
  border: 2px solid rgba(66, 185, 131, 0.3);
  border-radius: 5px;
  background-color: #1a252f;
}

.game-controls {
      display: flex;
      justify-content: center;
      width: 100%;
    }

.control-row {
  display: flex;
  gap: 8px;
}

.control-btn {
      width: 40px;
      height: 40px;
      font-size: 1rem;
      font-weight: bold;
      background-color: rgba(255, 255, 255, 0.1);
      border: 2px solid rgba(66, 185, 131, 0.3);
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.2s ease;
      color: #fff;
    }
    
    .control-btn.pause-resume-btn {
      background-color: rgba(255, 107, 107, 0.2);
      border-color: rgba(255, 107, 107, 0.5);
      transition: all 0.2s ease;
    }
    
    .control-btn.pause-resume-btn:hover {
      background-color: #ff6b6b;
      border-color: #ff6b6b;
      transform: scale(1.05);
    }
    
    .control-btn.pause-resume-btn:active {
      transform: scale(0.95);
    }
    
    .control-buttons-container {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 350px;
      margin-top: 15px;
      position: relative;
    }
    
    .direction-controls {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }
    
    .pause-resume-btn {
      position: absolute;
      right: 0;
    }

.control-btn:hover {
  background-color: #42b983;
  border-color: #42b983;
  transform: scale(1.05);
}

/* 隐蔽的游戏触发点 */
.secret-trigger {
  display: inline-block;
  font-size: 1em;
  opacity: 0.5;
  cursor: pointer;
  transition: all 0.3s ease;
  user-select: none;
}

.secret-trigger:hover {
  opacity: 1;
  transform: scale(1.2) rotate(10deg);
}

/* 作弊码输入框样式 */
.cheat-code-container {
  margin-top: 10px;
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: center;
}

.cheat-code-input {
  flex: 1;
  padding: 8px 12px;
  font-size: 0.9rem;
  border: 2px solid rgba(66, 185, 131, 0.3);
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.1);
  color: #fff;
  outline: none;
  transition: all 0.3s ease;
}

.cheat-code-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.cheat-code-input:focus {
  border-color: #42b983;
  background-color: rgba(66, 185, 131, 0.1);
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
}

.apply-cheat-btn {
  padding: 8px 16px;
  font-size: 0.9rem;
  font-weight: 600;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.apply-cheat-btn:hover {
  background-color: #35495e;
  transform: translateY(-1px);
}

.apply-cheat-btn:active {
  transform: translateY(0);
}

/* 响应式设计 */
@media (max-width: 480px) {
  .footer-content {
    flex-direction: column;
  }
  
  .footer-section {
    padding-right: 0;
  }
  
  .snake-area {
    margin: 15px auto;
    padding: 10px;
  }
  
  .control-btn {
    width: 35px;
    height: 35px;
    font-size: 0.9rem;
  }
}

@media (max-width: 360px) {
  .game-info {
    flex-wrap: wrap;
    gap: 8px;
  }
  
  .game-controls {
    margin-top: 10px;
  }
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
  width: 16px;
  height: 16px;
  filter: drop-shadow(0 0 3px rgba(255, 215, 0, 0.3));
  vertical-align: middle;
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
    padding-right: 0;}
  }
  @media (max-width: 480px) {}


/* 二维码弹窗样式 */
.qr-code-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  animation: fadeIn 0.3s ease;
}

.qr-code-modal {
  background-color: white;
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  max-width: 320px;
  width: 90%;
  animation: slideIn 0.3s ease;
}

.qr-code-content {
  text-align: center;
}

.qr-code-content h3 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.qr-code-image {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.qr-code-content p {
  color: #666;
  margin-bottom: 20px;
  font-size: 1rem;
}

.qr-code-content {
    text-align: center;
    min-width: 250px;
  }

  .qr-code-content .close-btn {
    background-color: #ff6b6b;
    color: white;
    border: none;
    padding: 20px 30px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    width: auto;
    min-width: 100px;
    display: inline-block;
    text-align: center;
    line-height: 1.2;
    white-space: nowrap;
    transition: all 0.3s ease;
  }

.qr-code-content .close-btn:hover {
  background-color: #ee5253;
  transform: translateY(-2px);
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .qr-code-modal {
    max-width: 90%;
    padding: 15px;
  }
  
  .qr-code-content h3 {
    font-size: 1.3rem;
  }
}
</style>

