"""
旅游规划助手 MCP 服务器
Travel Planner MCP Server

这是一个专业的旅游规划助手MCP服务器，提供：
- 旅游行程规划建议
- 景点推荐
- 美食推荐
- 穿衣指南
- 住宿建议
- 交通方式建议
"""

from typing import Any, List, Dict
from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP 服务器
mcp = FastMCP("travel-planner")

# --- 数据常量 ---

# 热门旅游目的地数据
POPULAR_DESTINATIONS = {
    "云南": {
        "大理": {
            "气候": "亚热带高原季风气候",
            "最佳季节": ["3-5月", "10-11月"],
            "主要景点": ["苍山", "洱海", "大理古城", "喜洲古镇", "双廊古镇"],
            "特色美食": ["白族酸辣鱼", "喜洲粑粑", "烤乳扇", "野生菌火锅"],
            "平均温度": "12-25°C",
            "建议天数": "3-4天"
        },
        "西双版纳": {
            "气候": "热带季风气候",
            "最佳季节": ["11-4月"],
            "主要景点": ["野象谷", "热带植物园", "原始森林公园", "曼听公园", "星光夜市"],
            "特色美食": ["傣味烧烤", "菠萝饭", "香茅草烤鱼", "泼水粑粑"],
            "平均温度": "15-30°C",
            "建议天数": "3-4天"
        },
        "昆明": {
            "气候": "亚热带高原季风气候",
            "最佳季节": ["全年"],
            "主要景点": ["滇池", "石林", "翠湖公园", "云南民族村"],
            "特色美食": ["过桥米线", "汽锅鸡", "野生菌火锅", "鲜花饼"],
            "平均温度": "10-22°C",
            "建议天数": "2-3天"
        },
        "丽江": {
            "气候": "亚热带高原季风气候",
            "最佳季节": ["3-5月", "10-11月"],
            "主要景点": ["丽江古城", "玉龙雪山", "蓝月谷", "泸沽湖"],
            "特色美食": ["腊排骨火锅", "丽江粑粑", "鸡豆凉粉", "三文鱼"],
            "平均温度": "8-23°C",
            "建议天数": "3-4天"
        }
    },
    "四川": {
        "成都": {
            "气候": "亚热带湿润季风气候",
            "最佳季节": ["3-6月", "9-11月"],
            "主要景点": ["宽窄巷子", "锦里", "大熊猫基地", "都江堰", "青城山"],
            "特色美食": ["火锅", "串串香", "麻婆豆腐", "夫妻肺片"],
            "平均温度": "12-25°C",
            "建议天数": "3-4天"
        }
    },
    "浙江": {
        "杭州": {
            "气候": "亚热带季风气候",
            "最佳季节": ["3-5月", "10-11月"],
            "主要景点": ["西湖", "灵隐寺", "千岛湖", "西溪湿地"],
            "特色美食": ["西湖醋鱼", "东坡肉", "龙井虾仁", "叫化鸡"],
            "平均温度": "10-28°C",
            "建议天数": "2-3天"
        }
    }
}

# 云南特色美食数据（虫子和菌菇）
YUNNAN_SPECIAL_FOOD = {
    "野生菌": [
        {"名称": "松茸", "特点": "菌中之王，香气浓郁", "推荐做法": ["刺身", "烧烤", "火锅"]},
        {"名称": "牛肝菌", "特点": "口感醇厚", "推荐做法": ["爆炒", "火锅"]},
        {"名称": "鸡枞菌", "特点": "鲜美异常", "推荐做法": ["油鸡枞", "火锅"]},
        {"名称": "青头菌", "特点": "云南特产", "推荐做法": ["爆炒", "煮汤"]},
        {"名称": "竹荪", "特点": "雪裙仙子", "推荐做法": ["煲汤", "火锅"]},
        {"名称": "羊肚菌", "特点": "营养丰富", "推荐做法": ["煲汤", "爆炒"]}
    ],
    "昆虫美食": [
        {"名称": "竹虫", "口感": "炸后酥脆如薯片", "推荐度": "⭐⭐⭐⭐⭐"},
        {"名称": "蜂蛹", "口感": "油炸后香甜", "推荐度": "⭐⭐⭐⭐⭐"},
        {"名称": "蚂蚱", "口感": "椒盐烤制", "推荐度": "⭐⭐⭐⭐"},
        {"名称": "蚕蛹", "口感": "高蛋白", "推荐度": "⭐⭐⭐⭐"},
        {"名称": "水蜻蜓", "口感": "丽江特色", "推荐度": "⭐⭐⭐"}
    ],
    "注意事项": [
        "野生菌火锅必须煮足20分钟才能食用",
        "不认识的野生菌千万不要采食",
        "建议选择必吃榜上榜餐厅品尝",
        "虫子美食建议从油炸竹虫/蜂蛹开始尝试"
    ]
}

