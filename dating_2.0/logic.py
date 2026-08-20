# -*- coding: utf-8 -*-
"""
逻辑文件：处理数据拼接，生成最终的行程 HTML 字符串
"""
from config import TIME_BLOCKS, gif_data_uri

def build_summary(selections: dict, her_name: str, days_together: int) -> str:
    """
    根据用户的选择字典，生成行程单的 HTML
    """
    paragraphs = []
    for block in TIME_BLOCKS:
        name = block["name"]
        items = selections.get(name, [])
        if not items:
            continue
        items_str = "、".join(items)
        paragraphs.append(
            f'<p style="margin:0.6rem 0;">'
            f'<b style="color:#ff4d8d;">{block["icon"]} {name}</b>：'
            f'我们一起去 <b>{items_str}</b>。</p>'
        )

    body = "".join(paragraphs)
    total_items = sum(len(v) for v in selections.values())

    # 恋爱天数展示
    days_html = ""
    if days_together > 0:
        days_html = f'<p style="color:#ff4d8d; text-align:center; font-weight:bold;">✨ 这是我们相爱的第 {days_together} 天 ✨</p>'

    cake_dog = gif_data_uri("cake.gif")
    html_result = f"""
    <div class="summary-card">
      <h3 style="text-align:center; color:#ff4d8d; margin-bottom:0.5rem;">💌 我们的周末甜蜜行程单 💌</h3>
      {days_html}
      <p style="margin:0.4rem 0;">亲爱的 <b>{her_name}</b>，计划新鲜出炉啦：</p>
      {body}
      <p style="margin-top:1rem; border-top: 1px dashed #ffb3c6; padding-top: 0.8rem;">
        🎀 一共为你准备了 <b>{total_items}</b> 个小甜蜜！期待和你度过的每一秒 💗
      </p>
      <p style="text-align:center; margin:0.8rem 0 0 0;">
        <img src="{cake_dog}" alt="举着蛋糕的小狗" style="width:100px; border-radius:18px;"/>
      </p>
    </div>
    """
    return html_result
