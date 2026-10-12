# 🧊 Rubik 3D AI Simulator & Mechanics Explorer

Ứng dụng giả lập Rubik 3D tương tác cao cấp viết bằng Python Streamlit và WebGL / 3D Canvas, tích hợp thuật toán AI gợi ý đường đi ngắn nhất, phân tích cơ chế tháo rời linh kiện (Exploded View), bộ đếm số lượt xoay, đồng hồ bấm giờ (Timer) và phím tắt chuẩn WCA.

---

## ✨ Tính Năng Nổi Bật

1. **Giả lập không gian 3D mượt mà (60 FPS):**
   - Hỗ trợ xoay góc nhìn 3D tự do (360 độ) bằng chuột/cảm ứng, phóng to thu nhỏ (Zoom).
   - Hoạt họa xoay mặt (Face rotation) mượt mà bằng phần cứng GPU (hardware-accelerated), không bị giật hay khựng khung hình.
   - Hàng đợi lệnh (Move queue) thông minh: nhấn nhiều phím liên tiếp sẽ thực thi nhịp nhàng, không lỗi trạng thái.

2. **Hệ thống điều khiển phím tắt chuẩn WCA:**
   - `U`, `D`, `L`, `R`, `F`, `B`: Xoay các mặt theo chiều kim đồng hồ.
   - `Shift + Phím`: Xoay ngược chiều kim đồng hồ (Prime moves).
   - `Phím Space`: Bắt đầu / Tạm dừng đồng hồ bấm giờ.
   - Các nút bấm cảm ứng trực quan hỗ trợ mọi thiết bị.

3. **Hai chế độ trải nghiệm:**
   - **Chế độ Người giải (Human Solve):** Đồng hồ bấm giờ chính xác từng mili-giây, đếm tổng số lượt xoay (Move Count), kiểm tra trạng thái hoàn thành và chúc mừng khi phá kỷ lục.
   - **Chế độ AI Giải & Huấn luyện (AI Solve & Training):** AI tính toán chuỗi đường đi ngắn nhất (Shortest Path) kèm giải thích chi tiết từng bước, hỗ trợ tự động giải (Auto-play với thanh trượt chỉnh tốc độ) hoặc đi từng bước (Step-by-step).

4. **Chế độ Rời bộ phận (Exploded View & Mechanics Anatomy):**
   - Kéo thanh trượt để tách rời 26 mảnh khỏi tâm ở khoảng cách tùy ý.
   - Trực quan hóa **Lõi trục 3D 6 nhánh (Core Spider & Springs)**, **6 Mảnh Tâm (Center Caps)**, **12 Mảnh Cạnh (Edge Torpedoes)** và **8 Mảnh Góc (Corner Feet)**.
   - Giải thích chi tiết nguyên lý hoạt động, cơ chế rãnh trượt chống văng (anti-pop) và lò xo nén hỗ trợ cắt góc (corner-cutting).

5. **Trình tạo xáo trộn ngẫu nhiên (Scramble Generator):**
   - Sinh công thức xáo trộn 20 bước chuẩn thi đấu quốc tế WCA (World Cube Association).
   - Tự động thực hiện xoay xáo trộn trên màn hình 3D.

---

## 🚀 Cài Đặt & Khởi Chạy

### 1. Yêu cầu hệ thống
- Python 3.8+
- Trình duyệt hiện đại hỗ trợ WebGL (Chrome, Edge, Firefox, Safari).

### 2. Cài đặt thư viện
```bash
git clone https://github.com/your-username/rubik-3d-ai-simulator.git
cd rubik-3d-ai-simulator
pip install -r requirements.txt
```

### 3. Chạy ứng dụng Streamlit
```bash
streamlit run app.py
```
Sau đó mở trình duyệt tại địa chỉ `http://localhost:8501`.

---

## 📁 Cấu Trúc Dự Án

```
rubik-3d-ai-simulator/
├── app.py                  # Giao diện chính Streamlit và điều khiển
├── solver.py               # Thuật toán AI giải, tối ưu hóa và sinh công thức WCA
├── rubik_component.html    # Thành phần WebGL / 3D Canvas hiệu năng cao
├── requirements.txt        # Danh sách thư viện Python
└── README.md               # Tài liệu hướng dẫn sử dụng
```

---

## 🎯 Hướng Dẫn Sử Dụng Phím Bấm

| Phím Bấm | Thao Tác | Ý Nghĩa |
| :---: | :---: | :--- |
| `U` / `Shift+U` | Xoay mặt Trên | Mặt Trắng (Up) |
| `D` / `Shift+D` | Xoay mặt Đáy | Mặt Vàng (Down) |
| `L` / `Shift+L` | Xoay mặt Trái | Mặt Cam (Left) |
| `R` / `Shift+R` | Xoay mặt Phải | Mặt Đỏ (Right) |
| `F` / `Shift+F` | Xoay mặt Trước | Mặt Xanh lá (Front) |
| `B` / `Shift+B` | Xoay mặt Sau | Mặt Xanh dương (Back) |
| `Space` | Timer | Bắt đầu / Dừng đồng hồ tính giờ |
| Kéo chuột trái | Xoay 3D | Xoay góc nhìn khối Rubik tự do trong không gian |
| Cuộn chuột | Zoom | Phóng to / Thu nhỏ mô hình |

---

## 📜 Giấy Phép
Dự án được phát hành theo giấy phép mã nguồn mở MIT.
