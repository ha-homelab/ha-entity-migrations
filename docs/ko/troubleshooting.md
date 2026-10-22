# 문제 해결

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

[설치](installation.md) · [제한](limitations.md)

**명령을 찾을 수 없음:** 설치할 때 쓴 같은 가상 환경을 활성화하세요. `python3 -m ha_entity_migrations --version`을 시도하고, 경로 불일치를 피하려고 시스템 Python에 설치하지 마세요.

**종료 2, schema_invalid:** 실행 가능한 예제 및 [입력 모델](model.md)과 키를 비교하세요. 알 수 없는 필드는 오류입니다. 버전은 정수 1이고 채널 식별자는 문자열입니다. 모든 동작 정책은 서비스 포인터가 필요합니다. 스냅샷에는 엔터티가, 매니페스트에는 할당과 소비자가 있으며 서로 교환할 수 없습니다.

**종료 2, duplicate_source:** 두 소스 이름이 같은 물리 파일을 가리킵니다. `sources`에 정규 이름 하나를 유지하고 소비자의 모든 `file` 필드를 갱신하세요. 중복 구분자 또는 하드 링크/대소문자 별칭을 제거하고 별칭에 두 번째 정책을 주지 마세요. 내용이 같은 별도 파일은 계속 지원합니다.

**stale_snapshot / stale_source:** 실제 변경을 승인된 소스와 비교하세요. 검토한 뒤에만 지문 명령을 사용하세요. 공백 변경도 해시에 영향을 줍니다. 이전 해시를 통과시키려고 오래된 사본을 가리키지 마세요.

**source_collision / destination_collision:** 물리 채널, 역할, 엔터티 ID가 중복되었습니다. 역할 교환의 양쪽을 명시하고, 바꾸지 않은 엔드포인트가 원하는 대상 ID를 유지하는지 확인하세요.

**role_not_allowed / capability_missing:** 소비자가 부적절한 부하에 도달하거나 기능을 잃게 됩니다. 역할을 따라야 하는지 하드웨어를 따라야 하는지 확인하세요. allowed_roles를 자동 확장하거나 하드웨어에 없는 기능을 주장하지 마세요. 켜기/끄기 릴레이로 바뀐 조명은 밝기 조절을 할 수 없습니다.

**missing_policy / unmodeled_reference:** 참조된 엔드포인트를 조사하고 목적을 확인한 후에만 명시적 소비자 선언을 추가하세요. 오래된 기록 문자열은 활성 범위 밖일 수 있습니다. 그 파일을 계획 범위에서 의도적으로 제외하고 제외를 문서화한 뒤 소스 계약을 다시 만드세요.

**dynamic_reference / embedded_reference / indirect_target:** 이 릴리스는 매핑을 입증할 수 없습니다. Jinja 또는 그룹/영역/레이블 동작을 별도로 검토하거나 명시적으로 정규화한 리터럴 설정을 제공하세요. 프로그램은 템플릿을 실행하지 않습니다.

**display_domain_review / service_data_review / mixed_action_targets:** 카드 기능, 동작 매개변수, 대상 묶음을 점검하세요. 여러 도메인에 걸친 동작은 별도 검토한 소스 변경에서 나누고, 서비스 도메인만 바꾸지 마세요.

**retire_scope_mixed / overlapping_edits:** 관련 없는 참조 없이 일관된 오래된 소비자 객체를 선택하세요. 동작에서 entity_id만 지우면 범위가 넓은 대상이나 잘못된 설정이 생길 수 있습니다. 프로그램은 자동 폐기를 적용하지 않습니다.

**unsupported_source:** JSON만 계획할 수 있습니다. YAML, 바이너리, 기타 파일을 조용히 건너뛰지 않습니다. 명시적으로 정규화한 JSON 사본이 분석에 도움이 될 수 있지만 실제 편집 전에 원본과 비교해야 합니다.

최소 합성 입력, 도구/Python 버전, 종료 코드, 진단 코드로 버그를 보고하세요. 가정 환경의 원본 내보내기나 API 자격 증명은 절대 첨부하지 마세요.
