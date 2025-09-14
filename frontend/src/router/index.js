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
    path: '/creative-lab',
    name: 'CreativeLab',
    component: () => import('@/views/CreativeLab.vue'),
    meta: { title: '创意实验室' },
  },
  {
    path: '/creative-lab/:id',
    name: 'CreativeWork',
    component: () => import('@/views/CreativeWork.vue'),
    meta: { title: '创意作品' },
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
