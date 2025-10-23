#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数据库连接工具 - 使用 AWS Secrets Manager
"""

import json
import boto3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from botocore.exceptions import ClientError

def get_secret(secret_name: str, region_name: str = "us-east-1"):
    """从 AWS Secrets Manager 获取密钥"""
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response['SecretString'])
    except ClientError as e:
        raise Exception(f"获取密钥失败: {e}")

def get_db_engine(secret_name: str, region_name: str = "us-east-1"):
    """创建数据库引擎"""
    secret = get_secret(secret_name, region_name)
    
    # Secrets Manager 标准格式
    host = secret['host']
    port = secret.get('port', 3306)
    username = secret['username']
    password = secret['password']
    database = secret.get('dbname', 'your_database')
    
    connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    
    engine = create_engine(
        connection_string,
        pool_pre_ping=True,
        pool_recycle=3600
    )
    
    return engine

def get_db_session(secret_name: str, region_name: str = "us-east-1"):
    """获取数据库会话"""
    engine = get_db_engine(secret_name, region_name)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()
