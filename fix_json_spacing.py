"""
Script sửa các lỗi encoding còn sót lại trong questions.json
"""
import json
import re

def fix_missing_spaces(text):
    """Thêm lại space bị mất giữa các từ"""
    
    # Dictionary các từ bị dính
    fixes = {
        'tínhđúng': 'tính đúng',
        'nguồnđiện': 'nguồn điện',
        'Startở': 'Start ở',
        'startở': 'start ở',
        'trađĩa': 'tra đĩa',
        'Sử dụngứng': 'Sử dụng ứng',
        'sử dụngứng': 'sử dụng ứng',
        'vệổđĩa': 'vệ ổ đĩa',
        'Khiđặt': 'Khi đặt',
        'khiđặt': 'khi đặt',
        'khôngđược': 'không được',
        'Khôngđược': 'Không được',
        'sauđây': 'sau đây',
        'Sauđây': 'Sau đây',
        'Ađến': 'A đến',
        'ađến': 'a đến',
        'sốđi': 'số đi',
        'Sốđi': 'Số đi',
        'máyđiều': 'máy điều',
        'Máyđiều': 'Máy điều',
        'làứng': 'là ứng',
        'Làứng': 'Là ứng',
        'dụngđể': 'dụng để',
        'Dụngđể': 'Dụng để',
        'giảiứng': 'giải ứng',
        'Giảiứng': 'Giải ứng',
        'toántrên': 'toán trên',
        'Toántrên': 'Toán trên',
        'Cpuđược': 'Cpu được',
        'cpuđược': 'cpu được',
        'CPUđược': 'CPU được',
        'bộxử': 'bộ xử',
        'Bộxử': 'Bộ xử',
        'xửlý': 'xử lý',
        'Xửlý': 'Xử lý',
        'nhớtrong': 'nhớ trong',
        'Nhớtrong': 'Nhớ trong',
        'trongcủa': 'trong của',
        'Trongcủa': 'Trong của',
        'củamáy': 'của máy',
        'Củamáy': 'Của máy',
        'thiết bịngoại': 'thiết bị ngoại',
        'Thiết bịngoại': 'Thiết bị ngoại',
        'ngoạivi': 'ngoại vi',
        'Ngoạivi': 'Ngoại vi',
        'bànphím': 'bàn phím',
        'Bànphím': 'Bàn phím',
        'mànhình': 'màn hình',
        'Mànhình': 'Màn hình',
        'chuột...làthiết': 'chuột... là thiết',
        'Chuột...làthiết': 'Chuột... là thiết',
        'làthiết': 'là thiết',
        'Làthiết': 'Là thiết',
        'thiếtbị': 'thiết bị',
        'Thiếtbị': 'Thiết bị',
        'bịngoại': 'bị ngoại',
        'Bịngoại': 'Bị ngoại',
        'ngoạivi': 'ngoại vi',
        'Ngoạivi': 'Ngoại vi',
        'ổcứng': 'ổ cứng',
        'Ổcứng': 'Ổ cứng',
        'đĩacứng': 'đĩa cứng',
        'Đĩacứng': 'Đĩa cứng',
        'ổđĩa': 'ổ đĩa',
        'Ổđĩa': 'Ổ đĩa',
        'đĩamềm': 'đĩa mềm',
        'Đĩamềm': 'Đĩa mềm',
        'phầnmềm': 'phần mềm',
        'Phầnmềm': 'Phần mềm',
        'phầncứng': 'phần cứng',
        'Phầncứng': 'Phần cứng',
        'yếutố': 'yếu tố',
        'Yếutố': 'Yếu tố',
        'hệđiều': 'hệ điều',
        'Hệđiều': 'Hệ điều',
        'điềuhành': 'điều hành',
        'Điềuhành': 'Điều hành',
        'chươngtrình': 'chương trình',
        'Chươngtrình': 'Chương trình',
        'dữliệu': 'dữ liệu',
        'Dữliệu': 'Dữ liệu',
        'tậptin': 'tập tin',
        'Tậptin': 'Tập tin',
        'thưmục': 'thư mục',
        'Thưmục': 'Thư mục',
        'mạngnội': 'mạng nội',
        'Mạngnội': 'Mạng nội',
        'nộibộ': 'nội bộ',
        'Nộibộ': 'Nội bộ',
        'mạngcộng': 'mạng cộng',
        'Mạngcộng': 'Mạng cộng',
        'cộngđồng': 'cộng đồng',
        'Cộngđồng': 'Cộng đồng',
        # Thêm các lỗi mới phát hiện
        'phảiđịnh': 'phải định',
        'Phảiđịnh': 'Phải định',
        'mảnhđĩa': 'mảnh đĩa',
        'Mảnhđĩa': 'Mảnh đĩa',
        'Đểổ': 'Để ổ',
        'đểổ': 'để ổ',
        'tốcđộ': 'tốc độ',
        'Tốcđộ': 'Tốc độ',
        'từđĩa': 'từ đĩa',
        'Từđĩa': 'Từ đĩa',
        'trongđĩa': 'trong đĩa',
        'Trongđĩa': 'Trong đĩa',
        'Mộtđoạn': 'Một đoạn',
        'mộtđoạn': 'một đoạn',
        'củađĩa': 'của đĩa',
        'Củađĩa': 'Của đĩa',
        'nàođể': 'nào để',
        'Nàođể': 'Nào để',
        'đểlưu': 'để lưu',
        'Đểlưu': 'Để lưu',
        'lưutrữ': 'lưu trữ',
        'Lưutrữ': 'Lưu trữ',
        'trongmáy': 'trong máy',
        'Trongmáy': 'Trong máy',
        'máytính': 'máy tính',
        'Máytính': 'Máy tính',
    }
    
    for wrong, correct in fixes.items():
        text = text.replace(wrong, correct)
    
    # Pattern tổng quát: từ + ký tự có dấu (không có space)
    # Ví dụ: "máyđiều" -> "máy điều"
    vietnamese_chars_with_diacritics = 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ'
    
    # Tìm: chữ cái thường + chữ cái viết hoa có dấu (không có space)
    # Ví dụ: "tínhĐúng" -> "tính Đúng"
    pattern = rf'([a-z{vietnamese_chars_with_diacritics}])([A-ZÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ])'
    text = re.sub(pattern, r'\1 \2', text)
    
    return text

def main():
    print("Đang sửa lỗi encoding trong questions.json...")
    
    # Đọc file JSON
    with open('questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"Tìm thấy {len(questions)} câu hỏi")
    
    # Sửa từng câu hỏi
    for q in questions:
        q['question'] = fix_missing_spaces(q['question'])
        q['answers'] = [fix_missing_spaces(ans) for ans in q['answers']]
    
    # Lưu lại file JSON
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print("✓ Đã sửa xong!")
    
    # Hiển thị 5 câu đầu để kiểm tra
    print("\n" + "=" * 70)
    print("5 câu hỏi đầu tiên (sau khi sửa):")
    print("=" * 70)
    for q in questions[:5]:
        print(f"\nCâu {q['id']}: {q['question']}")
        for i, ans in enumerate(q['answers']):
            marker = " ✓" if i == q['correctAnswer'] else ""
            print(f"  {chr(65+i)}. {ans}{marker}")
    
    print("\n" + "=" * 70)
    print("✅ Hoàn thành! File questions.json đã được sửa encoding.")
    print("=" * 70)

if __name__ == "__main__":
    main()
