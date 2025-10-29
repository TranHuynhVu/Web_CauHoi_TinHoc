"""
Script sửa lỗi encoding tiếng Việt bị tách ký tự
Ví dụ: "Ki ến" -> "Kiến", "đư ới" -> "dưới"
"""

def fix_vietnamese_encoding(text):
    """
    Sửa lỗi ký tự tiếng Việt bị tách bởi khoảng trắng
    """
    import re
    
    # Pattern 1: Xử lý các trường hợp cụ thể thường gặp
    patterns = [
        # Các từ thường gặp bị lỗi
        (r'Ki ến', 'Kiến'), (r'ki ến', 'kiến'),
        (r'Đ ể', 'Để'), (r'đ ể', 'để'),
        (r'ch ọn', 'chọn'), (r'Ch ọn', 'Chọn'),
        (r'ngu ồn', 'nguồn'), (r'Ngu ồn', 'Nguồn'),
        (r'h ộp', 'hộp'), (r'H ộp', 'Hộp'),
        (r'Nh ấn', 'Nhấn'), (r'nh ấn', 'nhấn'),
        (r'dư ới', 'dưới'), (r'Dư ới', 'Dưới'),
        (r'n ền', 'nền'), (r'N ền', 'Nền'),
        (r'Shu tdown', 'Shutdown'),
        (r'ch ống', 'chống'), (r'Ch ống', 'Chống'),
        (r't ốt', 'tốt'), (r'T ốt', 'Tốt'),
        (r'Thư ờng', 'Thường'), (r'thư ờng', 'thường'),
        (r'ki ểm', 'kiểm'), (r'Ki ểm', 'Kiểm'),
        (r'đ ĩa', 'đĩa'), (r'Đ ĩa', 'Đĩa'),
        (r'd ữ', 'dữ'), (r'D ữ', 'Dữ'),
        (r'c ập', 'cập'), (r'C ập', 'Cập'),
        (r'đ ặt', 'đặt'), (r'Đ ặt', 'Đặt'),
        (r't ệp', 'tệp'), (r'T ệp', 'Tệp'),
        (r'thư m ục', 'thư mục'), (r'Thư m ục', 'Thư mục'),
        (r'đư ợc', 'được'), (r'Đư ợc', 'Được'),
        (r'ch ữ', 'chữ'), (r'Ch ữ', 'Chữ'),
        (r'b ộ', 'bộ'), (r'B ộ', 'Bộ'),
        (r'nh ớ', 'nhớ'), (r'Nh ớ', 'Nhớ'),
        (r'thi ết', 'thiết'), (r'Thi ết', 'Thiết'),
        (r'đi ện', 'điện'), (r'Đi ện', 'Điện'),
        (r'trư ờng', 'trường'), (r'Trư ờng', 'Trường'),
        (r'phù h ợp', 'phù hợp'), (r'Phù h ợp', 'Phù hợp'),
        (r'đ ơn', 'đơn'), (r'Đ ơn', 'Đơn'),
        (r'nh ất', 'nhất'), (r'Nh ất', 'Nhất'),
        (r'xư ởng', 'xưởng'), (r'Xư ởng', 'Xưởng'),
        (r't ốc', 'tốc'), (r'T ốc', 'Tốc'),
        (r'đ ộ', 'độ'), (r'Đ ộ', 'Độ'),
        (r'kh ối', 'khối'), (r'Kh ối', 'Khối'),
        (r'k ỹ', 'kỹ'), (r'K ỹ', 'Kỹ'),
        (r'thu ật', 'thuật'), (r'Thu ật', 'Thuật'),
        (r'ch ương', 'chương'), (r'Ch ương', 'Chương'),
        (r'trình l ệnh', 'trình lệnh'), (r'Trình l ệnh', 'Trình lệnh'),
        (r'h ệ', 'hệ'), (r'H ệ', 'Hệ'),
        (r'đi ều', 'điều'), (r'Đi ều', 'Điều'),
        (r'khi ển', 'khiển'), (r'Khi ển', 'Khiển'),
        (r't ự', 'tự'), (r'T ự', 'Tự'),
        (r'đ ộng', 'động'), (r'Đ ộng', 'Động'),
        (r'n ội', 'nội'), (r'N ội', 'Nội'),
        (r'ngo ại', 'ngoại'), (r'Ngo ại', 'Ngoại'),
        (r'nh ập', 'nhập'), (r'Nh ập', 'Nhập'),
        (r'xu ất', 'xuất'), (r'Xu ất', 'Xuất'),
        (r'hi ển', 'hiển'), (r'Hi ển', 'Hiển'),
        (r'th ị', 'thị'), (r'Th ị', 'Thị'),
        (r'k ết', 'kết'), (r'K ết', 'Kết'),
        (r'n ối', 'nối'), (r'N ối', 'Nối'),
        (r'b ị', 'bị'), (r'B ị', 'Bị'),
        (r'ng ười', 'người'), (r'Ng ười', 'Người'),
        (r'l ập', 'lập'), (r'L ập', 'Lập'),
        (r'gi ải', 'giải'), (r'Gi ải', 'Giải'),
        (r'tr ên', 'trên'), (r'Tr ên', 'Trên'),
        (r'c ần', 'cần'), (r'C ần', 'Cần'),
        (r'nh ững', 'những'), (r'Nh ững', 'Những'),
        (r't ín', 'tín'), (r'T ín', 'Tín'),
        (r'hi ệu', 'hiệu'), (r'Hi ệu', 'Hiệu'),
        (r't ập', 'tập'), (r'T ập', 'Tập'),
        (r'h ợp', 'hợp'), (r'H ợp', 'Hợp'),
        (r't ử', 'tử'), (r'T ử', 'Tử'),
        (r'ứng', 'ứng'), (r'Ứng', 'Ứng'),
        (r'b ảng', 'bảng'), (r'B ảng', 'Bảng'),
        (r's ẽ', 'sẽ'), (r'S ẽ', 'Sẽ'),
        (r'đư ờng', 'đường'), (r'Đư ờng', 'Đường'),
        (r'd ẫn', 'dẫn'), (r'D ẫn', 'Dẫn'),
        (r'c ơ', 'cơ'), (r'C ơ', 'Cơ'),
        (r's ở', 'sở'), (r'S ở', 'Sở'),
        (r'li ệu', 'liệu'), (r'Li ệu', 'Liệu'),
        (r'm ở', 'mở'), (r'M ở', 'Mở'),
        (r't ệp', 'tệp'), (r'T ệp', 'Tệp'),
        (r'ch ứa', 'chứa'), (r'Ch ứa', 'Chứa'),
        (r'm ạng', 'mạng'), (r'M ạng', 'Mạng'),
        (r'c ộng', 'cộng'), (r'C ộng', 'Cộng'),
        (r't ạo', 'tạo'), (r'T ạo', 'Tạo'),
        (r'l ưu', 'lưu'), (r'L ưu', 'Lưu'),
        (r'đ ĩa', 'đĩa'), (r'Đ ĩa', 'Đĩa'),
        (r'c ứng', 'cứng'), (r'C ứng', 'Cứng'),
        (r'm ềm', 'mềm'), (r'M ềm', 'Mềm'),
        (r'ph ần', 'phần'), (r'Ph ần', 'Phần'),
        (r'y ếu', 'yếu'), (r'Y ếu', 'Yếu'),
        (r't ố', 'tố'), (r'T ố', 'Tố'),
    ]
    
    # Áp dụng các pattern cụ thể
    for pattern, replacement in patterns:
        text = text.replace(pattern, replacement)
    
    # Pattern 2: Xử lý tổng quát - chữ cái + space + ký tự có dấu
    vietnamese_chars = 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ'
    vietnamese_chars += vietnamese_chars.upper()
    
    # Xử lý pattern: chữ + space + ký tự có dấu
    pattern = rf'([a-zA-Z{vietnamese_chars}]) ([{vietnamese_chars}])'
    def remove_space(match):
        return match.group(1) + match.group(2)
    
    # Lặp nhiều lần để xử lý các trường hợp liên tiếp
    for _ in range(3):
        text = re.sub(pattern, remove_space, text)
    
    return text

