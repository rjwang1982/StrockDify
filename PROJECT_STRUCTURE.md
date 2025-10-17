# 项目结构说明

## 📁 目录结构

```
StrockDify/
├── src/                                    # 源代码目录
│   ├── strock.py                          # FastAPI 主服务
│   └── test_client.py                     # 测试客户端
│
├── workflows/                              # Dify 工作流配置
│   ├── strock_chatflow.yml                # 对话式工作流
│   ├── 股票分析工作流.yml                  # 标准工作流
│   └── 股票分析工作流-小白版.yml           # 小白版工作流
│
├── docs/                                   # 文档目录
│   ├── DEPLOYMENT.md                      # 部署指南
│   ├── BEGINNER_WORKFLOW.md               # 小白版工作流说明
│   ├── FAQ.md                             # 常见问题
│   └── PROJECT_FILE_ANALYSIS.md           # 文件分析报告
│
├── scripts/                                # 脚本目录
│   └── start_server.sh                    # 服务器启动脚本
│
├── myenv/                                  # Python 虚拟环境（不提交）
│
├── .kiro/                                  # Kiro IDE 配置（不提交）
│
├── README.md                               # 主文档
├── CHANGELOG.md                            # 更新日志
├── CONTRIBUTING.md                         # 贡献指南
├── LICENSE                                 # MIT 许可证
├── requirements.txt                        # Python 依赖
├── .gitignore                              # Git 忽略配置
└── PROJECT_STRUCTURE.md                    # 本文件
```

---

## 📄 文件说明

### 核心源代码 (`src/`)

#### `src/strock.py`
- **类型**：Python 主服务文件
- **功能**：
  - FastAPI 应用入口
  - RESTful API 端点定义
  - 股票数据获取（AkShare）
  - 技术指标计算（MA、RSI、MACD等）
  - 智能评分系统
  - Token 认证
- **依赖**：FastAPI、Uvicorn、Pandas、AkShare
- **运行**：`python src/strock.py`

#### `src/test_client.py`
- **类型**：Python 测试脚本
- **功能**：
  - 快速测试 API 接口
  - 自动禁用代理
  - 显示详细的分析结果
  - 支持批量测试
- **运行**：`python src/test_client.py`

---

### Dify 工作流 (`workflows/`)

#### `workflows/strock_chatflow.yml`
- **类型**：Dify 对话式工作流
- **特点**：
  - 支持多轮对话
  - AI 投资大师角色
  - 根据市场类型选择分析策略
- **模型**：通义千问
- **适用场景**：需要追问细节的交互式分析

#### `workflows/股票分析工作流.yml`
- **类型**：Dify 标准工作流
- **特点**：
  - 单次执行
  - 结构化输出
  - 适合批量分析
- **模型**：通义千问
- **适用场景**：快速分析、定时任务

#### `workflows/股票分析工作流-小白版.yml`
- **类型**：Dify 小白版工作流
- **特点**：
  - 双层解读（专业版 + 小白版）
  - 串行双 LLM 架构
  - 通俗易懂的语言
- **模型**：DeepSeek Chat + Moonshot Kimi
- **适用场景**：投资新手、教育培训

---

### 文档 (`docs/`)

#### `docs/DEPLOYMENT.md`
- **内容**：详细的部署和配置指南
- **包含**：
  - 环境要求
  - 安装步骤
  - 配置说明
  - Docker 部署
  - 故障排查

#### `docs/BEGINNER_WORKFLOW.md`
- **内容**：小白版工作流详细说明
- **包含**：
  - 工作流架构
  - 节点详解
  - 使用方法
  - 输出示例

#### `docs/FAQ.md`
- **内容**：常见问题解答
- **包含**：
  - 安装和配置
  - API 使用
  - Dify 工作流
  - 技术指标
  - 错误处理
  - 性能优化

#### `docs/PROJECT_FILE_ANALYSIS.md`
- **内容**：项目文件分析报告
- **包含**：
  - 文件清单
  - 冗余文件识别
  - 逻辑一致性检查
  - 优化建议

---

### 脚本 (`scripts/`)

#### `scripts/start_server.sh`
- **类型**：Shell 启动脚本
- **功能**：
  - 自动停止旧进程
  - 启动新服务器
  - 显示访问 URL
  - 提供测试链接
- **运行**：`./scripts/start_server.sh`

---

### 根目录文件