# 穿衣指南数据
CLOTHING_GUIDE = {
    "大理": {
        "春季": "长袖+外套，昼夜温差大需保暖",
        "夏季": "短袖+薄外套，防晒必备",
        "秋季": "长袖+厚外套，洋葱式穿衣",
        "冬季": "羽绒服/厚外套，注意保暖",
        "必备物品": ["防晒霜", "墨镜", "遮阳帽", "雨具"]
    },
    "西双版纳": {
        "春季": "短袖+薄外套，透气速干",
        "夏季": "短袖短裤，防蚊必备",
        "秋季": "短袖+薄外套，轻便舒适",
        "冬季": "长袖+薄外套，早晚保暖",
        "必备物品": ["防晒霜", "防蚊液", "透气衣物", "遮阳帽"]
    }
}


# --- MCP 工具函数 ---

@mcp.tool()
async def get_destination_info(province: str, city: str = None) -> str:
    """
    获取指定旅游目的地的详细信息，包括景点、美食、气候等。

    参数:
        province: 省份名称（如：云南、四川、浙江）
        city: 城市名称（可选，如：大理、成都、杭州）
    """
    if province not in POPULAR_DESTINATIONS:
        return f"抱歉，暂时没有{province}的详细旅游信息。目前支持的地区包括：{', '.join(POPULAR_DESTINATIONS.keys())}"

    province_data = POPULAR_DESTINATIONS[province]

    if city:
        if city not in province_data:
            available_cities = ', '.join(province_data.keys())
            return f"{province}暂无{city}的信息。可用城市：{available_cities}"

        city_info = province_data[city]
        return f"""
📍 {city} 旅游信息

🌤️ 气候：{city_info['气候']}
📅 最佳旅游季节：{', '.join(city_info['最佳季节'])}
🌡️ 平均温度：{city_info['平均温度']}
⏰ 建议游玩天数：{city_info['建议天数']}

🏞️ 主要景点：
{chr(10).join(f'  • {spot}' for spot in city_info['主要景点'])}

🍽️ 特色美食：
{chr(10).join(f'  • {food}' for food in city_info['特色美食'])}
"""

    # 返回省份所有城市概览
    result = f"📍 {province}旅游目的地概览\n\n"
    for city_name, city_info in province_data.items():
        result += f"**{city_name}**\n"
        result += f"  • 景点：{', '.join(city_info['主要景点'][:3])}等\n"
        result += f"  • 美食：{', '.join(city_info['特色美食'][:2])}等\n"
        result += f"  • 建议天数：{city_info['建议天数']}\n\n"

    return result


