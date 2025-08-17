# 一体化部署和修复脚本使用指南

## 概述

`deploy_all_in_one.sh` 是一个集成了以下四个脚本功能的超级脚本：

- ✅ `health_check.sh` - 基础健康检查
- ✅ `health_check_enhanced.sh` - 增强版健康检查
- ✅ `fix_static_assets.sh` - 静态资源404修复
- ✅ `deploy_and_fix.sh` - 部署和修复

## 快速开始

### 1. 一键更新
```bash
chmod +x update_all_scripts.sh
./update_all_scripts.sh
```

### 2. 基本使用
```bash
# 健康检查
./deploy_all_in_one.sh check

# 智能修复
./deploy_all_in_one.sh repair

# 修复静态资源404
./deploy_all_in_one.sh fix-assets

# 完整检查+修复流程
./deploy_all_in_one.sh full

# 查看帮助
./deploy_all_in_one.sh help
```

### 3. 服务器部署
```bash
# 上传到服务器
scp deploy_all_in_one.sh root@39.105.10.216:/usr/local/bin/

# 设置权限
ssh root@39.105.10.216 "chmod +x /usr/local/bin/deploy_all_in_one.sh"

# 执行完整流程
ssh root@39.105.10.216 "/usr/local/bin/deploy_all_in_one.sh full"

# 设置定时任务
ssh root@39.105.10.216 "echo '*/5 * * * * /usr/local/bin/deploy_all_in_one.sh check >> /var/log/health_check.log 2>&1' | crontab -"
```

## 功能详解

### 🔍 健康检查功能
- ✅ 网站可访问性检查
- ✅ 静态资源完整性验证
- ✅ 后端API健康状态
- ✅ 前端构建文件检查
- ✅ 响应时间监控
- ✅ 关键资源文件验证

### 🛠️ 修复功能
- ✅ 智能备份和恢复
- ✅ 前端依赖安装
- ✅ 前端重新构建
- ✅ Nginx配置修复
- ✅ 自动重启服务
- ✅ 修复结果验证

### 📦 部署功能
- ✅ 一键上传到服务器
- ✅ 自动设置权限
- ✅ 创建日志目录
- ✅ 部署验证

## 向后兼容

更新后，原来的脚本命令仍然可用：

```bash
# 原命令仍然有效
./health_check.sh          # 等同于 ./deploy_all_in_one.sh check
./health_check_enhanced.sh # 等同于 ./deploy_all_in_one.sh check
./fix_static_assets.sh     # 等同于 ./deploy_all_in_one.sh fix-assets
./deploy_and_fix.sh        # 等同于 ./deploy_all_in_one.sh deploy
```

## 配置选项

### 环境变量
```bash
# 设置项目路径
export PROJECT_PATH="/custom/path"

# 设置日志文件
export LOG_FILE="/var/log/myapp.log"

# 设置响应时间限制
export RESPONSE_TIME_LIMIT=5
```

### 命令行参数
```bash
# 自定义路径
./deploy_all_in_one.sh check --project-path /custom/path --log-file /var/log/app.log

# 自定义服务器部署
./deploy_all_in_one.sh deploy --server-ip 192.168.1.100 --username ubuntu
```

## 日志和监控

### 日志文件
- 主日志：`/var/log/deploy_all_in_one.log`
- 健康检查：`/var/log/health_check.log`
- Nginx访问：`/var/log/nginx/learningtree.access.log`
- Nginx错误：`/var/log/nginx/learningtree.error.log`

### 查看日志
```bash
# 实时查看健康检查日志
tail -f /var/log/health_check.log

# 查看完整日志
cat /var/log/deploy_all_in_one.log

# 查看Nginx错误日志
tail -f /var/log/nginx/learningtree.error.log
```

## 故障排查

### 常见问题

1. **权限问题**
```bash
chmod +x deploy_all_in_one.sh
chmod +x update_all_scripts.sh
```

2. **依赖问题**
```bash
# 检查系统依赖
which curl nginx node npm

# 安装缺失依赖
apt update && apt install -y curl nginx nodejs npm
```

3. **网络问题**
```bash
# 测试网络连接
curl -I https://learningtree.fun
ping 39.105.10.216
```

### 调试模式
```bash
# 查看详细输出
bash -x deploy_all_in_one.sh check
```

## 监控设置

### 添加定时任务
```bash
# 每5分钟检查一次
crontab -e
# 添加：*/5 * * * * /usr/local/bin/deploy_all_in_one.sh check >> /var/log/health_check.log 2>&1

# 每天凌晨2点完整检查
crontab -e
# 添加：0 2 * * * /usr/local/bin/deploy_all_in_one.sh full >> /var/log/deploy_all_in_one.log 2>&1
```

### 监控告警
```bash
# 检查脚本状态
systemctl status cron

# 查看定时任务日志
grep CRON /var/log/syslog
```

## 备份和恢复

### 备份目录
- 备份路径：`/www/wwwroot/learningtree.fun/backups/`
- 按时间戳组织：`20240816_143000/`

### 手动备份
```bash
# 创建备份
./deploy_all_in_one.sh repair

# 查看备份
ls -la /www/wwwroot/learningtree.fun/backups/
```

## 性能优化

### 响应时间优化
```bash
# 调整响应时间限制
export RESPONSE_TIME_LIMIT=2
./deploy_all_in_one.sh check
```

### Nginx优化
脚本已包含以下优化：
- 静态资源缓存（1年）
- Gzip压缩
- 浏览器缓存头
- CDN友好配置

## 联系支持

如有问题，请检查：
1. 日志文件内容
2. 网络连接状态
3. 文件权限设置
4. 系统依赖安装

## 更新记录

- v1.0.0: 初始版本，整合四个脚本功能
- v1.0.1: 添加向后兼容支持
- v1.0.2: 优化错误处理和日志记录