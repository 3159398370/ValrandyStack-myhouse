# 个人网站项目
#大型项目个人网页开发
这是一个使用Vue 2 + Vite作为前端，Django 4.2作为后端，MySQL 5.7作为数据库的个人网站项目。

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
- Axios (HTTP请求)
- Vue Router (路由管理)

### 后端
- Django 4.2
- Django REST Framework (API开发)
- MySQL 5.7 (数据库)

## 页面结构

1. 首页 - 个人简介和技能雷达图
2. 作品集 - 分类展示项目，支持图片/视频预览
3. 代码仓库 - 嵌入GitHub API展示仓库卡片
4. 博客 - 内容管理系统
5. 联系页 - 表单和地图组件

## 开发规范

- ESLint + Prettier (Airbnb规则)
- 组件化开发
- RESTful API设计
- 响应式布局

## 环境配置

项目包含Dockerfile配置，支持Docker部署。
cd frontend 
npm install 
npm run dev 