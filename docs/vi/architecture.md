# Kiến trúc và hợp đồng báo cáo

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/architecture.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/architecture.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/architecture.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/architecture.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/architecture.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/architecture.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/architecture.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/architecture.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/architecture.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/architecture.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/architecture.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/architecture.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/architecture.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/architecture.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/architecture.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/architecture.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/architecture.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/architecture.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/architecture.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/architecture.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/architecture.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/architecture.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/architecture.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/architecture.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Mô hình](model.md) · [Giới hạn](limitations.md)

![Luồng dữ liệu chỉ đọc](../diagrams/pipeline.svg)

`io.py` áp dụng giới hạn tệp/đường dẫn/JSON và con trỏ chính xác. `planner.py` kiểm tra khai báo, tạo ánh xạ trước/sau, quét giá trị nguồn, giải quyết chính sách tường minh và thu thập chẩn đoán. `cli.py` thêm thông báo đã dịch và in báo cáo. `i18n.py` chứa bốn danh mục thông báo đầy đủ. Luồng này không phụ thuộc mạng hay Home Assistant.

Bộ quét cố ý thận trọng. Chuỗi khớp chính xác dạng tham chiếu thực thể được đối chiếu với ảnh chụp trạng thái. Chuỗi chứa tham chiếu nhúng vẫn chưa được giải quyết. Mẫu trong khóa hoặc giá trị và khóa đích thiết bị/khu vực/nhãn vẫn chưa được giải quyết dù có vẻ dễ đoán. Trường dịch vụ thông thường không được coi là ID thực thể; dịch vụ động vẫn chưa được giải quyết. Tệp không phải JSON được ghi nhận là nguồn không hỗ trợ và chặn lập kế hoạch. Đây không phải bộ phân tích HA tổng quát.

![Luồng quyết định chính sách](../diagrams/policy.svg)

## Lớp bao JSON ổn định, phiên bản lược đồ 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Với đầu vào hợp lệ, `status` là ready hoặc blocked. `scope` luôn là `supplied_files_only`; `read_only` luôn là true. Lỗi đầu vào dùng lớp bao invalid nhỏ hơn được mô tả trong hướng dẫn cài đặt.

Mỗi chỉnh sửa có thao tác, tệp và con trỏ. `replace_reference` còn chứa before/after/policy; `replace_service` chứa before/after; `remove_consumer` chứa tham chiếu cần loại bỏ. Đây **không phải JSON Patch có thể thực thi**. Chúng thiếu ngữ nghĩa giao dịch, dịch chuyển chỉ số và vòng đời HA. Hãy xem xét như đề xuất; phiên bản này cố ý không cung cấp bộ áp dụng bản vá.

Chẩn đoán chứa `code`, `location`, `severity` ổn định và `message` đã dịch. Cả `error` và `unresolved` đều chặn kế hoạch. Báo cáo `blocked` có thể chứa chỉnh sửa ứng viên cho tham chiếu không bị ảnh hưởng, nhưng không chỉnh sửa nào tạo thành giao dịch sẵn sàng. Mô hình ban đầu cũ hoặc mâu thuẫn loại bỏ mọi chỉnh sửa tham chiếu ứng viên. Các phép gán luôn phản ánh mô hình người dùng yêu cầu, không phải thay đổi đã hoàn tất.

Báo cáo sắp xếp nguồn, phép gán, chỉnh sửa và chẩn đoán để tái lập được. Không có dấu thời gian hiện tại hay điểm tin cậy tự đặt. Hàm băm byte chứng minh phiên bản đầu vào đã phân tích, không chứng minh tính đúng đắn của đầu vào hay việc thiết bị sẽ tuân theo lệnh.
