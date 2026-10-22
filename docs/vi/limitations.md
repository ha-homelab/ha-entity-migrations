# Giới hạn và ranh giới xem xét

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/limitations.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/limitations.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/limitations.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/limitations.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/limitations.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/limitations.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/limitations.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/limitations.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/limitations.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/limitations.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/limitations.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/limitations.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/limitations.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/limitations.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/limitations.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/limitations.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/limitations.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/limitations.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/limitations.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/limitations.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/limitations.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/limitations.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/limitations.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/limitations.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Kiến trúc](architecture.md) · [Bảo mật](../../SECURITY.md)

Độ chính xác của kế hoạch phụ thuộc vào khai báo phần cứng/kênh/vai trò và tệp bạn cung cấp. Công cụ không khám phá bảng điều khiển bị bỏ sót, bộ kích hoạt thiết bị, cảnh, blueprint, tự động hóa lưu nơi khác, bộ lọc Matter, máy khách bên ngoài hay trạng thái ẩn của tích hợp. Không gọi báo cáo sẵn sàng là kiểm toán Home Assistant đầy đủ. Mỗi vai trò là duy nhất trong phiên bản này; vai trò ngữ nghĩa nhiều-nhiều và nhóm cần phân tách thủ công.

Nguồn cấu hình JSON được hỗ trợ. YAML, include, bí danh, neo, thẻ thực thi, thành phần tùy chỉnh và mẫu sinh lúc chạy không được diễn giải. Chuẩn hóa nằm ngoài phiên bản này và có thể làm mất ngữ nghĩa; giữ bản gốc và kiểm tra tính tương đương. Ngay cả JSON được hỗ trợ cũng không được đối chiếu với toàn bộ lược đồ cấu hình HA. Xóa đối tượng sử dụng tường minh có thể để lại đối tượng cha không hợp lệ; kiểm tra cha và chạy bộ kiểm tra cấu hình HA trong quy trình thử nghiệm trước triển khai thông thường.

Khả năng và vai trò được phép là ràng buộc tường minh, không phải suy luận an toàn. Công cụ không biết một bơm hay động cơ cửa gara đã được cắm vào ổ trước đây vô hại. Trạng thái rơ-le được báo không chứng minh hành vi tiếp điểm/tải. Không chạy script cho cả nhà hoặc ngắt rồi cấp điện lại thiết bị đang hoạt động chỉ để xác minh tên. Đưa phần cứng vào vận hành cần quy trình kiểm soát riêng.

Phiên bản này không áp dụng kế hoạch, đổi tên thực thể trong registry, sửa ID duy nhất, tải lại HA, khởi động lại bộ điều khiển, loại bỏ tích hợp hay hoàn tác thay đổi. Thao tác trả về là khuyến nghị, không phải JSON Patch thực thi. Nếu áp dụng thủ công, lấy ảnh chụp mới và xác minh sau từng thay đổi đã xem xét; chỉ số và phiên bản có thể đã đổi. Hàm băm không cung cấp chữ ký hay kiểm soát truy cập.

Báo cáo có thể chứa tên và định danh riêng tư. Không đưa chúng lên Git công khai, trình theo dõi issue hay hiện vật CI. Ví dụ công khai dùng thiết bị tổng hợp và không tuyên bố đã kiểm chứng thực địa. Chẩn đoán chặn kế hoạch theo thiết kế; không có cờ ép buộc, danh sách bỏ qua hay chế độ dễ dãi ẩn.
