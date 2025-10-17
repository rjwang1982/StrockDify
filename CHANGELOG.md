# 更新日志

所有重要的项目更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

**Author:** RJ.Wang  
**Email:** wangrenjun@gmail.com  
**GitHub:** https://github.com/rjwang1982/StrockDify

---

## [Unreleased]

### 计划中
- 添加更多技术指标（KDJ、CCI等）
- 支持更多市场（新加坡、日本股市）
- 添加基本面分析功能
- 实现历史回测功能
- 支持批量分析和定时任务

---

## [1.0.0] - 2025-01-17

### 新增
- 🎉 首次发布
- 📊 支持 A股、港股、美股、ETF、LOF 多市场分析
- 📈 实现 7 种核心技术指标（MA、RSI、MACD、布林带、ATR、ROC、成交量）
- 🎯 智能评分系统（0-100分）
- 💡 自动投资建议生成
- 🔐 Bearer Token 认证机制
- 🌐 局域网访问支持
- 🤖 集成 Dify 工作流（3种）
  - 对话式工作流
  - 标准工作流
  - 小白版工作流（双层解读）
- 🧪 测试客户端和启动脚本
- 📚 完整的文档体系

### 技术栈
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pandas 2.1.3
- AkShare 1.12.60
- Python 3.8+

### 文档
- README.md - 完整使用指南
- DEPLOYMENT.md - 部署指南
- BEGINNER_WORKFLOW.md - 小白版工作流说明
- LICENSE - MIT 许可证

---

## [0.2.0] - 2025-01-16

### 新增
- 添加小白版工作流（双层解读）
- 使用 DeepSeek 和 Moonshot Kimi 双模型
- 通俗易懂的语言转换

### 改进
- 优化 API 响应速度
- 增强错误处理机制
- 完善日志记录

---

## [0.1.0] - 2025-01-15

### 新增
- 基础 FastAPI 服务
- 股票数据获取（AkShare）
- 基本技术指标计算
- 对话式和标准 Dify 工作流

---

## 版本说明

### 版本号格式
- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

### 更新类型
- **新增**：新功能
- **改进**：对现有功能的改进
- **修复**：Bug 修复
- **变更**：对现有功能的修改
- **移除**：移除的功能
- **安全**：安全相关的修复
- **废弃**：即将移除的功能

---

## 贡献

欢迎提交 Issue 和 Pull Request！

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献。

---

## 链接

- [GitHub 仓库](https://github.com/rjwang1982/StrockDify)
- [问题反馈](https://github.com/rjwang1982/StrockDify/issues)
- [发布页面](https://github.com/rjwang1982/StrockDify/releases)
