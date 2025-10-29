# Web Trắc Nghiệm Tin Học - 288 Câu Hỏi

## 🎓 Giới thiệu
Web trắc nghiệm tin học cơ bản với 288 câu hỏi, giao diện hiện đại và dễ sử dụng.

## ✨ Tính năng
- ✅ 288 câu hỏi trắc nghiệm tin học cơ bản (đã được trích xuất từ PDF)
- ✅ Hiển thị ngẫu nhiên câu hỏi, không lặp lại
- ✅ Danh sách câu hỏi từ 1-288 bên sidebar
- ✅ Highlight câu đúng (màu xanh) và câu sai (màu đỏ)
- ✅ Lưu tiến trình tự động (LocalStorage)
- ✅ Thống kê kết quả real-time
- ✅ Tìm kiếm và lọc câu hỏi
- ✅ Giao diện responsive, thân thiện với mobile
- ✅ Phím tắt: ← → để chuyển câu, R để random

## 🚀 Cách sử dụng

### 1. Chạy web
Mở file `index.html` bằng trình duyệt web (Chrome, Firefox, Edge...)

## 📁 Cấu trúc thư mục
```
Web_CauHoi_TinHoc/
├── index.html                          # Trang chính
├── style.css                           # Stylesheet
├── script.js                           # Logic ứng dụng
├── questions.json                      # Dữ liệu 288 câu hỏi
├── DE CUONG _TRAC NGHIEM CO BAN.pdf   # File PDF gốc
├── extract_pdf.py                      # Script trích xuất PDF (Python)
├── parse_questions.py                  # Script parse câu hỏi (Python)
├── full_text.txt                       # Text từ PDF
└── README.md                           # Hướng dẫn
```

## 🎨 Tính năng giao diện

### Header
- Thống kê: Đã làm, Đúng, Sai, Tỷ lệ %
- Nút làm lại để reset tiến trình

### Khu vực câu hỏi
- Hiển thị số thứ tự câu hỏi
- Nội dung câu hỏi và 4 đáp án
- Feedback ngay lập tức khi chọn đáp án
- Nút điều hướng: Câu trước, Câu sau, Random

### Sidebar danh sách câu hỏi
- Grid 5 cột hiển thị số câu 1-300
- Màu xanh: Câu đã trả lời đúng
- Màu đỏ: Câu đã trả lời sai
- Màu xám: Câu chưa làm
- Màu tím: Câu đang xem
- Tìm kiếm theo số câu
- Lọc: Tất cả, Đúng, Sai, Chưa làm

## 💾 Lưu trữ
Tiến trình được lưu tự động vào LocalStorage của trình duyệt, bạn có thể thoát và quay lại sau mà không mất dữ liệu.

## 🎯 Keyboard Shortcuts
- `←` : Câu trước
- `→` : Câu sau  
- `R` : Câu ngẫu nhiên

## 📱 Responsive
- Desktop: Layout 2 cột (câu hỏi + sidebar)
- Tablet: Layout 1 cột, sidebar dưới
- Mobile: Tối ưu cho màn hình nhỏ

## 🔧 Tùy chỉnh

### Thay đổi màu sắc
Chỉnh sửa CSS variables trong `style.css`:
```css
:root {
    --primary-color: #4f46e5;
    --success-color: #10b981;
    --error-color: #ef4444;
}
```

### Thay đổi số lượng cột sidebar
Trong `style.css`, tìm:
```css
.question-list {
    grid-template-columns: repeat(5, 1fr);
}
```

## 📝 Template dữ liệu JSON
Mỗi câu hỏi cần có cấu trúc:
```json
{
    "id": 1,
    "question": "Nội dung câu hỏi",
    "answers": ["A", "B", "C", "D"],
    "correctAnswer": 0
}
```

## 🐛 Troubleshooting
- **Câu hỏi không hiển thị:** Kiểm tra format JSON trong `script.js`
- **Không lưu tiến trình:** Kiểm tra LocalStorage có bị block không
- **Lỗi hiển thị:** Xóa cache trình duyệt và reload

## 📞 Hỗ trợ
Nếu cần hỗ trợ thêm, vui lòng liên hệ hoặc tạo issue.

---
Made with ❤️ for students
