# 设计文档

## 概述

本设计在现有股票分析工作流基础上，添加一个"小白友好输出"功能。通过在工作流末端插入新的 LLM 节点，将专业分析报告转换为通俗易懂的版本，同时保持原有功能完整性。

## 架构

### 工作流拓扑变更

**原有流程:**
```
开始 → 验证输入 → 获取股票数据 → 解析响应数据 → AI投资分析 → 结束
```

**新流程:**
```
开始 → 验证输入 → 获取股票数据 → 解析响应数据 → AI投资分析 → 小白版转换 → 结束
```

### 节点关系

- **analyze_llm** (AI投资分析) 的输出连接到新节点 **simplify_llm** (小白版转换)
- **simplify_llm** 的输出连接到 **end** (结束)
- 原有的 **analyze_llm → end** 连接将被移除

## 组件和接口

### 新增节点: simplify_llm

**节点类型:** LLM

**输入:**
- `analyze_llm.text`: 专业版分析报告（字符串）
- `parse_response.stock_code`: 股票代码（字符串）
- `parse_response.price`: 当前价格（字符串）
- `parse_response.recommendation`: 系统建议（字符串）

**输出:**
- `text`: 小白版分析报告（字符串）

**配置参数:**
```yaml
model:
  provider: langgenius/tongyi/tongyi  # 默认使用通义千问，可配置为腾讯元宝
  name: qwen3-235b-a22b
  mode: chat
  completion_params:
    temperature: 0.8  # 较高温度以获得更生动的表达
    max_tokens: 1500
```

**Prompt 模板:**
```
系统角色: 你是一位善于用通俗语言解释复杂金融概念的投资顾问助手。

任务: 将以下专业股票分析报告转换为投资小白都能听懂的版本。

股票代码: {{#parse_response.stock_code#}}
当前价格: {{#parse_response.price#}}元
系统建议: {{#parse_response.recommendation#}}

专业分析报告:
{{#analyze_llm.text#}}

要求:
1. 用生活化比喻解释技术指标（如RSI用"热度计"、MACD用"趋势信号灯"）
2. 避免专业术语，必须使用时立即用括号给出通俗解释
3. 将投资建议转换为具体行动（"建议买入"、"建议观望"、"建议卖出"）
4. 用百分比说明风险和收益预期
5. 控制在500-800字，分段清晰
6. 使用emoji增加可读性（📈📉⚠️💰等）

输出格式:
【股票概况】
【当前走势】
【风险提示】
【操作建议】
【总结】
```

### 修改节点: end

**新增输出字段:**
- `simplified_analysis`: 小白版分析报告

**完整输出列表:**
```yaml
outputs:
  - variable: stock_code
    value_selector: [parse_response, stock_code]
  - variable: current_price
    value_selector: [parse_response, price]
  - variable: score
    value_selector: [parse_response, score]
  - variable: recommendation
    value_selector: [parse_response, recommendation]
  - variable: analysis_report
    value_selector: [analyze_llm, text]
  - variable: simplified_analysis  # 新增
    value_selector: [simplify_llm, text]
```

### 新增环境变量（可选）

```yaml
environment_variables:
  - id: simplifier_model_provider
    name: simplifier_model_provider
    value: langgenius/tongyi/tongyi
    value_type: string
    description: 小白版转换使用的模型提供商
  
  - id: simplifier_model_name
    name: simplifier_model_name
    value: qwen3-235b-a22b
    value_type: string
    description: 小白版转换使用的具体模型
```

## 数据模型

### 节点位置坐标

```yaml
simplify_llm:
  position:
    x: 1550
    y: 380
  width: 250
  height: 120

end:  # 调整位置
  position:
    x: 1850
    y: 300
  width: 250
  height: 180  # 增加高度以容纳新输出
```

### 边连接定义

**新增边:**
```yaml
- id: llm-source-simplify-target
  source: analyze_llm
  sourceHandle: source
  target: simplify_llm
  targetHandle: target
  type: custom
  data:
    isInLoop: false
    sourceType: llm
    targetType: llm

- id: simplify-source-end-target
  source: simplify_llm
  sourceHandle: source
  target: end
  targetHandle: target
  type: custom
  data:
    isInLoop: false
    sourceType: llm
    targetType: end
```

**移除边:**
```yaml
# 删除原有的直接连接
- id: llm-source-end-target
  source: analyze_llm
  target: end
```

## 错误处理

### 简化器节点失败

**场景:** simplify_llm 调用失败或超时

**处理策略:**
- 在 prompt 中不添加特殊错误处理
- 依赖 Dify 平台的默认重试机制（已配置 max_retries: 3）
- 如果最终失败，工作流将在该节点停止，用户仍可获得专业版分析结果

### 模型配置错误

**场景:** 配置的模型提供商不可用

**处理策略:**
- 在文档中说明默认使用通义千问
- 建议用户在切换模型前先测试可用性
- 提供回退到默认配置的说明

## 测试策略

### 功能测试

1. **基本流程测试**
   - 输入: 股票代码 "002352", 市场类型 "A"
   - 验证: 输出包含 `analysis_report` 和 `simplified_analysis` 两个字段
   - 验证: `simplified_analysis` 内容通俗易懂，无专业术语

2. **多市场测试**
   - 测试 A股、港股、美股、ETF 四种市场类型
   - 验证: 小白版输出适配不同市场特点

3. **边界情况测试**
   - 输入无效股票代码
   - 验证: 在验证节点被拦截，不会到达简化器节点

### 输出质量测试

1. **可读性测试**
   - 验证: 输出字数在 500-800 字范围
   - 验证: 包含生活化比喻
   - 验证: 使用 emoji 增强可读性

2. **准确性测试**
   - 对比专业版和小白版的核心建议（买入/卖出/观望）
   - 验证: 两个版本的投资建议一致

3. **术语转换测试**
   - 验证: RSI、MACD、支撑位、压力位等术语被正确解释
   - 验证: 技术指标数值被转换为易懂的描述

### 性能测试

1. **响应时间**
   - 测量新增节点对整体工作流耗时的影响
   - 目标: 增加耗时不超过 10 秒

2. **并发测试**
   - 模拟多个用户同时请求
   - 验证: 工作流稳定性不受影响

### 集成测试

1. **端到端测试**
   - 从开始节点到结束节点完整执行
   - 验证: 所有输出字段正确填充

2. **兼容性测试**
   - 验证: 新 DSL 文件可被 Dify 平台正确加载
   - 验证: 原有功能未受影响

## 实现注意事项

1. **DSL 版本兼容性**: 保持 `version: 0.4.0` 不变
2. **节点 ID 唯一性**: 新节点 ID 使用 `simplify_llm`，确保不与现有节点冲突
3. **依赖项**: 如使用腾讯元宝，需在 `dependencies` 中添加相应插件
4. **Prompt 优化**: 可根据实际效果迭代 prompt 模板
5. **环境变量**: 保持原有 `apikey` 环境变量不变
