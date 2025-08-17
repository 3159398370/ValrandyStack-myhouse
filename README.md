# 个人网站项目

#大型项目个人网页开发
这是一个使用 Vue 2 + Vite 作为前端，Django 4.2 作为后端，MySQL 5.7 作为数据库的个人网站项目。

## 项目结构

```
./
├── frontend/           # 前端Vue项目
└── backend/            # 后端Django项目
```

## 技术栈

### 前端

- Vue 2
- Vite
- HTML + CSS + JavaScript
- ECharts (数据可视化)
- Axios (HTTP 请求)
- Vue Router (路由管理)

### 后端

- Django 4.2
- Django REST Framework (API 开发)
- MySQL 5.7 (数据库)

## 页面结构

1. 首页 - 个人简介和技能雷达图
2. 作品集 - 分类展示项目，支持图片/视频预览
3. 代码仓库 - 嵌入 GitHub API 展示仓库卡片
4. 博客 - 内容管理系统
5. 联系页 - 表单和地图组件

## 开发规范

- ESLint + Prettier (Airbnb 规则)
- 组件化开发
- RESTful API 设计
- 响应式布局

## 快速开始

### 本地开发

1. 克隆项目
```bash
git clone https://github.com/your-username/ValrandyStack-myhouse.git
cd ValrandyStack-myhouse
```

2. 后端设置
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # 编辑.env文件配置数据库等信息
python init_db.py  # 初始化数据库
python manage.py runserver
```

3. 前端设置
```bash
cd frontend
npm install
npm run dev
```

### Docker部署

1. 使用Docker Compose一键部署
```bash
docker-compose up -d
```

2. 访问应用
- 前端: http://localhost
- 后端API: http://localhost/api/
- 管理后台: http://localhost/admin/
- API文档: http://localhost/swagger/

### 生产环境部署

详细的生产环境部署指南请参考 [DEPLOYMENT.md](DEPLOYMENT.md)

## 项目文件说明

- `deploy.sh` - 自动化部署脚本
- `nginx.conf.example` - Nginx配置模板
- `myhouse.service.example` - Systemd服务配置模板
- `Dockerfile` - Docker镜像构建文件
- `docker-compose.yml` - Docker Compose配置
- `DEPLOYMENT.md` - 详细部署文档
