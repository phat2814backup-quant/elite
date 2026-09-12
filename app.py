# -*- coding: utf-8 -*-
"""
ELITE FARROW 10-MINUTE ENGINE (V2)
Ứng dụng Nén Tri Thức & Phản Xạ 10 Phút theo Phương pháp Kỷ lục gia Guinness Dave Farrow
Tích hợp: 3 Trụ Cột Trinity, 88 Mô Hình Hạt Nhân, 100 Nguyên Lý Khởi Thủy, Máy Ép AI 1-Click & Trạm Thở.
"""

import os
import time
import streamlit as st

from core.knowledge_vault import get_all_farrow_topics, get_farrow_topic_by_id
from core.farrow_engine import compress_with_farrow_ai
from core.models_engine import (
    get_farrow_models_grouped,
    get_farrow_principles_grouped,
    draw_random_farrow_sprint_trio,
    load_all_mental_models,
    load_all_principles
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

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
st.markdown("""
<div class="farrow-header">
    <div class="farrow-badge">⚡ DAVE FARROW 10-MINUTE MEMORY ENGINE</div>
    <h1 style="color: #f8fafc; margin: 4px 0 8px 0; font-weight: 800;">ELITE THINKING: FARROW EDITION</h1>
    <p style="color: #94a3b8; margin: 0; font-size: 1.05rem;">
        Loại bỏ 90% chữ rườm rà. Nén toàn bộ <b>88 Mô Hình & 100 Nguyên Lý</b> về đúng <b>Bộ 3 Hạt Nhân (Rule of 3)</b>, 
        ghim vào <b>Lâu Đài Ký Ức</b> và chiếm lĩnh trong <b>10 Phút Nước Rút</b>.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🧭 ĐIỀU HƯỚNG FARROW")
    app_mode = st.radio(
        "Chọn phòng chức năng:",
        [
            "🏛️ Lâu Đài Ký Ức (The 3 Trinity)",
            "🕸️ 88 Mô Hình Hạt Nhân (Farrow Latticework)",
            "📚 Thư Viện Nguyên Lý (100 First Principles)",
            "⏱️ Phòng Ép Xung 10 Phút (Focus Sprint)",
            "⚡ Máy Ép Farrow 1-Click (AI Compressor)",
            "🫁 Trạm Thở Bụng Sạc Pin"
        ],
        index=0
    )
    
    st.divider()
    st.markdown("#### 🔑 Cấu Hình Gemini AI (Tùy chọn)")
    api_key_input = st.text_input(
        "Nhập Gemini API Key:",
        type="password",
        value=os.getenv("GEMINI_API_KEY", ""),
        help="Dùng cho tính năng Máy Ép Farrow 1-Click. Nếu để trống, app sẽ tự động kích hoạt bộ nén Heuristic dự phòng."
    )
    if api_key_input:
        os.environ["GEMINI_API_KEY"] = api_key_input

    st.caption("💡 *Quy chuẩn Dave Farrow: Não chỉ là cục pin nhỏ, đừng học dồn 2 tiếng. Hãy chạy nước rút 10 phút rồi xả hơi.*")

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
            st.markdown(f"""
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
            """, unsafe_allow_html=True)

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
# PHÒNG 2: 88 MÔ HÌNH HẠT NHÂN (FARROW LATTICEWORK)
# -----------------------------------------------------------------------------
elif app_mode == "🕸️ 88 Mô Hình Hạt Nhân (Farrow Latticework)":
    st.markdown("### 🕸️ Ma Trận 88 Mô Hình Munger: Quy Chuẩn Farrow")
    st.caption("Toàn bộ 88 mô hình được quy về đúng 3 Ngăn Kéo Farrow. Không văn bản hàn lâm, chỉ giữ lại Nguyên lý 1 câu, Phản xạ 5s và Cạm bẫy.")

    models_grouped = get_farrow_models_grouped()
    all_models = load_all_mental_models()
    tier1_models = [m for m in all_models if m.get("tier") == 1]

    # Metrics row
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric("📦 Tổng Số Mô Hình", f"{len(all_models)} mô hình")
    with col_m2:
        st.metric("⭐ Tier 1 (Pareto 80/20)", f"{len(tier1_models)} hạt nhân")
    with col_m3:
        st.metric("🚪 Soi Gốc / 🖥️ Đọc Dòng", f"{len(models_grouped['root'])} / {len(models_grouped['flow'])}")
    with col_m4:
        st.metric("🪑 Ra Đòn Bất Đối Xứng", f"{len(models_grouped['strike'])} mô hình")

    # Filters
    col_filter1, col_filter2 = st.columns([1, 2])
    with col_filter1:
        tier_filter = st.selectbox(
            "Lọc cấp độ ưu tiên:",
            ["Tất cả", "⭐ Chỉ xem Tier 1 (Siêu hạt nhân 80/20)", "Cấp 2 & 3"]
        )
    with col_filter2:
        search_kw = st.text_input("🔍 Tìm kiếm nhanh mô hình:", placeholder="Gõ tên mô hình, đòn bẩy, entropy, bayes...")

    # 3 Farrow Tabs
    tab_root, tab_flow, tab_strike = st.tabs([
        f"🚪 TRỤ 1: SOI GỐC ({len(models_grouped['root'])})",
        f"🖥️ TRỤ 2: ĐỌC DÒNG ({len(models_grouped['flow'])})",
        f"🪑 TRỤ 3: RA ĐÒN ({len(models_grouped['strike'])})"
    ])

    def render_model_list(models_list):
        filtered = models_list
        if tier_filter == "⭐ Chỉ xem Tier 1 (Siêu hạt nhân 80/20)":
            filtered = [m for m in filtered if m.get("tier") == 1]
        elif tier_filter == "Cấp 2 & 3":
            filtered = [m for m in filtered if m.get("tier") in [2, 3]]
        
        if search_kw.strip():
            kw = search_kw.strip().lower()
            filtered = [
                m for m in filtered 
                if kw in str(m.get("name_vi", "")).lower() 
                or kw in str(m.get("name_en", "")).lower() 
                or kw in str(m.get("first_principle", "")).lower()
                or kw in str(m.get("trigger_question", "")).lower()
            ]

        if not filtered:
            st.info("Không tìm thấy mô hình phù hợp với bộ lọc.")
            return

        st.caption(f"Hiển thị **{len(filtered)}** thẻ bài Farrow")
        
        # Grid display 2 columns
        col_left, col_right = st.columns(2)
        for idx, m in enumerate(filtered):
            target_col = col_left if idx % 2 == 0 else col_right
            with target_col:
                pillar_tag = m.get("pillar", "")
                tier_badge = '<span class="badge-tier1">⭐ TIER 1</span>' if m.get("tier") == 1 else ""
                
                st.markdown(f"""
                <div class="model-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="badge-{m.get('farrow_pillar', 'root')}">{m.get('pillar', 'Đa ngành')}</span>
                        {tier_badge}
                    </div>
                    <div class="model-title">#{m.get('id', '')} {m.get('name_vi', '')} <span style="font-size: 0.85rem; color: #64748b;">({m.get('name_en', '')})</span></div>
                    <div class="model-rule">💡 <b>Nguyên lý gốc:</b> {m.get('first_principle', '')}</div>
                    <div class="trigger-box">
                        ⚡ <b>PHẢN XẠ 5 GIÂY:</b><br>
                        <i>"{m.get('trigger_question', '')}"</i>
                    </div>
                    <div class="trap-box">
                        🪤 <b>BẪY ĐẢO NGƯỢC CẦN NÉ:</b><br>
                        {m.get('inversion_trap', '')}
                    </div>
                    <div style="margin-top: 8px; font-size: 0.85rem; color: #a5b4fc;">
                        🎯 <b>Đòn bẩy:</b> {m.get('elite_leverage', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab_root:
        st.markdown("**Bản chất:** Đập vụn về giới hạn vật lý, loại bỏ giả định rườm rà, lộn ngược tìm rủi ro chết người.")
        render_model_list(models_grouped["root"])

    with tab_flow:
        st.markdown("**Bản chất:** Bắt nhịp chuyển động, cập nhật xác suất liên tục, đọc vị động cơ và nhìn trước nước cờ bậc 2.")
        render_model_list(models_grouped["flow"])

    with tab_strike:
        st.markdown("**Bản chất:** Ra đòn bất đối xứng (Cắt lỗ 1 cọng lông, ăn dày 3 bát thóc), kích hoạt phản ứng dây chuyền với chi phí nhỏ nhất.")
        render_model_list(models_grouped["strike"])

# -----------------------------------------------------------------------------
# PHÒNG 3: THƯ VIỆN NGUYÊN LÝ (100 FIRST PRINCIPLES)
# -----------------------------------------------------------------------------
elif app_mode == "📚 Thư Viện Nguyên Lý (100 First Principles)":
    st.markdown("### 📚 Thư Viện 100 Nguyên Lý Khởi Thủy: Chuẩn Farrow 10 Giây")
    st.caption("Các định luật gốc rễ từ Vật lý, Sinh học, Toán học, Hóa học được nén về: Bản chất trực giác 1 câu, Công thức cốt lõi và Tiêu chuẩn khả bác.")

    principles_grouped = get_farrow_principles_grouped()
    all_p = load_all_principles()

    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.metric("🔬 Tổng Số Nguyên Lý", f"{len(all_p)} định luật")
    with col_p2:
        st.metric("🚪 Soi Gốc (Bảo Toàn & Ranh Giới)", f"{len(principles_grouped['root'])} nguyên lý")
    with col_p3:
        st.metric("🖥️ Đọc Dòng & 🪑 Ra Đòn", f"{len(principles_grouped['flow']) + len(principles_grouped['strike'])} nguyên lý")

    p_search = st.text_input("🔍 Tìm kiếm nguyên lý khoa học:", placeholder="Arrhenius, Le Chatelier, Newton, Entropy, Bayes, Lavoisier...")

    t_p_root, t_p_flow, t_p_strike = st.tabs([
        f"🚪 BẢO TOÀN & RANH GIỚI ({len(principles_grouped['root'])})",
        f"🖥️ DÒNG CHẢY & CÂN BẰNG ({len(principles_grouped['flow'])})",
        f"🪑 ĐÒN BẨY & NĂNG LƯỢNG ({len(principles_grouped['strike'])})"
    ])

    def render_principle_list(p_list):
        filtered = p_list
        if p_search.strip():
            kw = p_search.strip().lower()
            filtered = [
                p for p in filtered
                if kw in str(p.get("principle_name", "")).lower()
                or kw in str(p.get("domain", "")).lower()
                or kw in str(p.get("intuitive_summary", "")).lower()
                or kw in str(p.get("formal_definition", "")).lower()
            ]
        
        st.caption(f"Hiển thị **{len(filtered)}** nguyên lý")
        col_a, col_b = st.columns(2)
        for idx, p in enumerate(filtered):
            target = col_a if idx % 2 == 0 else col_b
            with target:
                st.markdown(f"""
                <div class="model-card">
                    <span class="badge-{p.get('farrow_pillar', 'root')}">{p.get('domain', 'Khoa học')}</span>
                    <div class="model-title">{p.get('principle_name', '')}</div>
                    <div style="background: rgba(99, 102, 241, 0.1); border-left: 3px solid #6366f1; padding: 10px; border-radius: 0 8px 8px 0; margin: 8px 0; color: #c7d2fe; font-size: 0.95rem;">
                        💡 <b>Bản chất đời thường:</b><br>{p.get('intuitive_summary', p.get('description', ''))}
                    </div>
                    <div class="model-rule">📐 <b>Định luật chính xác:</b> {p.get('formal_definition', '')}</div>
                    <div class="trap-box">
                        🔬 <b>TIÊU CHUẨN KHẢ BÁC (FALSIFY):</b><br>
                        {p.get('falsification_test', 'Không có')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with t_p_root:
        render_principle_list(principles_grouped["root"])
    with t_p_flow:
        render_principle_list(principles_grouped["flow"])
    with t_p_strike:
        render_principle_list(principles_grouped["strike"])

# -----------------------------------------------------------------------------
# PHÒNG 4: PHÒNG ÉP XUNG 10 PHÚT (10-MINUTE FOCUS SPRINT)
# -----------------------------------------------------------------------------
elif app_mode == "⏱️ Phòng Ép Xung 10 Phút (Focus Sprint)":
    st.markdown("### ⏱️ Phòng Ép Xung 10 Phút (The 10-Minute Focus Sprint)")
    st.caption("Chạy nước rút tập trung cao độ trong 10 phút. Bạn có thể chọn chủ đề có sẵn hoặc Rút ngẫu nhiên 3 thẻ bài để thử thách não bộ!")

    sprint_type = st.radio(
        "Chọn chế độ Sprint:",
        ["🎲 Rút 3 Thẻ Ngẫu Nhiên (Bộ 3 Farrow Tarot)", "📖 Chọn Chủ Đề Chuyên Sâu Có Sẵn"],
        horizontal=True
    )

    if sprint_type == "🎲 Rút 3 Thẻ Ngẫu Nhiên (Bộ 3 Farrow Tarot)":
        if "random_trio" not in st.session_state or st.button("🔀 Rút Lại 3 Thẻ Mới", type="secondary"):
            st.session_state.random_trio = draw_random_farrow_sprint_trio()
        
        trio = st.session_state.random_trio
        st.info("🎯 **Thử thách 10 phút của bạn:** Hãy ghi nhớ và kết nối 3 mô hình này vào Lâu đài ký ức trong phòng!")
        
        c_r1, c_r2, c_r3 = st.columns(3)
        cols_t = [c_r1, c_r2, c_r3]
        anchors = [("🚪 CỬA RA VÀO", "Soi Gốc"), ("🖥️ MÀN HÌNH", "Đọc Dòng"), ("🪑 BÀN GHẾ", "Ra Đòn")]
        for idx, (col_item, m, (anc_name, anc_desc)) in enumerate(zip(cols_t, trio, anchors)):
            with col_item:
                st.markdown(f"""
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
                """, unsafe_allow_html=True)
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
        st.markdown(f"""
        <div class="timer-container">
            <div style="color: #94a3b8; font-weight: 600; text-transform: uppercase;">ĐỒNG HỒ ĐẾM NGƯỢC NƯỚC RÚT</div>
            <div class="timer-digits">{mins:02d}:{secs:02d}</div>
            <div style="color: #38bdf8; font-weight: 600; margin-top: 8px;">
                {
                    "CHẶNG 1: BÓC TÁCH VÀ NÉN (00-02m)" if mins >= 8 else
                    "CHẶNG 2: GẮN VÀO LÂU ĐÀI KÝ ỨC (02-05m)" if mins >= 5 else
                    "CHẶNG 3: ÉP XUNG QUÉT TỐC ĐỘ X3 (05-08m)" if mins >= 2 else
                    "CHẶNG 4: PHẢN XẠ VÀ THỞ BỤNG SẠC PIN (08-10m)"
                }
            </div>
        </div>
        """, unsafe_allow_html=True)

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
# PHÒNG 5: MÁY ÉP FARROW 1-CLICK (AI COMPRESSOR)
# -----------------------------------------------------------------------------
elif app_mode == "⚡ Máy Ép Farrow 1-Click (AI Compressor)":
    st.markdown("### ⚡ Máy Ép Farrow 1-Click (Universal Text Compressor)")
    st.caption("Dán bất kỳ tài liệu dài, bài luận, case study, hoặc cuốn sách dày cộp nào vào đây. AI sẽ tự động ép nát về đúng 3 khối hạt nhân.")

    user_raw_text = st.text_area(
        "Dán văn bản thô vào đây (tối đa 8.000 ký tự):",
        placeholder="Ví dụ: Dán một bài phân tích dài về kinh tế vĩ mô, một chiến lược kinh doanh 10 trang, hoặc một bài giảng khó hiểu của trường học...",
        height=200
    )

    if st.button("💥 ÉP NÉN THEO CHUẨN DAVE FARROW (RULE OF 3)", type="primary"):
        if not user_raw_text.strip():
            st.warning("Vui lòng dán nội dung văn bản cần nén!")
        else:
            with st.spinner("🤖 Đang nghiền nát văn bản thừa, trích xuất 3 hạt nhân và tạo hình ảnh kỳ quặc..."):
                result = compress_with_farrow_ai(user_raw_text)
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
                st.markdown(f"""
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
                """, unsafe_allow_html=True)

        st.success(f"🎯 **Đòn bẩy Bất đối xứng (Actionable Strike):** {res.get('asymmetric_action', '')}")

# -----------------------------------------------------------------------------
# PHÒNG 6: TRẠM THỞ BỤNG SẠC PIN
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
st.caption("⚡ **Elite Farrow Engine v2.0** — Hệ thống tư duy tinh hoa nén tối giản dành cho con người hiện đại.")
