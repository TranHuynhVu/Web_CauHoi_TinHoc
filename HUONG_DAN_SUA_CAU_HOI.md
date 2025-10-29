# Hướng dẫn thêm/chỉnh sửa câu hỏi

## 📝 Cách thêm câu hỏi mới vào file questions.json

### Format của mỗi câu hỏi:
```json
{
  "id": 289,
  "question": "Nội dung câu hỏi của bạn?",
  "answers": [
    "Đáp án A",
    "Đáp án B",
    "Đáp án C",
    "Đáp án D"
  ],
  "correctAnswer": 0
}
```

**Lưu ý:**
- `id`: Số thứ tự câu hỏi (phải là số nguyên duy nhất)
- `question`: Nội dung câu hỏi
- `answers`: Mảng 4 đáp án (A, B, C, D)
- `correctAnswer`: Index của đáp án đúng (0=A, 1=B, 2=C, 3=D)

## 🔧 Cách chỉnh sửa câu hỏi

1. Mở file `questions.json`
2. Tìm câu hỏi cần sửa theo `id`
3. Chỉnh sửa nội dung
4. Lưu file
5. Reload trang web

## ⚠️ Lưu ý khi chỉnh sửa

- Đảm bảo format JSON đúng (dấu phẩy, ngoặc, quotes)
- Không trùng `id` giữa các câu hỏi
- `correctAnswer` phải từ 0 đến 3
- Luôn có đủ 4 đáp án

## 🐛 Kiểm tra lỗi JSON

Nếu web không load được câu hỏi, có thể file JSON bị lỗi format.

Kiểm tra bằng công cụ:
- Online: https://jsonlint.com/
- VS Code: Có built-in JSON validator

## 📊 Thống kê hiện tại

- Tổng số câu hỏi: **288 câu**
- Nguồn: DE CUONG _TRAC NGHIEM CO BAN.pdf
- Format: Multiple choice (4 đáp án)

## 🔄 Cập nhật lại từ PDF

Nếu có file PDF mới, chạy lại script:

```bash
# Bước 1: Trích xuất text từ PDF
python extract_pdf.py

# Bước 2: Parse câu hỏi thành JSON
python parse_questions.py
```

Script sẽ tự động tạo file `questions.json` mới.
