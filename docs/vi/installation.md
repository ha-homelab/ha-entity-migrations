# Cài đặt và CLI

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/installation.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/installation.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/installation.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/installation.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/installation.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/installation.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/installation.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/installation.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/installation.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/installation.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/installation.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/installation.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/installation.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/installation.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/installation.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/installation.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/installation.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/installation.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/installation.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/installation.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/installation.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/installation.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/installation.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/installation.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Mục lục tài liệu](../../README.md#documentation)

Dùng Python 3.11 trở lên. Tạo và kích hoạt môi trường ảo riêng, rồi chạy `python3 -m pip install -e .` từ bản sao kho mã. Gói không có phụ thuộc lúc chạy; pip có thể tải bộ máy dựng gói. Với máy ngoại tuyến, chuẩn bị trước wheel và phụ thuộc dựng gói. Xác minh bản cài đặt đã chọn bằng `ha-entity-migrations --version`; lệnh hiển thị phiên bản gói đang cài.

CLI có hai lệnh, với tùy chọn ngôn ngữ toàn cục đặt trước lệnh:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` in SHA-256 viết thường của chính xác các byte trong tệp. Nó không kiểm tra tệp có phải JSON hợp lệ hay không. Dấu vân tay ảnh chụp và nguồn trong tệp kê khai phải khớp chính xác, kể cả khoảng trắng. Không cập nhật dấu vân tay chỉ để bỏ qua sai lệch bất ngờ; hãy so sánh và phê duyệt đầu vào mới trước.

`plan` đọc tệp kê khai JSON, ảnh chụp JSON đã chuẩn hóa và chỉ các tệp được nêu rõ trong `manifest.sources`, tương đối với `--root`. Công cụ không duyệt đệ quy thư mục hoặc tìm trong thư mục cá nhân. Đầu ra mặc định là JSON. Chỉ thông báo cho con người thay đổi với `--lang en|ru|de|es`; tên trường và mã chẩn đoán vẫn ổn định. `--help` có ở cấp cao nhất và từng lệnh. Không có lệnh áp dụng, tải lên, khám phá hay xác thực.

Trạng thái thoát:

- **0:** phạm vi đầu vào được hỗ trợ nhất quán nội bộ và sẵn sàng xem xét.
- **2:** đối số/đầu vào không hợp lệ, tệp không đọc được hoặc vi phạm lược đồ/giới hạn.
- **3:** đầu vào hợp lệ về cấu trúc tạo kế hoạch bị chặn do xung đột hoặc phạm vi chưa giải quyết.

Lỗi đầu vào sau khi phân tích đối số tạo lớp bao JSON trên stdout với `status: invalid`. Lỗi đối số in hướng dẫn đã bản địa hóa ra stderr. Tính dấu vân tay thành công chỉ in giá trị băm. Trong chế độ văn bản, các bản ghi chỉnh sửa giữ tên trường máy; phần giải thích được dịch.

Giữ tệp vận hành trong thư mục riêng tư. Chuyển hướng stdout tạo báo cáo riêng, có thể chứa tên thực thể và đường dẫn mang tính định danh. Bản thân công cụ không ghi gì. Gỡ cài đặt bằng `python3 -m pip uninstall ha-entity-migrations`. Xem kiểm tra cho nhà phát triển tại [CONTRIBUTING](../../CONTRIBUTING.md).
