#!/bin/bash

echo "停止旧服务器..."
pkill -f "python.*strock.py" 2>/dev/null || true
sleep 1

echo "启动服务器..."
./myenv/bin/python src/strock.py &
SERVER_PID=$!

echo "服务器PID: $SERVER_PID"
echo "等待启动..."
sleep 3

echo ""
echo "=========================================="
echo "服务器已启动！"
echo "=========================================="
echo ""
echo "本机访问URL："
echo ""
echo "1. 健康检查："
echo "   http://127.0.0.1:8000/"
echo "   http://127.0.0.1:8000/health"
echo ""
echo "2. 测试贵州茅台 (600519)："
echo "   http://127.0.0.1:8000/test-stock/600519?token=xue123"
echo ""
echo "3. 测试平安银行 (000001)："
echo "   http://127.0.0.1:8000/test-stock/000001?token=xue123"
echo ""
echo "=========================================="
echo "局域网访问URL："
echo "=========================================="
echo ""
echo "从其他机器访问，使用本机IP地址："
echo ""
echo "1. 健康检查："
echo "   http://192.168.132.2:8000/"
echo ""
echo "2. 测试贵州茅台："
echo "   http://192.168.132.2:8000/test-stock/600519?token=xue123"
echo ""
echo "3. 测试平安银行："
echo "   http://192.168.132.2:8000/test-stock/000001?token=xue123"
echo ""
echo "=========================================="
echo ""
echo "停止服务器: pkill -f 'python.*strock.py'"
