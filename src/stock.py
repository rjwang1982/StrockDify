#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
股票技术分析 API 主服务

Author: RJ.Wang
Email: wangrenjun@gmail.com
GitHub: https://github.com/rjwang1982/StrockDify
License: MIT
"""

from fastapi import FastAPI, HTTPException, Depends, Header, Request
from pydantic import BaseModel
from datetime import datetime, timedelta
import pandas as pd
import json
import akshare as ak
from db_utils import get_db_session

app = FastAPI()

# AWS Secrets Manager 配置
SECRET_NAME = "your-aurora-secret-name"  # 替换为你的 Secret 名称
AWS_REGION = "us-east-1"  # 替换为你的区域

# 数据库依赖
def get_db():
    db = get_db_session(SECRET_NAME, AWS_REGION)
    try:
        yield db
    finally:
        db.close()

# 添加请求日志中间件
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # 只记录POST请求
    if request.method == "POST":
        print(f"\n{'🔵'*30}")
        print(f"📨 原始HTTP请求信息:")
        print(f"  Method: {request.method}")
        print(f"  URL: {request.url}")
        print(f"  Client: {request.client.host}:{request.client.port}")
        print(f"  Headers:")
        for key, value in request.headers.items():
            if key.lower() != 'authorization':  # 不完整打印token
                print(f"    {key}: {value}")
            else:
                print(f"    {key}: {value[:20]}...")
        
        # 读取请求体
        body = await request.body()
        print(f"  Body (raw bytes): {body}")
        print(f"  Body (decoded): {body.decode('utf-8') if body else 'Empty'}")
        
        try:
            if body:
                body_json = json.loads(body)
                print(f"  Body (parsed JSON):")
                for key, value in body_json.items():
                    print(f"    {key}: '{value}' (type: {type(value).__name__})")
        except:
            print(f"  Body parsing failed")
        
        print(f"{'🔵'*30}\n")
        
        # 重新构造request以便后续处理
        async def receive():
            return {"type": "http.request", "body": body}
        
        request._receive = receive
    
    response = await call_next(request)
    return response

@app.get("/")
async def root():
    """健康检查端点"""
    return {"status": "ok", "message": "股票分析API正在运行"}

@app.get("/health")
async def health():
    """健康检查"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/test-stock/{stock_code}")
async def test_stock_browser(stock_code: str, market_type: str = 'A', token: str = None):
    """
    浏览器测试接口 - 使用GET方法
    示例: http://127.0.0.1:8000/test-stock/600519?token=xue123
    """
    # 验证token
    if token not in ["xue123", "xue1234"]:
        raise HTTPException(status_code=403, detail="Invalid token. Use ?token=xue123")
    
    try:
        print(f"\n{'='*60}")
        print(f"浏览器测试: {stock_code} ({market_type})")
        print(f"{'='*60}")
        
        # 获取股票数据
        stock_data = get_stock_data(stock_code, market_type)
        print(f"✓ 获取 {len(stock_data)} 条数据")
        
        # 计算技术指标
        stock_data = calculate_indicators(stock_data)
        
        # 计算评分
        score = calculate_score(stock_data)
        
        # 获取最新数据
        latest = stock_data.iloc[-1]
        prev = stock_data.iloc[-2]
        
        # 生成报告
        report = {
            'stock_code': stock_code,
            'market_type': market_type,
            'analysis_date': datetime.now().strftime('%Y-%m-%d'),
            'score': int(score),
            'price': float(latest['close']),
            'price_change': float((latest['close'] - prev['close']) / prev['close'] * 100),
            'ma_trend': 'UP' if latest['MA5'] > latest['MA20'] else 'DOWN',
            'rsi': float(latest['RSI']) if not pd.isna(latest['RSI']) else None,
            'macd_signal': 'BUY' if latest['MACD'] > latest['Signal'] else 'SELL',
            'volume_status': 'HIGH' if latest['Volume_Ratio'] > 1.5 else 'NORMAL',
            'recommendation': get_recommendation(score),
            'technical_indicators': {
                'MA5': float(latest['MA5']),
                'MA20': float(latest['MA20']),
                'MA60': float(latest['MA60']),
                'RSI': float(latest['RSI']) if not pd.isna(latest['RSI']) else None,
                'MACD': float(latest['MACD']),
                'volatility': f"{latest['Volatility']:.2f}%",
                'volume_ratio': float(latest['Volume_Ratio'])
            }
        }
        
        print("✓ 分析完成\n")
        return report
        
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# 参数配置
params = {
    'ma_periods': {'short': 5, 'medium': 20, 'long': 60},
    'rsi_period': 14,
    'bollinger_period': 20,
    'bollinger_std': 2,
    'volume_ma_period': 20,
    'atr_period': 14
}


