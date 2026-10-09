# -*- coding: utf-8 -*-
"""
Module Quản Trị Tủ Sách Tinh Hoa (Elite Bookshelf & Knowledge Vault).
Chịu trách nhiệm:
1. Tự động phát hiện, lập chỉ mục và phân tích cấu trúc các cuốn sách trong thư mục book/
2. Tách tầng nội dung: Bản Nén Nguyên Tắc Tinh Hoa (Core Principles) và Toàn Văn Theo Chương (Full Reader)
3. Hỗ trợ tìm kiếm toàn văn (Full-text search), tải file .md và Trợ lý AI đàm đạo trực tiếp với từng cuốn sách.
"""

from __future__ import annotations

import os
import re
from typing import Dict, List, Any, Optional
import streamlit as st

from core.farrow_engine import get_all_gemini_api_keys

try:
    import google.generativeai as genai
except ImportError:
    genai = None

# Danh sách các thư mục tìm kiếm sách theo thứ tự ưu tiên
BOOK_SEARCH_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "book"),
    "D:/02_HocTap/elite/book",
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "books"),
    "D:/02_HocTap/elite/books",
    os.path.join("book"),
    os.path.join("books"),
]

# Metadata tùy biến cho các cuốn sách đã biết (fallback nếu không đọc được từ file)
BOOK_METADATA_REGISTRY = {
    "tam_ly_trader_khi_giao_dich": {
        "title": "Tâm Lý Trader Khi Giao Dịch (Trading in the Zone)",
        "author": "Mark Douglas",
        "category": "Tâm lý Giao dịch & Xác suất",
        "icon": "🧠",
        "summary": "Tác phẩm kinh điển thế giới về tâm lý học trading, làm chủ trạng thái 'The Zone', 5 sự thật thị trường và 7 nguyên tắc nhất quán.",
        "tags": ["Trading", "Tâm lý học", "Xác suất", "Kỷ luật", "Mark Douglas"]
    },
    "xau_chiec_xe_bus_va_loi_the_chu_ga": {
        "title": "Chiếc Xe Bus Vàng & Lợi Thế Của Chú Gà Nhỏ",
        "author": "Elite Quant Master",
        "category": "Bản chất Thị trường & Vàng (XAU)",
        "icon": "🚌",
        "summary": "Ngụ ngôn thực chiến về bản chất giá vàng, động lực học dòng tiền, bẫy thanh khoản của Sói và lợi thế kẻ tí hon.",
        "tags": ["XAUUSD", "Thanh khoản", "Ngụ ngôn", "Sói & Gà"]
    },
    "xau_ngu_ngon_dau_tu": {
        "title": "Chuyện Ngụ Ngôn Đầu Tư XAU",
        "author": "Elite Quant Master",
        "category": "Bản chất Thị trường & Vàng (XAU)",
        "icon": "🏜️",
        "summary": "Tập hợp các câu chuyện ngụ ngôn bóc trần cuộc chơi tài chính, chi phí cơ hội, quy luật rung lắc và tâm lý đám đông.",
        "tags": ["XAUUSD", "Đầu tư", "Ngụ ngôn", "Tâm lý"]
    },
    "dave_farrow_memory": {
        "title": "Phương Pháp Trí Nhớ & Ép Xung Não Bộ Dave Farrow",
        "author": "Dave Farrow (Kỷ lục gia Guinness)",
        "category": "Não bộ & Siêu Trí Nhớ",
        "icon": "⚡",
        "summary": "Kỹ thuật tối ưu hóa pin não, Focus Burst 10 phút, mỏ neo không gian và tư duy hình ảnh dị biệt của kỷ lục gia thế giới.",
        "tags": ["Trí nhớ", "Dave Farrow", "Não bộ", "Focus Burst"]
    },
    "kho_sku_vang": {
        "title": "Kho SKU Vàng Thực Chiến (Dữ Liệu & Quy Luật)",
        "author": "Elite Quant System",
        "category": "Dữ liệu Thực chiến",
        "icon": "📊",
        "summary": "Kho lưu trữ mã nguồn, quy luật giá, hành vi nến và dữ liệu giải mã thị trường vàng thực chiến.",
        "tags": ["Dữ liệu", "SKU", "Vàng"]
    }
}


