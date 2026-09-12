# -*- coding: utf-8 -*-
"""
ELITE FARROW 10-MINUTE ENGINE (V2.1)
Ứng dụng Nén Tri Thức & Phản Xạ 10 Phút theo Phương pháp Kỷ lục gia Guinness Dave Farrow
Hợp nhất: 3 Trụ Cột Trinity, 152 Mô Hình & Nguyên Lý Tinh Hoa (Unified Farrow Latticework), 
Máy Ép AI Xoay Tua Đa Khóa & Trạm Thở Sạc Pin.
"""

import os
import time
import textwrap
import html
import streamlit as st

from core.knowledge_vault import get_all_farrow_topics, get_farrow_topic_by_id
from core.farrow_engine import (
    compress_with_farrow_ai,
    get_all_gemini_api_keys,
    get_api_key_status
)
from core.models_engine import (
    load_unified_farrow_catalog,
    get_farrow_models_grouped,
    get_farrow_metrics,
    draw_random_farrow_sprint_trio
)

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Elite Farrow — Động Cơ Nén Tri Thức 10 Phút",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
css_path = os.path.join("assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_html(html_content: str):
    """Render HTML an toàn, tự động loại bỏ thụt đầu dòng để tránh lỗi code-block của Markdown."""
    clean_html = textwrap.dedent(html_content).strip()
    st.markdown(clean_html, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
render_html("""
<div class="farrow-header">
    <div class="farrow-badge">⚡ DAVE FARROW 10-MINUTE MEMORY ENGINE</div>
    <h1 style="color: #f8fafc; margin: 4px 0 8px 0; font-weight: 800;">ELITE THINKING: FARROW EDITION</h1>
    <p style="color: #94a3b8; margin: 0; font-size: 1.05rem;">
        Loại bỏ 90% chữ rườm rà. Nén toàn bộ <b>152 Mô Hình & Nguyên Lý Tinh Hoa</b> về đúng <b>Bộ 3 Hạt Nhân (Rule of 3)</b>, 
        ghim vào <b>Lâu Đài Ký Ức</b> và chiếm lĩnh trong <b>10 Phút Nước Rút</b>.
    </p>
</div>
""")

# -----------------------------------------------------------------------------
# Sidebar Navigation & API Setup
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🧭 ĐIỀU HƯỚNG FARROW")
    app_mode = st.radio(
        "Chọn phòng chức năng:",
        [
            "🏛️ Lâu Đài Ký Ức (The 3 Trinity)",
            "🕸️ Ma Trận Mô Hình & Nguyên Lý (Unified Latticework)",
            "⏱️ Phòng Ép Xung 10 Phút (Focus Sprint)",
            "⚡ Máy Ép Farrow 1-Click (AI Compressor)",
            "🫁 Trạm Thở Bụng Sạc Pin"
        ],
        index=0
    )
    
    st.divider()
    st.markdown("#### 🔑 Kết Nối Trí Tuệ Nhân Tạo (Gemini AI)")
    api_status = get_api_key_status()
    if api_status["has_keys"]:
        st.success(f"🟢 **Hệ thống AI sẵn sàng:**\n{api_status['active_hint']}")
    else:
        st.warning("⚠️ Chưa phát hiện API Key trong `.env`.")

    custom_key = st.text_input(
        "Khóa API dự phòng (Tùy chọn ghi đè):",
        type="password",
        value="",
        help="Hệ thống đã tự động liên kết các key từ file cấu hình .env. Chỉ nhập vào đây nếu bạn muốn sử dụng một key cá nhân khác."
    )
    active_api_key = custom_key.strip() if custom_key.strip() else None

    st.caption("💡 *Quy chuẩn Dave Farrow: Não chỉ là cục pin nhỏ, đừng học dồn 2 tiếng. Hãy chạy nước rút 10 phút rồi thở bụng xả hơi.*")

# -----------------------------------------------------------------------------
# PHÒNG 1: LÂU ĐÀI KÝ ỨC (THE 3 TRINITY)
# -----------------------------------------------------------------------------
if app_mode == "🏛️ Lâu Đài Ký Ức (The 3 Trinity)":
    st.markdown("### 🏛️ Lâu Đài Ký Ức: Chọn Chủ Đề Nén Sẵn")
    st.caption("Mỗi chủ đề đã được tinh giản tuyệt đối theo Quy tắc số 3: 3 Khối hạt nhân gắn tại 3 mỏ neo phòng học của bạn.")

    topics = get_all_farrow_topics()
    topic_options = {t["id"]: f"{t['icon']} {t['title']}" for t in topics}
    
    selected_id = st.selectbox(
        "Chọn chủ đề tinh hoa cần nạp vào não:",
        options=list(topic_options.keys()),
        format_func=lambda x: topic_options[x]
    )
    
    topic = get_farrow_topic_by_id(selected_id)
    st.info(f"🎯 **Khẩu quyết:** *\"{topic['tagline']}\"*")
    
    # Render 3 Columns
    c1, c2, c3 = st.columns(3)
    chunks = topic["chunks"]
    cols = [c1, c2, c3]
    for idx, (col, chunk) in enumerate(zip(cols, chunks)):
        with col:
            card_html = f"""
            <div class="trinity-card">
                <div class="anchor-badge">{chunk['anchor_icon']} MỎ NEO: {chunk['anchor_name']}</div>
                <h3 style="color: #f8fafc; margin-top: 0; font-size: 1.25rem;">{chunk['label']}</h3>
                <p style="color: #38bdf8; font-size: 0.85rem; font-weight: 600;">{chunk.get('sub_modes', '')}</p>
                <div style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.5; margin: 12px 0;">
                    <b>Nguyên lý gốc:</b> {chunk['principle']}
                </div>
                <div class="crazy-image-box">
                    🧠 <b>HÌNH ẢNH DỊ BIỆT GHIM NÃO:</b><br>
                    {chunk['crazy_image']}
                </div>
                <div class="trigger-box">
                    ⚡ <b>CÂU HỎI KÍCH HOẠT 5 GIÂY:</b><br>
                    <i>"{chunk['trigger_question']}"</i>
                </div>
            </div>
            """
            render_html(card_html)

    st.markdown("---")
    st.markdown("### ⚡ Đấu Trường Phản Xạ 5 Giây (Feynman Challenge)")
    for q_idx, q in enumerate(topic.get("quiz", [])):
        with st.expander(f"🎯 Thử thách #{q_idx+1}: {q['question']}", expanded=True):
            user_ans = st.radio(
                "Phương án phản xạ của bạn:",
                q["options"],
                key=f"quiz_{selected_id}_{q_idx}",
                index=None
            )
            if user_ans is not None:
                chosen_idx = q["options"].index(user_ans)
                if chosen_idx == q["correct_idx"]:
                    st.success(f"🎉 **CHÍNH XÁC!** {q['explanation']}")
                else:
                    st.error("❌ **CHƯA ĐÚNG!** Hãy nhớ lại 3 mỏ neo trong lâu đài ký ức để phản xạ lại.")

# -----------------------------------------------------------------------------
# PHÒNG 2: MA TRẬN MÔ HÌNH & NGUYÊN LÝ TINH HOA (UNIFIED FARROW LATTICEWORK)
# -----------------------------------------------------------------------------
elif app_mode == "🕸️ Ma Trận Mô Hình & Nguyên Lý (Unified Latticework)":
    st.markdown("### 🕸️ Ma Trận Mô Hình & Nguyên Lý Tinh Hoa (Unified Farrow Latticework)")
    st.caption(
        "Hợp nhất toàn bộ **88 Mô Hình Munger & 64 Định Luật Khoa Học Khởi Thủy** vào 3 Ngăn Kéo Farrow. "
        "Đã loại bỏ hoàn toàn các mục rỗng, làm sạch dữ liệu và tối ưu cho phản xạ 10 giây."
    )

    models_grouped = get_farrow_models_grouped()
    all_items = load_unified_farrow_catalog()
    metrics = get_farrow_metrics()

    # Metrics row
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric("📦 Tổng Số Tinh Hoa", f"{metrics['total']} mục")
    with col_m2:
        st.metric("⭐ Siêu Hạt Nhân (Tier 1)", f"{metrics['tier1_count']} mô hình")
    with col_m3:
        st.metric("🚪 Soi Gốc / 🖥️ Đọc Dòng", f"{metrics['root_count']} / {metrics['flow_count']}")
    with col_m4:
        st.metric("🪑 Ra Đòn Bất Đối Xứng", f"{metrics['strike_count']} đòn bẩy")

    # Filter row
    col_filter1, col_filter2 = st.columns([1, 2])
    with col_filter1:
        tier_filter = st.selectbox(
            "Lọc phân loại:",
            [
                "Tất cả danh mục",
                "⭐ Chỉ xem Tier 1 (Siêu hạt nhân 80/20)",
                "Cấp 2 & 3",
                "🔬 Chỉ xem Nguyên lý Khoa học",
                "🧠 Chỉ xem Mô hình Tư duy"
            ]
        )
    with col_filter2:
        search_kw = st.text_input(
            "🔍 Tìm kiếm nhanh tinh hoa:", 
            placeholder="Gõ tên mô hình, định luật, đòn bẩy, bayes, entropy, le chatelier, acsimet..."
        )

    # 3 Farrow Tabs
    tab_root, tab_flow, tab_strike = st.tabs([
        f"🚪 TRỤ 1: SOI GỐC ({metrics['root_count']})",
        f"🖥️ TRỤ 2: ĐỌC DÒNG ({metrics['flow_count']})",
        f"🪑 TRỤ 3: RA ĐÒN ({metrics['strike_count']})"
    ])

    def render_unified_card_list(items_list):
        filtered = items_list
        if tier_filter == "⭐ Chỉ xem Tier 1 (Siêu hạt nhân 80/20)":
            filtered = [m for m in filtered if m.get("tier") == 1]
        elif tier_filter == "Cấp 2 & 3":
            filtered = [m for m in filtered if m.get("tier") in [2, 3]]
        elif tier_filter == "🔬 Chỉ xem Nguyên lý Khoa học":
            filtered = [m for m in filtered if m.get("source") in ["scientific_principle", "merged"]]
        elif tier_filter == "🧠 Chỉ xem Mô hình Tư duy":
            filtered = [m for m in filtered if m.get("source") in ["mental_model", "merged"]]
        
        if search_kw.strip():
            kw = search_kw.strip().lower()
            filtered = [
                m for m in filtered 
                if kw in str(m.get("name_vi", "")).lower() 
                or kw in str(m.get("name_en", "")).lower() 
                or kw in str(m.get("pillar", "")).lower()
                or kw in str(m.get("first_principle", "")).lower()
                or kw in str(m.get("trigger_question", "")).lower()
                or kw in str(m.get("inversion_trap", "")).lower()
            ]

        if not filtered:
            st.info("Không tìm thấy mô hình hoặc nguyên lý nào phù hợp với bộ lọc hiện tại.")
            return

        st.caption(f"Đang hiển thị **{len(filtered)}** thẻ bài tinh hoa")
        
        # Grid display 2 columns
        col_left, col_right = st.columns(2)
        for idx, m in enumerate(filtered):
            target_col = col_left if idx % 2 == 0 else col_right
            with target_col:
                tier_badge = '<span class="badge-tier1">⭐ TIER 1</span>' if m.get("tier") == 1 else ""
                
                source_label = "Khoa học" if m.get("source") == "scientific_principle" else ("Hợp nhất" if m.get("source") == "merged" else "Mô hình")
                source_badge = f'<span class="badge-source">{source_label}</span>'
                
                farrow_pill = m.get("farrow_pillar", "root")
                pillar_badge = f'<span class="badge-{farrow_pill}">{m.get("pillar", "Đa ngành")}</span>'
                
                name_en_display = f"<span style=\"font-size: 0.85rem; color: #64748b; font-weight: 500;\">({m.get('name_en')})</span>" if m.get('name_en') else ""
                
                # Formal definition box if distinct
                formal_def = m.get("formal_definition", "")
                formal_html = ""
                if formal_def and formal_def != m.get("first_principle"):
                    formal_html = f'<div style="background: rgba(99, 102, 241, 0.08); border-left: 3px solid #6366f1; padding: 8px 10px; border-radius: 0 6px 6px 0; margin: 6px 0; font-size: 0.88rem; color: #c7d2fe;">📐 <b>Định luật chính xác:</b> {formal_def}</div>'

                # Trap box
                trap_text = m.get("inversion_trap", "")
                trap_html = ""
                if trap_text and trap_text not in ["None", ""]:
                    trap_html = f'<div class="trap-box">🪤 <b>BẪY ĐẢO NGƯỢC / KHẢ BÁC:</b><br>{trap_text}</div>'

                # Action leverage
                leverage_text = m.get("elite_leverage", "")
                leverage_html = ""
                if leverage_text and leverage_text not in ["None", ""]:
                    leverage_html = f'<div style="margin-top: 8px; font-size: 0.86rem; color: #a5b4fc;">🎯 <b>Đòn bẩy hành động:</b> {leverage_text}</div>'

                card_html = f"""
                <div class="model-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <div style="display: flex; gap: 6px; align-items: center;">
                            {pillar_badge}
                            {source_badge}
                        </div>
                        {tier_badge}
                    </div>
                    <div class="model-title">#{m.get('id', '')} {m.get('name_vi', '')} {name_en_display}</div>
                    <div class="model-rule">💡 <b>Bản chất 1 câu:</b> {m.get('first_principle', '')}</div>
                    {formal_html}
                    <div class="trigger-box">
                        ⚡ <b>PHẢN XẠ 5 GIÂY:</b><br>
                        <i>"{m.get('trigger_question', '')}"</i>
                    </div>
                    {trap_html}
                    {leverage_html}
                </div>
                """
                render_html(card_html)

    with tab_root:
        st.markdown("**Bản chất Trụ 1:** Bóc trần sự thật vật lý gốc rễ, loại bỏ giả định rườm rà, lộn ngược tìm rủi ro chết người.")
        render_unified_card_list(models_grouped["root"])

    with tab_flow:
        st.markdown("**Bản chất Trụ 2:** Bắt nhịp chuyển động dòng chảy, cập nhật xác suất liên tục, dự báo phản ứng dây chuyền bậc hai.")
        render_unified_card_list(models_grouped["flow"])

    with tab_strike:
        st.markdown("**Bản chất Trụ 3:** Ra đòn bất đối xứng (Rủi ro tối thiểu, tiềm năng vô hạn), kích hoạt phản ứng dây chuyền chi phí nhỏ nhất.")
        render_unified_card_list(models_grouped["strike"])

# -----------------------------------------------------------------------------
# PHÒNG 3: PHÒNG ÉP XUNG 10 PHÚT (10-MINUTE FOCUS SPRINT)
# -----------------------------------------------------------------------------
elif app_mode == "⏱️ Phòng Ép Xung 10 Phút (Focus Sprint)":
    st.markdown("### ⏱️ Phòng Ép Xung 10 Phút (The 10-Minute Focus Sprint)")
    st.caption("Chạy nước rút tập trung cao độ trong 10 phút. Chọn một chủ đề Lâu Đài Ký Ức hoặc Rút 3 Thẻ Bài Farrow Tarot để thử thách não bộ!")

    sprint_type = st.radio(
        "Chọn chế độ Sprint:",
        ["🎲 Rút 3 Thẻ Ngẫu Nhiên (Bộ 3 Farrow Tarot)", "📖 Chọn Chủ Đề Lâu Đài Ký Ức"],
        horizontal=True
    )

    if sprint_type == "🎲 Rút 3 Thẻ Ngẫu Nhiên (Bộ 3 Farrow Tarot)":
        if "random_trio" not in st.session_state or st.button("🔀 Rút Lại 3 Thẻ Tinh Hoa Mới", type="secondary"):
            st.session_state.random_trio = draw_random_farrow_sprint_trio()
        
        trio = st.session_state.random_trio
        st.info("🎯 **Thử thách 10 phút của bạn:** Hãy ghi nhớ và kết nối 3 mô hình này vào 3 mỏ neo trong phòng học của bạn!")
        
        c_r1, c_r2, c_r3 = st.columns(3)
        cols_t = [c_r1, c_r2, c_r3]
        anchors = [("🚪 CỬA RA VÀO", "Soi Gốc"), ("🖥️ MÀN HÌNH", "Đọc Dòng"), ("🪑 BÀN GHẾ", "Ra Đòn")]
        for idx, (col_item, m, (anc_name, anc_desc)) in enumerate(zip(cols_t, trio, anchors)):
            with col_item:
                card_html = f"""
                <div class="trinity-card">
                    <div class="anchor-badge">{anc_name} ({anc_desc})</div>
                    <h3 style="color: #f8fafc; font-size: 1.15rem; margin-top: 4px;">{m.get('name_vi', '')}</h3>
                    <div style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 8px;">{m.get('pillar', '')}</div>
                    <div class="model-rule">💡 <b>Quy luật:</b> {m.get('first_principle', '')}</div>
                    <div class="trigger-box">
                        ⚡ <b>KÍCH HOẠT 5S:</b><br>
                        <i>"{m.get('trigger_question', '')}"</i>
                    </div>
                </div>
                """
                render_html(card_html)
    else:
        topics = get_all_farrow_topics()
        sprint_topic_id = st.selectbox(
            "Chọn chủ đề để chạy nước rút 10 phút:",
            options=[t["id"] for t in topics],
            format_func=lambda x: [t["title"] for t in topics if t["id"] == x][0]
        )
        s_topic = get_farrow_topic_by_id(sprint_topic_id)
        for chunk in s_topic["chunks"]:
            st.markdown(f"- **{chunk['anchor_icon']} {chunk['anchor_name']} ➔ {chunk['label']}**: {chunk['principle']}")

    st.markdown("---")

    # Sprint Interactive Controller
    if "sprint_running" not in st.session_state:
        st.session_state.sprint_running = False
    if "sprint_seconds" not in st.session_state:
        st.session_state.sprint_seconds = 600

    col_timer, col_ctrl = st.columns([2, 1])
    with col_timer:
        mins = st.session_state.sprint_seconds // 60
        secs = st.session_state.sprint_seconds % 60
        phase_label = (
            "CHẶNG 1: BÓC TÁCH VÀ NÉN (00-02m)" if mins >= 8 else
            "CHẶNG 2: GẮN VÀO LÂU ĐÀI KÝ ỨC (02-05m)" if mins >= 5 else
            "CHẶNG 3: ÉP XUNG QUÉT TỐC ĐỘ X3 (05-08m)" if mins >= 2 else
            "CHẶNG 4: PHẢN XẠ VÀ THỞ BỤNG SẠC PIN (08-10m)"
        )
        timer_html = f"""
        <div class="timer-container">
            <div style="color: #94a3b8; font-weight: 600; text-transform: uppercase;">ĐỒNG HỒ ĐẾM NGƯỢC NƯỚC RÚT</div>
            <div class="timer-digits">{mins:02d}:{secs:02d}</div>
            <div style="color: #38bdf8; font-weight: 600; margin-top: 8px;">{phase_label}</div>
        </div>
        """
        render_html(timer_html)

    with col_ctrl:
        st.write("")
        st.write("")
        if st.button("▶️ BẮT ĐẦU SPRINT 10 PHÚT", use_container_width=True, type="primary"):
            st.session_state.sprint_running = True
            st.success("🔥 Đồng hồ đã kích hoạt! Hãy tập trung 100% vào tài liệu phía trên.")
        if st.button("🔄 ĐẶT LẠI 10 PHÚT (RESET)", use_container_width=True):
            st.session_state.sprint_seconds = 600
            st.session_state.sprint_running = False
            st.rerun()

# -----------------------------------------------------------------------------
# PHÒNG 4: MÁY ÉP FARROW 1-CLICK (AI COMPRESSOR)
# -----------------------------------------------------------------------------
elif app_mode == "⚡ Máy Ép Farrow 1-Click (AI Compressor)":
    st.markdown("### ⚡ Máy Ép Farrow 1-Click (Universal AI Compressor)")
    st.caption("Dán bất kỳ tài liệu dài, bài luận, case study hoặc báo cáo nào vào đây. AI sẽ tự động ép nát về đúng 3 khối hạt nhân.")

    user_raw_text = st.text_area(
        "Dán văn bản thô vào đây (tối đa 8.000 ký tự):",
        placeholder="Ví dụ: Dán một bài phân tích dài về kinh tế vĩ mô, một chiến lược kinh doanh 10 trang, hoặc một bài giảng khó hiểu của trường học...",
        height=200
    )

    if st.button("💥 ÉP NÉN THEO CHUẨN DAVE FARROW (RULE OF 3)", type="primary"):
        if not user_raw_text.strip():
            st.warning("Vui lòng dán nội dung văn bản cần nén!")
        else:
            with st.spinner("🤖 Đang nghiền nát câu chữ rườm rà, bóc tách 3 hạt nhân và tạo hình ảnh kỳ quặc..."):
                result = compress_with_farrow_ai(user_raw_text, api_key=active_api_key)
                st.session_state.compress_result = result
                st.success("🎉 Nén thành công! Dưới đây là bộ 3 hạt nhân đã được giải mã:")

    if "compress_result" in st.session_state:
        res = st.session_state.compress_result
        st.markdown(f"### 📦 Kết quả: {res.get('title', 'Bản Nén Farrow')}")
        st.info(f"🎯 **Khẩu quyết cốt lõi:** *\"{res.get('tagline', '')}\"*")

        c1, c2, c3 = st.columns(3)
        cols = [c1, c2, c3]
        chunks = res.get("chunks", [])

        icons = ["🚪", "🖥️", "🪑"]
        for idx, (col, chunk) in enumerate(zip(cols, chunks)):
            with col:
                card_html = f"""
                <div class="trinity-card">
                    <div class="anchor-badge">{icons[idx]} MỎ NEO: {chunk.get('anchor', '')}</div>
                    <h3 style="color: #f8fafc; font-size: 1.2rem;">{chunk.get('label', '')}</h3>
                    <div style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.5; margin: 12px 0;">
                        <b>Nguyên lý gốc:</b> {chunk.get('principle', '')}
                    </div>
                    <div class="crazy-image-box">
                        🧠 <b>HÌNH ẢNH DỊ BIỆT:</b><br>
                        {chunk.get('crazy_image', '')}
                    </div>
                    <div class="trigger-box">
                        ⚡ <b>PHẢN XẠ 5S:</b><br>
                        <i>"{chunk.get('trigger_question', '')}"</i>
                    </div>
                </div>
                """
                render_html(card_html)

        st.success(f"🎯 **Đòn bẩy Bất đối xứng (Actionable Strike):** {res.get('asymmetric_action', '')}")

# -----------------------------------------------------------------------------
# PHÒNG 5: TRẠM THỞ BỤNG SẠC PIN
# -----------------------------------------------------------------------------
elif app_mode == "🫁 Trạm Thở Bụng Sạc Pin":
    st.markdown("### 🫁 Trạm Thở Bụng Sạc Pin (Dave Farrow Belly Breathing)")
    st.markdown("""
    Dave Farrow nhấn mạnh: **Học xong mà không thở là tự sát trí nhớ**.
    Khi bạn ép xung học nhanh, hạch hạnh nhân (amygdala) bị kích thích và sản sinh cortisol (hormone căng thẳng) làm tắc nghẽn khả năng truy xuất của hồi hải mã.
    Hít thở sâu bằng bụng giúp đưa nhịp tim về trạng thái thư giãn (sóng não Alpha) và đưa oxy tối đa lên não để hồi hải mã "đóng đinh" ký ức dài hạn.
    """)

    b1, b2, b3, b4 = st.columns(4)
    with b1:
        st.info("1️⃣ **HÍT VÀO** (4 Giây)<br>Phình căng bụng lên", icon="🌬️")
    with b2:
        st.warning("2️⃣ **GIỮ KHÍ** (4 Giây)<br>Khóa chặt không khí trong bụng", icon="🛑")
    with b3:
        st.success("3️⃣ **THỞ RA** (4 Giây)<br>Xẹp sát bụng lại tống hết khí độc", icon="😮‍💨")
    with b4:
        st.info("4️⃣ **NGHỈ NGƠI** (4 Giây)<br>Thả lỏng toàn bộ cơ thể", icon="🧘")

    st.markdown("---")
    st.markdown("#### ⏱️ Đồng Hồ Dẫn Nhịp Thở 4 Nhịp (Box Breathing)")
    
    if st.button("▶️ BẮT ĐẦU 1 PHÚT THỞ BỤNG PHỤC HỒI", type="primary"):
        cycle_placeholder = st.empty()
        for cycle in range(3):
            cycle_placeholder.markdown(f"### 🌊 Vòng Thở #{cycle+1}/3: **HÍT VÀO...** (Phình bụng)", unsafe_allow_html=True)
            time.sleep(4)
            cycle_placeholder.markdown(f"### 🛑 Vòng Thở #{cycle+1}/3: **GIỮ KHÍ...** (Khóa chặt)", unsafe_allow_html=True)
            time.sleep(4)
            cycle_placeholder.markdown(f"### 😮‍💨 Vòng Thở #{cycle+1}/3: **THỞ RA CHẬM...** (Xẹp bụng)", unsafe_allow_html=True)
            time.sleep(4)
            cycle_placeholder.markdown(f"### 🧘 Vòng Thở #{cycle+1}/3: **THẢ LỎNG...** (Tĩnh lặng)", unsafe_allow_html=True)
            time.sleep(4)
        cycle_placeholder.success("🎉 **CHÚC MỪNG!** Pin não của bạn đã được sạc đầy 100%. Bạn đã sẵn sàng cho thử thách tiếp theo!")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.caption("⚡ **Elite Farrow Engine v2.1** — Hệ thống tư duy tinh hoa nén tối giản dành cho con người hiện đại.")
