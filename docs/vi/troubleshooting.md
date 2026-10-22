# Khắc phục sự cố

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/troubleshooting.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/troubleshooting.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/troubleshooting.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/troubleshooting.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/troubleshooting.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/troubleshooting.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/troubleshooting.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/troubleshooting.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/troubleshooting.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/troubleshooting.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/troubleshooting.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/troubleshooting.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/troubleshooting.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/troubleshooting.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/troubleshooting.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/troubleshooting.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/troubleshooting.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/troubleshooting.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/troubleshooting.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/troubleshooting.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/troubleshooting.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/troubleshooting.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/troubleshooting.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/troubleshooting.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Cài đặt](installation.md) · [Giới hạn](limitations.md)

**Không tìm thấy lệnh:** kích hoạt đúng môi trường ảo dùng khi cài. Thử `python3 -m ha_entity_migrations --version`; không cài vào Python hệ thống chỉ để tránh đường dẫn không khớp.

**Thoát 2, schema_invalid:** so sánh khóa với ví dụ chạy được và [mô hình đầu vào](model.md). Trường không xác định là lỗi. Phiên bản là số nguyên 1; định danh kênh là chuỗi. Mọi chính sách hành động cần con trỏ dịch vụ. Ảnh chụp có thực thể; tệp kê khai có phép gán và đối tượng sử dụng. Hai tệp không thể thay thế nhau.

**Thoát 2, duplicate_source:** hai tên nguồn xác định một tệp vật lý. Giữ một tên chuẩn trong `sources` và cập nhật mọi trường `file` của đối tượng sử dụng. Bỏ dấu phân cách trùng hoặc bí danh liên kết cứng/hoa thường; không cấp chính sách thứ hai cho bí danh. Tệp riêng có nội dung giống nhau vẫn được hỗ trợ.

**stale_snapshot / stale_source:** so sánh thay đổi thực với nguồn đã phê duyệt. Chỉ dùng fingerprint sau khi xem xét. Khoảng trắng làm thay đổi giá trị băm. Không trỏ đến bản sao cũ chỉ để khớp hàm băm cũ.

**source_collision / destination_collision:** kênh vật lý, vai trò hoặc ID thực thể bị trùng. Thể hiện tường minh cả hai phía của hoán đổi vai trò và kiểm tra điểm cuối không đổi có đang giữ ID đích mong muốn hay không.

**role_not_allowed / capability_missing:** đối tượng sử dụng sẽ tác động tải không phù hợp hoặc mất khả năng. Xác nhận nó phải theo vai trò hay phần cứng. Không tự động mở rộng allowed_roles hay khai báo khả năng phần cứng không có. Đèn thay bằng rơ-le bật/tắt không thể điều chỉnh độ sáng.

**missing_policy / unmodeled_reference:** kiểm kê điểm cuối được tham chiếu và chỉ thêm khai báo đối tượng sử dụng sau khi xác nhận mục đích. Chuỗi lịch sử cũ có thể ngoài phạm vi hoạt động; chủ động loại tệp khỏi phạm vi, ghi lại việc loại trừ và tạo lại hợp đồng nguồn.

**dynamic_reference / embedded_reference / indirect_target:** phiên bản này không thể chứng minh ánh xạ. Xem xét riêng Jinja hoặc hành vi nhóm/khu vực/nhãn, hoặc cung cấp cấu hình hằng đã chuẩn hóa tường minh. Chương trình không bao giờ thực thi mẫu.

**display_domain_review / service_data_review / mixed_action_targets:** kiểm tra tính năng thẻ, tham số hành động và nhóm đích. Tách hành động đa miền trong thay đổi nguồn được xem xét riêng; không chỉ đổi miền của dịch vụ.

**retire_scope_mixed / overlapping_edits:** chọn đối tượng sử dụng cũ nhất quán, không có tham chiếu không liên quan. Không chỉ xóa entity_id khỏi hành động: điều đó có thể tạo đích quá rộng hoặc cấu hình sai. Chương trình không tự động áp dụng việc loại bỏ.

**unsupported_source:** chỉ JSON có thể được lập kế hoạch. YAML, tệp nhị phân và loại khác không bị âm thầm bỏ qua. Bản sao JSON chuẩn hóa tường minh có thể hỗ trợ phân tích nhưng phải đối chiếu bản gốc trước mọi chỉnh sửa thật.

Báo lỗi với đầu vào tổng hợp tối thiểu, phiên bản công cụ/Python, mã thoát và mã chẩn đoán. Không bao giờ đính kèm bản xuất nguyên gốc của nhà hay thông tin xác thực API.