def sanitize_book_id(filename: str) -> str:
    """Chuyển đổi tên file thành Book ID chuẩn hóa."""
    base = os.path.splitext(filename)[0].lower()
    base = re.sub(r"[^\w\s-]", "", base)
    base = re.sub(r"[-\s]+", "_", base).strip("_")
    # Bỏ hậu tố _principles nếu có
    if base.endswith("_principles"):
        base = base[:-11]
    return base


def parse_chapters_from_markdown(content: str) -> List[Dict[str, Any]]:
    """Tự động phân tách nội dung Markdown thành danh sách các chương dựa vào các heading."""
    # Mẫu nhận diện chương: ### CHƯƠNG X, ## Chương X, # CHƯƠNG X, hoặc Phần X
    chapter_pattern = re.compile(
        r"(?:^|\n)(#{1,3}\s+(?:CHƯƠNG|Chương|PHẦN|Phần|HỒI|Hồi|Chapter)\s+[\dIVXLCDM]+[^\n]*)",
        re.IGNORECASE
    )

    matches = list(chapter_pattern.finditer(content))
    if not matches:
        return [{
            "index": 1,
            "title": "Toàn bộ tác phẩm",
            "content": content.strip()
        }]

    # Bóc tách tất cả các block và trích xuất số chương
    raw_blocks = []
    for i, match in enumerate(matches):
        start_pos = match.start()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        chunk = content[start_pos:end_pos].strip()

        lines = chunk.splitlines()
        raw_title = lines[0].strip() if lines else f"Chương {i + 1}"
        clean_title = re.sub(r"^#+\s*", "", raw_title).strip()

        # Ghép tiêu đề phụ nếu có
        if len(lines) > 1 and lines[1].strip() and not lines[1].startswith("#"):
            sub_title = lines[1].strip()
            if len(sub_title) < 100:
                clean_title = f"{clean_title}: {sub_title}"

        # Trích xuất số chương nếu có
        num_m = re.search(r"(?:CHƯƠNG|Chương|Chapter|PHẦN|Phần)\s+(\d+)", clean_title, re.IGNORECASE)
        chap_num = int(num_m.group(1)) if num_m else None

        raw_blocks.append({
            "title": clean_title,
            "content": chunk,
            "len": len(chunk),
            "start": start_pos,
            "chap_num": chap_num
        })

    # Tìm vị trí bắt đầu của các chương thật:
    # Nếu có nhiều block chap_num == 1, ta tìm block chap_num == 1 cuối cùng hoặc block có độ dài lớn (> 1000 ký tự)
    real_start_idx = 0
    c1_indices = [idx for idx, b in enumerate(raw_blocks) if b["chap_num"] == 1 and b["len"] > 800]
    if c1_indices:
        real_start_idx = c1_indices[-1]

    real_chapters = raw_blocks[real_start_idx:]
    intro_cutoff = real_chapters[0]["start"] if real_chapters else 0
    intro_content = content[:intro_cutoff].strip() if intro_cutoff > 0 else ""

    chapters = []
    if intro_content:
        chapters.append({
            "index": 0,
            "title": "📖 Lời Mở Đầu & Mục Lục Tác Phẩm",
            "content": intro_content
        })

    for idx, c in enumerate(real_chapters):
        chapters.append({
            "index": len(chapters) + 1,
            "title": c["title"],
            "content": c["content"]
        })

    return chapters if chapters else [{
        "index": 1,
        "title": "Toàn bộ tác phẩm",
        "content": content.strip()
    }]