#### `README.md`
- **主文档**：完整的项目说明和使用指南
- **包含**：
  - 项目概述
  - 功能特性
  - 安装步骤
  - 快速开始
  - API 文档
  - Dify 工作流集成
  - 技术指标详解
  - 常见问题

#### `CHANGELOG.md`
- **更新日志**：版本历史和更新记录
- **格式**：遵循 Keep a Changelog 规范
- **包含**：
  - 版本号
  - 发布日期
  - 新增功能
  - Bug 修复
  - 破坏性变更

#### `CONTRIBUTING.md`
- **贡献指南**：如何为项目做贡献
- **包含**：
  - 行为准则
  - 开发流程
  - 代码规范
  - 提交规范
  - Pull Request 流程

#### `LICENSE`
- **许可证**：MIT License
- **允许**：
  - 商业使用
  - 修改
  - 分发
  - 私人使用
- **要求**：
  - 保留版权声明
  - 保留许可证声明

#### `requirements.txt`
- **依赖清单**：Python 包依赖
- **包含**：
  - FastAPI 0.104.1
  - Uvicorn 0.24.0
  - Pandas 2.1.3
  - AkShare 1.12.60
  - 其他依赖

#### `.gitignore`
- **Git 忽略配置**：不提交到仓库的文件
- **排除**：
  - `myenv/` - 虚拟环境
  - `.kiro/` - IDE 配置
  - `*.log` - 日志文件
  - `.DS_Store` - 系统文件
  - `__pycache__/` - Python 缓存

---

## 🎯 设计原则

### 1. 关注点分离
- **源代码** (`src/`)：业务逻辑
- **工作流** (`workflows/`)：AI 集成
- **文档** (`docs/`)：说明文档
- **脚本** (`scripts/`)：辅助工具

### 2. 清晰的命名
- 使用描述性的文件名
- 英文命名优先（更好的兼容性）
- 中文命名用于特定场景（工作流文件）

### 3. 文档完整性
- 每个功能都有对应文档
- 文档间相互引用
- 提供示例和最佳实践

### 4. 易于维护
- 逻辑分组
- 避免冗余
- 保持一致性

---

## 🔄 文件依赖关系

```
README.md
├── src/strock.py (主服务)
├── src/test_client.py (测试)
├── scripts/start_server.sh (启动)
├── requirements.txt (依赖)
├── docs/DEPLOYMENT.md (部署)
├── docs/FAQ.md (FAQ)
├── CONTRIBUTING.md (贡献)
└── CHANGELOG.md (更新)

workflows/*.yml
└── src/strock.py (API 服务)

docs/BEGINNER_WORKFLOW.md
└── workflows/股票分析工作流-小白版.yml
```

---

## 📊 文件统计

| 类型 | 数量 | 说明 |
|------|------|------|
| Python 源码 | 2 | strock.py, test_client.py |
| Dify 工作流 | 3 | 对话式、标准版、小白版 |
| Markdown 文档 | 7 | README, CHANGELOG, CONTRIBUTING, 等 |
| Shell 脚本 | 1 | start_server.sh |
| 配置文件 | 3 | requirements.txt, .gitignore, LICENSE |
| **总计** | **16** | 不含虚拟环境和 IDE 配置 |

---

## 🚀 快速导航

### 开始使用
1. 阅读 [README.md](README.md)
2. 查看 [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
3. 运行 `./scripts/start_server.sh`

### 开发贡献
1. 阅读 [CONTRIBUTING.md](CONTRIBUTING.md)
2. 查看 [CHANGELOG.md](CHANGELOG.md)
3. 提交 Pull Request

### 问题解决
1. 查看 [docs/FAQ.md](docs/FAQ.md)
2. 搜索 [GitHub Issues](https://github.com/rjwang1982/StrockDify/issues)
3. 提交新 Issue

---

## 📝 维护建议

### 添加新功能
1. 在 `src/` 中实现代码
2. 在 `docs/` 中添加文档
3. 更新 `README.md`
4. 更新 `CHANGELOG.md`

### 添加新工作流
1. 在 `workflows/` 中添加 `.yml` 文件
2. 在 `docs/` 中添加说明文档
3. 在 `README.md` 中添加引用

### 更新文档
1. 保持文档间的一致性
2. 更新交叉引用
3. 添加示例和截图
4. 更新版本号

---

**项目结构清晰，易于维护和扩展！** 🎉
