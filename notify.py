# -*- coding: utf-8 -*-
"""
通知模块：她提交后，通过 PushPlus 把选择推送到你的微信
"""
import json
import urllib.request
from datetime import datetime

import config

PUSHPLUS_URL = "https://www.pushplus.plus/send"


def _get_token() -> str:
    """优先读 config，其次读 Streamlit Secrets（云端部署用）"""
    token = getattr(config, "PUSHPLUS_TOKEN", "")
    if token:
        return token
    try:
        import streamlit as st
        return st.secrets.get("pushplus_token", "")
    except Exception:
        return ""


def _send(title: str, html_content: str) -> str:
    """调用 PushPlus 接口，返回给页面展示的结果描述"""
    token = _get_token()
    if not token:
        return "📱 未配置微信推送 token（见 config.py 顶部说明）"

    payload = json.dumps(
        {"token": token, "title": title, "content": html_content, "template": "html"}
    ).encode("utf-8")
    req = urllib.request.Request(
        PUSHPLUS_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        if result.get("code") == 200:
            return "💌 已把计划推送到小哥哥的微信啦～"
        return f"⚠️ 推送失败：{result.get('msg', '未知错误')}"
    except Exception as e:
        return f"⚠️ 推送失败：{e}"


def build_push_content(selections: dict, her_name: str, days_together: int) -> str:
    """把她的选择拼成一条适合微信阅读的 HTML 消息"""
    blocks_html = []
    for block in config.TIME_BLOCKS:
        items = selections.get(block["name"], [])
        if not items:
            continue
        items_str = "、".join(items)
        blocks_html.append(
            f'<p style="margin:4px 0;"><b>{block["icon"]} {block["name"]}</b>：{items_str}</p>'
        )

    body = "".join(blocks_html)
    total_items = sum(len(v) for v in selections.values())
    days_html = f'<p>✨ 这是你们相爱的第 <b>{days_together}</b> 天 ✨</p>' if days_together > 0 else ""
    now = datetime.now().strftime("%m月%d日 %H:%M")

    return f"""
    <h3 style="text-align:center;">💌 她的周末计划新鲜出炉！</h3>
    {days_html}
    <p>{her_name} 在 {now} 提交了她的选择：</p>
    {body}
    <p style="margin-top:8px;">🎀 一共 <b>{total_items}</b> 个小甜蜜，快为她安排起来吧！</p>
    """


def send_weekend_plan(selections: dict, her_name: str, days_together: int) -> str:
    """入口函数：她提交后调用，把整份计划推到微信"""
    title = f"💖 {her_name} 提交了周末计划"
    return _send(title, build_push_content(selections, her_name, days_together))