def main():
    print("Đang sửa lỗi encoding file full_text.txt...")
    
    # Đọc file gốc
    with open('full_text.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Kích thước file gốc: {len(content)} ký tự")
    
    # Sửa lỗi encoding
    fixed_content = fix_vietnamese_encoding(content)
    
    # Lưu file đã sửa
    with open('full_text_fixed.txt', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Đã lưu file sửa lỗi vào: full_text_fixed.txt")
    print("\nSo sánh trước và sau:")
    print("=" * 60)
    print("TRƯỚC:")
    print(content[:200])
    print("\nSAU:")
    print(fixed_content[:200])
    print("=" * 60)
    
    # Tự động parse lại questions.json
    print("\n\nĐang parse lại questions.json...")
    import parse_questions
    questions = parse_questions.parse_questions('full_text_fixed.txt')
    
    # Làm sạch text
    for q in questions:
        q['question'] = parse_questions.clean_text(q['question'])
        q['answers'] = [parse_questions.clean_text(ans) for ans in q['answers']]
    
    # Lưu ra file JSON
    import json
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Đã parse thành công {len(questions)} câu hỏi!")
    print("✓ Đã lưu vào questions.json")
    
    # Hiển thị 3 câu đầu
    print("\n" + "=" * 60)
    print("3 câu hỏi đầu tiên (đã sửa):")
    print("=" * 60)
    for q in questions[:3]:
        print(f"\nCâu {q['id']}: {q['question']}")
        for i, ans in enumerate(q['answers']):
            marker = " ✓" if i == q['correctAnswer'] else ""
            print(f"  {chr(65+i)}. {ans}{marker}")

if __name__ == "__main__":
    main()
