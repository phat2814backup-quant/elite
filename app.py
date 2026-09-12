# -*- coding: utf-8 -*-
"""
ELITE FARROW 10-MINUTE ENGINE (V2)
Ứng dụng Nén Tri Thức & Phản Xạ 10 Phút theo Phương pháp Kỷ lục gia Guinness Dave Farrow
"""

import os
import time
import streamlit as st
from core.knowledge_vault import get_all_farrow_topics, get_farrow_topic_by_id
from core.farrow_engine import compress_with_farrow_ai

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
        Loại bỏ 90% chữ rườm rà. Nén mọi kiến thức khổng lồ thành <b>Bộ 3 Hạt Nhân (Rule of 3)</b>, 
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
            "⏱️ Phòng Ép Xung 10 Phút",
            "⚡ Máy Ép Farrow 1-Click",
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
    st.caption("Kiểm tra phản xạ thực chiến không nhìn sách. Hãy chọn câu trả lời trong vòng 5 giây:")
    
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
# PHÒNG 2: PHÒNG ÉP XUNG 10 PHÚT (10-MINUTE FOCUS SPRINT)
# -----------------------------------------------------------------------------
elif app_mode == "⏱️ Phòng Ép Xung 10 Phút":
    st.markdown("### ⏱️ Phòng Ép Xung 10 Phút (The 10-Minute Focus Sprint)")
    st.markdown("""
    Theo Dave Farrow, **10 phút là thời lượng hoàng kim** để não bộ chạy hết công suất mà không bị kiệt pin hay xao nhãng.
    Một phiên sprint 10 phút chuẩn gồm 4 chặng:
    """)

    # 4 Stage Overview
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown("**1. Phút 00–02**<br>🔍 *Bóc Tách & Nén*<br>Rút gọn về 3 khối hạt nhân.", unsafe_allow_html=True)
    with s2:
        st.markdown("**2. Phút 02–05**<br>🚪 *Gắn Lâu Đài*<br>Phóng chiếu 3 hình ảnh phi lý.", unsafe_allow_html=True)
    with s3:
        st.markdown("**3. Phút 05–08**<br>⚡ *Ép Xung x3*<br>Quét mắt tốc độ cực đại.", unsafe_allow_html=True)
    with s4:
        st.markdown("**4. Phút 08–10**<br>🫁 *Phản Xạ & Thở*<br>Kiểm tra 5s + Thở bụng sạc pin.", unsafe_allow_html=True)

    st.markdown("---")

    topics = get_all_farrow_topics()
    sprint_topic_id = st.selectbox(
        "Chọn chủ đề để chạy nước rút 10 phút:",
        options=[t["id"] for t in topics],
        format_func=lambda x: [t["title"] for t in topics if t["id"] == x][0]
    )
    s_topic = get_farrow_topic_by_id(sprint_topic_id)

    # Sprint Interactive Controller
    if "sprint_running" not in st.session_state:
        st.session_state.sprint_running = False
    if "sprint_seconds" not in st.session_state:
        st.session_state.sprint_seconds = 600  # 10 mins

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
            st.success("🔥 Đồng hồ đã kích hoạt! Hãy tập trung 100% vào tài liệu bên dưới.")
        if st.button("🔄 ĐẶT LẠI 10 PHÚT (RESET)", use_container_width=True):
            st.session_state.sprint_seconds = 600
            st.session_state.sprint_running = False
            st.rerun()

    # Content of the sprint
    st.markdown(f"#### 📖 Tài Liệu Tinh Gọn Cần Nạp Cho: **{s_topic['title']}**")
    for chunk in s_topic["chunks"]:
        st.markdown(f"""
        - **{chunk['anchor_icon']} {chunk['anchor_name']} ➔ {chunk['label']}**: {chunk['principle']}  
          *Hình ảnh ghim não:* `{chunk['crazy_image']}`
        """)

# -----------------------------------------------------------------------------
# PHÒNG 3: MÁY ÉP FARROW 1-CLICK (UNIVERSAL COMPRESSOR)
# -----------------------------------------------------------------------------
elif app_mode == "⚡ Máy Ép Farrow 1-Click":
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
# PHÒNG 4: TRẠM THỞ BỤNG SẠC PIN (BREATHING RECHARGE)
# -----------------------------------------------------------------------------
elif app_mode == "🫁 Trạm Thở Bụng Sạc Pin":
    st.markdown("### 🫁 Trạm Thở Bụng Sạc Pin (Dave Farrow Belly Breathing)")
    st.markdown("""
    Dave Farrow nhấn mạnh: **Học xong mà không thở là tự sát trí nhớ**.
    Khi bạn ép xung học nhanh, hạch hạnh nhân (amygdala) bị kích thích và sản sinh cortisol (hormone căng thẳng) làm tắc nghẽn khả năng truy xuất của hồi hải mã.
    Hít thở sâu bằng bụng giúp:
    1. Đưa nhịp tim về trạng thái thư giãn (sóng não Alpha).
    2. Đưa oxy tối đa lên não để hồi hải mã "đóng đinh" ký ức dài hạn.
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
