# -*- coding: utf-8 -*-
"""
配置文件：存放所有静态数据、选项和 CSS 样式
"""
import base64
from pathlib import Path

ASSETS_DIR = Path(__file__).parent / "assets"


def gif_data_uri(filename: str) -> str:
    """读取 assets 里的 GIF，转成 base64 data URI，方便在 HTML 中直接引用"""
    data = (ASSETS_DIR / filename).read_bytes()
    return f"data:image/gif;base64,{base64.b64encode(data).decode()}"

# ================= 基础选项 =================
ACTIVITY_EMOJI = ["🎮", "🎾", "💪", "🛍️", "🎬", "🌳", "✈️", "☕", "📸", "🍽️"]
ACTIVITY_NAMES = ["打王者", "打网球", "健身", "逛街", "看电影", "逛公园", "旅游", "喝下午茶", "拍美照", "吃饭"]
ACTIVITY_OPTIONS = [f"{e} {n}" for e, n in zip(ACTIVITY_EMOJI, ACTIVITY_NAMES)]

TIME_BLOCKS = [
    {"tab": "🌙 周五晚上", "icon": "🌙", "name": "周五晚上", "hint": "忙碌的一周结束啦，开启甜蜜周末～"},
    {"tab": "☀️ 周六", "icon": "☀️", "name": "周六", "hint": "最自由的一整天，全都交给你来安排！"},
    {"tab": "🌇 周日", "icon": "🌇", "name": "周日", "hint": "周末的尾巴，也要甜甜蜜蜜地度过～"},
]

# ================= 微信推送（PushPlus）=================
# 获取方式：打开 https://www.pushplus.plus ，微信扫码登录后复制你的 token
# 填在这里即可本地生效；部署到 Streamlit Cloud 时建议留空，
# 改为在云端 Secrets 里配置 pushplus_token（更安全，不随代码上传）
PUSHPLUS_TOKEN = "7c11e4061044468583e3ba496f1476b4"

# ================= 吃饭专属选项 =================
FOOD_MENU = {
    "🏠 在家吃": ["🦀 大闸蟹", "🥩 牛排", "🍖 照烧肥牛", "🥗 共同下厨","🐔 "],
    "🏪 去外面": ["🍲 火锅", "🥘 炒菜", "🍢 烧烤", "🍣 日料", "🍕 西餐"]
}

# ================= CSS 样式 =================
CUSTOM_CSS = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(160deg, #fff5f7 0%, #ffe4ec 45%, #fff0f5 100%);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe4ec 0%, #fff0f5 100%);
}
html, body, [class*="css"] {
    font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
    color: #5a3a4a;
}
.title-heart {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(120deg, #ff4d8d, #ff8fab, #ff4d8d);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    animation: heartbeat 2s ease-in-out infinite;
}
.title-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.2rem;
}
.dog-img {
    width: 95px;
    height: 95px;
    flex-shrink: 0;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(255, 143, 171, 0.35);
    background: #ffffff;
}
.dog-center {
    display: block;
    margin: 0 auto;
}
@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    25%      { transform: scale(1.03); }
    50%      { transform: scale(1); }
    75%      { transform: scale(1.03); }
}
.subtitle {
    text-align: center;
    color: #b36b84;
    font-size: 1rem;
    margin-bottom: 2rem;
}
div[data-testid="stPills"] button {
    border-radius: 20px !important;
    border: 2px solid #ffb3c6 !important;
}
div[data-testid="stPills"] button[aria-selected="true"] {
    background: linear-gradient(135deg, #ff6b9d, #ff8fab) !important;
    color: #ffffff !important;
}
div.stButton > button {
    background: linear-gradient(135deg, #ff4d8d, #ff8fab);
    color: #ffffff;
    font-size: 1.15rem;
    font-weight: 700;
    border-radius: 999px;
    padding: 0.7rem;
    border: none;
    width: 100%;
    box-shadow: 0 4px 15px rgba(255, 77, 141, 0.4);
}
div.stButton > button:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #ff3d80, #ff7ba1);
}
.summary-card {
    background: #ffffff;
    border: 2px solid #ffb3c6;
    border-radius: 20px;
    padding: 1.5rem;
    margin-top: 1.5rem;
    box-shadow: 0 8px 25px rgba(255, 143, 171, 0.25);
}
</style>
"""