def scan_and_load_books() -> List[Dict[str, Any]]:
    """Quét các thư mục sách và xây dựng danh mục sách có cấu trúc hoàn chỉnh."""
    books_map: Dict[str, Dict[str, Any]] = {}
    principles_map: Dict[str, str] = {}

    # Bước 1: Quét tất cả các file trong các thư mục sách
    for s_dir in BOOK_SEARCH_DIRS:
        if not os.path.exists(s_dir) or not os.path.isdir(s_dir):
            continue

        for fname in os.listdir(s_dir):
            if not fname.endswith(".md"):
                continue

            full_path = os.path.join(s_dir, fname)
            bid = sanitize_book_id(fname)

            if fname.lower().endswith("_principles.md"):
                if bid not in principles_map:
                    principles_map[bid] = full_path
                continue

            if bid not in books_map:
                books_map[bid] = {
                    "id": bid,
                    "filename": fname,
                    "full_path": full_path,
                }

    # Bước 2: Tải nội dung và phân tích chi tiết từng cuốn sách
    catalog: List[Dict[str, Any]] = []

    for bid, item in books_map.items():
        full_path = item["full_path"]
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                full_content = f.read()
        except Exception:
            continue

        # Đọc bản principles tương ứng nếu có
        principles_content = ""
        p_path = principles_map.get(bid)
        if p_path and os.path.exists(p_path):
            try:
                with open(p_path, "r", encoding="utf-8", errors="replace") as pf:
                    principles_content = pf.read()
            except Exception:
                pass

        # Lấy metadata
        meta = BOOK_METADATA_REGISTRY.get(bid, {})
        title = meta.get("title")
        if not title:
            h1_match = re.search(r"^#\s+([^\n]+)", full_content, re.MULTILINE)
            title = h1_match.group(1).strip() if h1_match else item["filename"].replace(".md", "").replace("_", " ")

        author = meta.get("author", "Tác giả Tinh hoa")
        category = meta.get("category", "Tư duy & Đầu tư")
        icon = meta.get("icon", "📖")
        summary = meta.get("summary", "")
        if not summary:
            # Lấy 2 dòng đầu có nghĩa
            lines = [l.strip() for l in full_content.splitlines() if l.strip() and not l.startswith("#")]
            summary = lines[0][:150] + "..." if lines else "Tài liệu tinh hoa."

        tags = meta.get("tags", ["Sách"])
        chapters = parse_chapters_from_markdown(full_content)
        size_bytes = os.path.getsize(full_path)
        size_kb = round(size_bytes / 1024, 1)

        catalog.append({
            "id": bid,
            "title": title,
            "author": author,
            "category": category,
            "icon": icon,
            "summary": summary,
            "tags": tags,
            "full_path": full_path,
            "principles_path": p_path,
            "full_content": full_content,
            "principles_content": principles_content,
            "chapters": chapters,
            "chapter_count": len(chapters),
            "size_kb": size_kb
        })

    # Sắp xếp sách theo thứ tự ưu tiên: Tâm lý trader lên đầu
    catalog.sort(key=lambda b: (0 if "tam_ly" in b["id"] else 1, b["title"]))
    return catalog


