# 贡献指南

感谢你考虑为 StrockDify 做出贡献！🎉

## 📋 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发流程](#开发流程)
- [代码规范](#代码规范)
- [提交规范](#提交规范)
- [问题反馈](#问题反馈)

---

## 行为准则

### 我们的承诺

为了营造一个开放和友好的环境，我们承诺：

- 使用友好和包容的语言
- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

### 不可接受的行为

- 使用性化的语言或图像
- 人身攻击或侮辱性评论
- 公开或私下骚扰
- 未经许可发布他人的私人信息
- 其他不道德或不专业的行为

---

## 如何贡献

### 报告 Bug

如果你发现了 Bug，请：

1. 检查 [Issues](https://github.com/rjwang1982/StrockDify/issues) 是否已有相同问题
2. 如果没有，创建新 Issue，包含：
   - 清晰的标题
   - 详细的问题描述
   - 复现步骤
   - 预期行为 vs 实际行为
   - 环境信息（Python 版本、操作系统等）
   - 错误日志或截图

**Bug 报告模板：**
```markdown
## Bug 描述
简要描述问题

## 复现步骤
1. 执行 '...'
2. 输入 '...'
3. 看到错误 '...'

## 预期行为
应该发生什么

## 实际行为
实际发生了什么

## 环境信息
- Python 版本：3.9
- 操作系统：macOS 13.0
- StrockDify 版本：1.0.0

## 错误日志
```
粘贴错误日志
```

## 截图
如果适用，添加截图
```

### 建议新功能

如果你有新功能建议，请：

1. 检查 [Issues](https://github.com/rjwang1982/StrockDify/issues) 是否已有类似建议
2. 创建新 Issue，标记为 `enhancement`，包含：
   - 功能描述
   - 使用场景
   - 预期效果
   - 可能的实现方案

**功能建议模板：**
```markdown
## 功能描述
简要描述新功能

## 使用场景
为什么需要这个功能？

## 预期效果
功能应该如何工作？

## 可能的实现方案
如果有想法，描述如何实现

## 替代方案
是否有其他解决方案？
```

### 提交代码

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 开发流程

### 1. 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/rjwang1982/StrockDify.git
cd StrockDify

# 创建虚拟环境
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# 或 myenv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖（如果有）
pip install pytest black flake8 mypy
```

### 2. 创建分支

```bash
# 从 main 分支创建新分支
git checkout -b feature/your-feature-name

# 或修复 Bug
git checkout -b fix/bug-description
```

### 3. 开发和测试

```bash
# 运行服务器
python src/strock.py

# 运行测试
python src/test_client.py

# 代码格式化
black src/

# 代码检查
flake8 src/
```

### 4. 提交更改

```bash
# 添加文件
git add .

# 提交（遵循提交规范）
git commit -m "feat: add new feature"

# 推送到远程
git push origin feature/your-feature-name
```

### 5. 创建 Pull Request

1. 访问 GitHub 仓库
2. 点击 "Pull Request"
3. 选择你的分支
4. 填写 PR 描述
5. 等待审核

---

## 代码规范

### Python 代码风格

遵循 [PEP 8](https://pep8.org/) 规范：

```python
# 好的示例
def calculate_rsi(series, period=14):
    """
    计算 RSI 指标
    
    Args:
        series: 价格序列
        period: 计算周期
        
    Returns:
        RSI 值
    """
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
```

### 命名规范

- **变量和函数**：小写 + 下划线 (`stock_code`, `calculate_score`)
- **类名**：大驼峰 (`StockAnalyzer`, `TechnicalIndicator`)
- **常量**：大写 + 下划线 (`MAX_RETRIES`, `API_TIMEOUT`)
- **私有变量**：前缀下划线 (`_internal_cache`)

### 文档字符串

使用 Google 风格的文档字符串：

```python
def get_stock_data(stock_code, market_type='A', start_date=None):
    """
    获取股票数据
    
    Args:
        stock_code (str): 股票代码
        market_type (str): 市场类型，默认 'A'
        start_date (str): 开始日期，格式 YYYYMMDD
        
    Returns:
        pd.DataFrame: 股票数据
        
    Raises:
        ValueError: 股票代码格式错误
        Exception: 数据获取失败
        
    Example:
        >>> df = get_stock_data('600519', 'A')
        >>> print(df.head())
    """
    pass
```

### 代码注释

```python
# 好的注释：解释为什么
# 使用前复权数据，避免除权除息影响技术指标计算
df = ak.stock_zh_a_hist(symbol=stock_code, adjust="qfq")

# 不好的注释：重复代码
# 获取股票数据
df = ak.stock_zh_a_hist(symbol=stock_code, adjust="qfq")
```

---

## 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

### 提交类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构（不是新功能也不是修复）
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 提交格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 示例

```bash
# 简单提交
git commit -m "feat: add RSI indicator calculation"

# 详细提交
git commit -m "feat(indicators): add RSI indicator calculation

- Implement RSI calculation function
- Add unit tests for RSI
- Update documentation

Closes #123"

# 修复 Bug
git commit -m "fix: correct MACD signal calculation

The previous implementation had an off-by-one error in the
signal line calculation.

Fixes #456"

# 破坏性变更
git commit -m "feat!: change API response format

BREAKING CHANGE: The API now returns data in a different format.
Update your client code accordingly."
```

---

## 问题反馈

### 提问前

1. 阅读 [README.md](README.md)
2. 查看 [文档](docs/)
3. 搜索 [已有 Issues](https://github.com/rjwang1982/StrockDify/issues)

### 提问时

使用清晰的标题和详细的描述：

```markdown
## 问题
我在尝试分析港股时遇到错误

## 环境
- Python 3.9
- macOS 13.0
- StrockDify 1.0.0

## 复现步骤
1. 运行 `python src/strock.py`
2. 调用 API: `POST /analyze-stock/`
3. 请求体: `{"stock_code": "00700", "market_type": "HK"}`

## 错误信息
```
ValueError: Invalid stock code format
```

## 预期行为
应该返回腾讯控股的分析数据
```

---

## Pull Request 检查清单

提交 PR 前，请确保：

- [ ] 代码遵循项目的代码规范
- [ ] 添加了必要的测试
- [ ] 所有测试通过
- [ ] 更新了相关文档
- [ ] 提交信息遵循提交规范
- [ ] PR 描述清晰，说明了更改内容
- [ ] 关联了相关的 Issue（如果有）

---

## 审核流程

1. **自动检查**：CI/CD 自动运行测试
2. **代码审核**：维护者审核代码
3. **讨论**：如有需要，进行讨论和修改
4. **合并**：审核通过后合并到 main 分支

---

## 获取帮助

如果你有任何问题：

- 📧 发送邮件到项目维护者
- 💬 在 [Discussions](https://github.com/rjwang1982/StrockDify/discussions) 中提问
- 🐛 在 [Issues](https://github.com/rjwang1982/StrockDify/issues) 中报告问题

---

## 许可证

通过贡献代码，你同意你的贡献将在 [MIT License](LICENSE) 下发布。

---

**感谢你的贡献！** 🙏