# 鉴权 Token 验证
def verify_auth_token(authorization: str = Header(None)):
    """
    验证Authorization Header中的Bearer Token
    """
    print(authorization)
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization Header")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid Authorization scheme")
    # 这里可以替换为实际的 Token 验证逻辑
    valid_tokens = ["xue123", "xue1234"]  # 示例有效 Token 列表
    if token not in valid_tokens:
        raise HTTPException(status_code=403, detail="Invalid or Expired Token")
    return token


class StockAnalysisRequest(BaseModel):
    stock_code: str
    market_type: str = 'A'
    start_date: str = None
    end_date: str = None


def calculate_score(df):
    """
    计算评分
    """
    try:
        score = 0
        latest = df.iloc[-1]

        # 趋势得分（30分）
        if latest['MA5'] > latest['MA20']:
            score += 15
        if latest['MA20'] > latest['MA60']:
            score += 15

        # RSI得分（20分）
        if 30 <= latest['RSI'] <= 70:
            score += 20
        elif latest['RSI'] < 30:  # 超卖
            score += 15

        # MACD得分（20分）
        if latest['MACD'] > latest['Signal']:
            score += 20

        # 成交量得分（30分）
        if latest['Volume_Ratio'] > 1.5:
            score += 30
        elif latest['Volume_Ratio'] > 1:
            score += 15

        return score

    except Exception as e:
        print(f"计算评分时出错: {str(e)}")
        raise


def calculate_indicators(df):
    """
    计算技术指标
    """
    try:
        # 计算移动平均线
        df['MA5'] = calculate_ema(df['close'], params['ma_periods']['short'])
        df['MA20'] = calculate_ema(df['close'], params['ma_periods']['medium'])
        df['MA60'] = calculate_ema(df['close'], params['ma_periods']['long'])

        # 计算RSI
        df['RSI'] = calculate_rsi(df['close'], params['rsi_period'])

        # 计算MACD
        df['MACD'], df['Signal'], df['MACD_hist'] = calculate_macd(df['close'])

        # 计算布林带
        df['BB_upper'], df['BB_middle'], df['BB_lower'] = calculate_bollinger_bands(
            df['close'],
            params['bollinger_period'],
            params['bollinger_std']
        )

        # 成交量分析
        df['Volume_MA'] = df['volume'].rolling(window=params['volume_ma_period']).mean()
        df['Volume_Ratio'] = df['volume'] / df['Volume_MA']

        # 计算ATR和波动率
        df['ATR'] = calculate_atr(df, params['atr_period'])
        df['Volatility'] = df['ATR'] / df['close'] * 100

        # 动量指标
        df['ROC'] = df['close'].pct_change(periods=10) * 100

        return df

    except Exception as e:
        print(f"计算技术指标时出错: {str(e)}")
        raise


def _truncate_json_for_logging(json_obj, max_length=500):
    """截断JSON对象用于日志记录，避免日志过大"""
    json_str = json.dumps(json_obj, ensure_ascii=False)
    if len(json_str) <= max_length:
        return json_str
    return json_str[:max_length] + f"... [截断，总长度: {len(json_str)}字符]"


