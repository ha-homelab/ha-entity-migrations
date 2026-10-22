# Ví dụ có giải thích

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/examples.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/examples.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/examples.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/examples.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/examples.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/examples.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/examples.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/examples.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/examples.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/examples.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/examples.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/examples.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/examples.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/examples.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/examples.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/examples.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/examples.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/examples.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/examples.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/examples.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/examples.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/examples.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/examples.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/examples.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Mô hình đầu vào](model.md) · [Kiến trúc](architecture.md)

Mọi phần cứng và vai trò ở đây đều là dữ liệu tổng hợp. Tạo lại đầu vào giống hệt bằng `python3 tools/generate_examples.py`. Không lệnh nào kết nối với Home Assistant.

## Vai trò đèn rời ổ cắm đã đổi mục đích

Chạy lệnh README cho `examples/role-swap`. Ban đầu `plug-a/1` sở hữu `light.workbench`, còn `plug-b/1` sở hữu `switch.spare`. Tệp kê khai gán vai trò bơm cho ổ A và vai trò bàn làm việc cho ổ B. Tự động hóa chiếu sáng dùng `follows_role` và chỉ cho phép `workbench`. Tham chiếu vẫn là `light.workbench` trong khi phần cứng đích thay đổi. Không có chỉnh sửa văn bản là kết quả có chủ đích, không phải bỏ sót di chuyển. `assignments` trong báo cáo chứa thay đổi phần cứng để con người xem xét.

Đối tượng sử dụng dự phòng cũ bị loại bỏ tại `/1`, tức toàn bộ đối tượng tự động hóa thứ hai. Điều này không để lại chuỗi hành động rỗng. Báo cáo chỉ mang tính khuyến nghị; chương trình không xóa phần tử mảng JSON. Nếu áp dụng thủ công nhiều đề xuất xóa mảng, hãy tính đến chỉ số bị dịch chuyển và chạy lại từ ảnh chụp mới.

Đổi chính sách đầu tiên thành `follows_hardware` nhưng giữ vai trò được phép là `workbench`: kế hoạch bị chặn với `role_not_allowed`. Mở rộng danh sách để cho phép bơm là thay đổi ý định tường minh và nguy hiểm, không phải cách thông thường để xóa lỗi. Hãy khôi phục chính sách đúng.

## Rơ-le chuyển từ light sang switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Hai chỉnh sửa đề xuất thay đổi đích và dịch vụ `light.turn_off` của nó. Thêm dữ liệu độ sáng vào hành động nguồn, cập nhật dấu vân tay nguồn đã phê duyệt rồi chạy lại: `service_data_review` chặn chuyển đổi tự động. Không bỏ cấu hình độ sáng chỉ để qua kiểm tra; hãy xem xét hành vi mong muốn.

## Mẫu chưa được giải quyết

Chạy cùng lệnh với `examples/blocked-template`. Đích là Jinja động. Công cụ không đánh giá mẫu và trả mã 3. Kế hoạch đầy đủ được hỗ trợ cần cấu hình tường minh với đích hằng có thể chứng minh; nếu không, giữ phần này là di chuyển thủ công có tài liệu bên ngoài phạm vi sẵn sàng. Bỏ qua mã thoát không giải quyết được mẫu.

## Sai lệch và khả năng lặp lại

Sửa nguồn mà không đổi hàm băm trong tệp kê khai tạo ra `stale_source`. Sửa ảnh chụp tạo ra `stale_snapshot`. Không chỉnh sửa tham chiếu ứng viên nào được xuất cho các mô hình cũ này. Với tệp không đổi, kết quả JSON có tính xác định ngoại trừ ngôn ngữ đã chọn. Tệp nguồn giữ nguyên từng byte.

Với dự án thực, sao chép định dạng vào thư mục riêng tư, kiểm tra danh tính vật lý, liệt kê đối tượng sử dụng và chạy bộ lập kế hoạch. Xem xét mọi phép gán và chỉnh sửa, thực hiện kiểm tra riêng của HA trong quy trình triển khai đã thiết lập, rồi tạo ảnh chụp chỉ đọc mới để xác minh kết quả. Dự án không triển khai quy trình đó hay bộ thực hiện hoàn tác.
