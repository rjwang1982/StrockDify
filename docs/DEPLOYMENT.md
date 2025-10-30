# 部署指南

**Author:** RJ.Wang | **Email:** wangrenjun@gmail.com | **GitHub:** https://github.com/rjwang1982/StrockDify

---

## 环境要求

- Python 3.8+
- pip

---

## 快速部署

### 1. 克隆项目

```bash
git clone https://github.com/rjwang1982/StrockDify.git
cd StrockDify
```

### 2. 创建虚拟环境

```bash
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# myenv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动服务

```bash
# 使用启动脚本（推荐）
./scripts/start_server.sh

# 或手动启动
python src/stock.py
```

---

## 依赖说明

| 库 | 版本 | 用途 |
|---|---|---|
| fastapi | 0.115+ | Web 框架 |
| uvicorn | 0.32+ | ASGI 服务器 |
| pydantic | 2.10+ | 数据验证 |
| pandas | 2.2+ | 数据处理 |
| numpy | 1.26+ | 数值计算 |
| akshare | 1.14+ | 股票数据获取 |
| requests | 2.32+ | HTTP 请求 |
| python-multipart | 0.0.12+ | 表单处理 |

---

## 配置说明

### 修改端口

编辑 `src/stock.py` 最后一行：

```python
uvicorn.run(app, host="0.0.0.0", port=8000)  # 修改 port
```

### 修改 Token

编辑 `src/stock.py`：

```python
valid_tokens = ["xue123", "xue1234", "your_token"]
```

---

## 测试

### 健康检查

```bash
curl http://localhost:8000/health
```

### 浏览器测试

```
http://localhost:8000/test-stock/600519?token=xue123
```

### API 调用

```bash
curl -X POST http://localhost:8000/analyze-stock/ \
  -H "Authorization: Bearer xue123" \
  -H "Content-Type: application/json" \
  -d '{"stock_code": "600519", "market_type": "A"}'
```

---

## Docker 部署

### Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
EXPOSE 8000
CMD ["python", "src/stock.py"]
```

### 构建运行

```bash
docker build -t stock-api .
docker run -p 8000:8000 stock-api
```

---

## 局域网访问

服务默认绑定 `0.0.0.0:8000`，支持局域网访问。

**查看本机 IP：**
```bash
ifconfig | grep inet  # macOS/Linux
ipconfig              # Windows
```

**访问示例：**
```
http://192.168.x.x:8000/test-stock/600519?token=xue123
```

---

## 常见问题

### akshare 安装失败

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple akshare
```

### 端口被占用

```bash
lsof -i :8000
kill -9 <PID>
```

### 数据获取失败

- 检查网络连接
- 确认股票代码格式
- 更新 akshare：`pip install --upgrade akshare`

---

## 生产环境

### 使用环境变量

```python
import os
valid_tokens = os.getenv("API_TOKENS", "").split(",")
```

### 启用 HTTPS

```bash
uvicorn src.stock:app --ssl-keyfile key.pem --ssl-certfile cert.pem
```

### 进程管理

```bash
pip install supervisor
```

### 日志记录

```python
import logging
logging.basicConfig(level=logging.INFO)
```

---

## 更新

```bash
# 更新所有依赖
pip install --upgrade -r requirements.txt

# 更新 akshare
pip install --upgrade akshare
```
