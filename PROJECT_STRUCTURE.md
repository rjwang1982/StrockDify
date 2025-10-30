# 项目结构说明

**Author:** RJ.Wang | **Email:** wangrenjun@gmail.com | **GitHub:** https://github.com/rjwang1982/StrockDify

---

## 目录结构

```
StrockDify/
├── src/                                    # 源代码
│   ├── stock.py                           # FastAPI 主服务
│   └── test_client.py                     # 测试客户端
│
├── workflows/                              # Dify 工作流
│   ├── stock_chatflow.yml                 # 对话式工作流
│   ├── 股票分析工作流.yml                  # 标准工作流
│   └── 股票分析工作流-小白版.yml           # 小白版工作流
│
├── docs/                                   # 文档
│   ├── DEPLOYMENT.md                      # 部署指南
│   ├── BEGINNER_WORKFLOW.md               # 小白版说明
│   ├── FAQ.md                             # 常见问题
│   └── PROJECT_FILE_ANALYSIS.md           # 文件分析
│
├── scripts/                                # 脚本
│   └── start_server.sh                    # 启动脚本
│
├── README.md                               # 主文档
├── PROJECT_STRUCTURE.md                    # 本文件
├── requirements.txt                        # 依赖清单
├── .gitignore                              # Git 忽略
└── LICENSE                                 # MIT 许可证
```

---

## 文件说明

### 核心源代码

**src/stock.py**
- FastAPI 应用入口
- RESTful API 端点
- 股票数据获取（AkShare）
- 技术指标计算
- 智能评分系统
- Token 认证

**src/test_client.py**
- API 接口测试
- 自动禁用代理
- 批量测试支持

### Dify 工作流

**workflows/stock_chatflow.yml**
- 对话式工作流
- 多轮交互
- 通义千问模型

**workflows/股票分析工作流.yml**
- 标准工作流
- 单次执行
- 结构化输出

**workflows/股票分析工作流-小白版.yml**
- 小白版工作流
- 双层解读
- DeepSeek + Kimi 双模型

### 文档

**docs/DEPLOYMENT.md**
- 环境要求
- 安装步骤
- 配置说明
- 故障排查

**docs/BEGINNER_WORKFLOW.md**
- 工作流架构
- 节点详解
- 使用方法
- 输出示例

**docs/FAQ.md**
- 安装配置
- API 使用
- 错误处理
- 性能优化

### 脚本

**scripts/start_server.sh**
- 自动停止旧进程
- 启动新服务器
- 显示访问 URL
- 提供测试链接

### 根目录

**README.md**
- 项目概述
- 快速开始
- API 文档
- 使用指南

**requirements.txt**
- FastAPI 0.115+
- Uvicorn 0.32+
- Pandas 2.2+
- AkShare 1.14+

**.gitignore**
- 排除虚拟环境
- 排除日志文件
- 排除系统文件

---

## 文件依赖关系

```
README.md
├── src/stock.py (主服务)
├── src/test_client.py (测试)
├── scripts/start_server.sh (启动)
├── requirements.txt (依赖)
└── docs/*.md (文档)

workflows/*.yml
└── src/stock.py (API 服务)

docs/BEGINNER_WORKFLOW.md
└── workflows/股票分析工作流-小白版.yml
```

---

## 文件统计

| 类型 | 数量 | 说明 |
|------|------|------|
| Python 源码 | 2 | stock.py, test_client.py |
| Dify 工作流 | 3 | 对话式、标准版、小白版 |
| Markdown 文档 | 6 | README, FAQ, 部署等 |
| Shell 脚本 | 1 | start_server.sh |
| 配置文件 | 2 | requirements.txt, .gitignore |
| **总计** | **14** | 核心文件 |

---

## 快速导航

### 开始使用
1. 阅读 [README.md](README.md)
2. 查看 [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
3. 运行 `./scripts/start_server.sh`

### 问题解决
1. 查看 [docs/FAQ.md](docs/FAQ.md)
2. 搜索 [GitHub Issues](https://github.com/rjwang1982/StrockDify/issues)

---

**项目结构清晰，易于维护！** 🎉
