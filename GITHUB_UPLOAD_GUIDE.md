# GitHub 上传指南

## 📋 准备工作

### 1. 检查文件

确保以下文件已准备好：
- ✅ `.gitignore` - 已创建
- ✅ `LICENSE` - 已创建
- ✅ `README.md` - 已更新
- ✅ `requirements.txt` - 已创建
- ✅ 所有源代码文件

### 2. 清理不需要上传的文件

以下文件/目录不会上传（已在 .gitignore 中）：
- `myenv/` - 虚拟环境
- `*.log` - 日志文件
- `.DS_Store` - macOS 系统文件
- `__pycache__/` - Python 缓存

---

## 🚀 上传步骤

### 方法一：使用 GitHub 网页（推荐新手）

#### 步骤 1：创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角 `+` → `New repository`
3. 填写仓库信息：
   - **Repository name**: `StrockDify` 或 `stock-analysis-api`
   - **Description**: `基于 FastAPI 的股票技术分析 API，支持 A股/港股/美股，集成 Dify AI 工作流`
   - **Public** 或 **Private**：选择公开或私有
   - ❌ 不要勾选 "Initialize this repository with a README"（我们已有 README）
4. 点击 `Create repository`

#### 步骤 2：初始化本地仓库

在项目目录下执行：

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 查看将要提交的文件
git status

# 提交
git commit -m "Initial commit: Stock Analysis API with Dify workflows"
```

#### 步骤 3：连接远程仓库

```bash
# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/StrockDify.git

# 或使用 SSH（如果已配置 SSH key）
git remote add origin git@github.com:YOUR_USERNAME/StrockDify.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

---

### 方法二：使用 GitHub Desktop（推荐新手）

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 打开 GitHub Desktop
3. 点击 `File` → `Add Local Repository`
4. 选择项目目录
5. 点击 `Publish repository`
6. 填写仓库名称和描述
7. 选择公开或私有
8. 点击 `Publish Repository`

---

### 方法三：使用命令行（完整流程）

```bash
# 1. 初始化仓库
git init

# 2. 配置用户信息（首次使用需要）
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 3. 添加所有文件
git add .

# 4. 查看状态
git status

# 5. 提交
git commit -m "Initial commit: Stock Analysis API with Dify workflows

Features:
- FastAPI backend with technical indicators
- Support for A-share, HK, US stocks, ETF, LOF
- Dify workflow integration (standard + beginner-friendly)
- Comprehensive documentation
- Test client and startup scripts"

# 6. 创建 main 分支
git branch -M main

# 7. 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/StrockDify.git

# 8. 推送到 GitHub
git push -u origin main
```

---

## 🔐 配置 SSH Key（可选，推荐）

如果使用 SSH 方式推送，需要先配置 SSH key：

### 1. 生成 SSH Key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

按 Enter 使用默认路径，设置密码（可选）。

### 2. 添加 SSH Key 到 GitHub

```bash
# 复制公钥
cat ~/.ssh/id_ed25519.pub
```

1. 登录 GitHub
2. 点击头像 → `Settings`
3. 左侧菜单 → `SSH and GPG keys`
4. 点击 `New SSH key`
5. 粘贴公钥内容
6. 点击 `Add SSH key`

### 3. 测试连接

```bash
ssh -T git@github.com
```

看到 "Hi username! You've successfully authenticated" 表示成功。

---

## 📝 后续更新

### 更新代码到 GitHub

```bash
# 1. 查看修改的文件
git status

# 2. 添加修改的文件
git add .

# 3. 提交修改
git commit -m "描述你的修改"

# 4. 推送到 GitHub
git push
```

### 常用 Git 命令

```bash
# 查看状态
git status

# 查看提交历史
git log

# 查看远程仓库
git remote -v

# 拉取最新代码
git pull

# 创建新分支
git checkout -b feature-name

# 切换分支
git checkout main

# 合并分支
git merge feature-name

# 删除分支
git branch -d feature-name
```

---

## 🎯 推荐的仓库设置

### 1. 添加 Topics（标签）

在 GitHub 仓库页面，点击 `About` 旁边的齿轮图标，添加以下 topics：

```
python
fastapi
stock-analysis
technical-indicators
akshare
dify
ai
investment
trading
api
```

### 2. 添加 Description

```
基于 FastAPI 的股票技术分析 API，支持 A股/港股/美股，集成 Dify AI 工作流，提供专业版和小白版双层解读
```

### 3. 设置 Website

如果有部署的在线服务，可以添加网址。

### 4. 启用 Issues

在 `Settings` → `Features` 中启用 Issues，方便用户反馈问题。

### 5. 添加 GitHub Actions（可选）

创建 `.github/workflows/test.yml` 自动测试：

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python test_client.py
```

---

## 📊 添加徽章（Badges）

在 README.md 顶部添加徽章：

```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Stars](https://img.shields.io/github/stars/YOUR_USERNAME/StrockDify)
![Forks](https://img.shields.io/github/forks/YOUR_USERNAME/StrockDify)
```

---

## ⚠️ 注意事项

### 1. 敏感信息

确保不要上传：
- ❌ API 密钥
- ❌ 数据库密码
- ❌ 个人隐私信息
- ❌ 生产环境配置

### 2. 大文件

GitHub 单个文件限制 100MB，仓库建议不超过 1GB。

### 3. 许可证

已添加 MIT License，允许他人自由使用和修改。

### 4. 文档

确保 README.md 包含：
- ✅ 项目介绍
- ✅ 安装步骤
- ✅ 使用方法
- ✅ API 文档
- ✅ 示例代码
- ✅ 贡献指南
- ✅ 许可证信息

---

## 🎉 完成后

1. 访问你的 GitHub 仓库页面
2. 检查所有文件是否正确上传
3. 测试 README 中的链接和代码示例
4. 分享你的项目链接！

---

## 🆘 常见问题

### Q: 推送时提示 "Permission denied"

**A:** 检查：
1. 是否正确配置了 SSH key
2. 远程仓库 URL 是否正确
3. 是否有仓库的写入权限

### Q: 推送时提示 "Updates were rejected"

**A:** 先拉取远程更新：
```bash
git pull origin main --rebase
git push origin main
```

### Q: 如何删除已提交的敏感文件？

**A:** 使用 git filter-branch 或 BFG Repo-Cleaner：
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH_TO_FILE" \
  --prune-empty --tag-name-filter cat -- --all
```

### Q: 如何修改最后一次提交？

**A:**
```bash
# 修改提交信息
git commit --amend -m "新的提交信息"

# 添加遗漏的文件
git add forgotten_file
git commit --amend --no-edit
```

---

## 📚 参考资源

- [GitHub 官方文档](https://docs.github.com/)
- [Git 教程](https://git-scm.com/book/zh/v2)
- [GitHub Desktop 文档](https://docs.github.com/en/desktop)
- [Markdown 语法](https://www.markdownguide.org/)

---

**祝你的项目在 GitHub 上获得成功！⭐**