@mcp.tool()
async def get_yunnan_food_recommendation(food_type: str = "全部") -> str:
    """
    获取云南特色美食推荐，包括野生菌和昆虫美食。

    参数:
        food_type: 美食类型，可选值："野生菌"、"昆虫美食" 或 "全部"（默认）
    """
    result = "🍽️ 云南特色美食推荐\n\n"

    if food_type in ["全部", "野生菌"]:
        result += "🍄 野生菌系列\n"
        result += "─" * 40 + "\n"
        for mushroom in YUNNAN_SPECIAL_FOOD["野生菌"]:
            result += f"""
**{mushroom['名称']}**
  • 特点：{mushroom['特点']}
  • 推荐做法：{', '.join(mushroom['推荐做法'])}
"""
        result += "\n"

    if food_type in ["全部", "昆虫美食"]:
        result += "🐛 昆虫美食系列（云南十八怪之一）\n"
        result += "─" * 40 + "\n"
        for insect in YUNNAN_SPECIAL_FOOD["昆虫美食"]:
            result += f"""**{insect['名称']}**
  • 口感：{insect['口感']}
  • 推荐度：{insect['推荐度']}
"""
        result += "\n"

    result += "⚠️ 注意事项\n"
    result += "─" * 40 + "\n"
    for note in YUNNAN_SPECIAL_FOOD["注意事项"]:
        result += f"  • {note}\n"

    return result


@mcp.tool()
async def get_clothing_guide(city: str, season: str = None) -> str:
    """
    获取指定城市的穿衣指南。

    参数:
        city: 城市名称（如：大理、西双版纳）
        season: 季节（可选：春季、夏季、秋季、冬季）
    """
    if city not in CLOTHING_GUIDE:
        return f"抱歉，暂时没有{city}的穿衣指南。目前支持：{', '.join(CLOTHING_GUIDE.keys())}"

    city_guide = CLOTHING_GUIDE[city]
    result = f"👔 {city}穿衣指南\n\n"

    if season:
        if season not in city_guide:
            return f"无效的季节参数。支持的季节：{', '.join([k for k in city_guide.keys() if k != '必备物品'])}"
        result += f"📅 {season}穿衣建议：{city_guide[season]}\n\n"
    else:
        result += "📅 季节穿衣建议：\n"
        for s, advice in city_guide.items():
            if s != "必备物品":
                result += f"  • {s}：{advice}\n"
        result += "\n"

    result += "🎒 必备物品：\n"
    for item in city_guide["必备物品"]:
        result += f"  • {item}\n"

    return result


@mcp.tool()
async def plan_itinerary(
    destination: str,
    days: int,
    pace: str = "适中",
    interests: str = None
) -> str:
    """
    根据用户需求生成旅游行程建议。

    参数:
        destination: 目的地（城市名称）
        days: 旅游天数
        pace: 行程节奏（轻松/适中/紧凑）
        interests: 兴趣偏好（如：自然风光、美食、历史文化等）
    """
    # 查找目的地信息
    city_info = None
    for province, cities in POPULAR_DESTINATIONS.items():
        if destination in cities:
            city_info = cities[destination]
            break

    if not city_info:
        return f"抱歉，暂时没有{destination}的行程规划信息。"

    # 调整行程安排
    spots = city_info['主要景点']
    if interests:
        if "美食" in interests:
            return get_foodie_itinerary(destination, days, pace, city_info)
        elif "自然" in interests:
            return get_nature_itinerary(destination, days, pace, spots)

    return get_general_itinerary(destination, days, pace, spots, city_info)


