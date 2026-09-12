# -*- coding: utf-8 -*-
"""
Kho Tri Thức Nén Sẵn Chuẩn Dave Farrow (Pre-packaged Farrow Knowledge Vault)
Hợp nhất toàn bộ 152 Mô hình & Nguyên lý thành 11 chủ đề Lâu Đài Ký Ức chuyên sâu.

QUY CHUẨN ĐỒNG BỘ 1:1:1 BẮT BUỘC:
Mỗi chủ đề gồm đúng 3 Khối Trinity (Soi Gốc -> Đọc Dòng -> Ra Đòn).
Trong mỗi Khối:
- sub_modes: Gồm đúng 3 mô hình/nguyên lý cụ thể (1) + (2) + (3).
- principle: Đúng 3 vế tương ứng theo thứ tự 1 ➔ 2 ➔ 3 (không viết hàn lâm).
- crazy_image: Hoạt cảnh dị biệt tại đúng Mỏ Neo gắn kết tuần tự đúng 3 chi tiết đại diện cho 1, 2, 3.
- trigger_question: Câu hỏi kích hoạt 5 giây bao quát 3 yếu tố sống còn.
"""

from typing import Dict, List, Any

FARROW_TOPICS: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # NHÓM 1: BỘ TƯ DUY NỀN TẢNG & THỰC CHIẾN
    # =========================================================================
    "trinity_thinking": {
        "id": "trinity_thinking",
        "category": "👑 Tư Duy Hạt Nhân",
        "title": "Bộ 3 Tư Duy Tinh Hoa (The Farrow Trinity)",
        "icon": "🧠",
        "tagline": "Nén toàn bộ 9 chế độ tư duy và 88 mô hình Munger về 3 động tác sinh tử",
        "summary": "Mọi vĩ nhân từ Elon Musk, Charlie Munger đến Feynman hay Taleb đều vận hành theo chu trình 3 nhịp: Soi Gốc -> Đọc Dòng -> Ra Đòn.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: SOI GỐC (ROOT)",
                "sub_modes": "(1) First Principles (Nguyên lý Khởi thủy) + (2) Inversion (Tư duy Đảo ngược) + (3) Latticework (Mạng lưới Đa ngành)",
                "principle": "1. Đập vụn mọi giả định về chân lý vật lý gốc rễ ➔ 2. Luôn lộn ngược bài toán tìm mọi cách chết để né tránh ➔ 3. Đan kết các mô hình đa ngành lại thành tấm lưới đỡ quyết định.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Một chiếc máy ép thủy lực khổng lồ nghiền nát cả núi sách thành viên kim cương phát sáng (First Principles), (2) trên đỉnh viên kim cương có con dơi đeo kính lúp X-Quang đang treo ngược người soi tìm bẫy tử thần (Inversion), (3) phía dưới giăng một tấm lưới nhện titan đa sắc màu đan kết bền bỉ hứng trọn mọi rủi ro (Latticework)!",
                "trigger_question": "Sự thật vật lý gốc rễ ở đây là gì? Nếu muốn thất bại thảm hại thì làm thế nào để né? Tấm lưới đa ngành nào đang soi chiếu?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: ĐỌC DÒNG (FLOW)",
                "sub_modes": "(1) Xác suất Bayes + (2) Tư duy Bậc hai + (3) Game Theory (Lý thuyết Trò chơi)",
                "principle": "1. Liên tục cập nhật xác suất khi có dữ liệu mới ➔ 2. Luôn tự hỏi 'Và rồi sau đó chuyện gì xảy ra tiếp theo?' ➔ 3. Đọc vị động cơ và nước cờ phản ứng của đối thủ.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một chiếc cân điện tử Bayes siêu nhạy đang lắc lư theo từng giọt dữ liệu mới rơi xuống (Bayes), (2) từ chiếc cân mọc ra chiếc kính viễn vọng 2 tầng nhìn xuyên thời gian đến hậu quả bậc hai (Second-order), (3) phóng tầm mắt thấy đối thủ trên bàn cờ vua đang toát mồ hôi vì bị bạn bắt thóp toàn bộ động cơ ngầm (Game Theory)!",
                "trigger_question": "Xác suất hiện tại là bao nhiêu? Sau sự kiện này thì phản ứng bậc hai là gì? Đối thủ có động cơ gì để đi nước cờ đó?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: RA ĐÒN (STRIKE)",
                "sub_modes": "(1) Optionality Barbell (Bất đối xứng Taleb) + (2) Thử nghiệm Tinh gọn (Lean Experiment) + (3) Đa quy mô Thời gian (Multi-timeframe)",
                "principle": "1. Khóa chặt rủi ro cực nhỏ ở mức 1 cọng lông để đón tiềm năng ăn dày 3 bát thóc ➔ 2. Tung thử nghiệm vi mô chi phí bằng 0 ngay hôm nay ➔ 3. Kiên định nắm giữ vị thế trong tầm nhìn 10 năm.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một chú gà con mặc giáp titan đòn tạ Barbell bất hoại (Optionality Barbell), (2) tay cầm chiếc kính hiển vi bấm nút thử nghiệm nhỏ phát ra tiếng 'tách' nhẹ nhàng không tốn kém (Lean Experiment), (3) nhưng chân đạp chiếc lò xo thời gian nén cong vút phóng mũi tên xé gió cắm trúng hồng tâm 10 năm sau (Đa quy mô thời gian)!",
                "trigger_question": "Rủi ro tối đa chỉ là 1 cọng lông chứ? Thử nghiệm nhỏ nhất hôm nay là gì? Vị thế này có nở hoa trong 10 năm tới không?"
            }
        ],
        "quiz": [
            {
                "question": "Khi đứng trước một bài toán đầu tư bị bao vây bởi tin đồn, phản xạ đầu tiên của bạn là gì?",
                "options": [
                    "Bật chỉ báo kỹ thuật và nghe lời khuyên của chuyên gia đám đông.",
                    "Đập vụn bài toán về nguyên lý gốc (Trụ 1: Soi Gốc) và tìm cách tự sát để né tránh.",
                    "Lập tức đặt cược hết vốn để không bỏ lỡ cơ hội."
                ],
                "correct_idx": 1,
                "explanation": "Đúng! Trụ 1 (Soi Gốc) yêu cầu bóc sạch mọi ý kiến cảm xúc, chỉ nhìn vào giới hạn vật lý và tư duy đảo ngược."
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
                "label": "TRỤ 1: BẢN CHẤT ZERO CASH FLOW & CHI PHÍ CƠ HỘI",
                "sub_modes": "(1) Zero Cash Flow + (2) Lãi suất thực Mỹ (Real Yields) + (3) Cuộc chơi Tổng âm (Negative-sum Game)",
                "principle": "1. Vàng không tự đẻ ra tiền cũng không có cổ tức ➔ 2. Giá vàng chạy nghịch chiều tuyệt đối với Lãi suất thực của Mỹ (Chi phí cơ hội) ➔ 3. Mọi giao dịch phái sinh chỉ là cuộc chiến cướp tiền lẫn nhau sau khi trừ phí sàn.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Một thỏi vàng khổng lồ hình đầu lâu lạnh ngắt không mọc ra nổi một chiếc lá (Zero Cash Flow), (2) bị Thần Nắng USD dùng tia laser lãi suất thực thiêu đốt làm thỏi vàng tan chảy (Real Yields), (3) dưới sàn một chiếc máy hút bụi của sàn giao dịch tự động hút sạch 2% phí trên mỗi lượt cược của các đấu thủ (Negative-sum Game)!",
                "trigger_question": "Lãi suất thực của Mỹ đang tăng hay giảm? Chi phí cơ hội giữ vàng hiện tại là bao nhiêu? Có đang mù quáng tưởng vàng tự đẻ ra tiền?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: THANH KHOẢN LÀ NHIÊN LIỆU (SWEEP)",
                "sub_modes": "(1) Đỉnh Đáy Đều (Equal Highs/Lows) + (2) Bồn Chứa Xăng Stop Loss + (3) Sói Săn Thanh Khoản (Smart Money Sweep)",
                "principle": "1. Nơi đám đông nhìn thấy kháng cự/hỗ trợ đẹp chính là nơi họ đặt lệnh dừng lỗ dày đặc ➔ 2. Khối lượng Stop Loss đó chính là cây xăng thanh khoản dồi dào nhất thị trường ➔ 3. Sói già luôn đẩy giá quét sạch bồn xăng đó trước khi quay đầu chuyển động thật sự.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một hàng rào cọc gỗ cắm cờ đỏ thẳng tắp đánh dấu các đỉnh đáy đều (Equal Highs/Lows), (2) dưới chân cọc là một bồn chứa xăng Stop Loss lộ thiên đầy ắp (Bồn chứa thanh khoản), (3) một chiếc xe bus 50 tấn do Lão Sói cầm lái đâm sầm vào cán nát hàng cọc, hút cạn bồn xăng rồi bốc đầu quay ngoắt 180 độ (Smart Money Sweep)!",
                "trigger_question": "Đám đông đang cắm cọc dừng lỗ ở đâu đông nhất? Bồn xăng đó đã bị Sói quét sạch chưa? Giá đã quay đầu xác nhận sau quét chưa?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: HẤP THỤ CVD & LÒ XO NÉN RÂU NẾN",
                "sub_modes": "(1) Hấp thụ Lệnh Giới hạn (Limit Absorption) + (2) Râu nến Phanh Gấp + (3) Nén Lò xo Năng lượng (Compression)",
                "principle": "1. Khối lượng bán chủ động cực lớn (CVD âm) nhưng giá không giảm sâu chứng tỏ có bức tường mua ẩn ➔ 2. Cây nến rút chân để lại râu dài thể hiện lực phanh gấp đảo chiều ➔ 3. Biên độ dao động bị bóp nghẹt như lò xo nén báo hiệu một vụ nổ Marubozu sắp giải phóng năng lượng.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một chiếc đe thép Limit Buy khổng lồ nuốt trọn cơn mưa đạn bán tháo CVD mà không hề sứt mẻ (Limit Absorption), (2) chiếc xe bus cắm mũi xuống cát để lại một vệt râu nến dài ngoằng rồi bị nảy ngược lên trời (Râu nến phanh gấp), (3) chiếc ghế ngồi bị ép chặt thành một chiếc lò xo thép kêu rít xé tai sẵn sàng bật tung tung nóc phòng (Nén lò xo Compression)!",
                "trigger_question": "CVD có phân kỳ hấp thụ không? Nến có rút chân để lại râu phanh gấp? Biên độ đã nén đến điểm cực hạn sắp nổ bùng chưa?"
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
        "summary": "Không có kiến thức khó, chỉ có những văn bản rườm rà chưa được nén đúng quy chuẩn sinh học của não bộ.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: BÓC TÁCH KHÔNG DÙNG TỪ HÀN LÂM",
                "sub_modes": "(1) Kỹ thuật Feynman + (2) Phân biệt Biết Tên vs Hiểu Bản Chất + (3) Phép Loại suy Đời thường (Analogy)",
                "principle": "1. Nếu không thể giải thích cho một đứa trẻ 10 tuổi hiểu thì bạn chưa hiểu nó ➔ 2. Biết tên gọi của một vật không đồng nghĩa với việc hiểu cơ chế vận hành của nó ➔ 3. Sử dụng các hình ảnh ẩn dụ đời thường quen thuộc để thế chỗ cho các thuật ngữ trừu tượng.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Giáo sư Feynman cầm kéo cắt vụn một chiếc áo choàng tiến sĩ lộng lẫy để lộ đứa trẻ 10 tuổi bên trong (Kỹ thuật Feynman), (2) trên tay đứa trẻ cầm cuốn từ điển bách khoa dày cộp ném thẳng vào sọt rác vì 'chỉ toàn tên gọi rỗng tuếch' (Biết tên vs Hiểu), (3) đứa trẻ lấy một quả táo cắn dở giải thích thuyết vạn vật hấp dẫn cho mọi người cùng ồ lên thấu hiểu (Phép loại suy Analogy)!",
                "trigger_question": "Nếu phải giải thích điều này cho một đứa trẻ 10 tuổi mà không dùng từ chuyên môn, tôi sẽ nói gì? Tôi đang hiểu bản chất hay chỉ thuộc vẹt tên gọi?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: QUY TẮC SỐ 3 & MỎ NEO KHÔNG GIAN FARROW",
                "sub_modes": "(1) Dave Farrow Rule of 3 + (2) Lâu đài Ký ức Không gian (Memory Palace) + (3) Hình ảnh Dị biệt Phi lý (Absurd Vivid Imagery)",
                "principle": "1. Não người chỉ xử lý tối đa 3 khối thông tin cùng một lúc ➔ 2. Ghim 3 khối hạt nhân vào 3 đồ vật không gian quen thuộc trong phòng ➔ 3. Phóng đại hình ảnh thành dị biệt, quái đản và phi lý gấp 10 lần để đóng đinh vào trí nhớ dài hạn.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Dave Farrow đang cầm đúng 3 củ khoai tây phát sáng hình tam giác ghim thẳng vào trán (Rule of 3), (2) mắt ông phóng ra 3 tia chớp xanh lét cắm chặt vào Cửa - Màn hình - Ghế ngồi trong phòng (Lâu đài ký ức), (3) mỗi đồ vật lập tức biến dạng thành một quái thú hoạt hình nhảy múa điên cuồng phát ra tiếng cười khanh khách (Hình ảnh dị biệt phi lý)!",
                "trigger_question": "3 hạt nhân cốt lõi nhất ở đây là gì? Chúng gắn vào 3 đồ vật nào trong phòng tôi? Hình ảnh dị biệt quái đản nhất để không thể quên là gì?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: ÉP XUNG 10 PHÚT & THỞ BỤNG SẠC PIN",
                "sub_modes": "(1) 10-Minute Focus Sprint + (2) Xả Cortisol Giảm Căng thẳng + (3) Thở Bụng Đưa Não về Sóng Alpha",
                "principle": "1. Chạy nước rút tập trung 100% trong đúng 10 phút để triệt tiêu xao nhãng ➔ 2. Dừng lại ngay lập tức khi hết giờ để không kích thích hạch amygdala tiết cortisol ➔ 3. Hít thở sâu bằng bụng 4 nhịp để đưa oxy lên não, đưa sóng não về Alpha lưu trữ ký ức.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một chiếc đồng hồ cát bốc cháy ngùn ngụt đếm ngược 10 phút trong tiếng còi giục giã (Focus Sprint), (2) vừa hết 10 phút, một gáo nước mát lạnh dập tắt ngọn lửa xả trôi hết đám khói độc cortisol đen ngòm (Xả cortisol), (3) một lá phổi silicon khổng lồ trên ghế phập phồng bơm bọt khí oxy lấp lánh đưa hào quang xanh Alpha bao bọc toàn bộ cơ thể (Thở bụng sóng Alpha)!",
                "trigger_question": "Tôi đã chạy hết tốc lực 10 phút chưa? Đã đến lúc buông bàn phím nghỉ ngơi? Tôi đã hít thở sâu bằng bụng để khóa chặt ký ức chưa?"
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

    # =========================================================================
    # NHÓM 2: VẬT LÝ HỌC TINH HOA (2 PHẦN)
    # =========================================================================
    "physics_core_1": {
        "id": "physics_core_1",
        "category": "⚛️ Vật Lý Học",
        "title": "Vật Lý Tinh Hoa 1: Bảo Toàn, Quán Tính & Đòn Bẩy",
        "icon": "⚖️",
        "tagline": "Nén toàn bộ cơ học cổ điển về 3 nguyên lý gốc: Bảo toàn -> Lực cản -> Điểm tựa",
        "summary": "Tổng hợp các định luật Newton, bảo toàn năng lượng Lavoisier, quán tính, ma sát và đòn bẩy Acsimet.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: BẢO TOÀN NĂNG LƯỢNG & KHỐI LƯỢNG TỚI HẠN",
                "sub_modes": "(1) Định luật 1 Newton (Quán tính) + (2) Bảo toàn Năng lượng Lavoisier + (3) Khối lượng Tới hạn (Critical Mass)",
                "principle": "1. Một vật đứng yên hoặc đang chuyển động sẽ giữ nguyên trạng thái nếu không có ngoại lực ➔ 2. Năng lượng không tự sinh ra, muốn có thành quả bắt buộc phải bỏ công tương ứng ➔ 3. Phải tích tụ đủ khối lượng tới hạn mới kích hoạt được phản ứng dây chuyền bùng nổ.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Một tảng thiên thạch 100 tấn đứng lì chắn ngang cửa đẩy cật lực không nhúc nhích (Quán tính Newton), (2) trên lưng tảng đá gắn chiếc cân Lavoisier phát sáng báo tổng năng lượng vào = ra không hao hụt 1 miligram (Bảo toàn Lavoisier), (3) một chú kiến thả thêm hạt bụi uranium cuối cùng làm chạm ngưỡng khối lượng tới hạn, phát ra tiếng nổ rền vang biến cánh cửa thành cổng plasma chói lòa (Khối lượng tới hạn)!",
                "trigger_question": "Quán tính cũ đang kéo về đâu? Có ảo tưởng làm giàu vi phạm bảo toàn năng lượng không? Đã tích tụ đủ khối lượng tới hạn để bùng nổ chưa?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: MA SÁT, ĐỘ NHỚT & VẬN TỐC THOÁT",
                "sub_modes": "(1) Ma sát & Độ nhớt (Friction & Viscosity) + (2) Lực cản Môi trường (Drag) + (3) Vận tốc Thoát ly (Escape Velocity)",
                "principle": "1. Mọi chuyển động nội tại đều sinh ma sát làm hao tổn năng lượng quý giá ➔ 2. Càng di chuyển nhanh lực cản môi trường càng tăng theo cấp số nhân ➔ 3. Chỉ có gia tốc cực đại vượt qua vận tốc thoát mới không bị trọng trường cũ hút ngược rơi lại đáy vực.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một bánh răng kim loại đang cọ xát bốc khói đen kịt trong vũng siro đặc quánh (Ma sát & Độ nhớt), (2) chiếc mũi tên cố lao đi nhưng bị một bức tường gió bão cuộn trào tạt ngược lại theo cấp số nhân (Lực cản Drag), (3) bất ngờ một động cơ phản lực tên lửa phụt luồng lửa xanh rực rỡ vượt qua vận tốc thoát 11.2 km/s bay vút vào không gian vũ trụ tự do (Vận tốc thoát)!",
                "trigger_question": "Độ nhớt và ma sát nội bộ đang cắn xé bao nhiêu % năng lượng? Lực cản môi trường có đang tăng tốc? Tốc độ hiện tại đã đủ để thoát ly trọng trường cũ chưa?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: ĐÒN BẨY ACSIMET & CỘNG HƯỞNG",
                "sub_modes": "(1) Nguyên lý Đòn bẩy Acsimet + (2) Điểm tựa Vững chắc (Fulcrum) + (3) Tần số Dao động Cộng hưởng (Resonance)",
                "principle": "1. Cánh tay đòn càng dài lực nâng càng nhân lên gấp bội ➔ 2. Phải có điểm tựa bất di bất dịch thì đòn bẩy mới phát huy tác dụng ➔ 3. Tác động một lực nhỏ nhưng đúng tần số dao động tự nhiên sẽ làm rung chuyển cả hệ thống khổng lồ.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một thanh xà beng titan dài 100 mét vươn qua bàn nâng bổng cả một quả núi đá (Đòn bẩy Acsimet), (2) dưới thanh xà là chiếc đe thép kim cương cắm sâu vào sàn nhà không hề rung chuyển (Điểm tựa Fulcrum), (3) một chiếc âm thoa nhỏ đặt trên bàn rung lên đúng tần số riêng làm cả quả núi nứt toác sụp đổ tan tành (Cộng hưởng Resonance)!",
                "trigger_question": "Cánh tay đòn của tôi đã đủ dài chưa? Điểm tựa vững chắc ở đâu? Tôi có đang tác động đúng nhịp tần số cộng hưởng để khuếch đại lực không?"
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
                "label": "TRỤ 1: ENTROPY & QUY LUẬT SUY THOÁI TẤT YẾU",
                "sub_modes": "(1) Định luật 2 Nhiệt động học (Entropy) + (2) Độ không Tuyệt đối (Absolute Zero) + (3) Tản tán Năng lượng (Dissipation)",
                "principle": "1. Mọi hệ thống không được nạp năng lượng bảo dưỡng đều tất yếu tự phân rã về hỗn loạn ➔ 2. Tại độ không tuyệt đối mọi dao động phân tử mới hoàn toàn đóng băng ➔ 3. Năng lượng hữu ích luôn bị tản tán ra môi trường dưới dạng nhiệt thải vô ích.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Cánh cửa gỗ sang trọng đang tự động mục nát, rụng vụn thành đống cát bụi hỗn độn (Entropy tăng), (2) một cột băng âm 273.15 độ C phủ kín chân cửa làm đóng băng mọi chuyển động của thời gian (Độ không tuyệt đối), (3) một làn khói nhiệt mờ ảo bốc lên từ đống tro tàn bay mất hút vào không trung không thể thu hồi (Tản tán năng lượng)!",
                "trigger_question": "Hệ thống có được bảo trì hàng ngày để chống lại Entropy không? Năng lượng hữu ích đang bị rò rỉ ở đâu? Có đang bị đóng băng tê liệt?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: DÒNG CHẢY NHIỆT & BIẾN ĐIỆU SÓNG DOPPLER",
                "sub_modes": "(1) Gradient Thế năng (Dòng nhiệt) + (2) Cân bằng Nhiệt động (Thermal Equilibrium) + (3) Hiệu ứng Sóng Doppler",
                "principle": "1. Nhiệt lượng chỉ tự truyền từ nơi nhiệt độ cao sang nơi nhiệt độ thấp ➔ 2. Dòng chảy sẽ ngừng lại khi hai bên đạt trạng thái cân bằng triệt tiêu ➔ 3. Tần số sóng bạn nhận được phụ thuộc vào chuyển động tương đối giữa bạn và nguồn phát.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một dòng dung nham đỏ rực cuồn cuộn đổ từ đỉnh núi cao xuống đáy thung lũng băng giá (Gradient thế năng), (2) khi hai dòng hòa trộn biến thành mặt hồ nước ấm phẳng lặng không còn gợn sóng (Cân bằng nhiệt), (3) một đoàn tàu cao tốc lao vụt qua trên màn hình phát ra tiếng còi hú lúc the thé dồn dập, lúc trầm bổng kéo dài (Hiệu ứng Doppler)!",
                "trigger_question": "Thế năng chênh lệch đang chảy về đâu? Trạng thái cân bằng sắp tới chưa? Tôi đang tiến lại gần hay lùi xa nguồn phát tín hiệu?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: BƯỚC NHẢY CHUYỂN PHA TẠI 100°C",
                "sub_modes": "(1) Nhiệt dung Tiềm ẩn (Latent Heat) + (2) Ngưỡng Chuyển pha (Phase Transition) + (3) Năng lượng Hoạt hóa Bùng nổ",
                "principle": "1. Hấp thụ năng lượng liên tục mà không thấy tăng nhiệt độ gọi là tích lũy nhiệt tiềm ẩn ➔ 2. Đúng 100°C chất lỏng bùng nổ chuyển hóa toàn diện thành thể khí ➔ 3. Vượt qua năng lượng hoạt hóa sẽ giải phóng sức mạnh kéo chuyển cả đoàn tàu.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Chiếc ấm đồng trên ghế đun mãi ở 99 độ C vẫn im lìm không thấy khói (Tích lũy nhiệt tiềm ẩn), (2) kim đo vừa chạm đúng 100 độ C lập tức nắp ấm bật tung biến nước thành luồng hơi nước áp suất cực cao (Chuyển pha bùng nổ), (3) luồng hơi nước đẩy mạnh pít-tông máy hơi nước làm quay bánh đà khổng lồ cuốn bay chiếc bàn (Giải phóng năng lượng hoạt hóa)!",
                "trigger_question": "Tôi đang âm thầm tích lũy nhiệt tiềm ẩn hay lãng phí thời gian? Đã chạm đúng ngưỡng 100°C chuyển pha chưa? Đâu là cú hích hoạt hóa?"
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

    # =========================================================================
    # NHÓM 3: SINH HỌC & TIẾN HÓA
    # =========================================================================
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
                "sub_modes": "(1) Hốc sinh thái Độc quyền (Niche) + (2) Cân bằng Nội môi (Homeostasis) + (3) Sức chứa Môi trường (Carrying Capacity)",
                "principle": "1. Tìm và chiếm lĩnh một ngóc ngách độc quyền không bị cạnh tranh trực diện ➔ 2. Cơ thể liên tục phản hồi để giữ vững các chỉ số sinh hóa sống còn ➔ 3. Không một quần thể nào có thể tăng trưởng vượt quá sức chứa tài nguyên của môi trường.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Một chú chim ruồi mỏ dài ngoằng cắm sâu vào bông hoa kèn độc quyền trên cửa không loài nào với tới (Hốc sinh thái), (2) trên ngực chim đeo chiếc máy đo nhịp tim và nhiệt kế tự điều hòa mồ hôi giữ chuẩn 37 độ C (Cân bằng nội môi), (3) chiếc tổ chim treo trên cửa có vạch mức đỏ ghi 'Chỉ chứa tối đa 2 trứng - vượt mức sẽ sập gãy' (Sức chứa môi trường)!",
                "trigger_question": "Hốc sinh thái độc tôn của tôi ở đâu? Trạng thái cân bằng nội bộ có đang bị đe dọa? Hệ thống đã chạm trần sức chứa của môi trường chưa?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: NỮ HOÀNG ĐỎ & CHỌN LỌC TỰ NHIÊN",
                "sub_modes": "(1) Chọn lọc Tự nhiên Darwin + (2) Áp lực Tiến hóa Đào thải + (3) Cuộc đua Nữ hoàng Đỏ (Red Queen)",
                "principle": "1. Kẻ thích nghi tốt nhất với sự thay đổi của môi trường sẽ sống sót truyền lại gen ➔ 2. Khi môi trường biến đổi, những cá thể mang đặc tính lỗi thời bị tuyệt diệt không thương tiếc ➔ 3. Phải chạy hết tốc lực chỉ để giữ nguyên vị trí trong cuộc đua sinh tồn với đối thủ.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một đàn hươu cổ dài vươn tới tán lá cao trong khi hươu cổ ngắn gục chết đói (Chọn lọc tự nhiên), (2) một cơn bão tuyết ập tới xóa sạch dấu vết các sinh vật máu lạnh không tiến hóa lông dày (Áp lực đào thải), (3) Bà Hoàng Hậu Đỏ đang lôi tay con báo gấm chạy trối chết trên máy chạy bộ bốc khói để không bị trôi tuột ra mép vực (Nữ hoàng Đỏ)!",
                "trigger_question": "Môi trường vừa thay đổi điều gì? Những thói quen cũ nào đang bị tự nhiên đào thải? Tôi có đang chạy đủ nhanh để không bị đối thủ qua mặt?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: ĐỘT BIẾN NGẪU NHIÊN & BẮT CHƯỚC SINH HỌC",
                "sub_modes": "(1) Đột biến Ngẫu nhiên (Random Mutation) + (2) Bắt chước Sinh học (Biomimicry) + (3) Đa dạng Di truyền Phòng hộ",
                "principle": "1. Dành một phần nhỏ tài nguyên cho các thử nghiệm sai lệch ngẫu nhiên để tìm ra đột phá ➔ 2. Học hỏi và sao chép các cấu trúc đã được tự nhiên thử nghiệm thành công 4 tỷ năm ➔ 3. Đa dạng hóa nguồn gen để không bị một căn bệnh duy nhất quét sạch toàn bộ giống loài.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một chú tắc kè hoa ngồi trên ghế bất ngờ biến đổi mã ADN mọc ra chiếc sừng phát sáng lạ lùng (Đột biến ngẫu nhiên), (2) lớp da chân của nó cấu tạo như gai tắc kè bám chặt vào vách kính thẳng đứng nâng bổng chiếc bàn (Bắt chước sinh học Biomimicry), (3) xung quanh là đàn tắc kè 10 màu sắc khác nhau, một con bị ốm nhưng 9 con khác hoàn toàn miễn nhiễm (Đa dạng phòng hộ)!",
                "trigger_question": "Tôi có dành 10% cho các đột biến thử nghiệm không? Có giải pháp tự nhiên nào có thể bắt chước? Danh mục của tôi có đủ đa dạng để chống dịch bệnh tài chính?"
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

    # =========================================================================
    # NHÓM 4: TOÁN HỌC & XÁC SUẤT THỰC CHIẾN
    # =========================================================================
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
                "sub_modes": "(1) Tư duy Đảo ngược Jacobi + (2) Phân phối Chuẩn Gaussian vs Đuôi béo Mandelbrot + (3) Quy luật Số lớn (Law of Large Numbers)",
                "principle": "1. Tìm tất cả các cách để cháy sạch tài khoản rồi loại bỏ chúng hoàn toàn ➔ 2. Đừng tin vào đồ thị hình chuông bình yên, thế giới thực bị thống trị bởi thiên nga đen ở phần đuôi béo ➔ 3. Kết quả ngắn hạn có thể do may rủi, nhưng số lượng mẫu đủ lớn sẽ phơi bày bản chất kỳ vọng thực sự.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Nhà toán học Jacobi trồng cây chuối trước cửa, dùng bút đỏ gạch chéo tất cả các cửa tử thần (Đảo ngược Jacobi), (2) dưới chân ông, một chiếc chuông Gaussian bình yên bỗng bị đuôi của một con cá voi đen khổng lồ quẫy nát vụn (Đuôi béo Fat Tails), (3) trên cửa có chiếc máy quay xúc xắc quay 1 triệu lần, kim đo dần kéo thẳng tắp về đúng giá trị trung bình toán học (Quy luật số lớn)!",
                "trigger_question": "Nếu muốn tự sát trong thương vụ này thì làm cách nào? Kịch bản thiên nga đen tồi tệ nhất ở đuôi béo là gì? Cỡ mẫu đã đủ lớn chưa?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: CẬP NHẬT BAYES & HỒI QUY TRUNG BÌNH",
                "sub_modes": "(1) Xác suất Tiên nghiệm (Prior Probability) + (2) Cập nhật Dữ liệu Mới Bayes (Posterior) + (3) Hồi quy về Giá trị Trung bình (Regression to the Mean)",
                "principle": "1. Bắt đầu bằng xác suất nền tảng khách quan trong lịch sử ➔ 2. Lập tức điều chỉnh niềm tin khi xuất hiện bằng chứng dữ liệu mới ➔ 3. Sau một chuỗi kết quả cực đoan bất thường, mọi thứ tất yếu sẽ quay trở về mức trung bình dài hạn.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một chiếc cân hiển thị con số xác suất gốc 20% (Tiên nghiệm Prior), (2) một chiếc phễu thông tin đổ những giọt bằng chứng mới vào làm kim cân lập tức nhảy vọt lên 75% (Cập nhật Bayes), (3) một mũi tên đồ thị bắn vọt lên trời cao rồi bị một sợi dây cao su vô hình kéo giật lùi về đúng đường kẻ trung tâm (Hồi quy trung bình)!",
                "trigger_question": "Tỷ lệ xác suất nền tảng ban đầu là bao nhiêu? Bằng chứng mới này làm tăng hay giảm xác suất? Đây là phong độ xuất chúng bền vững hay chỉ là độ lệch chuẩn sắp hồi quy?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: LÃI KÉP KỲ DIỆU & CÔNG THỨC KELLY",
                "sub_modes": "(1) Lãi kép Lũy thừa (Compound Growth) + (2) Định luật Pareto 80/20 + (3) Tiêu chuẩn Đặt cược Kelly (Kelly Criterion)",
                "principle": "1. Tích lũy liên tục không ngắt quãng biến tăng trưởng chậm ban đầu thành đường dốc đứng khổng lồ ➔ 2. 80% kết quả đột phá chỉ đến từ 20% nguyên nhân cốt lõi ➔ 3. Khi nắm chắc lợi thế toán học dương, chỉ đặt cược theo tỷ lệ phần trăm tối ưu của công thức Kelly để không bao giờ cháy túi.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một đồng xu vàng nhỏ xíu trên ghế tự đẻ ra 2 đồng, 4 đồng, rồi nổ tung thành một núi vàng ngập tràn căn phòng (Lãi kép lũy thừa), (2) trên mặt bàn một hòn đá nhỏ bằng nắm tay chiếm 20% diện tích nhưng đè bẹp cả 80% mớ giấy tờ vụn vặt xung quanh (Pareto 80/20), (3) chiếc máy tính Kelly trên bàn tự động đóng van khóa cứng lệnh cược ở mức 8% tài khoản, ngăn chủ nhân cược tất tay (Kelly Criterion)!",
                "trigger_question": "Hành động này có được cộng dồn theo lãi kép không? Tôi đã tập trung vào 20% cốt lõi chưa? Tỷ lệ cược vốn có chuẩn theo công thức Kelly?"
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

    # =========================================================================
    # NHÓM 5: KINH TẾ HỌC & ĐẦU TƯ (2 PHẦN)
    # =========================================================================
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
                "label": "TRỤ 1: CHI PHÍ CƠ HỘI & CHI PHÍ CHÌM",
                "sub_modes": "(1) Chi phí Cơ hội (Opportunity Cost) + (2) Hiệu dụng Biên Giảm dần (Diminishing Marginal Utility) + (3) Bẫy Chi phí Chìm (Sunk Cost Fallacy)",
                "principle": "1. Giá trị thực của một quyết định là giá trị của lựa chọn tốt nhất bị bỏ qua ➔ 2. Càng tiêu thụ nhiều một món đồ, mức độ thỏa mãn của mỗi đơn vị tiếp theo càng tụt dốc ➔ 3. Tiền bạc và thời gian đã mất trong quá khứ không thể lấy lại và không được phép chi phối quyết định tương lai.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Hai cánh cửa mở ra hai hướng: một bên là vali tiền 1 triệu USD, một bên là tấm vé tự do; bạn bước sang một bên thì cánh cửa bên kia tự bốc cháy vĩnh viễn (Chi phí cơ hội), (2) một thực khách ăn đến chiếc bánh pizza thứ 10 trên cửa thì nôn thốc nôn tháo vì ngấy ngấy (Hiệu dụng biên giảm dần), (3) một chiếc tàu đắm dưới biển sâu đang kéo theo một người cố ôm mỏ neo rỉ sét vì tiếc tiền mua neo (Bẫy chi phí chìm)!",
                "trigger_question": "Nếu chọn việc này, tôi đang phải đánh đổi mất cơ hội nào quý giá hơn? Giá trị gia tăng của đơn vị tiếp theo là bao nhiêu? Tôi có đang tiếc chi phí chìm đã mất?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: QUY LUẬT CUNG CẦU & ĐỘNG LỰC TƯ LỢI",
                "sub_modes": "(1) Cân bằng Cung Cầu Thị trường + (2) Tín hiệu Giá cả (Price Mechanism) + (3) Động lực Khen thưởng Munger (Incentive Bias)",
                "principle": "1. Nguồn cung khan hiếm mà nhu cầu bùng nổ thì giá tất yếu leo thang ➔ 2. Giá cả là tín hiệu dẫn đường điều phối tài nguyên không cần ai chỉ đạo ➔ 3. Thiết kế sai cơ chế thưởng phạt sẽ biến những người tử tế nhất thành những kẻ phá hoại tồi tệ nhất.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một đàn người chen lấn giẫm đạp nhau để mua 1 chai nước ngọt duy nhất trên sa mạc (Cung cầu khan hiếm), (2) biển hiệu giá cả trên màn hình phát sáng đèn xanh đèn đỏ điều phối dòng xe cộ tấp nập tự động (Tín hiệu giá cả), (3) Charlie Munger đứng bên cạnh giơ miếng pho mát buộc dây câu nhử một bầy chuột chạy theo đúng hướng ông muốn (Động lực Incentive)!",
                "trigger_question": "Nguồn cung đang thắt hay phình to? Tín hiệu giá đang chỉ báo điều gì? Cơ chế trả thưởng đang khuyến khích các bên làm điều tử tế hay lừa đảo?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: PHÁ HỦY SÁNG TẠO & LỢI THẾ SO SÁNH",
                "sub_modes": "(1) Phá hủy Sáng tạo Schumpeter + (2) Lợi thế So sánh Ricardo (Comparative Advantage) + (3) Chuyên môn hóa Lao động",
                "principle": "1. Đổi mới công nghệ tất yếu nghiền nát và chôn vùi các mô hình kinh doanh cũ lỗi thời ➔ 2. Hãy chỉ tập trung làm việc bạn làm với chi phí cơ hội thấp nhất và trao đổi phần còn lại ➔ 3. Chia nhỏ quy trình và chuyên môn hóa sâu giúp năng suất tăng gấp hàng nghìn lần.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một chiếc máy tính xách tay phát ra luồng sóng laser nghiền nát máy đánh chữ, xe ngựa và đĩa than trên bàn thành tro bụi (Phá hủy sáng tạo Schumpeter), (2) hai người ngồi hai đầu bàn: một người chỉ vẽ tranh, một người chỉ viết code, đổi sản phẩm cho nhau cả hai cùng giàu to (Lợi thế so sánh Ricardo), (3) một dây chuyền tự động trên bàn chia làm 10 cánh tay robot mỗi con chỉ vặn đúng 1 con ốc với tốc độ tia chớp (Chuyên môn hóa)!",
                "trigger_question": "Mô hình này có đang bị làn sóng phá hủy sáng tạo chôn vùi? Lợi thế so sánh duy nhất của tôi là gì? Tôi đã chuyên môn hóa sâu hay vẫn ôm đồm?"
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
        "summary": "Con hào kinh tế (Economic Moat), Hiệu ứng mạng lưới (Network Effects), Lợi thế kinh tế theo quy mô và Chi phí chuyển đổi.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: CON HÀO KINH TẾ & CHI PHÍ CHUYỂN ĐỔI",
                "sub_modes": "(1) Con hào Kinh tế Buffett (Economic Moat) + (2) Chi phí Chuyển đổi (Switching Costs) + (3) Tài sản Vô hình Độc quyền",
                "principle": "1. Pháo đài kinh doanh phải có con hào sâu bảo vệ lợi nhuận biên trước sự tấn công của đối thủ ➔ 2. Làm cho khách hàng cảm thấy việc rời bỏ sản phẩm gây tổn thất đau đớn đến mức không dám chuyển đổi ➔ 3. Sở hữu bằng sáng chế, giấy phép độc quyền hoặc thương hiệu ăn sâu vào tiềm thức.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Cửa phòng bị bao quanh bởi một con hào nước sâu hun hút thả đầy cá sấu bọc giáp gai (Con hào kinh tế Buffett), (2) tay nắm cửa bôi loại keo dính siêu chắc, ai đã chạm tay vào muốn giật ra phải lột cả mảng da đau điếng (Chi phí chuyển đổi Switching Costs), (3) trên đỉnh cổng khắc con dấu hoàng gia bằng vàng rực rỡ độc quyền không ai được phép sao chép (Tài sản vô hình độc quyền)!",
                "trigger_question": "Con hào kinh tế bảo vệ lợi thế này là gì? Khách hàng rời đi có phải trả giá đau đớn không? Có tài sản độc quyền nào không thể sao chép?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: HIỆU ỨNG MẠNG LƯỚI & HIỆU ỨNG BÁNH ĐÀ",
                "sub_modes": "(1) Hiệu ứng Mạng lưới Metcalfe (Network Effects) + (2) Bánh đà Tự tăng trưởng (Flywheel Effect) + (3) Cạnh tranh Độc quyền Nhóm",
                "principle": "1. Càng có nhiều người tham gia mạng lưới thì giá trị của nó càng tăng theo hàm số mũ ➔ 2. Đẩy bánh đà quay những vòng đầu tiên cực nhọc nhưng sau đó nó sẽ tự tích lũy động lượng quay tít ➔ 3. Kẻ thống lĩnh mạng lưới sẽ tạo ra vị thế độc quyền tự nhiên nuốt chửng thị phần.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một mạng nhện bằng dây cáp quang phát sáng, cứ thêm một nút kết nối mới thì toàn bộ mạng nhện lại sáng gấp đôi (Hiệu ứng mạng lưới Metcalfe), (2) một bánh đà bằng thép 10 tấn trên màn hình sau cú hích ban đầu bỗng tự quay vù vù tạo ra gió lốc hút tiền về tâm (Bánh đà Flywheel), (3) các đấu thủ nhỏ xung quanh bị lực hút của bánh đà cuốn phăng và sáp nhập vào cỗ máy khổng lồ (Độc quyền nhóm)!",
                "trigger_question": "Sản phẩm này có giá trị hơn khi có thêm 1 triệu người dùng không? Bánh đà đã bắt đầu tự quay chưa? Kẻ dẫn đầu có đang tạo rào cản độc quyền?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: QUY MÔ KINH TẾ & CHI PHÍ BIÊN = 0",
                "sub_modes": "(1) Lợi thế Kinh tế nhờ Quy mô (Economies of Scale) + (2) Chi phí Biên tiệm cận 0 (Zero Marginal Cost) + (3) Kẻ Thắng Nuốt Trọn (Winner-Takes-All)",
                "principle": "1. Sản lượng càng khổng lồ thì chi phí cố định trên mỗi đơn vị càng giảm sâu không đối thủ nào đọ nổi ➔ 2. Khi nhân bản thêm 1 sản phẩm mới tốn chi phí bằng 0, biên lợi nhuận sẽ bùng nổ vô tận ➔ 3. Thị trường kỹ thuật số luôn nghiêng về quy luật kẻ số một chiếm lĩnh gần như toàn bộ miếng bánh.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một cỗ máy dập cơ khí trên ghế dập 1 triệu chi tiết trong nháy mắt, đẩy giá thành mỗi cái xuống còn 1 xu lẻ đè bẹp xưởng thủ công (Quy mô kinh tế), (2) một chiếc ổ cứng máy tính trên bàn nhấn nút sao chép 1 tỷ bản phần mềm gửi đi toàn cầu mà tiền điện không tăng 1 đồng (Chi phí biên = 0), (3) trên ghế có chú gấu trúc khổng lồ ôm trọn cả chiếc bánh kem 10 tầng, chỉ vứt lại vài mẩu vụn cho các con vật khác (Winner-takes-all)!",
                "trigger_question": "Quy mô có đang tạo ra bức tường lửa về chi phí không? Chi phí biên để phục vụ thêm một khách hàng là bao nhiêu? Cuộc chơi này có dẫn tới Winner-takes-all?"
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

    # =========================================================================
    # NHÓM 6: TÂM LÝ HỌC & BẪY NHẬN THỨC
    # =========================================================================
    "psychology_biases": {
        "id": "psychology_biases",
        "category": "🎭 Tâm Lý & Nhận Thức",
        "title": "Tâm Lý Học: Bẫy Não, Mỏ Neo & Hiệu Ứng Lollapalooza",
        "icon": "🎭",
        "tagline": "Nén 25 thiên kiến nhận thức của Charlie Munger vào 3 cạm bẫy sinh tử",
        "summary": "Ác cảm mất mát (Loss Aversion), Thiên kiến xác nhận, Bằng chứng xã hội, Mỏ neo và Hiệu ứng cộng hưởng Lollapalooza.",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: ÁC CẢM MẤT MÁT & NEO GIÁ TÂM LÝ",
                "sub_modes": "(1) Ác cảm Mất mát Kahneman (Loss Aversion) + (2) Hiệu ứng Mỏ neo (Anchoring Effect) + (3) Hiệu ứng Sở hữu (Endowment Effect)",
                "principle": "1. Nỗi đau khi mất 100 đô la tác động mạnh gấp đôi niềm vui kiếm được 100 đô la ➔ 2. Não bộ tự động bám chặt vào con số đầu tiên nhìn thấy làm chuẩn mực so sánh lệch lạc ➔ 3. Khi đã nắm giữ một món đồ trong tay, con người vô thức định giá nó cao hơn nhiều lần giá trị thị trường thực tế.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Một người đàn ông gào khóc thảm thiết vì làm rơi tờ 500 nghìn dù trong túi vừa nhặt được 1 triệu (Ác cảm mất mát), (2) dưới chân anh ta là chiếc mỏ neo tàu biển nặng 5 tấn ghim chặt con số giá đỉnh cũ '100 ĐÔ' vào sàn nhà kéo không lên (Hiệu ứng mỏ neo), (3) tay kia anh ta ôm khư khư một chiếc cốc sứ sứt mẻ hét lên đòi bán giá 1 tỷ đồng vì 'đây là cốc của tôi!' (Hiệu ứng sở hữu)!",
                "trigger_question": "Quyết định này do phân tích khách quan hay do sợ cắt lỗ đau đớn? Con số nào đang là mỏ neo trói buộc tâm trí tôi? Tôi có đang tự định giá quá cao món đồ của mình?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: THIÊN KIẾN XÁC NHẬN & TÂM LÝ BẦY CỪU",
                "sub_modes": "(1) Thiên kiến Xác nhận (Confirmation Bias) + (2) Bằng chứng Xã hội (Social Proof) + (3) Thiên kiến Sẵn có (Availability Bias)",
                "principle": "1. Não bộ chỉ lọc và thu nhận thông tin trùng khớp với định kiến có sẵn và tự động mù lòa trước bằng chứng phản bác ➔ 2. Khi hoang mang không biết làm gì, con người nhắm mắt bắt chước hành vi của số đông ➔ 3. Đánh giá xác suất của một sự việc dựa trên mức độ dễ dàng hồi tưởng lại các ký ức gần đây nhất.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một người đeo kính màu hồng chỉ nhìn thấy những chữ 'BẠN ĐÃ ĐÚNG' và xóa sạch mọi chữ 'BẠN ĐANG SAI' trên màn hình (Thiên kiến xác nhận), (2) một đàn cừu đeo chuông đang nối đuôi nhau nhảy xuống hố sâu chỉ vì con đầu đàn trượt chân (Bằng chứng xã hội), (3) một chiếc TV phát đi phát lại cảnh máy bay rơi làm cả phòng sợ hãi hủy vé bay đòi đi xe máy nguy hiểm hơn gấp trăm lần (Thiên kiến sẵn có)!",
                "trigger_question": "Tôi có đang chủ động tìm bằng chứng để bác bỏ quan điểm của mình không? Tôi làm theo vì logic hay vì đám đông đang làm? Ký ức giật gân nào đang bóp méo nhận định?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: CỘNG HƯỞNG TÂM LÝ LOLLAPALOOZA & BẪY NHẤT QUÁN",
                "sub_modes": "(1) Bẫy Cam kết & Nhất quán (Commitment & Consistency) + (2) Hiệu ứng Uy quyền Giả tạo (Authority Bias) + (3) Cơn Lốc Lollapalooza Charlie Munger",
                "principle": "1. Khi đã công khai tuyên bố một quan điểm, con người sẽ ngoan cố bảo vệ nó đến cùng dù biết mình sai ➔ 2. Dễ dàng phục tùng một mệnh lệnh phi lý nếu kẻ ra lệnh khoác lên mình chiếc áo choàng chuyên gia uy quyền ➔ 3. Khi nhiều thiên kiến tâm lý cùng bùng phát đồng thời theo một hướng, lý trí bị xóa sổ hoàn toàn tạo nên cơn điên tập thể.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một người tự lấy khóa xích chặt tay mình vào thành ghế sau khi hô to 'Tôi quyết không đổi ý!' (Bẫy cam kết nhất quán), (2) một diễn viên mặc áo blouse trắng bước vào nói hươu nói vượn nhưng mọi người đều quỳ gối gật đầu lia lịa (Uy quyền giả tạo), (3) Charlie Munger đứng trên bàn bấm còi báo động khi một cơn lốc xoáy ngũ sắc Lollapalooza quét phăng cả sàn chứng khoán đang say máu (Hiệu ứng Lollapalooza)!",
                "trigger_question": "Tôi có đang ngoan cố vì sĩ diện đã trót tuyên bố không? Kẻ đang thuyết phục tôi có thực tài hay chỉ mượn danh uy quyền? Có bao nhiêu thiên kiến đang cùng lúc kích động tôi?"
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

    # =========================================================================
    # NHÓM 7: LÝ THUYẾT HỆ THỐNG PHỨC HỢP & ĐIỀU KHIỂN HỌC
    # =========================================================================
    "systems_complex": {
        "id": "systems_complex",
        "category": "🕸️ Hệ Thống Phức Hợp",
        "title": "Hệ Thống Phức Hợp: Vòng Lặp, Nút Thắt & Biên An Toàn",
        "icon": "🕸️",
        "tagline": "Nén tư duy hệ thống và kỹ thuật điều khiển học vào 3 nguyên lý sống còn",
        "summary": "Vòng lặp phản hồi, Thuyết điểm nghẽn (Theory of Constraints), Độ trễ hệ thống, Điểm lỗi đơn lẻ và Biên an toàn (Margin of Safety).",
        "chunks": [
            {
                "id": "chunk_1",
                "label": "TRỤ 1: VÒNG LẶP PHẢN HỒI & ĐỘ TRỄ HỆ THỐNG",
                "sub_modes": "(1) Vòng lặp Phản hồi Dương khuếch đại (Reinforcing Loop) + (2) Vòng lặp Phản hồi Âm cân bằng (Balancing Loop) + (3) Độ trễ Hệ thống (System Delays)",
                "principle": "1. Vòng lặp dương làm gia tăng liên tục dẫn đến bùng nổ theo cấp số nhân hoặc sụp đổ dây chuyền ➔ 2. Vòng lặp âm hoạt động như chiếc van điều nhiệt tự động kéo hệ thống về trạng thái cân bằng ổn định ➔ 3. Tác động can thiệp hôm nay nhưng hậu quả thường chỉ xuất hiện sau một khoảng trễ thời gian dài gây ảo tưởng kiểm soát.",
                "anchor_name": "CỬA RA VÀO PHÒNG",
                "anchor_icon": "🚪",
                "crazy_image": "Ngay tại CỬA RA VÀO: (1) Một quả cầu tuyết lăn từ đỉnh cửa xuống chân cửa tự lăn tự phình to bằng ngôi nhà (Vòng lặp dương khuếch đại), (2) một chiếc phao nổi tự động đóng chặt vòi nước khi mực nước dâng tới mép cửa (Vòng lặp âm cân bằng), (3) chiếc vòi tắm nước nóng ngay cửa vặn hết cỡ 5 phút sau mới bắt đầu phụt ra nước sôi làm bỏng rát người đứng tắm (Độ trễ hệ thống)!",
                "trigger_question": "Hệ thống đang nằm trong vòng xoáy tự khuếch đại hay tự triệt tiêu? Độ trễ từ hành động đến kết quả là bao lâu? Tôi có đang quá tay vì kết quả chưa xuất hiện ngay?"
            },
            {
                "id": "chunk_2",
                "label": "TRỤ 2: NÚT THẮT CỔ CHAI & ĐIỂM LỖI ĐƠN LẺ",
                "sub_modes": "(1) Thuyết Điểm nghẽn Goldratt (Theory of Constraints) + (2) Điểm Lỗi Đơn lẻ (Single Point of Failure - SPOF) + (3) Cân bằng Động Le Chatelier",
                "principle": "1. Năng lực của toàn bộ chuỗi sản xuất chỉ bằng năng lực của mắt xích thắt cổ chai yếu nhất ➔ 2. Một hệ thống không có phương án dự phòng sẽ sụp đổ hoàn toàn nếu mắt xích duy nhất (SPOF) gặp sự cố ➔ 3. Khi một hệ thống cân bằng bị tác động ngoại lực, nó sẽ tự chuyển dịch theo hướng làm giảm thiểu tác động của ngoại lực đó.",
                "anchor_name": "MÀN HÌNH MÁY TÍNH",
                "anchor_icon": "🖥️",
                "crazy_image": "Trên MÀN HÌNH MÁY TÍNH: (1) Một đường ống nước khổng lồ nhưng ở giữa bị thắt lại bé bằng ngón tay út, nước ứ đọng cuồn cuộn không thể chảy qua (Nút thắt cổ chai Goldratt), (2) một cây cầu dây văng khổng lồ chỉ treo lơ lửng bằng đúng một sợi cáp thép duy nhất đang bị nứt gỉ (Điểm lỗi đơn lẻ SPOF), (3) khi ai đó lấy búa gõ vào màn hình thì một lò xo đối nghịch tự bung ra hấp thụ toàn bộ lực đập trả lại trạng thái cũ (Cân bằng Le Chatelier)!",
                "trigger_question": "Đâu là nút thắt cổ chai duy nhất đang kìm hãm tốc độ? Mắt xích chết người nào nếu đứt sẽ làm sụp đổ toàn bộ? Hệ thống sẽ tự phản ứng kháng cự ra sao?"
            },
            {
                "id": "chunk_3",
                "label": "TRỤ 3: BIÊN AN TOÀN & THIẾT KẾ DỰ PHÒNG DƯ THỪA",
                "sub_modes": "(1) Biên An toàn Graham (Margin of Safety) + (2) Kỹ thuật Dự phòng Dư thừa (Redundancy Engineering) + (3) Tính Chống Mong manh Taleb (Antifragile)",
                "principle": "1. Luôn chừa lại một khoảng đệm an toàn đủ lớn để hấp thụ sai số của các giả định ➔ 2. Luôn có hệ thống song song thứ hai sẵn sàng tiếp quản khi hệ thống thứ nhất chết ➔ 3. Không chỉ chống chọi với biến động mà còn học cách mạnh mẽ và tiến hóa hơn sau những cú sốc và hỗn loạn.",
                "anchor_name": "CHIẾC BÀN & GHẾ NGỒI",
                "anchor_icon": "🪑",
                "crazy_image": "Tại CHIẾC BÀN & GHẾ NGỒI: (1) Một chiếc cầu trên bàn tải trọng thiết kế 50 tấn dù biển báo chỉ cho xe 10 tấn chạy qua (Biên an toàn Graham), (2) dưới gầm ghế gắn sẵn hai động cơ máy phát điện dự phòng tự động nổ máy khi nguồn chính mất điện (Dự phòng dư thừa Redundancy), (3) chiếc bàn làm bằng loại hợp kim Hydras thần kỳ, cứ mỗi lần bị búa đập lõm thì lại tự tôi luyện cứng chắc hơn gấp bội lần (Chống mong manh Antifragile)!",
                "trigger_question": "Biên an toàn của tôi là bao nhiêu %? Nếu nguồn điện/kênh bán hàng chính bị cắt, hệ thống dự phòng có kích hoạt ngay không? Hệ thống có trở nên mạnh hơn sau khủng hoảng?"
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