def get_stock_data(stock_code, market_type='A', start_date=None, end_date=None):
    """获取股票或基金数据"""
    if start_date is None:
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
    if end_date is None:
        end_date = datetime.now().strftime('%Y%m%d')

    # 禁用代理
    import os
    os.environ['NO_PROXY'] = '*'
    os.environ['no_proxy'] = '*'
    if 'HTTP_PROXY' in os.environ:
        del os.environ['HTTP_PROXY']
    if 'HTTPS_PROXY' in os.environ:
        del os.environ['HTTPS_PROXY']
    if 'http_proxy' in os.environ:
        del os.environ['http_proxy']
    if 'https_proxy' in os.environ:
        del os.environ['https_proxy']

    try:
        # 验证股票代码格式
        if market_type == 'A':
            valid_prefixes = ['0', '3', '6', '688', '8']
            valid_format = False

            for prefix in valid_prefixes:
                if stock_code.startswith(prefix):
                    valid_format = True
                    break

            if not valid_format:
                error_msg = (
                    f"无效的A股股票代码格式: {stock_code}。\n"
                    "A股代码应以0、3、6、688或8开头"
                )
                raise ValueError(error_msg)

            df = ak.stock_zh_a_hist(
                symbol=stock_code,
                start_date=start_date,
                end_date=end_date,
                adjust="qfq"
            )
        elif market_type == 'HK':
            df = ak.stock_hk_daily(
                symbol=stock_code,
                adjust="qfq"
            )
        elif market_type == 'US':
            df = ak.stock_us_hist(
                symbol=stock_code,
                start_date=start_date,
                end_date=end_date,
                adjust="qfq"
            )
        elif market_type == 'ETF':
            df = ak.fund_etf_hist_em(
                symbol=stock_code,
                period="daily",
                start_date=start_date,
                end_date=end_date,
                adjust="qfq"
            )

        elif market_type == 'LOF':
            df = ak.fund_lof_hist_em(
                symbol=stock_code,
                period="daily",
                start_date=start_date,
                end_date=end_date,
                adjust="qfq"
            )
        else:
            raise ValueError(f"不支持的市场类型:{market_type}")

        # 重命名列名以匹配分析需求
        df = df.rename(columns={
            "日期": "date",
            "开盘": "open",
            "收盘": "close",
            "最高": "high",
            "最低": "low",
            "成交量": "volume"
        })

        # 确保日期格式正确
        df['date'] = pd.to_datetime(df['date'])

        # 数据类型转换
        numeric_columns = ['open', 'close', 'high', 'low', 'volume']
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
        # 删除空值
        df = df.dropna()

        return df.sort_values('date')

    except Exception as e:
        raise Exception(f"获取数据失败: {str(e)}")


def calculate_ema(series, period):
    """
    计算指数移动平均线
    """
    return series.ewm(span=period, adjust=False).mean()


def calculate_rsi(series, period):
    """
    计算RSI指标
    """
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def calculate_macd(series):
    """
    计算MACD指标
    """
    exp1 = series.ewm(span=12, adjust=False).mean()
    exp2 = series.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    hist = macd - signal
    return macd, signal, hist


def calculate_bollinger_bands(series, period, std_dev):
    """
    计算布林带
    """
    middle = series.rolling(window=period).mean()
    std = series.rolling(window=period).std()
    upper = middle + (std * std_dev)
    lower = middle - (std * std_dev)
    return upper, middle, lower


def calculate_atr(df, period):
    """
    计算ATR指标
    """
    high = df['high']
    low = df['low']
    close = df['close'].shift(1)

    tr1 = high - low
    tr2 = abs(high - close)
    tr3 = abs(low - close)

    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()


# def calculate_indicators(df):
#     """
#     计算技术指标
#     """
#     try:
#         # 计算移动平均线
#         df['MAS'] = calculate_ema(df['close'], params['ma_periods']['short'])
#         df['MA20'] = calculate_ema(df['close'], params['ma_periods']['medium'])
#         df['MA60'] = calculate_ema(df['close'], params['ma_periods']['long'])
#
#         # 计算RSI
#         df['RSI'] = calculate_rsi(df['close'], params['rsi_period'])
#
#         # 计算MACD
#         df['MACD'], df['Signal'], df['MACD_hist'] = calculate_macd(df['close'])
#
#         # 计算布林带
#         df['BB_upper'], df['BB_middle'], df['BB_lower'] = calculate_bollinger_bands(
#             df['close'],
#             params['bollinger_period'],
#             params['bollinger_std']
#         )

