# ValrandyStack 个人网站项目

> 一个现代化的全栈个人网站，展示技术实力与创意作品

## 项目特色

- **现代化 UI 设计** - 响应式布局
- **完整技术栈** - Vue 2 + Vite + Django 4.2 + MySQL
- **一键部署** - 自动化部署脚本，支持 Docker 和原生部署
- **数据可视化** - ECharts 图表展示技能雷达图
- **多媒体支持** - 图片、视频、代码项目展示
- **安全保护** - 敏感信息自动排除，生产环境安全配置
- **移动端适配** - 完美支持手机、平板、桌面设备

## 技术架构

### 前端技术栈

```
Vue 3.3+ + Vite 5.x + TypeScript
├── 状态管理：Pinia
├── 路由：Vue Router 4.x
├── UI组件：Element Plus
├── 样式：SCSS + Tailwind CSS
├── 图标：@element-plus/icons-vue
├── 图表：ECharts 5.x
└── HTTP客户端：Axios
```

### 后端技术栈

```
Django 4.2 + Python 3.8+
├── Web框架：Django 4.2 LTS
├── API：Django REST Framework
├── 数据库：MySQL 5.7+
├── 缓存：Redis（可选）
└── 部署：Gunicorn + Nginx
```

## 项目结构

```
ValrandyStack-myhouse/
├── frontend/                 # 前端Vue项目
│   ├── src/
│   │   ├── components/      # 可复用组件
│   │   ├── views/          # 页面组件
│   │   ├── router/         # 路由配置
│   │   ├── stores/         # 状态管理
│   │   ├── utils/          # 工具函数
│   │   └── assets/         # 静态资源
│   ├── package.json
│   └── vite.config.ts
├── backend/                 # 后端Django项目
│   ├── myhouse/            # Django主配置
│   ├── projects/           # 作品管理应用
│   ├── users/              # 用户管理应用
│   ├── creative_lab/       # 创意实验室
│   ├── requirements.txt
│   └── manage.py
├── issues-archive/         # 问题归档（保留在Git中）
├── docs/                   # 项目文档
├── docker-compose.yml     # Docker配置
├── deploy_all_in_one.sh   # 一体化部署脚本
└── README.md
```

## 快速开始

### 前置要求

- Python 3.8+
- Node.js 16+
- MySQL 5.7+ 或 PostgreSQL 12+
- Git

### 1. 克隆项目

```bash
git clone https://github.com/your-username/ValrandyStack-myhouse.git
cd ValrandyStack-myhouse
```

### 2. 后端配置

```bash
cd backend

# 创建虚拟环境
python -m venv venv
source /www/wwwroot/learningtree.fun/backend/venv/bin/activate  # 使用指定的虚拟环境

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件配置数据库连接

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
```

### 3. 前端配置

```bash
cd frontend

# 安装依赖
npm install

# 配置环境变量
cp .env.example .env.local
# 编辑 .env.local 文件配置API地址

# 启动开发服务器
npm run dev
```

### 4. 访问应用

- 前端开发服务器：http://localhost:5173
- 后端 API 服务器：http://localhost:8000
- Django 管理后台：http://localhost:8000/admin

## Docker 部署（推荐）

### 开发环境

```bash
# 使用Docker Compose一键启动
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```



### 本地测试

```bash
# 后端测试
cd backend
python manage.py test

# 前端测试
cd frontend
npm run test
npm run build
```

## 在线演示

- **演示地址**：https://learningtree.fun

> 注：演示环境为生产配置，部分功能可能受限

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- **项目维护者**：Valrandy·Joses
- **邮箱**：user_wrjc5857@foxmail.com
- **GitHub**：[ValrandyStack](https://github.com/ValrandyStack)

---

<div align="center">
  <p>如果这个项目对你有帮助，请给个Star支持！</p>
  <p>有任何问题或建议，欢迎提交Issue或Pull Request</p>
</div>
