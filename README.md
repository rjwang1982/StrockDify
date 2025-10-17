# 股票技术分析 API (StrockDify)

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Stars](https://img.shields.io/github/stars/rjwang1982/StrockDify)
![Forks](https://img.shields.io/github/forks/rjwang1982/StrockDify)

基于 FastAPI 的专业股票技术分析服务，支持 A股、港股、美股、ETF 和 LOF 基金的多维度技术指标分析和智能投资建议。本项目提供 RESTful API 接口，并集成 Dify 工作流，可实现 AI 驱动的智能投资分析，包括专业版和小白版双层解读。

---

**Author:** RJ.Wang  
**Email:** wangrenjun@gmail.com  
**GitHub:** https://github.com/rjwang1982/StrockDify  
**License:** MIT

---

## 📋 项目概述

StrockDify 是一个完整的股票技术分析解决方案，包含以下核心组件：

### 后端服务
- **FastAPI 后端服务** (`src/strock.py`)：提供股票数据获取、技术指标计算和评分系统
- **Python 测试客户端** (`src/test_client.py`)：用于快速测试 API 接口
- **启动脚本** (`scripts/start_server.sh`)：一键启动服务器
- **依赖管理** (`requirements.txt`)：Python 依赖包清单

### Dify 工作流配置
- **对话式工作流** (`workflows/strock_chatflow.yml`)：支持连续对话的股票分析
- **标准工作流** (`workflows/股票分析工作流.yml`)：单次执行的专业分析
- **小白版工作流** (`workflows/股票分析工作流-小白版.yml`)：专业版 + 通俗版双层解读

### 文档
- **主文档** (`README.md`)：完整的项目说明和使用指南
- **部署指南** ([docs/DEPLOYMENT.md](docs/DEPLOYMENT.md))：详细的部署和配置说明
- **小白版说明** ([docs/BEGINNER_WORKFLOW.md](docs/BEGINNER_WORKFLOW.md))：小白版工作流详细文档
- **常见问题** ([docs/FAQ.md](docs/FAQ.md))：常见问题解答
- **贡献指南** ([CONTRIBUTING.md](CONTRIBUTING.md))：如何贡献代码
- **更新日志** ([CHANGELOG.md](CHANGELOG.md))：版本更新记录

## 功能特性

### 核心功能

- 📊 **多市场支持**：A股、港股、美股、ETF、LOF 基金
- 📈 **丰富的技术指标**：
  - 移动平均线（MA5/MA20/MA60）
  - 相对强弱指标（RSI）
  - MACD 指标
  - 布林带（Bollinger Bands）
  - 平均真实波幅（ATR）
  - 变动率指标（ROC）
  - 成交量分析
- 🎯 **智能评分系统**：综合多个技术指标给出 0-100 分评分
- 💡 **投资建议生成**：根据评分自动生成投资建议
- 🔐 **Token 认证**：Bearer Token 安全认证机制
- 🌐 **局域网访问**：支持局域网内其他设备访问
- 🤖 **AI 增强分析**：集成 Dify 工作流，提供 AI 驱动的深度分析

### 技术特点

- 使用 AkShare 获取实时股票数据
- 支持前复权数据处理
- 详细的请求日志记录
- 完善的错误处理机制
- 支持自定义日期范围查询

## 环境要求

- Python 3.8+
- 依赖库：
  - FastAPI
  - Uvicorn
  - Pandas
  - AkShare
  - Requests
  - Pydantic

## 📦 安装步骤

### 方法一：使用 requirements.txt（推荐）

1. **克隆项目**

```bash
git clone https://github.com/rjwang1982/StrockDify.git
cd StrockDify
```

2. **创建虚拟环境**（推荐）

```bash
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# 或
myenv\Scripts\activate  # Windows
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

这将自动安装以下依赖：
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pydantic 2.5.0
- Pandas 2.1.3
- Numpy 1.26.2
- AkShare 1.12.60
- Requests 2.31.0
- Python-multipart 0.0.6

### 方法二：手动安装

```bash
pip install fastapi uvicorn pandas akshare requests pydantic
```

### 验证安装

```bash
python -c "import fastapi, akshare, pandas; print('安装成功！')"
```

## 🚀 快速开始

### 方法一：使用启动脚本（推荐）⭐

```bash
chmod +x scripts/start_server.sh  # 首次使用需要添加执行权限
./scripts/start_server.sh
```

**启动脚本功能：**
- ✅ 自动停止旧的服务器进程（避免端口冲突）
- ✅ 启动新的服务器实例
- ✅ 显示服务器 PID
- ✅ 显示本机访问 URL
- ✅ 显示局域网访问 URL
- ✅ 提供测试链接示例

**输出示例：**
```
停止旧服务器...
启动服务器...
服务器PID: 12345
等待启动...

==========================================
服务器已启动！
==========================================

本机访问URL：

1. 健康检查：
   http://127.0.0.1:8000/
   http://127.0.0.1:8000/health

2. 测试贵州茅台 (600519)：
   http://127.0.0.1:8000/test-stock/600519?token=xue123

3. 测试平安银行 (000001)：
   http://127.0.0.1:8000/test-stock/000001?token=xue123

==========================================
局域网访问URL：
==========================================

从其他机器访问，使用本机IP地址：

1. 健康检查：
   http://192.168.132.2:8000/

2. 测试贵州茅台：
   http://192.168.132.2:8000/test-stock/600519?token=xue123

==========================================

停止服务器: pkill -f 'python.*strock.py'
```

### 方法二：手动启动

```bash
# 使用虚拟环境中的 Python
./myenv/bin/python src/strock.py

# 或直接使用系统 Python
python src/strock.py

# 或使用 uvicorn
uvicorn src.strock:app --host 0.0.0.0 --port 8000
```

服务器将在 `http://0.0.0.0:8000` 启动，支持本机和局域网访问。

### 方法三：后台运行

```bash
# 后台运行并保存日志
nohup ./myenv/bin/python src/strock.py > server.log 2>&1 &

# 查看日志
tail -f server.log

# 停止服务
pkill -f 'python.*src/strock.py'
```

### 🧪 测试接口

#### 1. 浏览器快速测试（GET 请求）⭐ 最简单

直接在浏览器中访问，无需任何工具：

```
http://127.0.0.1:8000/test-stock/600519?token=xue123
```

**支持的参数：**
- `stock_code`：股票代码（必填）
- `token`：认证令牌，使用 `xue123` 或 `xue1234`（必填）
- `market_type`：市场类型，默认 `A`（可选）

**更多示例：**
```
# A股 - 贵州茅台
http://127.0.0.1:8000/test-stock/600519?token=xue123

# A股 - 平安银行
http://127.0.0.1:8000/test-stock/000001?token=xue123&market_type=A

# ETF - 沪深300ETF
http://127.0.0.1:8000/test-stock/510300?token=xue123&market_type=ETF

# 港股 - 腾讯控股
http://127.0.0.1:8000/test-stock/00700?token=xue123&market_type=HK

# 美股 - 苹果
http://127.0.0.1:8000/test-stock/AAPL?token=xue123&market_type=US
```

#### 2. 使用 Python 测试客户端 (`test_client.py`)

**功能特点：**
- ✅ 自动禁用代理设置（解决 502 错误）
- ✅ 测试多个股票代码
- ✅ 显示详细的分析结果
- ✅ 友好的错误提示

**运行测试：**
```bash
./myenv/bin/python src/test_client.py
```

**输出示例：**
```
============================================================
测试1: 分析A股股票 (贵州茅台 600519)
============================================================
正在分析股票: 600519
请求URL: http://127.0.0.1:8000/analyze-stock/
响应状态码: 200

✅ 分析成功!

股票代码: 600519
当前价格: 1461.00
涨跌幅: 0.69%
综合评分: 65
投资建议: 建议买入

技术指标:
  趋势: upward
  波动率: 1.51%
  成交量: decreasing
  RSI: 58.32

============================================================
测试2: 分析A股股票 (平安银行 000001)
============================================================
...
```

**自定义测试：**

编辑 `src/test_client.py` 添加更多测试：

```python
# 测试你自己的股票
test_stock_analysis("002352", "A")  # 顺丰控股
test_stock_analysis("300750", "A")  # 宁德时代
```

#### 3. 使用 cURL 测试（POST 请求）

**基本请求：**
```bash
curl -X POST "http://127.0.0.1:8000/analyze-stock/" \
  -H "Authorization: Bearer xue123" \
  -H "Content-Type: application/json" \
  -d '{
    "stock_code": "600519",
    "market_type": "A"
  }'
```

**带日期范围的请求：**
```bash
curl -X POST "http://127.0.0.1:8000/analyze-stock/" \
  -H "Authorization: Bearer xue123" \
  -H "Content-Type: application/json" \
  -d '{
    "stock_code": "600519",
    "market_type": "A",
    "start_date": "20240101",
    "end_date": "20241231"
  }'
```

**格式化输出（使用 jq）：**
```bash
curl -X POST "http://127.0.0.1:8000/analyze-stock/" \
  -H "Authorization: Bearer xue123" \
  -H "Content-Type: application/json" \
  -d '{"stock_code": "600519", "market_type": "A"}' \
  | jq '.'
```

#### 4. 使用 Python Requests

**基本用法：**
```python
import requests

url = "http://127.0.0.1:8000/analyze-stock/"
headers = {
    "Authorization": "Bearer xue123",
    "Content-Type": "application/json"
}
payload = {
    "stock_code": "600519",
    "market_type": "A"
}

response = requests.post(url, json=payload, headers=headers)
result = response.json()

# 打印结果
print(f"股票代码: {result['report']['stock_code']}")
print(f"当前价格: {result['report']['price']}")
print(f"综合评分: {result['report']['score']}")
print(f"投资建议: {result['report']['recommendation']}")
```

**批量分析：**
```python
import requests

stocks = ["600519", "000001", "002352", "300750"]

for stock_code in stocks:
    response = requests.post(
        "http://127.0.0.1:8000/analyze-stock/",
        headers={"Authorization": "Bearer xue123"},
        json={"stock_code": stock_code, "market_type": "A"}
    )
    result = response.json()
    print(f"{stock_code}: {result['report']['recommendation']}")
```

#### 5. 使用 Postman 测试

1. 创建新请求
2. 方法：POST
3. URL：`http://127.0.0.1:8000/analyze-stock/`
4. Headers：
   - `Authorization`: `Bearer xue123`
   - `Content-Type`: `application/json`
5. Body（raw JSON）：
```json
{
  "stock_code": "600519",
  "market_type": "A"
}
```
6. 点击 Send

## API 接口文档

### 1. 健康检查接口

检查服务器运行状态。

**端点：**
```
GET /
GET /health
```

**响应示例：**
```json
{
  "status": "ok",
  "message": "股票分析API正在运行"
}
```

### 2. 浏览器测试接口（GET）

适合浏览器直接访问，快速测试股票分析功能。

**端点：**
```
GET /test-stock/{stock_code}
```

**查询参数：**
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `stock_code` | string | 是 | - | 股票代码 |
| `token` | string | 是 | - | 认证令牌（`xue123` 或 `xue1234`） |
| `market_type` | string | 否 | `A` | 市场类型（A/HK/US/ETF/LOF） |

**请求示例：**
```
http://127.0.0.1:8000/test-stock/600519?token=xue123
http://127.0.0.1:8000/test-stock/000001?token=xue123&market_type=A
http://127.0.0.1:8000/test-stock/510300?token=xue123&market_type=ETF
```

**响应示例：**
```json
{
  "stock_code": "600519",
  "market_type": "A",
  "analysis_date": "2025-01-15",
  "score": 65,
  "price": 1461.00,
  "price_change": 0.69,
  "ma_trend": "UP",
  "rsi": 58.32,
  "macd_signal": "BUY",
  "volume_status": "NORMAL",
  "recommendation": "建议买入",
  "technical_indicators": {
    "MA5": 1455.20,
    "MA20": 1420.50,
    "MA60": 1380.30,
    "RSI": 58.32,
    "MACD": 12.45,
    "volatility": "1.51%",
    "volume_ratio": 1.23
  }
}
```

### 3. 股票分析接口（POST）

完整的股票技术分析接口，支持自定义日期范围。

**端点：**
```
POST /analyze-stock/
```

**请求头：**
```
Authorization: Bearer xue123
Content-Type: application/json
```

**请求体参数：**
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `stock_code` | string | 是 | - | 股票代码 |
| `market_type` | string | 否 | `A` | 市场类型 |
| `start_date` | string | 否 | 365天前 | 开始日期（格式：YYYYMMDD） |
| `end_date` | string | 否 | 今天 | 结束日期（格式：YYYYMMDD） |

**请求示例：**
```json
{
  "stock_code": "600519",
  "market_type": "A",
  "start_date": "20240101",
  "end_date": "20241231"
}
```

**响应示例：**
```json
{
  "technical_summary": {
    "trend": "upward",
    "volatility": "1.51%",
    "volume_trend": "decreasing",
    "rsi_level": 58.32
  },
  "recent_data": [
    {
      "date": "2024-12-20",
      "open": 1450.00,
      "close": 1461.00,
      "high": 1465.00,
      "low": 1448.00,
      "volume": 12345678
    }
  ],
  "report": {
    "stock_code": "600519",
    "market_type": "A",
    "analysis_date": "2025-01-15",
    "score": 65,
    "price": 1461.00,
    "price_change": 0.69,
    "ma_trend": "UP",
    "rsi": 58.32,
    "macd_signal": "BUY",
    "volume_status": "NORMAL",
    "recommendation": "建议买入"
  }
}
```

**错误响应：**
```json
{
  "detail": "数据验证错误: 无效的A股股票代码格式"
}
```

## 支持的市场类型

| 市场类型 | 代码 | 说明 | 数据源 |
|---------|------|------|--------|
| A股 | `A` | 中国A股市场（默认） | AkShare |
| 港股 | `HK` | 香港股票市场 | AkShare |
| 美股 | `US` | 美国股票市场 | AkShare |
| ETF | `ETF` | 交易型开放式指数基金 | AkShare |
| LOF | `LOF` | 上市型开放式基金 | AkShare |

## 股票代码示例

### A股代码格式
A股代码必须以以下数字开头：
- `0`：深圳主板（如 `000001` 平安银行）
- `3`：创业板（如 `300750` 宁德时代）
- `6`：上海主板（如 `600519` 贵州茅台）
- `688`：科创板（如 `688981` 中芯国际）
- `8`：北交所（如 `830799` 艾融软件）

### 常用股票代码

**A股热门股票：**
- `600519`：贵州茅台
- `000001`：平安银行
- `000858`：五粮液
- `300750`：宁德时代
- `002352`：顺丰控股

**ETF 基金：**
- `510300`：沪深300ETF
- `510500`：中证500ETF
- `159915`：创业板ETF
- `512880`：证券ETF

**美股示例：**
- `AAPL`：苹果
- `TSLA`：特斯拉
- `MSFT`：微软
- `GOOGL`：谷歌

## 局域网访问

服务器默认绑定到 `0.0.0.0:8000`，支持局域网内其他设备访问。

### 获取本机 IP 地址

**macOS/Linux：**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**Windows：**
```cmd
ipconfig
```

### 局域网访问示例

假设服务器 IP 为 `192.168.132.2`：

```
# 健康检查
http://192.168.132.2:8000/health

# 股票分析
http://192.168.132.2:8000/test-stock/600519?token=xue123

# 从手机或其他设备访问
http://192.168.132.2:8000/test-stock/000001?token=xue123&market_type=A
```

## 技术指标详解

### 1. 移动平均线（MA - Moving Average）

使用指数移动平均线（EMA）计算：

| 指标 | 周期 | 用途 |
|------|------|------|
| MA5 | 5日 | 短期趋势判断 |
| MA20 | 20日 | 中期趋势判断 |
| MA60 | 60日 | 长期趋势判断 |

**判断规则：**
- MA5 > MA20 > MA60：多头排列，上涨趋势
- MA5 < MA20 < MA60：空头排列，下跌趋势

### 2. 相对强弱指标（RSI - Relative Strength Index）

- **周期**：14天
- **取值范围**：0-100
- **判断标准**：
  - RSI > 70：超买区域，可能回调
  - 30 < RSI < 70：正常区域
  - RSI < 30：超卖区域，可能反弹

### 3. MACD 指标

- **快线（DIF）**：12日EMA - 26日EMA
- **慢线（DEA/Signal）**：DIF的9日EMA
- **柱状图（Histogram）**：DIF - DEA

**判断规则：**
- MACD > Signal：买入信号
- MACD < Signal：卖出信号
- 金叉（MACD上穿Signal）：强烈买入信号
- 死叉（MACD下穿Signal）：强烈卖出信号

### 4. 布林带（Bollinger Bands）

- **中轨**：20日移动平均线
- **上轨**：中轨 + 2倍标准差
- **下轨**：中轨 - 2倍标准差

**判断规则：**
- 价格触及上轨：超买，可能回调
- 价格触及下轨：超卖，可能反弹
- 布林带收窄：波动率降低，可能突破
- 布林带扩张：波动率增加

### 5. 平均真实波幅（ATR - Average True Range）

- **周期**：14天
- **用途**：衡量价格波动性
- **波动率计算**：ATR / 当前价格 × 100%

### 6. 变动率指标（ROC - Rate of Change）

- **周期**：10天
- **计算**：(当前价格 - 10天前价格) / 10天前价格 × 100%
- **用途**：衡量价格变动速度

### 7. 成交量分析

- **成交量均线**：20日成交量移动平均
- **成交量比率**：当日成交量 / 成交量均线
- **判断标准**：
  - 比率 > 1.5：成交量放大
  - 1.0 < 比率 < 1.5：成交量正常
  - 比率 < 1.0：成交量萎缩

## 智能评分系统

系统综合多个技术指标，给出 0-100 分的综合评分。

### 评分规则（总分100分）

| 评分项 | 分值 | 判断标准 |
|--------|------|----------|
| **趋势得分** | 30分 | MA5 > MA20（15分）+ MA20 > MA60（15分） |
| **RSI得分** | 20分 | 30 ≤ RSI ≤ 70（20分）或 RSI < 30（15分） |
| **MACD得分** | 20分 | MACD > Signal（20分） |
| **成交量得分** | 30分 | 成交量比率 > 1.5（30分）或 > 1.0（15分） |

### 投资建议分级

| 评分区间 | 建议 | 说明 |
|---------|------|------|
| **80-100分** | 强烈推荐买入 | 多项指标向好，趋势强劲 |
| **60-79分** | 建议买入 | 技术面较好，可适当建仓 |
| **40-59分** | 观望 | 技术面中性，等待明确信号 |
| **20-39分** | 建议卖出 | 技术面转弱，建议减仓 |
| **0-19分** | 强烈建议卖出 | 多项指标转差，风险较大 |

**注意：** 本评分系统仅供参考，不构成投资建议。投资有风险，决策需谨慎。

## 🤖 Dify 工作流集成

项目包含三个 Dify 工作流配置文件，可导入到 Dify 平台使用。

### 1. 对话式股票分析工作流 (`strock_chatflow.yml`)

**特点：**
- 💬 对话式交互界面
- 🔄 支持连续对话
- 🎓 AI 投资大师角色
- 🔗 自动调用股票分析 API

**功能流程：**
```
用户输入 → 验证输入 → 变量聚合 → HTTP请求 → 解析数据 → 条件分支 → LLM分析 → 输出结果
```

**工作流节点：**
1. **开始节点**：接收股票代码和市场类型
2. **判断节点**：验证股票代码是否为空
3. **变量聚合器**：整合输入参数
4. **HTTP 请求**：调用后端 API 获取数据
5. **代码执行**：解析 JSON 响应
6. **条件分支**：根据市场类型选择分析策略
7. **LLM 节点**：生成专业分析报告
8. **直接回复**：输出分析结果

**分析内容包括：**
- 趋势分析（支撑位和压力位）
- 成交量分析及其含义
- 风险评估（波动率分析）
- 短期和中期目标价位
- 关键技术位分析
- 具体交易建议（包含止损位）
- 当前交易策略

**适用场景：**
- 需要多轮对话的交互式分析
- 用户需要追问细节
- 实时咨询投资建议

---

### 2. 标准股票分析工作流 (`股票分析工作流.yml`)

**特点：**
- 📊 单次执行工作流
- 📋 结构化输出
- ⚡ 适合批量分析
- 🎯 专业技术分析

**功能流程：**
```
开始 → 验证输入 → 获取股票数据 → 解析响应 → AI投资分析 → 输出结果
```

**工作流节点：**
1. **开始**：输入股票代码和市场类型
2. **验证输入**：检查股票代码是否为空
3. **获取股票数据**：HTTP 请求调用 API
4. **解析响应数据**：Python 代码解析 JSON
5. **AI投资分析**：使用通义千问生成报告
6. **结束**：输出结构化结果

**输出字段：**
- `stock_code`：股票代码
- `current_price`：当前价格
- `score`：综合评分
- `recommendation`：投资建议
- `analysis_report`：AI 生成的详细分析报告

**适用场景：**
- 单次快速分析
- 批量处理多只股票
- 定时任务自动分析

---

### 3. 小白版股票分析工作流 (`股票分析工作流-小白版.yml`) ⭐ 推荐

**特点：**
- 💡 双层分析输出：专业版 + 小白版
- 🎨 通俗易懂的语言
- 😊 生活化比喻和 emoji
- 🔄 串行双 LLM 架构

**功能流程：**
```
开始 → 验证 → 获取数据 → 解析 → AI专业分析 → 小白版解读 → 双层输出
```

**工作流节点：**
1. **开始**：输入股票代码和市场类型
2. **验证输入**：检查代码有效性
3. **获取股票数据**：HTTP API 调用
4. **解析响应数据**：提取关键指标
5. **AI投资分析**（DeepSeek）：生成专业技术分析
6. **小白版解读**（Moonshot Kimi）：转换为通俗语言
7. **结束**：输出专业版 + 小白版两份报告

**双层输出示例：**

**专业版报告** (`professional_report`)：
```
## 趋势分析
- 当前趋势：短期上升，中期震荡
- 支撑位：45.20 元（MA20）
- 压力位：52.80 元（前期高点）
- RSI(14)：68.5，接近超买区域
```

**小白版报告** (`simplified_report`)：
```
📊 这只股票现在处于上涨趋势，但涨得有点快了！

✅ 好消息：价格在往上走，像爬楼梯一样
⚠️ 注意：涨太快可能要歇一歇
💡 建议：等降到 46-47 元再买
🚦 风险：黄灯（中等风险）
```

**转换策略：**
- 支撑位 → "安全垫"
- 压力位 → "天花板"
- RSI超买 → "商品太火爆，可能要降价"
- MACD金叉 → "两条线交叉，发出买入信号"
- 成交量 → "买卖的热闹程度"

**适用场景：**
- 投资新手需要通俗解释
- 需要同时查看专业和通俗版本
- 教育和培训场景
- 向非专业人士展示分析结果

**详细文档：** 查看 `股票分析工作流-小白版-README.md`

---

### 📥 导入 Dify 工作流

#### 步骤 1：导入配置文件

1. 登录 Dify 平台
2. 进入"工作流"管理页面
3. 点击"导入工作流"
4. 选择对应的 `.yml` 配置文件：
   - 对话式：`strock_chatflow.yml`
   - 标准版：`股票分析工作流.yml`
   - 小白版：`股票分析工作流-小白版.yml`
5. 点击"导入"

#### 步骤 2：配置环境变量

在工作流设置中配置环境变量：

| 变量名 | 值 | 说明 |
|--------|-----|------|
| `apikey` | `xue123` | API 认证密钥 |

#### 步骤 3：修改 API 地址

找到"HTTP 请求"节点，修改 URL：

```
# 默认地址（局域网）
http://192.168.132.2:8000/analyze-stock/

# 修改为你的服务器地址
http://YOUR_SERVER_IP:8000/analyze-stock/
```

#### 步骤 4：配置 AI 模型（仅小白版需要）

小白版工作流使用两个 AI 模型：

1. **AI投资分析节点**：
   - 模型：DeepSeek Chat
   - 用途：生成专业分析
   - 参数：temperature=0.7, max_tokens=2000

2. **小白版解读节点**：
   - 模型：Moonshot Kimi K2 Turbo
   - 用途：转换通俗语言
   - 参数：temperature=0.7, max_tokens=2000

确保已安装对应的模型插件：
- DeepSeek 插件
- Moonshot 插件

#### 步骤 5：测试工作流

1. 点击"运行"或"调试"
2. 输入测试数据：
   - 股票代码：`002352`
   - 市场类型：`A`
3. 查看输出结果
4. 验证数据正确性

#### 步骤 6：发布工作流

测试通过后：
1. 点击"发布"
2. 选择发布方式（API/应用）
3. 获取访问链接或 API 密钥

---

### 🔧 工作流对比

| 特性 | 对话式 | 标准版 | 小白版 |
|------|--------|--------|--------|
| **交互方式** | 多轮对话 | 单次执行 | 单次执行 |
| **输出格式** | 对话回复 | 结构化 | 双层结构化 |
| **AI 模型** | 通义千问 | 通义千问 | DeepSeek + Kimi |
| **分析深度** | 可追问 | 固定深度 | 双层深度 |
| **适用人群** | 所有用户 | 专业用户 | 投资新手 |
| **执行速度** | 较快 | 快 | 较慢（双LLM） |
| **成本** | 低 | 低 | 中（双模型） |

---

### 💡 使用建议

**选择对话式工作流，如果：**
- 需要多轮交互
- 用户想追问细节
- 实时咨询场景

**选择标准版工作流，如果：**
- 批量分析多只股票
- 定时任务自动执行
- 需要结构化输出

**选择小白版工作流，如果：**
- 用户是投资新手
- 需要通俗易懂的解释
- 教育培训场景
- 向非专业人士展示

## 📁 项目文件说明

### 核心服务文件

| 文件名 | 类型 | 说明 |
|--------|------|------|
| `src/strock.py` | Python | FastAPI 主服务文件，包含所有 API 端点和技术指标计算逻辑 |
| `src/test_client.py` | Python | 测试客户端，用于快速测试 API 功能，自动禁用代理 |
| `scripts/start_server.sh` | Shell | 服务器启动脚本，自动停止旧进程并启动新服务，显示访问 URL |
| `requirements.txt` | Text | Python 依赖包清单，包含 FastAPI、AkShare 等 |

### Dify 工作流配置

| 文件名 | 类型 | 说明 |
|--------|------|------|
| `strock_chatflow.yml` | YAML | 对话式工作流，支持多轮对话和连续分析 |
| `股票分析工作流.yml` | YAML | 标准工作流，单次执行，结构化输出 |
| `股票分析工作流-小白版.yml` | YAML | 小白版工作流，双层解读（专业版+通俗版） |

### 文档文件

| 文件名 | 说明 |
|--------|------|
| `README.md` | 项目主文档，包含完整的功能介绍和使用指南 |
| `README-部署指南.md` | 详细的部署、配置和故障排查指南 |
| `股票分析工作流-小白版-README.md` | 小白版工作流的详细说明文档 |

### 其他文件

| 文件/目录 | 说明 |
|----------|------|
| `myenv/` | Python 虚拟环境目录（不提交到 Git） |
| `.kiro/` | Kiro IDE 配置目录 |
| `.DS_Store` | macOS 系统文件（不提交到 Git） |

## 服务器管理

### 启动服务器

```bash
# 使用启动脚本（推荐）
./start_server.sh

# 或手动启动
./myenv/bin/python strock.py

# 或使用 uvicorn
uvicorn strock:app --host 0.0.0.0 --port 8000
```

### 停止服务器

```bash
# 方法1：使用 pkill
pkill -f 'python.*strock.py'

# 方法2：查找进程并杀死
ps aux | grep strock.py
kill <PID>

# 方法3：使用 Ctrl+C（如果在前台运行）
```

### 查看服务器日志

#### 前台运行（推荐）

直接在终端查看实时日志：

```bash
./myenv/bin/python strock.py
```

#### 后台运行

保存日志到文件：

```bash
# 启动并保存日志
nohup ./myenv/bin/python strock.py > server.log 2>&1 &

# 实时查看日志
tail -f server.log

# 查看最近 100 行
tail -n 100 server.log
```

#### 日志内容说明

服务器输出的详细日志包括：

**POST 请求日志：**
- 请求方法和 URL
- 客户端 IP 和端口
- 请求头（Headers）
- 请求体原始数据和解析后的 JSON
- 参数类型和值

**分析过程日志：**
- 股票代码和市场类型
- 数据获取进度（记录条数）
- 技术指标计算状态
- 综合评分结果
- 分析完成状态

**错误日志：**
- 数据验证错误
- 服务器错误
- 完整的错误堆栈信息

**日志位置：**
- `@app.middleware("http")`：记录所有 POST 请求详情
- `analyze_stock()`：分析步骤和进度
- `test_stock_browser()`：GET 请求测试日志

## 常见问题与解决方案

### 1. 代理问题导致连接失败

**问题：** 本地测试时出现 502 错误或连接超时

**解决方案：**
```python
# 在测试脚本中禁用代理
import os
os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'
```

或在系统设置中为 `127.0.0.1` 和 `localhost` 添加代理例外。

### 2. 首次请求响应慢

**原因：** AkShare 需要下载历史数据

**解决方案：**
- 首次请求耐心等待（通常 10-30 秒）
- 后续请求会快很多
- 可以设置更短的日期范围

### 3. 股票代码格式错误

**错误信息：** "无效的A股股票代码格式"

**解决方案：**
- 确保 A股代码以 0、3、6、688 或 8 开头
- 检查代码长度（通常为 6 位数字）
- 使用正确的市场类型参数

### 4. Token 认证失败

**错误信息：** "Invalid or Expired Token"

**解决方案：**
- 使用有效的 token：`xue123` 或 `xue1234`
- 确保 Authorization header 格式正确：`Bearer xue123`
- GET 请求使用查询参数：`?token=xue123`

### 5. 端口被占用

**错误信息：** "Address already in use"

**解决方案：**
```bash
# 查找占用 8000 端口的进程
lsof -i :8000

# 杀死进程
kill -9 <PID>

# 或使用启动脚本（会自动处理）
./start_server.sh
```

### 6. 虚拟环境问题

**问题：** 找不到依赖库

**解决方案：**
```bash
# 确保激活虚拟环境
source myenv/bin/activate

# 重新安装依赖
pip install -r requirements.txt

# 或手动安装
pip install fastapi uvicorn pandas akshare requests pydantic
```

## 使用注意事项

1. **数据延迟**：股票数据可能有 15 分钟延迟，具体取决于数据源
2. **请求频率**：避免过于频繁的请求，建议间隔至少 1 秒
3. **数据准确性**：技术指标基于历史数据计算，仅供参考
4. **投资风险**：本系统不构成投资建议，投资有风险，决策需谨慎
5. **网络要求**：需要稳定的网络连接以获取实时数据
6. **Token 安全**：生产环境应使用更安全的认证机制
7. **日期格式**：日期参数使用 `YYYYMMDD` 格式（如 `20240101`）
8. **市场时间**：非交易时间获取的是最近一个交易日的数据

## 技术架构

```
┌─────────────────┐
│   客户端请求     │
│ (Browser/API)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FastAPI 服务   │
│  - 路由处理     │
│  - Token 认证   │
│  - 请求日志     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  数据获取层     │
│  - AkShare API  │
│  - 数据清洗     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  技术指标计算   │
│  - MA/RSI/MACD  │
│  - 布林带/ATR   │
│  - 成交量分析   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  评分系统       │
│  - 综合评分     │
│  - 投资建议     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  JSON 响应      │
│  - 技术指标     │
│  - 分析报告     │
└─────────────────┘
```

## 扩展开发

### 添加新的技术指标

在 `src/strock.py` 中添加计算函数：

```python
def calculate_new_indicator(df, period):
    """计算新指标"""
    # 实现计算逻辑
    return result

# 在 calculate_indicators 函数中调用
df['NEW_INDICATOR'] = calculate_new_indicator(df, period)
```

### 修改评分规则

在 `calculate_score` 函数中调整权重：

```python
def calculate_score(df):
    score = 0
    latest = df.iloc[-1]
    
    # 修改权重或添加新的评分项
    if latest['MA5'] > latest['MA20']:
        score += 20  # 调整分值
    
    return score
```

### 添加新的市场类型

在 `get_stock_data` 函数中添加新的市场支持：

```python
elif market_type == 'NEW_MARKET':
    df = ak.new_market_api(
        symbol=stock_code,
        # 其他参数
    )
```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证。详见 LICENSE 文件。

## 免责声明

本项目仅供学习和研究使用，不构成任何投资建议。股市有风险，投资需谨慎。使用本系统进行投资决策所产生的任何损失，开发者不承担任何责任。

## 联系方式

如有问题或建议，欢迎通过以下方式联系：

- 提交 GitHub Issue
- 发送邮件至项目维护者

## 更新日志

### v1.0.0 (2025-01-15)
- 初始版本发布
- 支持 A股、港股、美股、ETF、LOF 分析
- 实现 7 种技术指标计算
- 智能评分系统
- Dify 工作流集成
- 完整的 API 文档

---

## 👤 作者信息

**Author:** RJ.Wang  
**Email:** wangrenjun@gmail.com  
**GitHub:** [@rjwang1982](https://github.com/rjwang1982)  
**Project:** [StrockDify](https://github.com/rjwang1982/StrockDify)

### 联系方式

- 📧 Email: wangrenjun@gmail.com
- 🐙 GitHub: https://github.com/rjwang1982
- 💬 Issues: https://github.com/rjwang1982/StrockDify/issues
- 🌟 Star this project: https://github.com/rjwang1982/StrockDify

---

**感谢使用 StrockDify！祝投资顺利！** 📈