def get_recommendation(score):
    """
    根据得分给出建议
    """
    if score >= 80:
        return '强烈推荐买入'
    elif score >= 60:
        return '建议买入'
    elif score >= 40:
        return '观望'
    elif score >= 20:
        return '建议卖出'
    else:
        return '强烈建议卖出'


@app.post("/analyze-stock/")
async def analyze_stock(request: StockAnalysisRequest, auth_token: str = Depends(verify_auth_token)):
    try:
        print(f"\n{'='*60}")
        print(f"📥 收到POST请求 - /analyze-stock/")
        print(f"{'='*60}")
        print(f"🔍 请求详情:")
        print(f"  - stock_code: '{request.stock_code}' (类型: {type(request.stock_code).__name__}, 长度: {len(request.stock_code)})")
        print(f"  - market_type: '{request.market_type}'")
        print(f"  - start_date: {request.start_date}")
        print(f"  - end_date: {request.end_date}")
        print(f"  - 原始字节: {request.stock_code.encode('utf-8') if request.stock_code else 'None'}")
        print(f"{'='*60}")
        print(f"开始分析股票: {request.stock_code} ({request.market_type})")
        print(f"{'='*60}")
        
        # 获取股票数据
        print("步骤1: 获取股票数据...")
        stock_data = get_stock_data(
            request.stock_code,
            request.market_type,
            request.start_date,
            request.end_date
        )
        print(f"✓ 成功获取 {len(stock_data)} 条数据记录")

        # 计算技术指标
        print("步骤2: 计算技术指标...")
        stock_data = calculate_indicators(stock_data)
        print("✓ 技术指标计算完成")

        # 检查数据完整性
        if len(stock_data) < 2:
            raise ValueError("数据不足，至少需要2条记录")

        # 计算评分
        print("步骤3: 计算综合评分...")
        score = calculate_score(stock_data)
        print(f"✓ 综合评分: {score}")

        # 获取最新数据
        latest = stock_data.iloc[-1]
        prev = stock_data.iloc[-2]

        # 生成技术指标概要
        technical_summary = {
            'trend': 'upward' if latest['MA5'] > latest['MA20'] else 'downward',
            'volatility': f"{latest['Volatility']:.2f}%",
            'volume_trend': 'increasing' if latest['Volume_Ratio'] > 1 else 'decreasing',
            'rsi_level': float(latest['RSI']) if not pd.isna(latest['RSI']) else 0
        }

        # 获取近14日交易数据
        recent_data = stock_data.tail(14).to_dict('records')

        # 生成报告
        report = {
            'stock_code': request.stock_code,
            'market_type': request.market_type,
            'analysis_date': datetime.now().strftime('%Y-%m-%d'),
            'score': int(score),
            'price': float(latest['close']),
            'price_change': float((latest['close'] - prev['close']) / prev['close'] * 100),
            'ma_trend': 'UP' if latest['MA5'] > latest['MA20'] else 'DOWN',
            'rsi': float(latest['RSI']) if not pd.isna(latest['RSI']) else None,
            'macd_signal': 'BUY' if latest['MACD'] > latest['Signal'] else 'SELL',
            'volume_status': 'HIGH' if latest['Volume_Ratio'] > 1.5 else 'NORMAL',
            'recommendation': get_recommendation(score)
        }

        print("✓ 分析完成\n")
        
        # 返回结果
        return {
            "technical_summary": technical_summary,
            "recent_data": recent_data,
            "report": report
        }

    except ValueError as e:
        print(f"❌ 数据验证错误: {str(e)}")
        raise HTTPException(status_code=400, detail=f"数据验证错误: {str(e)}")
    except Exception as e:
        print(f"❌ 服务器错误: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

if __name__ == '__main__':
    import uvicorn

    # 使用 0.0.0.0 允许局域网访问
    uvicorn.run(app, host="0.0.0.0", port=8000)