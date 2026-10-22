# 아키텍처와 보고서 계약

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

[모델](model.md) · [제한](limitations.md)

![읽기 전용 데이터 흐름](../diagrams/pipeline.svg)

`io.py`는 파일/경로/JSON 한계와 정확한 포인터를 강제합니다. `planner.py`는 선언을 검증하고, 전후 매핑을 만들고, 소스 값을 스캔하고, 명시적 정책을 해석하며 진단 기록을 모읍니다. `cli.py`는 번역 메시지를 추가하고 보고서를 출력합니다. `i18n.py`에는 완전한 메시지 카탈로그 네 개가 있습니다. 이 경로에는 네트워크나 Home Assistant 의존성이 없습니다.

스캐너는 의도적으로 보수적입니다. 정확히 엔터티 참조 형태인 문자열을 스냅샷과 대조합니다. 참조가 삽입된 문자열은 미해결 상태입니다. 키나 값의 템플릿, 기기/영역/레이블 대상 키는 쉽게 추측할 수 있어 보여도 미해결입니다. 일반 서비스 필드는 엔터티 ID로 취급하지 않지만 동적 서비스는 미해결 상태입니다. JSON이 아닌 파일은 지원하지 않는 소스로 등록되어 계획을 막습니다. 범용 HA 파서는 아닙니다.

![정책 결정 흐름](../diagrams/policy.svg)

## 안정적인 JSON 외곽 구조, 스키마 버전 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. 유효한 입력의 `status`는 ready 또는 blocked입니다. `scope`는 항상 `supplied_files_only`이고 `read_only`는 항상 true입니다. 입력 오류는 설치 안내서에 설명한 더 작은 invalid 외곽 구조를 사용합니다.

편집에는 연산, 파일, 포인터가 있습니다. `replace_reference`에는 before/after/policy도, `replace_service`에는 before/after도, `remove_consumer`에는 폐기할 참조도 들어갑니다. 이는 **실행 가능한 JSON Patch가 아닙니다**. 트랜잭션, 인덱스 이동, HA 수명 주기 의미가 없습니다. 제안으로 검토하세요. 이 릴리스는 의도적으로 패치 적용기를 제공하지 않습니다.

진단은 안정적인 `code`, `location`, `severity`와 번역된 `message`를 포함합니다. `error`와 `unresolved`는 모두 계획을 차단합니다. `blocked` 보고서에는 영향받지 않는 참조의 편집 후보가 있을 수 있지만, 어느 것도 바로 실행 가능한 트랜잭션은 아닙니다. 오래되거나 충돌하는 초기 모델은 모든 참조 편집 후보를 억제합니다. 할당은 언제나 사용자가 요청한 모델을 되풀이하며, 완료된 변경을 나타내지 않습니다.

재현성을 위해 보고서는 소스, 할당, 편집, 진단을 정렬합니다. 현재 타임스탬프나 임의로 만든 신뢰도 점수는 없습니다. 바이트 해시는 분석한 입력 버전을 입증할 뿐, 입력이 사실인지 또는 기기가 명령을 따를지는 입증하지 않습니다.