def ask_gemini_book_ai(book: Dict[str, Any], user_question: str, custom_api_key: Optional[str] = None) -> str:
    """Sử dụng Gemini AI để đàm đạo và giải đáp thắc mắc dựa trên tư tưởng và nguyên lý của cuốn sách."""
    keys = []
    if custom_api_key and custom_api_key.strip():
        keys.append(custom_api_key.strip())
    keys.extend(get_all_gemini_api_keys())

    if not keys:
        return "⚠️ Chưa cấu hình Gemini API Key. Vui lòng nhập API Key ở thanh bên (Sidebar) để kích hoạt Trợ lý Sách AI."

    # Xây dựng ngữ cảnh cô đọng từ bản principles và các chương liên quan
    context_text = book.get("principles_content", "")
    if not context_text:
        # Lấy tóm tắt 2 chương đầu
        context_text = book["full_content"][:4000]
    else:
        context_text = context_text[:5000]

    system_instruction = f"""Bạn là Trợ lý Tinh hoa đại diện cho tác phẩm '{book['title']}' của tác giả {book['author']}.
Phong cách của bạn: Sắc sảo, điềm tĩnh, bám sát các nguyên lý gốc (First Principles), không nói đãi bôi.

Dưới đây là BẢN NÉN NGUYÊN TẮC TINH HOA CỦA CUỐN SÁCH:
{context_text}

Nhiệm vụ của bạn:
1. Trả lời câu hỏi của người dùng dưới góc nhìn và tư tưởng cốt lõi của cuốn sách này.
2. Nêu rõ nguyên tắc, sự thật thị trường hoặc chương liên quan.
3. Đưa ra lời khuyên hành động thực chiến cụ thể (không sáo rỗng).
4. Định dạng Markdown đẹp, rõ ràng, có điểm nhấn.
"""

    prompt = f"Người dùng hỏi: \"{user_question}\"\n\nHãy giải đáp cặn kẽ dựa trên tư tưởng của cuốn sách."

    for key in keys:
        try:
            if hasattr(genai, "Client"):
                client = genai.Client(api_key=key)
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[prompt],
                    config={"system_instruction": system_instruction}
                )
                if response and hasattr(response, "text") and response.text:
                    return response.text
            else:
                genai.configure(api_key=key)
                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash",
                    system_instruction=system_instruction
                )
                resp = model.generate_content(prompt)
                if resp and resp.text:
                    return resp.text
        except Exception:
            continue

    return "⚠️ Đã thử các API keys nhưng gặp sự cố kết nối. Vui lòng thử lại sau ít giây hoặc kiểm tra khóa API."


# -----------------------------------------------------------------------------
# GIAO DIỆN PHÒNG ĐỌC SÁCH TINH HOA (ELITE BOOKSHELF ROOM)
# -----------------------------------------------------------------------------

