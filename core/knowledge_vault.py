# -*- coding: utf-8 -*-
"""
Kho Tri Thức Nén Sẵn Chuẩn Dave Farrow (Pre-packaged Farrow Knowledge Vault)
Hợp nhất toàn bộ 152 Mô hình & Nguyên lý thành các chủ đề Lâu Đài Ký Ức chuyên sâu.
Mỗi chủ đề tuân thủ nghiêm ngặt Quy tắc số 3 (Rule of 3):
3 Khối hạt nhân + 3 Mỏ neo không gian (Memory Palace) + 3 Hình ảnh phi lý ghim não + Đấu trường 5s.
"""

from typing import Dict, List, Any

FARROW_TOPICS: Dict[str, Dict[str, Any]] = {
    # -------------------------------------------------------------------------
    # NHÓM 1: BỘ TƯ DUY NỀN TẢNG & THỰC CHIẾN
    # -------------------------------------------------------------------------
    "trinity_thinking": {
        "id": "trinity_thinking",
        "category": "👑 Tư Duy Hạt Nhân",
        "title": "Bộ 3 Tư Duy Tinh Hoa (The Farrow Trinity)",
        "icon": "🧠",
        "tagline": "Nén toàn bộ 9 chế độ tư duy và 88 mô hình Munger về 3 động tác sinh tử",
        "summary": "Mọi vĩ nhân từ Elon Musk, Charlie Munger đến Feynman hay Taleb đều chỉ vận hành theo chu trình 3 nhịp: Soi Gốc -> Đọc Dòng -> Ra Đòn.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: SOI GỐC (ROOT)",
                "sub_modes": "First Principles + Inversion + Latticework",
                "principle": "Đập vụn mọi giả định về chân lý vật lý không thể chối cãi. Luôn lộn ngược để tìm ra cách chết chắc chắn rồi tránh xa.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Một chiếc máy ép thủy lực khổng lồ ngay trước cửa đang nghiền nát cả núi sách thành một viên kim cương phát sáng, trên đỉnh có con dơi đeo kính lúp X-Quang soi ngược!",
                "trigger_question": "Sự thật vật lý không thể suy diễn thêm ở đây là gì, và đâu là điều ngu xuẩn chết người cần tránh?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: ĐỌC DÒNG (FLOW)",
                "sub_modes": "Xác suất Bayes + Tư duy Bậc hai + Game Theory",
                "principle": "Mọi thứ luôn dịch chuyển. Cập nhật xác suất liên tục theo dữ liệu mới, đọc vị động cơ kẻ khác và nhìn trước nước cờ bậc 2.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình bốc cháy sấm sét dữ dội! Trên đó một bàn cờ vua đang tự động chạy, mỗi quân cờ gắn một radar phát hiện bẫy trước 3 bước đi!",
                "trigger_question": "Kẻ khác đang có động cơ gì để bẫy tôi, và 'sau đó thì điều gì sẽ xảy ra tiếp theo'?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: RA ĐÒN (STRIKE)",
                "sub_modes": "Optionality (Barbell) + Thực nghiệm Lean + Đa quy mô thời gian",
                "principle": "Cắt lỗ 1 cọng lông, ăn dày 3 bát thóc. Thử sai cực nhỏ hôm nay để nắm bắt cơ hội bùng nổ trong tầm nhìn 10 năm.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một chú gà con mặc giáp titan bất hoại, tay đè chặt chiếc lò xo thép bị nén cong vòng, chuẩn bị bật phóng mũi tên trúng hồng tâm cách xa 10 năm!",
                "trigger_question": "Rủi ro tối đa chỉ là 1 cọng lông chứ? Nếu đúng, cơ hội này có đem lại lợi nhuận bất đối xứng không?"
            }
        ],
        "quiz": [
            {
                "question": "Khi đứng trước một bài toán đầu tư hoặc quyết định lớn bị bao vây bởi tin đồn, phản xạ đầu tiên của bạn là gì?",
                "options": [
                    "Bật chỉ báo kỹ thuật và nghe lời khuyên của chuyên gia đông đảo.",
                    "Đập vụn bài toán về nguyên lý gốc (Trụ 1: Soi Gốc) và tìm cách tự sát để né tránh.",
                    "Lập tức đặt cược hết vốn để không bỏ lỡ cơ hội."
                ],
                "correct_idx": 1,
                "explanation": "Đúng! Trụ 1 (Soi Gốc) yêu cầu bóc sạch mọi ý kiến cảm xúc, chỉ nhìn vào giới hạn vật lý và tư duy đảo ngược."
            },
            {
                "question": "Thấy thị trường tăng dựng đứng và đám đông hò reo mua vào, bạn kích hoạt tư duy nào?",
                "options": [
                    "Trụ 2 (Đọc Dòng): Hỏi 'Và rồi sao nữa?' - Động lực của kẻ tạo lập là gì? Có phải họ đang cần thanh khoản để xả hàng?",
                    "Nhảy vào mua ngay lập tức theo quán tính đám đông.",
                    "Chờ đợi 1 tháng sau xem chuyện gì xảy ra."
                ],
                "correct_idx": 0,
                "explanation": "Chính xác! Trụ 2 giúp bạn nhìn ra nước cờ bậc 2 và động cơ thực sự đằng sau sự hưng phấn của đám đông."
            }
        ]
    },

    "xau_gold_farrow": {
        "id": "xau_gold_farrow",
        "category": "👑 Tư Duy Hạt Nhân",
        "title": "Bản Chất & Vi Cấu Trúc Vàng (XAU/USD)",
        "icon": "🪙",
        "tagline": "Nén toàn bộ 59 trang nghiên cứu vi cấu trúc XAU vào 3 cơ chế động lực học thuần túy",
        "summary": "Bỏ hết chỉ báo vẽ bùa trên cát. Thị trường vàng chỉ là cuộc chiến vật lý giữa Lực cản, Khối lượng và Cây xăng thanh khoản.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: BẢN CHẤT ZERO CASH FLOW",
                "sub_modes": "Lãi suất thực Mỹ + Sức mua USD + Negative-sum Game",
                "principle": "Vàng không đẻ ra tiền, không cổ tức. Giá chỉ chạy theo Chi phí cơ hội (US Real Yields) và nỗi sợ USD mất giá. Mọi phân tích doanh nghiệp đều vô nghĩa.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Một thỏi vàng khổng lồ hình đầu lâu lạnh ngắt, không mọc ra một chiếc lá nào, đang bị Thần Nắng USD dùng tia laser thiêu đốt chi phí cơ hội!",
                "trigger_question": "Lãi suất thực của Mỹ đang tăng hay giảm? Chi phí cơ hội giữ vàng hiện tại là bao nhiêu?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: THANH KHOẢN LÀ NHIÊN LIỆU (SWEEP)",
                "sub_modes": "Equal Highs/Lows + Bồn chứa xăng + Sói săn mồi",
                "principle": "Giá không đi ngẫu nhiên. Giá luôn lao về nơi tập trung Stop Loss của đám đông (Equal Highs/Lows) để nạp xăng trước khi quay đầu thật sự.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Một chiếc xe bus 50 tấn do Lão Sói cầm lái đâm sầm vào một hàng rào cọc gỗ cắm cờ đỏ (Stop Loss đám gà), hút cạn xăng rồi bốc đầu quay ngoắt 180 độ!",
                "trigger_question": "Đám đông đang cắm cọc dừng lỗ ở đâu đông nhất? Sói đã quét cạn bồn xăng đó chưa?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: LỰC PHANH RÂU NẾN & LÒ XO NÉN",
                "sub_modes": "CVD Hấp thụ Limit Buy + Compression + Bất đối xứng Taleb",
                "principle": "CVD âm cực đại nhưng giá rút chân tạo râu dài = Smart Money nuốt trọn lực bán. Lò xo co thắt biên độ = Năng lượng sắp nổ bùng bằng nến Marubozu.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một chiếc lò xo thép bị ép chặt giữa 2 vách đá phát ra tiếng rít xé tai, mũi xe bus cắm xuống cát để lại vết lõm dài ngoằng rồi bị bật tung lên trời cao!",
                "trigger_question": "Có dấu hiệu hấp thụ rút chân khối lượng lớn không? Biên độ đã nén đến điểm cực hạn chưa?"
            }
        ],
        "quiz": [
            {
                "question": "Khi thấy giá Vàng cắm đầu lao dốc với khối lượng bán cực lớn, nhưng cây nến lại rút chân để lại râu nến dưới dài ngoằng, điều gì đang thực sự xảy ra?",
                "options": [
                    "Phe bán đang áp đảo hoàn toàn, chuẩn bị bán tháo tiếp.",
                    "Lực bán chủ động đã đâm sầm vào bức tường Limit Buy khổng lồ của Smart Money (Hấp thụ).",
                    "Chỉ báo RSI bị quá bán nên thị trường tự nhiên dừng lại."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Đó là quy luật vi cấu trúc: CVD âm cực lớn nhưng giá rút chân là bằng chứng Smart Money đang hứng trọn lệnh bán của đám đông."
            }
        ]
    },

    "feynman_rapid_mastery": {
        "id": "feynman_rapid_mastery",
        "category": "👑 Tư Duy Hạt Nhân",
        "title": "Kỹ Thuật Học Siêu Tốc (Feynman & Farrow Meta-Learning)",
        "icon": "⚡",
        "tagline": "Phương pháp bóc tách và chiếm lĩnh mọi lĩnh vực phức tạp trong 10 phút",
        "summary": "Không có khái niệm 'kiến thức khó', chỉ có những văn bản rườm rà chưa được nén đúng quy chuẩn sinh học của não bộ.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: BÓC TÁCH KHÔNG TỪ NGỮ HÀN LÂM",
                "sub_modes": "Feynman Technique + Phân biệt Biết Tên vs Hiểu Bản Chất",
                "principle": "Nếu bạn không thể giải thích cho một đứa trẻ 10 tuổi hiểu bằng ví dụ đời thường, bạn chưa hiểu nó. Bỏ hết thuật ngữ cao siêu che giấu sự dốt nát.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Giáo sư Feynman đang cầm kéo cắt vụn một chiếc áo choàng tiến sĩ lộng lẫy, để lộ bên trong là một đứa trẻ 10 tuổi đang chơi xếp hình lego!",
                "trigger_question": "Nếu phải giải thích điều này cho một đứa trẻ 10 tuổi mà không dùng từ chuyên môn, tôi sẽ nói gì?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: QUY TẮC SỐ 3 & MỎ NEO KHÔNG GIAN",
                "sub_modes": "Dave Farrow Rule of 3 + Memory Palace + Absurd Imagery",
                "principle": "Não chỉ nhớ tối đa 3 khối thông tin cùng lúc. Hãy ghim chúng vào 3 đồ vật quen thuộc bằng hình ảnh quái dị, phi lý gấp 10 lần thực tế.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Dave Farrow đang cầm 3 củ khoai tây phát sáng ghim thẳng vào trán mình, mắt phóng ra 3 tia chớp xanh lét cắm vào 3 góc phòng!",
                "trigger_question": "3 hạt nhân cốt lõi nhất ở đây là gì, và chúng gắn vào đồ vật nào trong phòng tôi?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: ÉP XUNG 10 PHÚT & THỞ BỤNG SẠC PIN",
                "sub_modes": "10-Min Sprint + Xả Cortisol + Sóng não Alpha",
                "principle": "Học nhanh trong 10 phút rồi dừng lại thở bụng sâu 1 phút. Não là cục pin nhỏ, đừng ép nó chạy dồn 2 tiếng mà không sạc điện.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một quả đồng hồ cát bốc cháy ngùn ngụt đếm ngược 10 phút, cạnh đó một lá phổi silicon khổng lồ đang phập phồng bơm bọt khí oxy lấp lánh vào chiếc ghế!",
                "trigger_question": "Tôi đã chạy hết tốc lực 10 phút chưa? Đã đến lúc buông bàn phím và hít thở sâu bằng bụng chưa?"
            }
        ],
        "quiz": [
            {
                "question": "Tại sao Dave Farrow yêu cầu bạn phải tưởng tượng hình ảnh kỳ quặc, phi lý thay vì hình ảnh đời thường?",
                "options": [
                    "Vì để giải trí cho đỡ buồn ngủ.",
                    "Vì cơ chế tiến hóa của não bộ: Những thứ bình thường sẽ bị bộ lọc não xóa đi trong 24h, chỉ những dị biệt gây sốc mới được đóng đinh vào ký ức dài hạn.",
                    "Vì hình ảnh kỳ quặc tốn ít calo hơn."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Tiến hóa dạy não rằng điều bình thường là an toàn (không cần nhớ), còn dị biệt bất thường là sinh tử (bắt buộc phải nhớ)."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # NHÓM 2: VẬT LÝ HỌC TINH HOA (2 PHẦN)
    # -------------------------------------------------------------------------
    "physics_core_1": {
        "id": "physics_core_1",
        "category": "⚛️ Vật Lý Học",
        "title": "Vật Lý Tinh Hoa 1: Bảo Toàn, Quán Tính & Đòn Bẩy",
        "icon": "⚖️",
        "tagline": "Nén toàn bộ cơ học cổ điển về 3 nguyên lý gốc: Bảo toàn -> Lực cản -> Điểm tựa",
        "summary": "Tổng hợp các định luật Newton, bảo toàn năng lượng, quán tính, ma sát và đòn bẩy Acsimet. Không ai có thể phá vỡ định luật vật lý.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: BẢO TOÀN NĂNG LƯỢNG & KHỐI LƯỢNG",
                "sub_modes": "Định luật 1 Newton (Quán tính) + Bảo toàn Năng lượng Lavoisier + Khối lượng tới hạn",
                "principle": "Năng lượng không tự sinh ra cũng không tự mất đi. Một vật đứng yên hoặc đang lao dốc sẽ tiếp tục trạng thái đó nếu không có ngoại lực tác động.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Một tảng thiên thạch 100 tấn đang đứng im chắn ngang cửa, đẩy cật lực không nhúc nhích, trên thân gắn cân đo năng lượng không hao hụt 1 miligram!",
                "trigger_question": "Hệ thống này có đang vi phạm bảo toàn năng lượng (bánh vẽ làm giàu không tốn công) không? Quán tính của nó đang kéo về đâu?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: MA SÁT, ĐỘ NHỚT & VẬN TỐC THOÁT",
                "sub_modes": "Ma sát lăn/trượt + Lực cản môi trường + Escape Velocity",
                "principle": "Mọi chuyển động đều sinh nhiệt và bị ma sát cắn xé. Để thoát khỏi trọng trường cũ cần một gia tốc cực đại trong thời gian ngắn, nửa vời sẽ bị hút rơi lại.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình biến thành một đầm lầy hắc ín sôi sùng sục, một tên lửa vũ trụ đang phụt lửa rực rỡ để bứt phá khỏi lực hút của đầm lầy!",
                "trigger_question": "Lực cản ma sát vô hình ở đây là gì? Ta có đủ lực đẩy để đạt vận tốc thoát ly hoàn toàn hay sẽ rơi lại đáy vực?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: ĐÒN BẨY ACSIMET & CỘNG HƯỞNG",
                "sub_modes": "Nguyên lý đòn bẩy + Cánh tay đòn + Tần số cộng hưởng cưỡng bức",
                "principle": "Cho tôi một điểm tựa, tôi sẽ nhấc bổng quả đất. Tác động nhỏ nhưng đúng tần số dao động riêng sẽ làm sập cả cây cầu nghìn tấn.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Acsimet râu tóc bạc phơ đang ngồi trên chiếc ghế, dùng một thanh sắt dài 1 cây số bẩy tung cả tòa nhà chọc trời chỉ bằng 1 ngón tay út!",
                "trigger_question": "Điểm tựa vững chắc ở đâu? Cánh tay đòn đã đủ dài để tạo lợi thế bất đối xứng cực đại chưa?"
            }
        ],
        "quiz": [
            {
                "question": "Khi khởi nghiệp hoặc chuyển nghề, tại sao hầu hết mọi người thất bại ở giai đoạn đầu?",
                "options": [
                    "Vì họ thiếu may mắn.",
                    "Vì không đạt được 'Vận tốc thoát' (Escape Velocity), bị lực cản ma sát và thói quen cũ hút ngược trở lại mặt đất.",
                    "Vì họ không có bằng cấp cao."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Nửa vời không tạo đủ gia tốc thoát ly trọng trường cũ, dẫn đến việc bị ma sát nuốt chửng năng lượng."
            }
        ]
    },

    "physics_core_2": {
        "id": "physics_core_2",
        "category": "⚛️ Vật Lý Học",
        "title": "Vật Lý Tinh Hoa 2: Nhiệt Động Lực, Sóng & Chuyển Pha",
        "icon": "🔥",
        "tagline": "Nén vũ trụ năng lượng vào 3 quy luật: Entropy tăng -> Cân bằng nhiệt -> Bùng nổ chuyển pha",
        "summary": "Tổng hợp Định luật 2 Nhiệt động học (Entropy), cân bằng nhiệt, hiệu ứng Doppler, khúc xạ ánh sáng và bước nhảy chuyển pha.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: ENTROPY & QUY LUẬT HỖN LOẠN TẤT YẾU",
                "sub_modes": "Định luật 2 Nhiệt động học + Độ không tuyệt đối + Tán xạ nhiệt",
                "principle": "Nếu không bơm năng lượng và bảo dưỡng liên tục, mọi hệ thống (phòng ốc, doanh nghiệp, cơ thể) đều tất yếu suy thoái về trạng thái hỗn loạn và sụp đổ.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Cánh cửa phòng đang tự vỡ vụn thành cát bụi gỉ sét, một ly trà nóng tự nguội ngắt đóng băng, báo hiệu sự suy kiệt năng lượng không thể đảo ngược!",
                "trigger_question": "Hệ thống này đang phải trả bao nhiêu chi phí năng lượng để chống lại Entropy? Nếu buông tay 1 tuần thì chuyện gì sẽ nát vụn?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: DÒNG CHẢY CÂN BẰNG & SÓNG NĂNG LƯỢNG",
                "sub_modes": "Gradient nhiệt/áp suất + Hiệu ứng Doppler + Cân bằng nhiệt động",
                "principle": "Năng lượng luôn chảy từ nơi thế năng cao về nơi thế năng thấp. Người đứng yên nghe tiếng còi tàu thay đổi tần số vì sự chuyển động tương đối của nguồn phát.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình chia làm hai nửa: một bên dung nham đỏ rực đang ồ ạt chảy sang bên băng tuyết xanh lè, kèm theo tiếng còi tàu hú réo chói tai biến điệu!",
                "trigger_question": "Dòng chênh lệch thế năng (giá cả, thông tin, quyền lực) đang chảy theo hướng nào? Tôi đang đứng ngược chiều hay thuận chiều sóng?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: CHUYỂN PHA ĐỘT BIẾN TẠI 100°C",
                "sub_modes": "Phase Transition + Nhiệt dung tiềm ẩn + Chạm ngưỡng lượng đổi chất đổi",
                "principle": "Ở 99°C nước vẫn là chất lỏng tĩnh lặng. Chỉ cần thêm đúng 1°C, toàn bộ hệ thống bùng nổ chuyển pha thành hơi nước mang năng lượng kéo đoàn tàu.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Chiếc ghế đang làm bằng băng đá trong suốt bỗng phát nổ 'BÙM' một phát thành quả cầu lửa hơi nước cuồn cuộn thổi tung trần nhà!",
                "trigger_question": "Tôi đang ở phút thứ 99 hay đã chạm ngưỡng 100°C? Đâu là giọt nước cuối cùng làm thay đổi hoàn toàn tính chất cuộc chơi?"
            }
        ],
        "quiz": [
            {
                "question": "Một tổ chức không đặt ra quy trình dọn dẹp và kỷ luật thì điều gì xảy ra sau 6 tháng?",
                "options": [
                    "Tổ chức vẫn vận hành bình thường vì con người có ý thức.",
                    "Theo Định luật 2 Nhiệt động học (Entropy), tổ chức sẽ tự động thoái hóa thành mớ hỗn độn, quan liêu và tê liệt.",
                    "Tổ chức sẽ tự động tiến hóa lên bậc cao hơn."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Entropy quy định trật tự đòi hỏi năng lượng bảo trì liên tục. Thiếu năng lượng, hệ thống mặc định rơi vào hỗn loạn."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # NHÓM 3: SINH HỌC & TIẾN HÓA
    # -------------------------------------------------------------------------
    "biology_evolution": {
        "id": "biology_evolution",
        "category": "🧬 Sinh Học & Tiến Hóa",
        "title": "Sinh Học Tinh Hoa: Chọn Lọc, Thích Nghi & Đột Biến",
        "icon": "🧬",
        "tagline": "Nén 4 tỷ năm tiến hóa sự sống vào 3 cơ chế sinh tồn tàn khốc",
        "summary": "Hợp nhất Chọn lọc tự nhiên Darwin, Hốc sinh thái, Hiệu ứng Nữ hoàng Đỏ, Cân bằng nội môi (Homeostasis) và Đột biến di truyền.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: HỐC SINH THÁI & CÂN BẰNG NỘI MÔI",
                "sub_modes": "Niche Specialization + Homeostasis + Sức chứa môi trường (Carrying Capacity)",
                "principle": "Muốn sống sót, hãy chiếm một hốc sinh thái riêng biệt mà đối thủ không thể với tới. Cơ thể liên tục tự điều chỉnh để giữ trạng thái sinh hóa cân bằng nội bộ.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Một chú gấu túi Koala chỉ ăn duy nhất một loại lá bạch đàn độc chắn cửa, trên ngực đeo chiếc máy điều hòa thân nhiệt luôn giữ chuẩn 37°C!",
                "trigger_question": "Hốc sinh thái độc quyền của tôi là gì? Tôi đang bảo vệ trạng thái cân bằng nội môi trước biến động bên ngoài bằng cơ chế nào?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: CUỘC ĐUA NỮ HOÀNG ĐỎ & CHỌN LỌC TỰ NHIÊN",
                "sub_modes": "Red Queen Effect + Áp lực chọn lọc + Đồng tiến hóa (Co-evolution)",
                "principle": "Trong thế giới này, bạn phải chạy cật lực chỉ để đứng yên một chỗ. Kẻ sống sót không phải kẻ mạnh nhất hay thông minh nhất, mà là kẻ thích nghi nhanh nhất.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Bà Hoàng Hậu Đỏ trong Alice ở Xứ Thần Tiên đang kéo tay một con báo gấm chạy bở hơi tai trên máy chạy bộ bốc khói để không bị tụt lại phía sau!",
                "trigger_question": "Đối thủ và môi trường đang tiến hóa thế nào? Nếu tôi duy trì kỹ năng cũ thêm 1 năm nữa, tôi có trở thành hóa thạch khủng long không?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: ĐỘT BIẾN NGẪU NHIÊN & TÙY CHỌN DỊ BIỆT",
                "sub_modes": "Random Mutation + Bắt chước sinh học (Biomimicry) + Đa dạng sinh thái",
                "principle": "99% đột biến là vô dụng hoặc có hại, nhưng 1% đột biến thích hợp sẽ cứu cả giống loài khi thảm họa xảy ra. Không đa dạng dị biệt là tự sát.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một chú tắc kè hoa ngồi trên ghế, da biến đổi 7 màu liên tục, bỗng mọc thêm đôi cánh dơi bay vút lên trời né con trăn khổng lồ dưới đất!",
                "trigger_question": "Tôi có đang duy trì 10-20% thử nghiệm 'đột biến ngẫu nhiên' để đón đầu biến cố lớn, hay đang đồng nhất một màu chờ chết?"
            }
        ],
        "quiz": [
            {
                "question": "Hiệu ứng Nữ hoàng Đỏ (Red Queen Effect) trong kinh doanh và sự nghiệp cảnh báo điều gì?",
                "options": [
                    "Chỉ cần trở thành số 1 là có thể an tâm nghỉ ngơi cả đời.",
                    "Thị trường và đối thủ không ngừng tiến hóa; nếu bạn ngừng học hỏi và cải tiến, bạn đang thụt lùi và tiến thẳng tới tuyệt chủng.",
                    "Cạnh tranh là điều không cần thiết trong thế giới phẳng."
                ],
                "correct_idx": 1,
                "explanation": "Đúng! Giống như trong Alice ở Xứ Thần Tiên: 'Muốn giữ nguyên vị trí, ngươi phải chạy hết sức có thể'."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # NHÓM 4: TOÁN HỌC & XÁC SUẤT THỰC CHIẾN
    # -------------------------------------------------------------------------
    "math_probability": {
        "id": "math_probability",
        "category": "🎲 Toán & Xác Suất",
        "title": "Toán Học & Xác Suất: Bayes, Lãi Kép & Kelly",
        "icon": "🎲",
        "tagline": "Nén khoa học định lượng vào 3 cỗ máy tư duy: Đảo ngược -> Cập nhật -> Tối ưu cược",
        "summary": "Tổng hợp Lãi kép, Phân phối Pareto 80/20, Xác suất Bayes, Phân phối Đuôi béo (Fat Tails), Giá trị kỳ vọng & Tiêu chuẩn Kelly.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: ĐẢO NGƯỢC XÁC SUẤT & PHÂN PHỐI ĐUÔI BÉO",
                "sub_modes": "Inversion Jacobi + Fat Tails vs Gaussian + Quy luật Số lớn",
                "principle": "Thay vì tìm cách trúng độc đắc, hãy tìm tất cả các cách để cháy tài khoản rồi loại bỏ chúng. Thế giới thực bị thống trị bởi các sự kiện thiên nga đen đuôi béo.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Nhà toán học Jacobi trồng cây chuối trước cửa, cầm chiếc gậy bóng chày đập nát một chú thiên nga đen bằng cao su đang ngậm quả bom nổ chậm!",
                "trigger_question": "Điều tồi tệ nhất có thể khiến tôi mất trắng ở đây là gì? Đuôi rủi ro cực hạn đã được khóa chặt chưa?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: CẬP NHẬT XÁC SUẤT BAYES THEO DỮ LIỆU MỚI",
                "sub_modes": "Bayesian Updating + Prior vs Posterior + Hồi quy về giá trị trung bình",
                "principle": "Đừng yêu giả thuyết của mình. Khi có bằng chứng khách quan mới, phải lập tức cập nhật xác suất tiên nghiệm (Prior) thành xác suất hậu nghiệm (Posterior).",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình hiển thị một chiếc cân điện tử siêu nhạy, mỗi khi một giọt nước dữ liệu mới rơi xuống đĩa cân, kim đo xác suất lập tức nhảy tanh tách!",
                "trigger_question": "Niềm tin ban đầu của tôi là bao nhiêu %? Dữ liệu thực tế mới xuất hiện này làm xác suất thành công tăng hay giảm?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: LÃI KÉP LŨY THỪA & TIÊU CHUẨN ĐẶT CƯỢC KELLY",
                "sub_modes": "Compound Interest + Pareto 80/20 + Kelly Criterion Size",
                "principle": "Lãi kép là kỳ quan thứ 8, đòi hỏi sự kiên nhẫn không ngắt quãng. Khi có lợi thế toán học dương (Edge), dùng công thức Kelly để tính tỷ lệ vốn tối ưu, không all-in ngu ngốc.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một đồng xu 1 đô la đặt trên ghế sau 10 giây bỗng sinh sôi nảy nở thành một núi vàng ngập phòng, bên cạnh có chiếc máy tính Kelly tự động khóa van cược 5%!",
                "trigger_question": "Kèo này có kỳ vọng toán học dương (EV > 0) không? Tôi có đang giữ tỷ lệ cược an toàn theo Kelly để sống sót cho lãi kép làm việc không?"
            }
        ],
        "quiz": [
            {
                "question": "Nhà đầu tư huyền thoại Warren Buffett coi nguyên tắc số 1 trong đầu tư là gì?",
                "options": [
                    "Phải kiếm được lợi nhuận 50% mỗi năm.",
                    "Không bao giờ để mất tiền (Tư duy Đảo ngược & Quản trị rủi ro sinh tử).",
                    "Luôn mua cổ phiếu của công ty lớn nhất thế giới."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Buffett: 'Nguyên tắc 1: Đừng để mất tiền. Nguyên tắc 2: Đừng bao giờ quên nguyên tắc 1'. Đây là đỉnh cao của tư duy đảo ngược."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # NHÓM 5: KINH TẾ HỌC & ĐẦU TƯ (2 PHẦN)
    # -------------------------------------------------------------------------
    "economics_core_1": {
        "id": "economics_core_1",
        "category": "📈 Kinh Tế & Đầu Tư",
        "title": "Kinh Tế Học 1: Cung Cầu, Động Lực & Chi Phí Cơ Hội",
        "icon": "📊",
        "tagline": "Nén kinh tế học vi mô vào 3 động lực vận hành hành vi nhân loại",
        "summary": "Quy luật Cung & Cầu, Chi phí cơ hội, Động lực khuyến khích (Incentives), Hiệu dụng biên giảm dần và Phá hủy sáng tạo Schumpeter.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: CHI PHÍ CƠ HỘI & HIỆU DỤNG BIÊN",
                "sub_modes": "Opportunity Cost + Diminishing Marginal Utility + Sunk Cost",
                "principle": "Chi phí thực sự của một thứ là những gì bạn phải từ bỏ để có được nó. Mỗi đơn vị tiêu thụ thêm đều mang lại sự thỏa mãn ít hơn đơn vị trước đó.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Trước cửa có hai ngã rẽ: một bên là túi vàng, một bên là đồng hồ thời gian đang trôi; bạn chỉ được chọn bước chân vào một bên và vĩnh viễn mất bên kia!",
                "trigger_question": "Nếu làm việc này, tôi đang phải từ bỏ cơ hội tốt nhất nào khác? Chi phí chìm có đang ám ảnh tôi không?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: QUY LUẬT CUNG CẦU & ĐỘNG LỰC TƯ LỢI",
                "sub_modes": "Supply & Demand Equilibrium + Munger Incentive Bias + Price Signal",
                "principle": "Hãy chỉ cho tôi động lực khen thưởng của một người, tôi sẽ chỉ cho bạn hành vi của họ. Giá cả chỉ là tín hiệu cân bằng giữa lòng tham và sự khan hiếm.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình chiếu cảnh một đàn khỉ đang điên cuồng chuyền tay nhau một quả chuối vàng duy nhất (Khan hiếm), giá quả chuối nhảy vọt lên mây xanh!",
                "trigger_question": "Cơ chế trả thưởng đang khuyến khích các bên làm điều gì? Nguồn cung đang thắt chặt hay đang bị ngập lụt?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: PHÁ HỦY SÁNG TẠO & LỢI THẾ SO SÁNH",
                "sub_modes": "Creative Destruction Schumpeter + Comparative Advantage + Specialization",
                "principle": "Cái mới ra đời tất yếu tiêu diệt cái cũ kém hiệu quả. Hãy chỉ tập trung vào việc bạn làm giỏi nhất với chi phí cơ hội thấp nhất và thuê ngoài phần còn lại.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một chiếc điện thoại iPhone phát ra sóng xung kích nghiền nát máy ảnh cơ, bản đồ giấy và đồng hồ báo thức trên bàn thành tro bụi!",
                "trigger_question": "Lợi thế so sánh vượt trội của tôi là gì? Công nghệ mới nào đang âm thầm phá hủy ngành nghề của tôi?"
            }
        ],
        "quiz": [
            {
                "question": "Charlie Munger từng nói câu châm ngôn nổi tiếng nào về Động lực (Incentives)?",
                "options": [
                    "Con người luôn làm việc vì tình yêu thương đồng loại.",
                    "Đừng bao giờ nghĩ về điều gì khác nếu bạn chưa nghĩ về sức mạnh của động lực khen thưởng (Incentives).",
                    "Tiền bạc không quan trọng bằng danh vọng."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Munger: 'Chỉ cho tôi động lực, tôi sẽ chỉ cho bạn kết quả. Hầu hết sai lầm tai hại đều do thiết kế sai cơ chế khen thưởng'."
            }
        ]
    },

    "economics_core_2": {
        "id": "economics_core_2",
        "category": "📈 Kinh Tế & Đầu Tư",
        "title": "Kinh Tế Học 2: Con Hào Moat, Hiệu Ứng Mạng & Quy Mô",
        "icon": "🏰",
        "tagline": "Nén chiến lược kinh doanh và phòng thủ lợi nhuận vào 3 pháo đài độc quyền",
        "summary": "Con hào kinh tế (Economic Moat), Hiệu ứng mạng lưới (Network Effects), Lợi thế kinh tế theo quy mô (Economies of Scale) & Chi phí chuyển đổi (Switching Costs).",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: CON HÀO KINH TẾ & CHI PHÍ CHUYỂN ĐỔI",
                "sub_modes": "Buffett Economic Moat + Switching Costs + Thương hiệu độc quyền",
                "principle": "Một lâu đài nguy nga không có hào nước sâu đầy cá sấu bảo vệ sẽ sớm bị đối thủ san phẳng. Khiến khách hàng rời bỏ bạn tốn quá nhiều đau đớn là con hào vĩ đại nhất.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Cửa phòng bị bao quanh bởi một con hào sâu hoắm chứa đầy cá sấu mạ vàng, cây cầu rút bị kéo lên chỉ có người có mã khóa đặc quyền mới bước qua được!",
                "trigger_question": "Doanh nghiệp hoặc bản thân tôi có 'con hào bảo vệ' nào mà đối thủ dù có 1 tỷ USD cũng không thể cướp được trong 3 năm?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: HIỆU ỨNG MẠNG LƯỚI TỰ TĂNG TRƯỞNG",
                "sub_modes": "Metcalfe Law + Network Effects + Flywheel feedback",
                "principle": "Mỗi người dùng mới tham gia đều làm tăng trực tiếp giá trị của mạng lưới cho tất cả những người dùng cũ. Giá trị mạng lưới tăng theo bình phương số nút kết nối.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình chiếu một mạng nhện kim cương phát sáng khổng lồ, mỗi con côn trùng dính vào lại làm mạng nhện sáng gấp 10 lần và hút thêm hàng ngàn con khác!",
                "trigger_question": "Mô hình này có hiệu ứng mạng hai chiều không? Càng nhiều người dùng thì sản phẩm có càng khó bị thay thế không?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: LỢI THẾ KINH TẾ THEO QUY MÔ & CHI PHÍ BIÊN = 0",
                "sub_modes": "Economies of Scale + Zero Marginal Cost + Tích hợp chuỗi giá trị",
                "principle": "Sản xuất càng lớn, chi phí cố định trên mỗi đơn vị sản phẩm càng tiệm cận về 0. Khi chi phí sao chép bằng 0, kẻ dẫn đầu sẽ nuốt trọn toàn bộ thị trường (Winner takes all).",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Một chiếc máy in 3D trên ghế đang tự động nhân bản 1 triệu cuốn sách trong 1 giây với chi phí điện chỉ bằng 1 đồng xu lẻ!",
                "trigger_question": "Sản phẩm của tôi có khả năng mở rộng quy mô với chi phí biên tiệm cận 0 không? Quy mô có đang hạ gục đối thủ cạnh tranh giá rẻ?"
            }
        ],
        "quiz": [
            {
                "question": "Tại sao Facebook hay Microsoft rất khó bị lật đổ dù có nhiều đối thủ tạo ra sản phẩm tương tự?",
                "options": [
                    "Vì họ có trụ sở to đẹp hơn.",
                    "Vì họ sở hữu Hiệu ứng mạng lưới khổng lồ và Chi phí chuyển đổi (Switching Costs) quá đau đớn đối với người dùng.",
                    "Vì chính phủ cấm đối thủ cạnh tranh."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Khi tất cả bạn bè và công việc của bạn đều ở trên một mạng lưới, chi phí chuyển đổi sang nền tảng khác gần như là bất khả thi."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # NHÓM 6: TÂM LÝ HỌC & BẪY NHẬN THỨC
    # -------------------------------------------------------------------------
    "psychology_biases": {
        "id": "psychology_biases",
        "category": "🎭 Tâm Lý & Nhận Thức",
        "title": "Tâm Lý Học: Bẫy Não, Mỏ Neo & Hiệu Ứng Lollapalooza",
        "icon": "🎭",
        "tagline": "Nén 25 thiên kiến nhận thức của Charlie Munger vào 3 cạm bẫy sinh tử",
        "summary": "Ác cảm mất mát (Loss Aversion), Thiên kiến xác nhận (Confirmation Bias), Bằng chứng xã hội (Social Proof), Mỏ neo (Anchoring) và Hiệu ứng cộng hưởng Lollapalooza.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: ÁC CẢM MẤT MÁT & BẪY MỎ NEO TÂM LÝ",
                "sub_modes": "Kahneman Loss Aversion + Anchoring Effect + Sunk Cost Bias",
                "principle": "Nỗi đau mất 100 đô la lớn gấp đôi niềm vui khi kiếm được 100 đô la. Não bộ vô thức bám chặt vào con số đầu tiên nhìn thấy và đưa ra quyết định sai lầm.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Một chiếc mỏ neo sắt hoen gỉ nặng 10 tấn thả cắm chặt vào chân bạn ngay cửa, bên cạnh là một người đang khóc ròng vì đánh rơi chiếc ví rỗng!",
                "trigger_question": "Tôi đang bám vào mức giá quá khứ (mỏ neo) nào? Quyết định này là do phân tích lý trí hay vì nỗi sợ cắt lỗ đau đớn?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: THIÊN KIẾN XÁC NHẬN & TÂM LÝ BẦY ĐÀN",
                "sub_modes": "Confirmation Bias + Social Proof + Chống bầy cừu Asch Experiment",
                "principle": "Não chỉ thích tìm kiếm thông tin củng cố niềm tin có sẵn và tự động lờ đi các sự thật trái chiều. Khi bối rối, con người sao chép hành vi của bầy đàn như những chú cừu.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình chiếu cảnh một đàn cừu đeo kính râm đen kịt đang mù quáng nhảy xuống vực thẳm, con nào cũng vừa nhảy vừa hô: 'Mọi người đều làm thế mà!'",
                "trigger_question": "Tôi có đang chủ động tìm kiếm các bằng chứng chứng minh mình SAI không? Tôi hành động vì logic hay vì đám đông đang hò reo?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: HIỆU ỨNG CỘNG HƯỞNG TÂM LÝ LOLLAPALOOZA",
                "sub_modes": "Munger Lollapalooza Tendency + Cam kết & Nhất quán + Uy quyền giả tạo",
                "principle": "Khi 3-4 thiên kiến tâm lý cùng xảy ra một lúc theo cùng một hướng, não người sẽ hoàn toàn tê liệt tư duy phản biện, dẫn đến những quyết định điên rồ cực đại.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Charlie Munger đang ngồi trên ghế chỉ tay vào một cơn lốc xoáy ngũ sắc Lollapalooza cuốn phăng cả sàn giao dịch chứng khoán đầy các con bạc đang say máu!",
                "trigger_question": "Có bao nhiêu thiên kiến tâm lý đang đồng thời tấn công tôi lúc này? Tôi đã dừng lại 24h để xả cơn say hưng phấn/hoảng loạn chưa?"
            }
        ],
        "quiz": [
            {
                "question": "Hiệu ứng Lollapalooza của Charlie Munger xảy ra khi nào?",
                "options": [
                    "Khi một người uống quá nhiều rượu.",
                    "Khi nhiều thiên kiến tâm lý (tham lam, sợ bỏ lỡ, nghe lời chuyên gia, bầy đàn) đồng thời hợp lực tác động, biến con người thành cỗ máy phi lý trí tột độ.",
                    "Khi thị trường chứng khoán giảm điểm liên tục 3 ngày."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Munger chỉ ra rằng các bong bóng tài chính điên rồ nhất lịch sử đều sinh ra từ hiệu ứng cộng hưởng Lollapalooza."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # NHÓM 7: LÝ THUYẾT HỆ THỐNG PHỨC HỢP & ĐIỀU KHIỂN HỌC
    # -------------------------------------------------------------------------
    "systems_complex": {
        "id": "systems_complex",
        "category": "🕸️ Hệ Thống Phức Hợp",
        "title": "Hệ Thống Phức Hợp: Vòng Lặp, Nút Thắt & Biên An Toàn",
        "icon": "🕸️",
        "tagline": "Nén tư duy hệ thống và kỹ thuật điều khiển học vào 3 nguyên lý sống còn",
        "summary": "Vòng lặp phản hồi (Feedback Loops), Thuyết điểm nghẽn (Theory of Constraints), Độ trễ hệ thống, Điểm lỗi đơn lẻ và Biên an toàn (Margin of Safety).",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: VÒNG LẶP PHẢN HỒI & ĐỘ TRỄ HỆ THỐNG",
                "sub_modes": "Positive/Negative Feedback Loops + Hệ quả phi tuyến tính + System Delays",
                "principle": "Một hành động nhỏ có thể gây phản hồi khuếch đại nổ tung hệ thống (vòng lặp dương) hoặc bị triệt tiêu bởi cơ chế tự cân bằng (vòng lặp âm). Kết quả luôn đến trễ sau hành động.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Một chiếc micro đặt sát cạnh chiếc loa khổng lồ ngay cửa phát ra tiếng rít chói tai xé rách không gian, vòng âm thanh tự khuếch đại xoay tròn như lốc xoáy!",
                "trigger_question": "Đâu là vòng lặp phản hồi đang vận hành? Độ trễ giữa lúc ra quyết định và lúc hậu quả ập đến là bao lâu?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: NÚT THẮT CỔ CHAI & ĐIỂM LỖI ĐƠN LẺ",
                "sub_modes": "Goldratt Theory of Constraints + Single Point of Failure (SPOF) + Kháng cự",
                "principle": "Tốc độ của cả đoàn tàu chỉ bằng tốc độ của toa chậm nhất. Tối ưu hóa bất kỳ vị trí nào khác ngoài nút thắt cổ chai đều là sự ảo tưởng và lãng phí nguồn lực.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Màn hình biến thành một chai thủy tinh khổng lồ chứa hàng triệu viên bi đang bị kẹt cứng ngắc tại chiếc cổ chai nhỏ xíu, chỉ có từng viên rơi ra một!",
                "trigger_question": "Nút thắt cổ chai duy nhất đang kìm hãm toàn bộ hệ thống là gì? Có mắt xích hiểm yếu nào nếu đứt sẽ làm sập toàn bộ cỗ máy không?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: BIÊN AN TOÀN & THIẾT KẾ DỰ PHÒNG DƯ THỪA",
                "sub_modes": "Graham Margin of Safety + Redundancy Engineering + Chống sụp đổ chuỗi",
                "principle": "Một cây cầu tải trọng 10 tấn phải được xây dựng để chịu được 30 tấn. Đừng bao giờ lái một chiếc xe tải 9.9 tấn qua cây cầu chịu tải 10 tấn.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Chiếc ghế được gia cố bằng 10 chiếc chân thép titan siêu dày, trên mặt ghế cắm biển báo: 'Chỉ ngồi 1 người, nhưng chịu được cả đàn voi 50 tấn!'",
                "trigger_question": "Biên an toàn (Margin of Safety) của tôi ở đây là bao nhiêu %? Nếu dự báo của tôi sai lệch 30%, tôi có còn sống sót không?"
            }
        ],
        "quiz": [
            {
                "question": "Theo Thuyết điểm nghẽn (Theory of Constraints) của Goldratt, bạn cần làm gì khi một quy trình bị chậm?",
                "options": [
                    "Bắt tất cả các bộ phận làm việc tăng ca gấp đôi.",
                    "Tìm chính xác mắt xích cổ chai đang gây tắc nghẽn và tập trung 100% nguồn lực để giải phóng nút thắt đó.",
                    "Mua thêm máy móc mới cho các khâu vốn dĩ đã chạy nhanh."
                ],
                "correct_idx": 1,
                "explanation": "Chính xác! Tối ưu bất kỳ khâu nào nằm ngoài nút thắt cổ chai đều vô nghĩa, vì dòng chảy hệ thống chỉ bị giới hạn bởi khâu yếu nhất."
            }
        ]
    }
}


def get_all_farrow_topics() -> List[Dict[str, Any]]:
    """Trả về toàn bộ danh sách chủ đề Farrow tinh hoa đã nén sẵn."""
    return list(FARROW_TOPICS.values())


def get_farrow_topic_by_id(topic_id: str) -> Dict[str, Any]:
    """Lấy chi tiết một chủ đề theo ID."""
    return FARROW_TOPICS.get(topic_id, list(FARROW_TOPICS.values())[0])


def get_farrow_topics_by_category() -> Dict[str, List[Dict[str, Any]]]:
    """Phân loại danh sách chủ đề theo Danh Mục Cấp 1."""
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for t in FARROW_TOPICS.values():
        cat = t.get("category", "Khác")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(t)
    return grouped
