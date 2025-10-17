#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
股票分析 API 测试客户端

Author: RJ.Wang
Email: wangrenjun@gmail.com
GitHub: https://github.com/rjwang1982/StrockDify
License: MIT
"""

import requests
import json
import os

# 禁用代理 - 解决502错误
os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

# API配置
BASE_URL = "http://127.0.0.1:8000"
TOKEN = "xue123"  # 使用服务端定义的有效token

# 创建不使用代理的session
session = requests.Session()
session.trust_env = False  # 不使用环境变量中的代理设置

def test_stock_analysis(stock_code, market_type='A'):
    """测试股票分析接口"""
    url = f"{BASE_URL}/analyze-stock/"
    
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "stock_code": stock_code,
        "market_type": market_type
    }
    
    try:
        print(f"正在分析股票: {stock_code}")
        print(f"请求URL: {url}")
        print(f"请求头: {headers}")
        print(f"请求体: {json.dumps(payload, ensure_ascii=False)}\n")
        
        response = session.post(
            url, 
            json=payload, 
            headers=headers,
            timeout=30  # 设置30秒超时
        )
        
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("\n✅ 分析成功!")
            print(f"\n股票代码: {result['report']['stock_code']}")
            print(f"当前价格: {result['report']['price']:.2f}")
            print(f"涨跌幅: {result['report']['price_change']:.2f}%")
            print(f"综合评分: {result['report']['score']}")
            print(f"投资建议: {result['report']['recommendation']}")
            print(f"\n技术指标:")
            print(f"  趋势: {result['technical_summary']['trend']}")
            print(f"  波动率: {result['technical_summary']['volatility']}")
            print(f"  成交量: {result['technical_summary']['volume_trend']}")
            print(f"  RSI: {result['technical_summary']['rsi_level']:.2f}")
            return result
        else:
            print(f"\n❌ 请求失败: {response.status_code}")
            print(f"错误信息: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError as e:
        print(f"\n❌ 连接错误: 无法连接到服务器")
        print(f"请确保服务器已启动: python strock.py")
        print(f"详细错误: {str(e)}")
        return None
    except requests.exceptions.Timeout:
        print(f"\n❌ 请求超时: 服务器响应时间过长")
        return None
    except Exception as e:
        print(f"\n❌ 未知错误: {str(e)}")
        return None


if __name__ == "__main__":
    # 测试A股股票
    print("=" * 60)
    print("测试1: 分析A股股票 (贵州茅台 600519)")
    print("=" * 60)
    test_stock_analysis("600519", "A")
    
    print("\n" + "=" * 60)
    print("测试2: 分析A股股票 (平安银行 000001)")
    print("=" * 60)
    test_stock_analysis("000001", "A")
