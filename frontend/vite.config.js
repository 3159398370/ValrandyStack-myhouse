import { defineConfig } from 'vite';
import vue2 from '@vitejs/plugin-vue2';
import path from 'path';

export default defineConfig({
  // 不全局注入Vue，避免重复声明
  define: {
    'process.env': {},
  },
  plugins: [vue2()],
  base: '/',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    assetsDir: 'assets',
    rollupOptions: {
      output: {
        // 移除所有资源文件名中的哈希值
        assetFileNames: (assetInfo) => {
          // 确保favicon.ico保持原名
          if (assetInfo.name === 'favicon.ico') {
            return 'favicon.ico';
          }
          return 'assets/[name][extname]';
        },
        // 移除JavaScript chunks文件名中的哈希值
        chunkFileNames: 'assets/[name].js',
        // 移除入口文件中的哈希值
        entryFileNames: 'assets/[name].js',
      },
    },
  },
});