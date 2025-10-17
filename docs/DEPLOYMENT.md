# 股票分析 API 部署指南

**Author:** RJ.Wang  
**Email:** wangrenjun@gmail.com  
**GitHub:** https://github.com/rjwang1982/StrockDify

---

## 📦 环境要求

- Python 3.8+
- pip 或 conda

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python strock.py
```

服务将在 `http://0.0.0.0:8000` 启动

---

## 📚 依赖说明

| 库 | 版本 | 用途 |
|---|---|---|
| **fastapi** | 0.104.1 | Web 框架，提供 RESTful API |
| **uvicorn** | 0.24.0 | ASGI 服务器，运行 FastAPI 应用 |
| **pydantic** | 2.5.0 | 数据验证和序列化 |
| **pandas** | 2.1.3 | 数据处理和分析 |
| **numpy** | 1.26.2 | 数值计算（pandas 依赖） |
| **akshare** | 1.12.60 | 股票数据获取（核心库） |
| **requests** | 2.31.0 | HTTP 请求（akshare 依赖） |
| **python-multipart** | 0.0.6 | 处理表单数据 |

---

## 🔧 配置说明

### 修改端口

编辑 `strock.py` 最后一行：

```python
uvicorn.run(app, host="0.0.0.0", port=8000)  # 修改 port 参数
```

### 修改认证 Token

编辑 `strock.py` 第 102 行：

```python
valid_tokens = ["xue123", "xue1234", "your_token"]  # 添加你的 token
```

---

## 🧪 测试 API

### 健康检查

```bash
curl http://localhost:8000/health
```

### 浏览器测试（GET）

```
http://localhost:8000/test-stock/002352?token=xue123
```

### API 调用（POST）

```bash
curl -X POST http://localhost:8000/analyze-stock/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer xue123" \
  -d '{
    "stock_code": "002352",
    "market_type": "A"
  }'
```

---

## 🐳 Docker 部署（可选）

### 创建 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY strock.py .

EXPOSE 8000

CMD ["python", "strock.py"]
```

### 构建和运行

```bash
docker build -t stock-api .
docker run -p 8000:8000 stock-api
```

---

## 🌐 局域网访问

服务默认监听 `0.0.0.0`，可通过局域网 IP 访问：

```
http://192.168.x.x:8000
```

查看本机 IP：
- macOS/Linux: `ifconfig | grep inet`
- Windows: `ipconfig`

---

## ⚠️ 常见问题

### 1. akshare 安装失败

```bash
# 使用国内镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple akshare
```

### 2. 端口被占用

```bash
# 查看占用端口的进程
lsof -i :8000

# 杀死进程
kill -9 <PID>
```

### 3. 数据获取失败

- 检查网络连接
- 确认股票代码格式正确
- 查看 akshare 是否需要更新：`pip install --upgrade akshare`

---

## 📝 版本更新

### 更新所有依赖

```bash
pip install --upgrade -r requirements.txt
```

### 更新 akshare

```bash
pip install --upgrade akshare
```

---

## 🔒 生产环境建议

1. **使用环境变量管理 Token**
   ```python
   import os
   valid_tokens = os.getenv("API_TOKENS", "").split(",")
   ```

2. **启用 HTTPS**
   ```bash
   uvicorn strock:app --host 0.0.0.0 --port 8000 --ssl-keyfile key.pem --ssl-certfile cert.pem
   ```

3. **使用进程管理器**
   ```bash
   # 使用 supervisor 或 systemd
   pip install supervisor
   ```

4. **添加日志记录**
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   ```

---

## 📞 技术支持

如遇问题，请检查：
1. Python 版本是否 >= 3.8
2. 依赖是否完整安装
3. 网络连接是否正常
4. 股票代码格式是否正确
