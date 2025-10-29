# Deploy Web Trắc Nghiệm lên Vercel

## 🚀 Cách 1: Deploy qua Vercel Dashboard (Dễ nhất)

### Bước 1: Tạo tài khoản Vercel
1. Truy cập https://vercel.com
2. Click "Sign Up" và đăng nhập bằng GitHub/GitLab/Bitbucket
3. Hoặc đăng ký bằng email

### Bước 2: Deploy từ máy tính

#### Option A: Kéo thả (Drag & Drop)
1. Đăng nhập vào https://vercel.com/new
2. Kéo toàn bộ thư mục `Web_CauHoi_TinHoc` vào
3. Click "Deploy"
4. Đợi 30 giây - Xong! 🎉

#### Option B: Sử dụng Vercel CLI
```bash
# Cài đặt Vercel CLI
npm install -g vercel

# Đăng nhập
vercel login

# Deploy
cd Web_CauHoi_TinHoc
vercel

# Làm theo hướng dẫn trên terminal
```

### Bước 3: Cấu hình (nếu cần)
- **Project Name:** Đặt tên dự án (vd: `trac-nghiem-tin-hoc`)
- **Framework:** Chọn `Other` (static site)
- **Root Directory:** Để mặc định `./`
- **Build Command:** Để trống
- **Output Directory:** Để trống

### Bước 4: Nhận link web
Sau khi deploy xong, bạn sẽ nhận được link dạng:
```
https://your-project-name.vercel.app
```

## 🚀 Cách 2: Deploy qua GitHub (Tự động)

### Bước 1: Tạo GitHub Repository
1. Vào https://github.com/new
2. Đặt tên repo (vd: `trac-nghiem-tin-hoc`)
3. Click "Create repository"

### Bước 2: Push code lên GitHub
```bash
cd d:\Projects\Web_CauHoi_TinHoc

# Khởi tạo git
git init
git add .
git commit -m "Initial commit: Web trắc nghiệm tin học"

# Thêm remote
git remote add origin https://github.com/YOUR_USERNAME/trac-nghiem-tin-hoc.git
git branch -M main
git push -u origin main
```

### Bước 3: Kết nối Vercel với GitHub
1. Đăng nhập https://vercel.com
2. Click "New Project"
3. Click "Import Git Repository"
4. Chọn repo `trac-nghiem-tin-hoc`
5. Click "Deploy"

### Bước 4: Tự động deploy
- Mỗi lần bạn push code lên GitHub, Vercel sẽ tự động deploy
- Không cần làm gì thêm!

## ⚙️ Files quan trọng đã tạo

### `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "index.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

### `.vercelignore`
File này giúp loại bỏ các file không cần deploy:
- Python scripts (extract_pdf.py, parse_questions.py)
- PDF gốc (quá lớn)
- full_text.txt

## 📊 Những gì sẽ được deploy

✅ **Được deploy:**
- index.html
- style.css
- script.js
- questions.json (288 câu hỏi)
- README.md
- vercel.json

❌ **Không deploy:**
- *.pdf (quá lớn)
- *.py (script Python)
- full_text.txt

## 🔧 Custom Domain (Tùy chọn)

Nếu bạn có domain riêng:
1. Vào Vercel Dashboard
2. Chọn project
3. Settings > Domains
4. Thêm domain của bạn
5. Cấu hình DNS theo hướng dẫn

## 🎯 Lưu ý quan trọng

### File size
- Vercel miễn phí cho phép deploy file tối đa 100MB
- File `questions.json` của bạn (~200KB) hoàn toàn OK ✅

### Băng thông
- 100GB bandwidth/tháng (miễn phí)
- Đủ cho web trắc nghiệm nhỏ

### SSL/HTTPS
- Vercel tự động cấp SSL certificate
- Web của bạn sẽ có HTTPS miễn phí 🔒

## 🐛 Troubleshooting

### Lỗi: "questions.json not found"
**Nguyên nhân:** File JSON không được deploy
**Giải pháp:** 
- Kiểm tra `.vercelignore` không block file .json
- Đảm bảo questions.json có trong thư mục gốc

### Lỗi: CORS khi load JSON
**Nguyên nhân:** Browser block fetch local file
**Giải pháp:** Deploy lên Vercel sẽ fix tự động

### Web không load câu hỏi
**Kiểm tra:**
1. Mở Developer Tools (F12)
2. Tab Console - xem lỗi
3. Tab Network - xem request questions.json

## 📱 Sau khi deploy

1. **Test trên nhiều thiết bị:**
   - Desktop
   - Mobile
   - Tablet

2. **Chia sẻ link:**
   - Gửi cho bạn bè
   - Đăng lên mạng xã hội
   - Thêm vào CV 😄

3. **Cập nhật sau này:**
   ```bash
   # Sửa code
   git add .
   git commit -m "Update: thêm câu hỏi mới"
   git push
   # Vercel tự động deploy!
   ```

## 🎓 Tổng kết

**Cách nhanh nhất:**
1. Vào https://vercel.com/new
2. Kéo thả thư mục vào
3. Nhận link - Xong!

**Thời gian:** ~2 phút
**Chi phí:** Miễn phí 100%

---

Chúc bạn deploy thành công! 🚀
