# -*- coding: utf-8 -*-
"""
Bộ Xử Lý Ma Trận Mô Hình & Nguyên Lý Tinh Hoa (Unified Farrow Latticework Engine)
Hợp nhất 88 Mô hình & 100 Nguyên lý về 3 Trụ Cột Farrow:
1. 🚪 SOI GỐC (First Principles, Bảo Toàn & Ranh Giới)
2. 🖥️ ĐỌC DÒNG (Dòng Chảy, Xác Suất, Hệ Thống & Động Lực)
3. 🪑 RA ĐÒN (Đòn Bẩy Bất Đối Xứng, Xúc Tác & Điểm Tựa)
"""

import json
import os
import random
from typing import Dict, List, Any, Optional

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
UNIFIED_FILE = os.path.join(DATA_DIR, "unified_farrow_models.json")


def load_unified_farrow_catalog() -> List[Dict[str, Any]]:
    """Tải toàn bộ danh mục mô hình & nguyên lý tinh hoa đã làm sạch và hợp nhất."""
    if os.path.exists(UNIFIED_FILE):
        try:
            with open(UNIFIED_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("catalog", [])
        except Exception:
            pass

    # Fallback to core_mental_models.json if unified file is missing
    fallback_path = os.path.join(DATA_DIR, "core_mental_models.json")
    if os.path.exists(fallback_path):
        try:
            with open(fallback_path, "r", encoding="utf-8") as f:
                return json.load(f).get("models", [])
        except Exception:
            pass
    return []


def get_farrow_models_grouped() -> Dict[str, List[Dict[str, Any]]]:
    """Gom nhóm danh mục tinh hoa vào 3 Trụ Cột Farrow: root, flow, strike."""
    catalog = load_unified_farrow_catalog()
    grouped = {"root": [], "flow": [], "strike": []}
    for item in catalog:
        pillar = item.get("farrow_pillar", "root")
        if pillar not in grouped:
            pillar = "root"
        grouped[pillar].append(item)
    return grouped


def get_farrow_metrics() -> Dict[str, Any]:
    """Trả về các chỉ số thống kê tổng quan của ma trận tinh hoa."""
    catalog = load_unified_farrow_catalog()
    grouped = get_farrow_models_grouped()
    tier1 = [x for x in catalog if x.get("tier") == 1]
    return {
        "total": len(catalog),
        "tier1_count": len(tier1),
        "root_count": len(grouped["root"]),
        "flow_count": len(grouped["flow"]),
        "strike_count": len(grouped["strike"]),
    }


def draw_random_farrow_sprint_trio() -> List[Dict[str, Any]]:
    """Rút ngẫu nhiên 3 thẻ: 1 thẻ Soi Gốc, 1 thẻ Đọc Dòng, 1 thẻ Ra Đòn cho phiên 10 phút."""
    grouped = get_farrow_models_grouped()
    trio = []
    for k in ["root", "flow", "strike"]:
        pool = grouped[k]
        if pool:
            # Ưu tiên rút thẻ Tier 1 nếu có
            tier1_pool = [m for m in pool if m.get("tier") == 1]
            chosen = random.choice(tier1_pool if tier1_pool else pool)
            trio.append(chosen)
    return trio


# Backward compatibility aliases
def load_all_mental_models() -> List[Dict[str, Any]]:
    return load_unified_farrow_catalog()


def load_all_principles() -> List[Dict[str, Any]]:
    catalog = load_unified_farrow_catalog()
    return [x for x in catalog if x.get("source") in ["scientific_principle", "merged"]]


def get_farrow_principles_grouped() -> Dict[str, List[Dict[str, Any]]]:
    return get_farrow_models_grouped()
