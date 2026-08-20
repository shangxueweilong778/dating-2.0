# -*- coding: utf-8 -*-
"""
主程序入口：页面搭建与交互逻辑
"""

import streamlit as st
from datetime import date
# 从我们写好的模块里导入配置和逻辑
import config
import logic

# ==========================================
# 0. 页面基础配置与样式
# ==========================================
st.set_page_config(page_title="💖 专属我们的周末甜蜜计划 💖", page_icon="💖", layout="centered")
st.markdown(config.CUSTOM_CSS, unsafe_allow_html=True)

# ==========================================
# 1. 侧边栏：获取参数
# ==========================================
with st.sidebar:
    st.markdown(
        f'<div style="text-align:center;">'
        f'<img src="{config.gif_data_uri("call.gif")}" '
        f'style="width:100%; max-width:180px; border-radius:18px; margin-bottom:0.5rem;"/>'
        f'</div>',
        unsafe_allow_html=True)
    st.markdown("## 💌 专属小设置")
    her_name = st.text_input("她的专属昵称", value="宝宝")

    st.markdown("---")
    st.markdown("### ⏳ 恋爱时光机")
    start_date = st.date_input("我们在一起的那一天是？", value=date(2023, 1, 1), max_value=date.today())
    days_together = (date.today() - start_date).days

    st.markdown("---")
    effect = st.radio("提交后的惊喜特效", ["🎈 气球", "❄️ 飘雪", "🎈❄️ 都要"])

# ==========================================
# 2. 主页面：核心交互 (级联菜单逻辑)
# ==========================================
st.markdown(
    f'<div class="title-row">'
    f'<img class="dog-img" src="{config.gif_data_uri("heart.gif")}" alt="爱心小狗"/>'
    f'<div>'
    f'<div class="title-heart">💖 专属我们的周末甜蜜计划 💖</div>'
    f'<div class="subtitle">亲爱的，勾选你想一起做的事，剩下的一切都交给我 💕</div>'
    f'</div>'
    f'<img class="dog-img" src="{config.gif_data_uri("normal.gif")}" alt="乖乖小狗"/>'
    f'</div>',
    unsafe_allow_html=True)

tabs = st.tabs([b["tab"] for b in config.TIME_BLOCKS])
selections = {}

for tab, block in zip(tabs, config.TIME_BLOCKS):
    with tab:
        st.markdown(f"#### {block['icon']} {block['hint']}")

        # 基础活动选择
        try:
            chosen = st.pills("💝 想一起做的事（可多选）：", options=config.ACTIVITY_OPTIONS, selection_mode="multi",
                              key=f"pills_{block['name']}")
        except AttributeError:
            chosen = st.multiselect("💝 想一起做的事（可多选）：", options=config.ACTIVITY_OPTIONS,
                                    key=f"ms_{block['name']}")

        final_chosen = list(chosen) if chosen else []

        # 吃饭的子级联菜单逻辑
        if "🍽️ 吃饭" in final_chosen:
            st.markdown("##### 👩‍🍳 关于美味的特别安排...")
            eat_where = st.radio("想在哪儿吃呢？", ["🏠 在家吃", "🏪 去外面"], key=f"where_{block['name']}",
                                 horizontal=True)

            # 根据选择动态加载 config.py 里的菜单
            food_options = config.FOOD_MENU[eat_where]

            try:
                food_chosen = st.pills("想吃点什么呢？", options=food_options, selection_mode="multi",
                                       key=f"food_pills_{block['name']}")
            except AttributeError:
                food_chosen = st.multiselect("想吃点什么呢？", options=food_options, key=f"food_ms_{block['name']}")

            if food_chosen:
                final_chosen.remove("🍽️ 吃饭")
                food_str = "、".join(food_chosen)
                location = eat_where.split(" ")[1]
                final_chosen.append(f"🍽️ 享受美食（{location}：{food_str}）")

        # 保存该时间段的数据
        selections[block["name"]] = final_chosen

st.markdown("---")

# ==========================================
# 3. 提交与展示结果
# ==========================================
st.markdown(
    f'<div style="text-align:center; margin-top:1rem;">'
    f'<img class="dog-img" src="{config.gif_data_uri("jump.gif")}" alt="蹦蹦跳跳的小狗"/>'
    f'</div>',
    unsafe_allow_html=True)

submitted = st.button("🥰 选好啦，生成我们的周末行程！", use_container_width=True)

if submitted:
    if sum(len(v) for v in selections.values()) == 0:
        st.warning("哎呀，还没有勾选任何项目呢～ 快去上面挑几个吧 🥺")
    else:
        # 调用 logic.py 里的生成算法
        st.session_state["summary"] = logic.build_summary(selections, her_name, days_together)

        if "气球" in effect: st.balloons()
        if "飘雪" in effect: st.snow()

# 显示结果
if st.session_state.get("summary"):
    st.markdown(st.session_state["summary"], unsafe_allow_html=True)

st.markdown(
    f'<div style="text-align:center; margin-top:3rem;">'
    f'<img class="dog-img" style="width:70px; height:70px;" src="{config.gif_data_uri("walkdog.gif")}" alt="遛狗小狗"/>'
    f'</div>',
    unsafe_allow_html=True)

st.markdown(
    '<div style="text-align:center; color:#b36b84; font-size:0.8rem; margin-top:0.5rem;">💕 专属于你的小惊喜 · 代码由最爱你的程序员编写 💕</div>',
    unsafe_allow_html=True)
