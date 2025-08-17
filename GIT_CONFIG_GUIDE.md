# Git配置指南

## 配置变更说明

本项目已重新整合Git忽略配置，采用**统一配置+特定补充**的模式：

### 📁 文件结构
```
ValrandyStack-myhouse/
├── .gitignore                 # 🔧 统一忽略配置（主要配置）
├── frontend/.gitignore        # 🎨 前端特定忽略规则
├── backend/.gitignore         # 🐍 后端特定忽略规则
├── issues-archive/            # 📋 问题追踪（保留在git中）
└── GIT_CONFIG_GUIDE.md        # 📖 本指南
```

### 🛡️ 敏感文件保护
以下文件已被自动排除在Git之外：

#### 安全相关
- SSL证书文件：`*.key`, `*.pem`, `*.crt`, `*.p12`, `*.pfx`
- 配置文件：`config.json`, `secrets.yml`, `.env*`

#### 部署脚本
- 所有部署脚本：`deploy_*.sh`, `setup_*.sh`, `update_*.sh`
- 服务器配置：`*.conf`, `nginx.conf`

#### 日志和临时文件
- 日志文件：`*.log`, `logs/`, `tmp/`, `temp/`
- 构建缓存：`.cache/`, `.parcel-cache/`

### ✅ 保留在Git中的文件
以下文件**不会被忽略**，确保项目完整性：

```
# 核心项目文件
├── README.md
├── LICENSE
├── package.json
├── requirements.txt
├── vite.config.js
├── manage.py

# 文档和问题追踪
├── docs/
├── issues-archive/     # 完整保留问题记录
└── *.md

# 源代码
├── frontend/src/
├── backend/
└── 其他核心代码目录
```

### 🔄 验证配置

#### 检查当前状态
```bash
# 查看哪些文件被忽略
git status --ignored

# 查看忽略规则详情
git check-ignore -v filename
```

#### 测试敏感文件
```bash
# 创建测试敏感文件
touch deploy_test.sh secrets.key

# 确认被忽略
git status  # 应该看不到这些文件
```

### 📝 添加新忽略规则

如需添加新的忽略规则，请按以下优先级：

1. **通用规则** → 添加到根目录 `.gitignore`
2. **前端特定** → 添加到 `frontend/.gitignore`
3. **后端特定** → 添加到 `backend/.gitignore`

### 🔍 常见问题

#### Q: 为什么issues-archive要保留在Git中？
A: 问题追踪记录对项目维护很有价值，且不含敏感信息。

#### Q: 如何临时包含被忽略的文件？
A: 使用 `-f` 参数强制添加：
```bash
git add -f deploy_script.sh
```

#### Q: 如何查看历史忽略规则？
```bash
git log --grep="gitignore" --oneline
```

### 📊 配置效果

- ✅ **安全性**: 敏感文件100%排除
- ✅ **简洁性**: 减少冗余配置
- ✅ **可维护性**: 统一配置管理
- ✅ **完整性**: 保留所有必要文件

### 🎯 下一步

1. 执行 `git status` 确认配置生效
2. 执行 `git add .` 添加新配置
3. 执行 `git commit -m "优化Git忽略配置，增强安全性"`

配置文件已优化完成！现在您的项目具有企业级的Git安全配置。