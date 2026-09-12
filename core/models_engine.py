# -*- coding: utf-8 -*-
"""
Bộ Xử Lý 88 Mô Hình & 100 Nguyên Lý theo Chuẩn Farrow (Models & Principles Engine)
Phân loại toàn bộ về 3 Ngăn Kéo Farrow: SOI GỐC -> ĐỌC DÒNG -> RA ĐÒN.
"""

import json
import os
import random
from typing import Dict, List, Any, Optional

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

def load_all_mental_models() -> List[Dict[str, Any]]:
    path = os.path.join(DATA_DIR, "core_mental_models.json")
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("models", [])
    except Exception:
        return []

def load_all_principles() -> List[Dict[str, Any]]:
    path = os.path.join(DATA_DIR, "knowledge_base.json")
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("principles", [])
    except Exception:
        return []

def classify_to_farrow_pillar(item: Dict[str, Any], is_principle: bool = False) -> str:
    """
    Phân loại một mô hình hoặc nguyên lý vào 1 trong 3 Trụ Cột Farrow:
    - root: Soi Gốc (Chân lý vật lý, bảo toàn, đảo ngược, ranh giới)
    - flow: Đọc Dòng (Xác suất, phản ứng dây chuyền, động lực, tiến hóa)
    - strike: Ra Đòn (Đòn bẩy, xúc tác, năng lượng hoạt hóa, bất đối xứng)
    """
    text = ""
    if is_principle:
        text = (
            str(item.get("principle_name", "")) + " " +
            str(item.get("domain", "")) + " " +
            str(item.get("intuitive_summary", "")) + " " +
            str(item.get("description", ""))
        ).lower()
    else:
        text = (
            str(item.get("name_vi", "")) + " " +
            str(item.get("name_en", "")) + " " +
            str(item.get("pillar", "")) + " " +
            str(item.get("first_principle", "")) + " " +
            str(item.get("trigger_question", ""))
        ).lower()

    # Rule-based heuristics
    strike_keywords = ["đòn bẩy", "leverage", "xúc tác", "hoạt hóa", "action", "asymmetric", "bất đối xứng", "tùy chọn", "barbell", "lò xo", "chạm ngưỡng", "tích lũy", "tăng tốc", "hooke", "quy mô", "scale"]
    flow_keywords = ["xác suất", "bayes", "dòng", "cân bằng", "tiến hóa", "feedback", "vòng lặp", "trò chơi", "game theory", "nash", "chu kỳ", "động lực", "mạng lưới", "le chatelier", "entropy", "chaos"]
    
    if any(k in text for k in strike_keywords):
        return "strike"
    elif any(k in text for k in flow_keywords):
        return "flow"
    else:
        return "root"

def get_farrow_models_grouped() -> Dict[str, List[Dict[str, Any]]]:
    """Gom nhóm 88 mô hình vào 3 Trụ Cột Farrow."""
    models = load_all_mental_models()
    grouped = {"root": [], "flow": [], "strike": []}
    for m in models:
        pillar = classify_to_farrow_pillar(m, is_principle=False)
        m_copy = dict(m)
        m_copy["farrow_pillar"] = pillar
        grouped[pillar].append(m_copy)
    return grouped

def get_farrow_principles_grouped() -> Dict[str, List[Dict[str, Any]]]:
    """Gom nhóm 100 nguyên lý vào 3 Trụ Cột Farrow."""
    principles = load_all_principles()
    grouped = {"root": [], "flow": [], "strike": []}
    for p in principles:
        pillar = classify_to_farrow_pillar(p, is_principle=True)
        p_copy = dict(p)
        p_copy["farrow_pillar"] = pillar
        grouped[pillar].append(p_copy)
    return grouped

def draw_random_farrow_sprint_trio() -> List[Dict[str, Any]]:
    """Rút ngẫu nhiên 3 thẻ: 1 thẻ Soi Gốc, 1 thẻ Đọc Dòng, 1 thẻ Ra Đòn để làm phiên 10 phút."""
    models_g = get_farrow_models_grouped()
    trio = []
    for k in ["root", "flow", "strike"]:
        pool = models_g[k]
        if pool:
            # Ưu tiên Tier 1 nếu có
            tier1_pool = [m for m in pool if m.get("tier") == 1]
            chosen = random.choice(tier1_pool if tier1_pool else pool)
            trio.append(chosen)
    return trio
