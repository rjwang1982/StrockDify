# 常见问题 (FAQ)

## 📋 目录

- [安装和配置](#安装和配置)
- [API 使用](#api-使用)
- [Dify 工作流](#dify-工作流)
- [技术指标](#技术指标)
- [错误处理](#错误处理)
- [性能优化](#性能优化)

---

## 安装和配置

### Q: 支持哪些 Python 版本？

**A:** 支持 Python 3.8 及以上版本。推荐使用 Python 3.9 或 3.10。

```bash
# 检查 Python 版本
python --version
```

### Q: 如何安装依赖？

**A:** 使用 `requirements.txt` 安装：

```bash
pip install -r requirements.txt
```

如果安装失败，尝试使用国内镜像：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### Q: 虚拟环境是必须的吗？

**A:** 强烈推荐使用虚拟环境，避免依赖冲突：

```bash
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
```

### Q: 如何修改服务器端口？

**A:** 编辑 `src/strock.py` 最后一行：

```python
uvicorn.run(app, host="0.0.0.0", port=8000)  # 修改 port 参数
```

或使用命令行参数：

```bash
uvicorn src.strock:app --host 0.0.0.0 --port 9000
```

### Q: 如何配置 API Token？

**A:** 编辑 `src/strock.py` 中的 `valid_tokens` 列表：

```python
valid_tokens = ["xue123", "xue1234", "your_custom_token"]
```

生产环境建议使用环境变量：

```python
import os
valid_tokens = os.getenv("API_TOKENS", "").split(",")
```

---

## API 使用

### Q: 如何测试 API 是否正常运行？

**A:** 访问健康检查端点：

```bash
curl http://localhost:8000/health
```

或在浏览器中打开：`http://localhost:8000/`

### Q: 支持哪些市场类型？

**A:** 支持以下市场：

| 市场类型 | 代码 | 示例 |
|---------|------|------|
| A股 | `A` | 600519（贵州茅台） |
| 港股 | `HK` | 00700（腾讯控股） |
| 美股 | `US` | AAPL（苹果） |
| ETF | `ETF` | 510300（沪深300ETF） |
| LOF | `LOF` | 161725 |

### Q: A股股票代码格式是什么？

**A:** A股代码必须以以下数字开头：

- `0`：深圳主板（如 000001）
- `3`：创业板（如 300750）
- `6`：上海主板（如 600519）
- `688`：科创板（如 688981）
- `8`：北交所（如 830799）

### Q: 如何获取历史数据？

**A:** 使用 `start_date` 和 `end_date` 参数：

```bash
curl -X POST "http://localhost:8000/analyze-stock/" \
  -H "Authorization: Bearer xue123" \
  -H "Content-Type: application/json" \
  -d '{
    "stock_code": "600519",
    "market_type": "A",
    "start_date": "20230101",
    "end_date": "20231231"
  }'
```

### Q: API 响应时间多长？

**A:** 
- 首次请求：10-30 秒（需要下载历史数据）
- 后续请求：2-5 秒
- 可以通过缩短日期范围加快响应

### Q: 如何批量分析多只股票？

**A:** 使用 Python 脚本循环调用：

```python
import requests

stocks = ["600519", "000001", "002352"]
for stock in stocks:
    response = requests.post(
        "http://localhost:8000/analyze-stock/",
        headers={"Authorization": "Bearer xue123"},
        json={"stock_code": stock, "market_type": "A"}
    )
    print(f"{stock}: {response.json()['report']['recommendation']}")
```

---

## Dify 工作流

### Q: 如何导入 Dify 工作流？

**A:** 
1. 登录 Dify 平台
2. 进入"工作流"管理
3. 点击"导入工作流"
4. 选择 `workflows/` 目录下的 `.yml` 文件
5. 配置环境变量 `apikey`
6. 修改 HTTP 请求节点的 URL

### Q: 三个工作流有什么区别？

**A:** 

| 工作流 | 特点 | 适用场景 |
|--------|------|----------|
| 对话式 | 多轮对话 | 需要追问细节 |
| 标准版 | 单次执行 | 批量分析 |
| 小白版 | 双层解读 | 投资新手 |

### Q: 小白版工作流使用哪些 AI 模型？

**A:** 
- **专业分析**：DeepSeek Chat
- **小白解读**：Moonshot Kimi K2 Turbo

需要在 Dify 中安装对应的模型插件。

### Q: 如何修改工作流的 API 地址？

**A:** 在 Dify 工作流编辑器中：
1. 找到"HTTP 请求"节点
2. 修改 URL 为你的服务器地址
3. 保存并测试

### Q: 工作流执行失败怎么办？

**A:** 检查：
1. API 服务是否运行
2. 环境变量 `apikey` 是否配置
3. HTTP 请求 URL 是否正确
4. 网络连接是否正常
5. 查看 Dify 日志获取详细错误信息

---

## 技术指标

### Q: 支持哪些技术指标？

**A:** 当前支持：

- **移动平均线**：MA5、MA20、MA60
- **动量指标**：RSI、MACD、ROC
- **波动率指标**：布林带、ATR
- **成交量指标**：成交量比率

### Q: 技术指标是如何计算的？

**A:** 
- **MA**：使用指数移动平均（EMA）
- **RSI**：14 日相对强弱指标
- **MACD**：12/26/9 参数
- **布林带**：20 日均线 ± 2 倍标准差

详见 `src/strock.py` 中的计算函数。

### Q: 评分系统是如何工作的？

**A:** 综合评分（0-100分）由以下部分组成：

| 指标 | 权重 | 说明 |
|------|------|------|
| 趋势 | 30分 | MA5 > MA20 > MA60 |
| RSI | 20分 | 30-70 区间最佳 |
| MACD | 20分 | MACD > Signal |
| 成交量 | 30分 | 量比 > 1.5 |

### Q: 如何自定义技术指标参数？

**A:** 编辑 `src/strock.py` 中的 `params` 字典：

```python
params = {
    'ma_periods': {'short': 5, 'medium': 20, 'long': 60},
    'rsi_period': 14,
    'bollinger_period': 20,
    'bollinger_std': 2,
    'volume_ma_period': 20,
    'atr_period': 14
}
```

### Q: 投资建议是如何生成的？

**A:** 根据综合评分：

- 80-100分：强烈推荐买入
- 60-79分：建议买入
- 40-59分：观望
- 20-39分：建议卖出
- 0-19分：强烈建议卖出

---

## 错误处理

### Q: 出现 "Invalid stock code format" 错误

**A:** 检查：
1. 股票代码格式是否正确
2. 市场类型是否匹配
3. A股代码是否以 0/3/6/688/8 开头

### Q: 出现 "Permission denied" 或 "Invalid Token" 错误

**A:** 
- GET 请求：使用 `?token=xue123` 参数
- POST 请求：使用 `Authorization: Bearer xue123` 头

### Q: 出现 502 或连接超时错误

**A:** 
1. 检查服务器是否运行
2. 禁用代理设置：
```python
import os
os.environ['NO_PROXY'] = '127.0.0.1,localhost'
```
3. 检查防火墙设置

### Q: 出现 "数据获取失败" 错误

**A:** 
1. 检查网络连接
2. 确认股票代码有效
3. 尝试更新 AkShare：`pip install --upgrade akshare`
4. 检查是否在交易时间（数据源可能限流）

### Q: 首次请求很慢怎么办？

**A:** 
- 首次请求需要下载历史数据（10-30秒）
- 后续请求会快很多
- 可以缩短日期范围加快速度

### Q: 如何查看详细的错误日志？

**A:** 
- 服务器日志会打印到控制台
- 或保存到文件：
```bash
python src/strock.py > server.log 2>&1
tail -f server.log
```

---

## 性能优化

### Q: 如何提高 API 响应速度？

**A:** 
1. 缩短日期范围（默认 365 天）
2. 使用缓存机制
3. 部署到性能更好的服务器
4. 使用 CDN 加速数据获取

### Q: 可以并发处理多个请求吗？

**A:** 可以，FastAPI 支持异步处理。但注意：
- AkShare 有请求频率限制
- 建议间隔至少 1 秒
- 避免同时请求过多

### Q: 如何减少内存占用？

**A:** 
1. 限制历史数据天数
2. 及时清理不用的数据
3. 使用生成器而不是列表
4. 定期重启服务

### Q: 支持分布式部署吗？

**A:** 
- 当前版本不支持
- 可以部署多个实例，使用负载均衡
- 未来版本可能添加 Redis 缓存支持

---

## 其他问题

### Q: 数据来源是什么？

**A:** 使用 AkShare 库，数据来自：
- A股：东方财富、新浪财经
- 港股：雅虎财经
- 美股：雅虎财经
- ETF/LOF：天天基金网、东方财富

### Q: 数据有延迟吗？

**A:** 
- 实时数据可能有 15 分钟延迟
- 具体取决于数据源
- 非交易时间获取最近一个交易日数据

### Q: 可以用于实盘交易吗？

**A:** 
- ⚠️ 本系统仅供学习和研究
- 不构成投资建议
- 投资有风险，决策需谨慎
- 建议结合其他分析工具

### Q: 如何贡献代码？

**A:** 查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解详情。

### Q: 如何报告 Bug？

**A:** 在 [GitHub Issues](https://github.com/rjwang1982/StrockDify/issues) 中提交，包含：
- 问题描述
- 复现步骤
- 环境信息
- 错误日志

### Q: 有商业支持吗？

**A:** 
- 当前为开源项目，无商业支持
- 可以通过 GitHub Issues 获取社区帮助
- 欢迎贡献代码和文档

---

## 📚 更多资源

- [README.md](../README.md) - 完整使用指南
- [DEPLOYMENT.md](DEPLOYMENT.md) - 部署指南
- [BEGINNER_WORKFLOW.md](BEGINNER_WORKFLOW.md) - 小白版工作流
- [CHANGELOG.md](../CHANGELOG.md) - 更新日志
- [CONTRIBUTING.md](../CONTRIBUTING.md) - 贡献指南

---

**还有其他问题？** 

在 [GitHub Discussions](https://github.com/rjwang1982/StrockDify/discussions) 中提问！
