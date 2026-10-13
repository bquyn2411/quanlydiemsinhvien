import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 1. Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.markdown("---")

# Dữ liệu ban đầu
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.0, 8.5, 7.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Cuối kỳ': [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.5],
    'MSSV': ['SV001', 'SV002', 'SV003', 'SV004', 'SV005', 'SV006', 'SV007', 'SV008', 'SV009', 'SV010']
}
df = pd.DataFrame(data)

# Tính điểm tổng kết và xếp loại
df['Tổng kết'] = (0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# Sắp xếp lại thứ tự cột hiển thị cho đẹp
df_display = df[['Họ và tên', 'Chuyên cần', 'Giữa kỳ', 'Cuối kỳ', 'Tổng kết', 'Xếp loại']]

# 2. Hiển thị bảng điểm của 10 sinh viên
st.subheader("📋 Bảng điểm 10 sinh viên")
st.dataframe(df_display, use_container_width=True)

# 3, 4, 5. Các thông số thống kê chung
dtb_lop = df['Tổng kết'].mean()
max_sv = df.loc[df['Tổng kết'].idxmax()]
min_sv = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = len(df[df['Tổng kết'] >= 5.0])

st.subheader("📊 Thống kê chung của lớp")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm TB của lớp", f"{dtb_lop:.2f}")
col2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
col3.metric("Cao nhất", f"{max_sv['Họ và tên']} ({max_sv['Tổng kết']})")
col4.metric("Thấp nhất", f"{min_sv['Họ etên'] if 'Họ etên' in min_sv else min_sv['Họ và tên']} ({min_sv['Tổng kết']})")

st.markdown("---")

# 6 & 7. Danh sách xổ xuống chọn sinh viên và hiển thị chi tiết
st.subheader("🔍 Tra cứu thông tin chi tiết sinh viên")
selected_name = st.selectbox("Chọn tên sinh viên để xem chi tiết:", df['Họ và tên'].tolist())

# Lọc thông tin sinh viên được chọn
selected_student = df[df['Họ và tên'] == selected_name].iloc[0]

s_col1, s_col2, s_col3, s_col4, s_col5 = st.columns(5)
s_col1.metric("Chuyên cần", selected_student['Chuyên cần'])
s_col2.metric("Giữa kỳ", selected_student['Giữa kỳ'])
s_col3.metric("Cuối kỳ", selected_student['Cuối kỳ'])
s_col4.metric("Tổng kết", selected_student['Tổng kết'])
s_col5.metric("Xếp loại", selected_student['Xếp loại'])

st.markdown("---")

# 8. Biểu đồ cột điểm tổng kết của 10 sinh viên
st.subheader("📈 Biểu đồ cột điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Họ và tên'], df['Tổng kết'], color='skyblue', edgecolor='black')
ax.set_xlabel('Tên sinh viên', fontsize=12)
ax.set_ylabel('Điểm tổng kết', fontsize=12)
ax.set_title('Biểu đồ cột điểm tổng kết của 10 sinh viên', fontsize=14, fontweight='bold')
ax.set_ylim(0, 10)

for i, val in enumerate(df['Tổng kết']):
    ax.text(i, val + 0.2, str(val), ha='center', va='bottom', fontsize=10)

st.pyplot(fig)

# 9. Hiển thị họ tên và MSSV của người tạo ứng dụng ở cuối trang (chữ nhỏ)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "Người tạo ứng dụng: Nguyễn Bảo Quyên - MSSV: 001308001583"
    "</p>", 
    unsafe_allow_html=True
)
