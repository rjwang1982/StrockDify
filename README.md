# StockDify - 股票技术分析 API

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

基于 FastAPI 的股票技术分析服务，支持 A股、港股、美股、ETF 和 LOF 的多维度技术指标分析和智能投资建议。集成 Dify 工作流，实现 AI 驱动的智能投资分析。

**Author:** RJ.Wang | **Email:** wangrenjun@gmail.com | **GitHub:** https://github.com/rjwang1982/StrockDify

---

## 核心功能

### 后端服务
- **多市场支持**：A股、港股、美股、ETF、LOF
- **技术指标**：MA、RSI、MACD、布林带、ATR、ROC、成交量分析
- **智能评分**：0-100 分综合评分系统
- **双接口**：GET（浏览器测试）+ POST（API调用）
- **Token 认证**：Bearer Token 安全机制

### Dify 工作流
- **对话式**：多轮交互分析
- **标准版**：单次技术分析
- **小白版**：专业版 + 通俗版双层解读（DeepSeek + Kimi）

---

## 快速开始

### 1. 安装

```bash
git clone https://github.com/rjwang1982/StrockDify.git
cd StrockDify

# 创建虚拟环境
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# myenv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 启动服务

```bash
# 使用启动脚本（推荐）
chmod +x scripts/start_server.sh
./scripts/start_server.sh

# 或手动启动
python src/stock.py
```

服务运行在 `http://0.0.0.0:8000`

### 3. 测试

**浏览器测试（最简单）：**
```
http://127.0.0.1:8000/test-stock/600519?token=xue123
```

**Python 测试：**
```bash
python src/test_client.py
```

**cURL 测试：**
```bash
curl -X POST "http://127.0.0.1:8000/analyze-stock/" \
  -H "Authorization: Bearer xue123" \
  -H "Content-Type: application/json" \
  -d '{"stock_code": "600519", "market_type": "A"}'
```

---

## API 接口

### 健康检查
```
GET /health
```

### 浏览器测试接口
```
GET /test-stock/{stock_code}?token=xue123&market_type=A
```

### 股票分析接口
```
POST /analyze-stock/
Headers: Authorization: Bearer xue123
Body: {"stock_code": "600519", "market_type": "A"}
```

**响应示例：**
```json
{
  "technical_summary": {
    "trend": "upward",
    "volatility": "1.51%",
    "volume_trend": "increasing",
    "rsi_level": 58.32
  },
  "report": {
    "stock_code": "600519",
    "price": 1461.00,
    "score": 65,
    "recommendation": "建议买入"
  }
}
```

---

## 支持的市场

| 市场 | 代码 | 示例 |
|------|------|------|
| A股 | `A` | 600519（贵州茅台） |
| 港股 | `HK` | 00700（腾讯控股） |
| 美股 | `US` | AAPL（苹果） |
| ETF | `ETF` | 510300（沪深300ETF） |
| LOF | `LOF` | 161725 |

---

## 技术指标

| 指标 | 说明 | 用途 |
|------|------|------|
| MA5/20/60 | 移动平均线 | 趋势判断 |
| RSI | 相对强弱指标 | 超买超卖 |
| MACD | 指数平滑异同移动平均线 | 买卖信号 |
| 布林带 | 价格波动区间 | 压力支撑 |
| ATR | 平均真实波幅 | 波动率 |
| ROC | 变动率 | 动量分析 |
| 成交量 | 交易活跃度 | 资金流向 |

---

## 评分系统

**总分 100 分：**
- 趋势（30分）：MA5 > MA20 > MA60
- RSI（20分）：30-70 区间最佳
- MACD（20分）：金叉买入信号
- 成交量（30分）：量比 > 1.5

**投资建议：**
- 80-100分：强烈推荐买入
- 60-79分：建议买入
- 40-59分：观望
- 20-39分：建议卖出
- 0-19分：强烈建议卖出

---

## Dify 工作流

### 导入步骤

1. 登录 Dify 平台
2. 导入 `workflows/` 目录下的 `.yml` 文件
3. 配置环境变量 `apikey = xue123`
4. 修改 HTTP 请求节点 URL 为你的服务器地址
5. 测试运行

### 工作流对比

| 特性 | 对话式 | 标准版 | 小白版 |
|------|--------|--------|--------|
| 交互方式 | 多轮对话 | 单次执行 | 单次执行 |
| 输出格式 | 对话回复 | 结构化 | 双层结构化 |
| AI 模型 | 通义千问 | 通义千问 | DeepSeek + Kimi |
| 适用人群 | 所有用户 | 专业用户 | 投资新手 |

---

## 项目结构

```
StrockDify/
├── src/
│   ├── stock.py              # FastAPI 主服务
│   └── test_client.py        # 测试客户端
├── workflows/
│   ├── stock_chatflow.yml    # 对话式工作流
│   ├── 股票分析工作流.yml      # 标准工作流
│   └── 股票分析工作流-小白版.yml # 小白版工作流
├── scripts/
│   └── start_server.sh       # 启动脚本
├── docs/                     # 文档目录
├── requirements.txt          # 依赖清单
└── README.md                 # 本文件
```

---

## 常见问题

**Q: 首次请求很慢？**  
A: 需要下载历史数据（10-30秒），后续请求会快很多。

**Q: 出现 502 错误？**  
A: 禁用代理设置，或在系统代理中添加 `127.0.0.1` 例外。

**Q: Token 认证失败？**  
A: 使用 `xue123` 或 `xue1234`，GET 请求用 `?token=xue123`，POST 请求用 `Authorization: Bearer xue123`。

**Q: 股票代码格式错误？**  
A: A股代码必须以 0/3/6/688/8 开头。

更多问题查看 [docs/FAQ.md](docs/FAQ.md)

---

## 局域网访问

服务器默认绑定 `0.0.0.0:8000`，支持局域网访问。

**获取本机 IP：**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1  # macOS/Linux
ipconfig  # Windows
```

**局域网访问示例：**
```
http://192.168.x.x:8000/test-stock/600519?token=xue123
```

---

## 技术栈

- **后端**：Python 3.8+, FastAPI, Uvicorn
- **数据**：AkShare, Pandas, Numpy
- **AI**：Dify, DeepSeek, Moonshot Kimi
- **认证**：Bearer Token

---

## 文档

- [部署指南](docs/DEPLOYMENT.md) - 详细部署说明
- [小白版工作流](docs/BEGINNER_WORKFLOW.md) - 小白版详细文档
- [常见问题](docs/FAQ.md) - FAQ 解答
- [项目结构](PROJECT_STRUCTURE.md) - 文件说明

---

## 免责声明

本项目仅供学习和研究使用，不构成任何投资建议。股市有风险，投资需谨慎。

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

**感谢使用 StockDify！** 📈
