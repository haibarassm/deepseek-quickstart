# 🌍 旅游规划助手 MCP 服务器

> 专业的旅游规划助手，擅长根据用户需求规划行程合理、性价比高的旅游方案

## 📋 功能特性

### 核心功能

- **目的地信息查询**：获取热门旅游城市的详细信息
  - 景点推荐
  - 特色美食
  - 气候信息
  - 最佳旅游季节

- **云南特色美食指南**
  - 🍄 野生菌系列（松茸、牛肝菌、鸡枞菌等）
  - 🐛 昆虫美食系列（竹虫、蜂蛹、蚂蚱等）
  - ⚠️ 安全提示

- **穿衣指南**
  - 按季节推荐穿衣方案
  - 必备物品清单
  - 针对性建议

- **行程规划**
  - 多种节奏选择（轻松/适中/紧凑）
  - 主题定制（美食/自然风光/文化）
  - 智能景点分配

- **旅游小贴士**
  - 行前准备清单
  - 注意事项
  - 省钱技巧

---

## 🚀 快速开始

### 安装

```bash
# 使用 uv 安装（推荐）
uv pip install -e .

# 或使用 pip
pip install -e .
```

### 运行

```bash
# 方式一：直接运行 Python 模块
python -m travel_planner

# 方式二：使用安装的脚本
travel-planner
```

---

## 🔧 MCP 工具列表

### 1. `get_destination_info`
获取指定旅游目的地的详细信息。

**参数**：
- `province`（必填）：省份名称，如"云南"、"四川"
- `city`（可选）：城市名称，如"大理"、"成都"

**示例**：
```
获取云南大理的旅游信息
```

---

### 2. `get_yunnan_food_recommendation`
获取云南特色美食推荐，包括野生菌和昆虫美食。

**参数**：
- `food_type`（可选）：美食类型
  - `"野生菌"` - 只返回野生菌信息
  - `"昆虫美食"` - 只返回昆虫美食信息
  - `"全部"` - 返回所有特色美食（默认）

**示例**：
```
推荐云南的野生菌美食
```

---

### 3. `get_clothing_guide`
获取指定城市的穿衣指南。

**参数**：
- `city`（必填）：城市名称，如"大理"、"西双版纳"
- `season`（可选）：季节（春季、夏季、秋季、冬季）

**示例**：
```
大理春季应该穿什么衣服？
```

---

### 4. `plan_itinerary`
根据用户需求生成旅游行程建议。

**参数**：
- `destination`（必填）：目的地城市名称
- `days`（必填）：旅游天数
- `pace`（可选）：行程节奏（轻松/适中/紧凑，默认"适中"）
- `interests`（可选）：兴趣偏好（如"自然风光"、"美食"等）

**示例**：
```
帮我规划一个大理5日游，节奏轻松，主要看自然风光
```

---

### 5. `get_travel_tips`
获取旅游目的地的小贴士和注意事项。

**参数**：
- `destination`（必填）：目的地城市名称

**示例**：
```
去大理旅游有什么需要注意的？
```

---

## 🗺️ 支持的目的地

### 云南
- **大理**：苍山洱海、古城古镇
- **西双版纳**：热带雨林、傣族风情
- **昆明**：春城花都、滇池石林
- **丽江**：古城雪山、纳西文化

### 其他地区
- 四川成都
- 浙江杭州
- （持续扩展中...）

---

## 📦 项目结构

```
travel-planner/
├── travel_planner.py      # MCP 服务器主代码
├── pyproject.toml          # 项目配置
├── mcp-config.json         # MCP 配置文件
├── README.md              # 项目说明
└── 春节云南7日游旅游计划.md # 示例旅游计划文档
```

---

## 🔌 MCP 配置

### Claude Desktop 配置

在 Claude Desktop 的 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "12306-mcp": {
      "type": "streamable_http",
      "url": "https://mcp.api-inference.modelscope.net/a7895f9ee59e43/mcp"
    },
    "XingYuWeather": {
      "type": "sse",
      "url": "https://mcp.api-inference.modelscope.net/362b18ed816b42/sse"
    },
    "travel-planner": {
      "command": "python",
      "args": [
        "-m",
        "travel_planner"
      ]
    }
  }
}
```

### 配置说明

| MCP 服务器 | 类型 | 功能 |
|-----------|------|------|
| **12306-mcp** | streamable_http | 高铁班次查询 |
| **XingYuWeather** | sse | 天气预报查询 |
| **travel-planner** | 本地 stdio | 旅游规划助手 |

---

## 📚 使用示例

### 示例 1：云南7日游规划

**用户输入**：
> 我想在春节的时候去云南旅游，出发地是杭州，考虑坐高铁出行，去7天，行程轻松舒适一些，主要以自然风光和美食为主，推荐虫子和菌菇等当地特色美食，想去苍山洱海和西双版纳。

**助手响应**：
1. 调用 `12306-mcp` 查询杭州到昆明高铁班次
2. 调用 `XingYuWeather` 查询春节期间天气
3. 调用 `get_destination_info` 获取大理和西双版纳信息
4. 调用 `get_yunnan_food_recommendation` 推荐特色美食
5. 调用 `get_clothing_guide` 提供穿衣建议
6. 生成完整的旅游计划文档

---

### 示例 2：美食主题游

**用户输入**：
> 帮我规划一个云南4日美食之旅，主要想吃野生菌和虫子。

**助手响应**：
```
调用 plan_itinerary(destination="云南", days=4, interests="美食")
```

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 添加新目的地

在 `travel_planner.py` 的 `POPULAR_DESTINATIONS` 字典中添加：

```python
"省份名": {
    "城市名": {
        "气候": "...",
        "最佳季节": ["..."],
        "主要景点": ["...", "..."],
        "特色美食": ["...", "..."],
        "平均温度": "...",
        "建议天数": "..."
    }
}
```

---

## 📄 许可证

Apache License 2.0

---

## 🙏 致谢

- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- 极客时间 AI 全栈课程

---

**祝您旅途愉快！🎉**
