import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    meta: { title: '首页' },
  },
  {
    path: '/projects',
    name: 'Projects',
    component: () => import('@/views/Projects.vue'),
    meta: { title: '作品集' },
  },
  {
    path: '/projects/:id',
    name: 'ProjectDetail',
    component: () => import('@/views/ProjectDetail.vue'),
    meta: { title: '项目详情' },
  },
  {
    path: '/repositories',
    name: 'Repositories',
    component: () => import('@/views/Repositories.vue'),
    meta: { title: '代码仓库' },
  },
  {
    path: '/blog',
    name: 'Blog',
    component: () => import('@/views/Blog.vue'),
    meta: { title: '博客' },
  },
  {
    path: '/blog/:id',
    name: 'BlogPost',
    component: () => import('@/views/BlogPost.vue'),
    meta: { title: '博客文章' },
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue'),
    meta: { title: '关于我' },
  },
  {
    path: '*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue'),
    meta: { title: '页面未找到' },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: import.meta.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title || '页面'} - ValrandyStack`;
  next();
});

export default router;