def render_book_shelf_room(active_api_key: Optional[str] = None):
    """Render giao diện Tủ Sách Tinh Hoa (Elite Bookshelf)."""
    st.markdown("### 📖 Tủ Sách Tinh Hoa (Elite Bookshelf & Knowledge Vault)")
    st.caption("Kho tàng nguyên tác và bản nén nguyên lý thực chiến. Chuyển hóa sách dày hàng trăm trang thành phản xạ vô điều kiện 10 phút.")

    books = scan_and_load_books()
    if not books:
        st.warning("⚠️ Hiện chưa tìm thấy sách nào trong thư mục `book/`.")
        return

    # Bộ lọc danh mục và chọn sách
    categories = ["Tất cả thể loại"] + sorted(list(set(b["category"] for b in books)))
    
    col_filter, col_select = st.columns([1, 2])
    with col_filter:
        selected_cat = st.selectbox("Lọc theo thể loại:", categories, key="book_cat_filter")
    
    filtered_books = books if selected_cat == "Tất cả thể loại" else [b for b in books if b["category"] == selected_cat]

    book_options = {b["id"]: f"{b['icon']} {b['title']} — {b['author']} ({b['size_kb']} KB)" for b in filtered_books}

    with col_select:
        selected_bid = st.selectbox(
            "Chọn cuốn sách muốn đọc / nghiên cứu:",
            options=list(book_options.keys()),
            format_func=lambda x: book_options[x],
            key="book_selector_main"
        )

    current_book = next((b for b in filtered_books if b["id"] == selected_bid), filtered_books[0])

    # Card thông tin sách nổi bật
    st.markdown(f"""
    <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 12px; padding: 16px 20px; margin: 12px 0 20px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <h3 style="margin: 0; color: #f8fafc; font-size: 1.35rem;">{current_book['icon']} {current_book['title']}</h3>
                <p style="margin: 4px 0 8px 0; color: #818cf8; font-weight: 600;">✍️ Tác giả: {current_book['author']} | 📂 Thể loại: {current_book['category']} | 📑 Quy mô: {current_book['chapter_count']} chương ({current_book['size_kb']} KB)</p>
            </div>
        </div>
        <p style="margin: 0; color: #cbd5e1; font-size: 0.95rem; line-height: 1.5;">{current_book['summary']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 3 Tab điều hướng chính
    tab_principles, tab_reader, tab_ai = st.tabs([
        "⚡ 1. Bản Nén Nguyên Tắc (Core Principles & Mindset)",
        "📚 2. Toàn Văn Tác Phẩm Theo Chương (Full Reader)",
        "🤖 3. Trợ Lý Đàm Đạo Với Sách (Ask This Book AI)"
    ])

    # ---------------------------------------------------------
    # TAB 1: BẢN NÉN NGUYÊN TẮC TINH HOA
    # ---------------------------------------------------------
    with tab_principles:
        if current_book.get("principles_content"):
            c_p_left, c_p_right = st.columns([3, 1])
            with c_p_left:
                st.markdown(f"**⚡ Bản nén theo phương pháp Kỷ lục gia Guinness Dave Farrow — Đọc & Khắc sâu trong 5-10 phút**")
            with c_p_right:
                st.download_button(
                    label="📥 Tải Bản Nén (.md)",
                    data=current_book["principles_content"],
                    file_name=f"{current_book['id']}_principles.md",
                    mime="text/markdown",
                    key=f"dl_prin_{current_book['id']}"
                )

            st.markdown(current_book["principles_content"])
        else:
            st.info(f"Cuốn sách này hiện chưa có file nguyên tắc độc lập `{current_book['id']}_principles.md`.")
            st.markdown("Bạn có thể sang Tab **⚡ Máy Ép Farrow 1-Click** hoặc sử dụng Tab **Trợ Lý Đàm Đạo AI** để đúc kết bộ nguyên tắc 10 phút.")

    # ---------------------------------------------------------
    # TAB 2: TOÀN VĂN THEO CHƯƠNG (FULL READER)
    # ---------------------------------------------------------
    with tab_reader:
        chapters = current_book.get("chapters", [])
        
        # Thanh công cụ: Chọn chương, tìm kiếm, tải toàn văn
        col_c_sel, col_c_search, col_c_dl = st.columns([2, 2, 1])
        
        with col_c_sel:
            chap_titles = [f"{c['title']}" for c in chapters]
            selected_chap_idx = st.selectbox(
                "📑 Chọn chương để đọc:",
                range(len(chapters)),
                format_func=lambda i: chap_titles[i],
                key=f"chap_select_{current_book['id']}"
            )
            
        with col_c_search:
            search_query = st.text_input("🔍 Tìm kiếm từ khóa trong sách:", "", key=f"search_book_{current_book['id']}")

        with col_c_dl:
            st.write("")
            st.download_button(
                label="📥 Tải File Full (.md)",
                data=current_book["full_content"],
                file_name=current_book["filename"],
                mime="text/markdown",
                key=f"dl_full_{current_book['id']}"
            )

        # Xử lý tìm kiếm nếu người dùng nhập từ khóa
        if search_query.strip():
            kw = search_query.strip().lower()
            matching_chapters = []
            for c in chapters:
                if kw in c["content"].lower():
                    # Đếm số lần xuất hiện
                    count = c["content"].lower().count(kw)
                    matching_chapters.append((c, count))

            if matching_chapters:
                st.success(f"🔍 Tìm thấy `{len(matching_chapters)}` chương có chứa từ khóa **'{search_query}'**:")
                for m_c, cnt in matching_chapters:
                    with st.expander(f"📌 {m_c['title']} (xuất hiện {cnt} lần)"):
                        st.markdown(m_c["content"])
                st.divider()
            else:
                st.warning(f"Không tìm thấy từ khóa '{search_query}' trong sách.")

        # Hiển thị chương đang chọn
        current_chapter = chapters[selected_chap_idx]
        
        # Nút điều hướng Trước / Sau
        col_prev, col_center, col_next = st.columns([1, 2, 1])
        with col_prev:
            if selected_chap_idx > 0:
                if st.button("⬅️ Chương trước", key=f"btn_prev_{current_book['id']}"):
                    st.session_state[f"chap_select_{current_book['id']}"] = selected_chap_idx - 1
                    st.rerun()
        with col_center:
            st.caption(f"<div style='text-align: center; color: #94a3b8;'>Đang đọc chương {selected_chap_idx + 1} / {len(chapters)}</div>", unsafe_allow_html=True)
        with col_next:
            if selected_chap_idx < len(chapters) - 1:
                if st.button("Chương tiếp ➡️", key=f"btn_next_{current_book['id']}"):
                    st.session_state[f"chap_select_{current_book['id']}"] = selected_chap_idx + 1
                    st.rerun()

        st.markdown(f"### {current_chapter['title']}")
        st.markdown(current_chapter["content"])

    # ---------------------------------------------------------
    # TAB 3: TRỢ LÝ ĐÀM ĐẠO VỚI SÁCH (ASK THIS BOOK AI)
    # ---------------------------------------------------------
    with tab_ai:
        st.markdown("#### 🤖 Đối Thoại Trực Tiếp Với Tư Tưởng Của Sách")
        st.caption(f"Trợ lý AI nhập vai tác giả **{current_book['author']}**, phân tích mọi nan đề tâm lý và quyết định thực chiến dựa trên nguyên tắc của cuốn sách.")

        # Chip gợi ý câu hỏi mẫu thông minh theo từng sách
        sample_prompts = []
        if "tam_ly" in current_book["id"]:
            sample_prompts = [
                "Tôi vừa dính 3 lệnh Stop Loss liên tiếp và đang rất ức chế muốn vào lệnh gỡ gạc, Mark Douglas khuyên gì?",
                "Giải thích cặn kẽ 5 sự thật thị trường và cách áp dụng vào việc loại bỏ nỗi sợ hãi?",
                "Làm sao để thực sự chấp nhận rủi ro hoàn toàn thay vì chỉ đặt Stop Loss trên danh nghĩa?",
                "Thế nào là trạng thái The Zone và 3 cấp độ phát triển của một Trader chuyên nghiệp?"
            ]
        elif "bus" in current_book["id"] or "ngu_ngon" in current_book["id"]:
            sample_prompts = [
                "Thanh khoản là bình xăng của Lão Sói nghĩa là gì?",
                "Tại sao chú gà nhỏ không nên cắm cọc Stop Loss ở các điểm Equal Highs/Lows?",
                "Chi phí cơ hội và Thần Nắng USD ảnh hưởng đến giá Vàng ra sao?"
            ]
        else:
            sample_prompts = [
                "Tóm tắt 3 hạt nhân quan trọng nhất của cuốn sách này?",
                "Nguyên tắc nào trong sách có thể áp dụng ngay hôm nay để có đòn bẩy lớn nhất?",
                "Sai lầm phổ biến nhất của người mới khi tiếp cận tư tưởng này là gì?"
            ]

        st.markdown("**💡 Câu hỏi mẫu bạn có thể hỏi ngay:**")
        cols_prompt = st.columns(len(sample_prompts))
        for idx, prompt_text in enumerate(sample_prompts):
            with cols_prompt[idx]:
                if st.button(f"👉 {prompt_text[:35]}...", key=f"chip_q_{current_book['id']}_{idx}", help=prompt_text):
                    st.session_state[f"input_q_{current_book['id']}"] = prompt_text

        default_val = st.session_state.get(f"input_q_{current_book['id']}", "")
        user_q = st.text_area(
            "Nhập nan đề hoặc câu hỏi của bạn:",
            value=default_val,
            height=90,
            placeholder="Ví dụ: Khi thị trường biến động dữ dội và nến giật liên tục, tâm lý tôi cần neo vào đâu?",
            key=f"text_q_{current_book['id']}"
        )

        if st.button("🚀 Gửi Câu Hỏi Cho Sách", type="primary", key=f"btn_ask_{current_book['id']}"):
            if not user_q.strip():
                st.warning("Vui lòng nhập câu hỏi trước khi bấm gửi.")
            else:
                with st.spinner(f"Đang đàm đạo cùng tác giả {current_book['author']} qua lăng kính nguyên lý..."):
                    answer = ask_gemini_book_ai(current_book, user_q.strip(), active_api_key)
                    st.markdown("---")
                    st.markdown(f"#### 🎙️ Trả lời từ tác giả {current_book['author']}:")
                    st.markdown(answer)
