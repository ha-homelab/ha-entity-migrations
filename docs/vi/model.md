# Mô hình đầu vào

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/model.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/model.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/model.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/model.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/model.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/model.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/model.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/model.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/model.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/model.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/model.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/model.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/model.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/model.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/model.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/model.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/model.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/model.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/model.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/model.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/model.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/model.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/model.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/model.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Cài đặt](installation.md) · [Ví dụ](examples.md)

Mọi tài liệu dùng JSON UTF-8 nghiêm ngặt. Khóa trùng, số không hữu hạn và trường lược đồ không xác định đều bị từ chối. Ví dụ chính xác trong `examples/` là tham chiếu có thể chạy. Trường phiên bản phải là số nguyên `1`, không phải chuỗi hay boolean.

## Ảnh chụp trạng thái

Đối tượng cấp cao nhất chỉ chứa `version` và `entities`. Mỗi thực thể chứa chính xác:

- `entity_id`: ID miền/đối tượng viết thường, như `light.workbench`.
- `hardware_id`: định danh riêng tư không diễn giải, do người vận hành chọn.
- `channel`: định danh kênh vật lý, dạng chuỗi.
- `role`: mục đích logic duy nhất, như `workbench` hoặc `pump_enable`.
- `capabilities`: chuỗi duy nhất mô tả khả năng, ví dụ `on_off`.

Cặp phần cứng/kênh xác định điểm cuối vật lý. ID thực thể, điểm cuối vật lý và vai trò logic phải lần lượt là duy nhất. Biểu diễn chẩn đoán vật lý bằng kênh khác, ví dụ `rssi`, với vai trò riêng duy nhất. Vai trò là nhãn lập kế hoạch, không phải khu vực, nhãn hay lớp thiết bị HA. Các khai báo này không phải phép đo; công cụ không thể kiểm chứng với phần cứng.

## Tệp kê khai

Đối tượng cấp cao nhất có chính xác `version`, `snapshot_sha256`, `sources`, `assignments` và `consumers`. `sources` ánh xạ tên tệp tương đối sang giá trị băm SHA-256. `assignments` chứa bản ghi thực thể thay thế đầy đủ cho điểm cuối vật lý đã có trong ảnh chụp. Điểm cuối không được liệt kê giữ nguyên. Để thêm thiết bị mới, trước hết đưa điểm cuối dự phòng đã quan sát vào ảnh chụp. Không có tạo/xóa phần cứng ngầm và phiên bản này yêu cầu vai trò duy nhất.

Mỗi đối tượng sử dụng xác định một **giá trị chuỗi hằng** bằng `file` và `pointer` RFC 6901. Mã hóa `/` thành `~1` và `~` thành `~0`; chỉ số danh sách bắt đầu từ 0, không có số 0 ở đầu. Mọi tham chiếu được phát hiện cần chính sách tường minh:

- `follows_role`: tìm đích sở hữu vai trò logic của nguồn.
- `follows_hardware`: giữ kênh vật lý nguồn và dùng ID thực thể mới của nó.
- `retire`: đề xuất xóa đối tượng tường minh `retire_scope` chứa tham chiếu.

Đối tượng không bị loại bỏ còn cần `kind` (`action`, `display`, `reference`), `allowed_roles` (không rỗng) và `required_capabilities` (có thể rỗng). Hành động cần `service_pointer`. Các ràng buộc này ngăn dùng bơm vừa đổi mục đích làm đích chiếu sáng. Đây là khai báo, không phải ý định suy luận.

Đối tượng bị loại bỏ có chính xác bốn trường: file, pointer, policy và retire_scope. Phạm vi phải là đối tượng tổ tiên khác gốc. Nó chỉ được chứa tham chiếu đến cùng nguồn bị loại bỏ; tham chiếu hỗn hợp hoặc động sẽ chặn. Chọn toàn bộ tự động hóa cũ nếu xóa hành động sẽ để lại chuỗi rỗng không hợp lệ. Công cụ không chạy bộ kiểm tra lược đồ HA.

## Thay đổi miền

Với hành động qua light/switch, chỉ hỗ trợ `turn_on`, `turn_off`, `toggle` và các dịch vụ `homeassistant.*` tương ứng. `data` hoặc `data_template` không rỗng không được chấp nhận khi chuyển dịch vụ tự động. Dịch vụ riêng của miền có nhiều đích hằng bị chặn. Con trỏ dịch vụ phải sở hữu đích dưới hành động của nó. Thay đổi miền hiển thị luôn cần xem xét thủ công tính năng thẻ; công tắc không thể âm thầm kế thừa điều khiển độ sáng.

## Giới hạn

2 MiB mỗi tệp; tổng nguồn 16 MiB; 64 tệp; 5.000 thực thể, phép gán hoặc đối tượng sử dụng; độ sâu JSON 40 và 100.000 nút giá trị mỗi tệp. Định danh là chuỗi không rỗng tối đa 256 ký tự; danh sách khả năng/vai trò được phép tối đa 64 chuỗi duy nhất. Đường dẫn tương đối không được đi lên thư mục cha, là đường dẫn tuyệt đối hay chứa liên kết tượng trưng. Chỉ nhận tệp thường.

Bộ nạp từ chối hai tên nguồn dẫn đến cùng đường dẫn chuẩn hoặc danh tính tệp mở (thiết bị/inode). Điều này gồm dấu phân cách lặp, liên kết cứng và bí danh chữ hoa/thường trên hệ thống không phân biệt hoa thường. Giữ một tên và cập nhật đối tượng sử dụng; bí danh không được mang chính sách di chuyển khác nhau cho một tệp vật lý. Các tệp độc lập có nội dung giống nhau vẫn hợp lệ. API thuần `plan` không truy cập hệ thống tệp: bên gọi tự xây dựng ánh xạ nguồn phải áp dụng ranh giới danh tính này trước khi gọi.