def get_general_itinerary(destination: str, days: int, pace: str, spots: list, city_info: dict) -> str:
    """生成通用行程"""
    spots_per_day = max(1, len(spots) // days) if pace == "轻松" else max(2, len(spots) // days)
    if pace == "紧凑":
        spots_per_day += 1

    result = f"🗓️ {destination}{days}日游行程建议（{pace}节奏）\n\n"

    for day in range(1, days + 1):
        start_idx = (day - 1) * spots_per_day
        day_spots = spots[start_idx:start_idx + spots_per_day]

        result += f"**第{day}天**\n"
        if day_spots:
            result += f"  • 上午：{day_spots[0] if len(day_spots) > 0 else '自由活动'}\n"
            result += f"  • 下午：{day_spots[1] if len(day_spots) > 1 else '继续游览'}\n"
            result += f"  • 晚上：品尝{city_info['特色美食'][0] if day < days else '当地特色'}\n"
        else:
            result += f"  • 自由活动/购物/返程\n"
        result += "\n"

    result += f"\n💡 **温馨提示**：\n"
    result += f"  • {destination}平均温度：{city_info['平均温度']}\n"
    result += f"  • 建议游玩天数：{city_info['建议天数']}\n"
    result += f"  • 最佳季节：{', '.join(city_info['最佳季节'])}\n"

    return result


def get_foodie_itinerary(destination: str, days: int, pace: str, city_info: dict) -> str:
    """生成美食主题行程"""
    result = f"🍴 {destination}{days}日美食之旅（{pace}节奏）\n\n"

    foods = city_info['特色美食']
    spots = city_info['主要景点']

    for day in range(1, days + 1):
        result += f"**第{day}天**\n"
        food_idx = (day - 1) % len(foods)
        spot_idx = (day - 1) % len(spots)

        result += f"  • 上午：游览{spots[spot_idx]}\n"
        result += f"  • 午餐：品尝{foods[food_idx]}\n"
        result += f"  • 下午：继续游览或逛当地市场\n"
        result += f"  • 晚餐：探索{foods[(food_idx + 1) % len(foods)]}\n\n"

    return result


def get_nature_itinerary(destination: str, days: int, pace: str, spots: list) -> str:
    """生成自然风光主题行程"""
    result = f"🌿 {destination}{days}日自然风光之旅（{pace}节奏）\n\n"

    nature_spots = [s for s in spots if any(keyword in s for keyword in ["山", "湖", "公园", "森林", "谷"])]

    for day in range(1, days + 1):
        result += f"**第{day}天**\n"
        spot_idx = min(day - 1, len(nature_spots) - 1)
        result += f"  • 全天：深度游览{nature_spots[spot_idx]}\n"
        result += f"  • 建议：早起看日出/日落，带好相机\n\n"

    return result


@mcp.tool()
async def get_travel_tips(destination: str) -> str:
    """
    获取旅游目的地的小贴士和注意事项。

    参数:
        destination: 目的地城市名称
    """
    tips_map = {
        "大理": """
📌 大理旅游小贴士

🎒 行前准备：
  • 防晒霜（SPF50+）：高原紫外线强
  • 墨镜+遮阳帽：必备防晒用品
  • 便携雨具：天气多变
  • 舒适运动鞋：苍山洱海需要徒步

⚠️ 注意事项：
  • 高原反应：海拔约2000米，注意休息
  • 饮食卫生：选择正规餐厅
  • 野生菌：务必煮熟20分钟以上
  • 购物：翡翠玉石不懂行不要买

💡 省钱技巧：
  • 洱海环游建议拼车
  • 古城内吃饭比景点便宜
  • 住宿可选才村，性价比高
""",
        "西双版纳": """
📌 西双版纳旅游小贴士

🎒 行前准备：
  • 防蚊液：热带地区蚊虫多
  • 透气速干衣物：湿热气候
  • 防晒霜：热带紫外线强
  • 轻便运动鞋/凉鞋

⚠️ 注意事项：
  • 防蚊防虫：热带雨林蚊虫较多
  • 饮食卫生：选择干净餐厅
  • 尊重民族习俗：傣族等少数民族
  • 热带水果：适量食用

💡 省钱技巧：
  • 星光夜市可砍价
  • 江边菜市场水果便宜
  • 告庄西双景住宿便利
  • 景点套票比单买划算
""",
        "昆明": """
📌 昆明旅游小贴士

🎒 行前准备：
  • 春城：全年气候温和
  • 防晒用品：紫外线强
  • 薄外套：早晚温差大

⚠️ 注意事项：
  • 野生菌：务必煮熟
  • 海鸥：翠湖公园红嘴鸥可喂食

💡 省钱技巧：
  • 过桥米线：本地小店更地道
  • 云南鲜花饼：嘉华等品牌店
"""
    }

    return tips_map.get(destination, f"暂无{destination}的旅游小贴士。")


# --- 服务器启动 ---

if __name__ == "__main__":
    mcp.run(transport='stdio')
