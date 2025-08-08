import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
});

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 从localStorage获取token并添加到请求头
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    const { response } = error;
    
    // 处理常见错误
    if (response) {
      switch (response.status) {
        case 401: // 未授权
          // 清除token并重定向到登录页
          localStorage.removeItem('token');
          // 如果有需要，可以在这里添加重定向逻辑
          break;
        case 403: // 禁止访问
          console.error('Access forbidden');
          break;
        case 404: // 资源不存在
          console.error('Resource not found');
          break;
        case 500: // 服务器错误
          console.error('Server error');
          break;
        default:
          console.error(`Error with status code: ${response.status}`);
      }
    } else {
      // 网络错误或请求被取消
      console.error('Network error or request cancelled');
    }
    
    return Promise.reject(error);
  },
);

export default api;