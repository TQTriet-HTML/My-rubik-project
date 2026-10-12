import streamlit as st
import streamlit.components.v1 as components
import random
import os
import sys

# Set Streamlit Page Config
st.set_page_config(
    page_title="Rubik 3D AI Simulator & Mechanics Explorer",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit Shell
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stMetric {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(99, 102, 241, 0.2);
        padding: 12px;
        border-radius: 10px;
    }
    .guide-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .guide-card h4 {
        color: #38bdf8;
        margin-top: 0;
    }
    .badge-key {
        background: #334155;
        color: #facc15;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: monospace;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
col_title, col_stat1, col_stat2 = st.columns([3, 1, 1])
with col_title:
    st.title("🧊 Rubik 3D AI Simulator & Mechanics Explorer")
    st.caption("Mô phỏng 3D Rubik với hoạt họa mượt mà 60fps, AI gợi ý đường đi ngắn nhất, chế độ tháo rời linh kiện (Exploded View), bàn phím chuẩn WCA và đồng hồ bấm giờ.")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Bảng Điều Khiển")
    
    app_mode = st.radio(
        "Chế độ hoạt động:",
        ["🎮 Con người giải (Luyện tập)", "🤖 AI Giải & Huấn luyện (CFOP)", "🔍 Khám phá Cấu tạo 3D (Exploded View)"],
        index=0
    )
    
    st.divider()
    st.subheader("💡 Mẹo luyện tập Speedcubing")
    if "Con người" in app_mode:
        st.info("Nhấn **Phím Space** để Bắt đầu/Dừng Timer. Dùng các phím **U, D, L, R, F, B** (kèm Shift để xoay ngược chiều) để thao tác mà không cần dùng chuột!")
    elif "AI" in app_mode:
        st.success("AI sẽ tính toán các bước giải tối ưu dựa trên trạng thái hiện tại. Bạn có thể bấm 'Next' để học từng bước hoặc bấm 'Tự động giải'.")
    else:
        st.warning("Kéo thanh trượt để bung các mảnh Rubik ra, quan sát cơ chế trục lò xo (Center Core), ngàm cạnh (Edge Torpedo) và chân góc (Corner Feet).")

    st.divider()
    st.markdown("### ⌨️ Phím Tắt Chuẩn WCA")
    st.markdown("""
    - <span class="badge-key">U</span> / <span class="badge-key">Shift+U</span>: Mặt Trên (Up)
    - <span class="badge-key">D</span> / <span class="badge-key">Shift+D</span>: Mặt Đáy (Down)
    - <span class="badge-key">L</span> / <span class="badge-key">Shift+L</span>: Mặt Trái (Left)
    - <span class="badge-key">R</span> / <span class="badge-key">Shift+R</span>: Mặt Phải (Right)
    - <span class="badge-key">F</span> / <span class="badge-key">Shift+F</span>: Mặt Trước (Front)
    - <span class="badge-key">B</span> / <span class="badge-key">Shift+B</span>: Mặt Sau (Back)
    - <span class="badge-key">Space</span>: Bắt đầu / Dừng Timer
    """, unsafe_allow_html=True)

# Load the embedded 3D WebGL / CSS 3D Engine
HTML_FILE_PATH = os.path.join(os.path.dirname(__file__), "rubik_component.html")
if not os.path.exists(HTML_FILE_PATH):
    # Fallback to shared location if needed
    HTML_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "artifacts", "file_generation", "ttl=63d", "output", "rubik_3d_simulator.html")

try:
    with open(HTML_FILE_PATH, "r", encoding="utf-8") as f:
        html_code = f.read()
except Exception:
    html_code = "<h3>Đang tải mô hình Rubik 3D...</h3>"

# Render the interactive 3D Simulator directly in Streamlit
components.html(html_code, height=760, scrolling=False)

# Educational & CFOP Guide Below the 3D Canvas
st.divider()
col_g1, col_g2, col_g3, col_g4 = st.columns(4)

with col_g1:
    st.markdown("""
    <div class="guide-card">
        <h4>1. White Cross</h4>
        <p style="font-size:0.85rem; color:#cbd5e1;">Tạo dấu cộng trắng ở đáy, khớp chính xác 4 tâm màu xung quanh. Người chơi pro luôn hoàn thành trong tối đa 8 bước.</p>
    </div>
    """, unsafe_allow_html=True)

with col_g2:
    st.markdown("""
    <div class="guide-card">
        <h4>2. F2L (First 2 Layers)</h4>
        <p style="font-size:0.85rem; color:#cbd5e1;">Ghép đôi 4 cặp góc - cạnh rồi đưa vào các khe tương ứng. Đây là bước quan trọng nhất quyết định tốc độ Sub-20s.</p>
    </div>
    """, unsafe_allow_html=True)

with col_g3:
    st.markdown("""
    <div class="guide-card">
        <h4>3. OLL (Orient Layer 3)</h4>
        <p style="font-size:0.85rem; color:#cbd5e1;">Lật tất cả các mặt màu vàng lên trên bằng 57 công thức (hoặc 2-Look OLL gồm 10 công thức cho người mới).</p>
    </div>
    """, unsafe_allow_html=True)

with col_g4:
    st.markdown("""
    <div class="guide-card">
        <h4>4. PLL (Permute Layer 3)</h4>
        <p style="font-size:0.85rem; color:#cbd5e1;">Hoán vị các góc và cạnh tầng cuối về đúng vị trí để hoàn thành khối Rubik. Nhận diện nhanh nhờ các dải đèn xe (Headlights).</p>
    </div>
    """, unsafe_allow_html=True)
