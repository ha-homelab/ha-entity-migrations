# 입력 모델

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

[설치](installation.md) · [예제](examples.md)

모든 문서는 UTF-8 엄격 JSON을 사용합니다. 중복 키, 유한하지 않은 숫자, 알 수 없는 스키마 필드는 거부합니다. `examples/`의 정확한 예제가 실행 가능한 기준입니다. 버전 필드는 문자열이나 불리언이 아닌 정수 `1`이어야 합니다.

## 스냅샷

최상위 객체에는 `version`과 `entities`만 있습니다. 각 엔터티는 정확히 다음을 포함합니다.

- `entity_id`: `light.workbench` 같은 소문자 도메인/객체 ID.
- `hardware_id`: 운영자가 고른 비공개 불투명 식별자.
- `channel`: 문자열로 된 물리 채널 식별자.
- `role`: `workbench`나 `pump_enable` 같은 고유한 논리 목적.
- `capabilities`: `on_off`처럼 기능을 설명하는 고유 문자열.

하드웨어/채널 쌍이 물리 엔드포인트를 식별합니다. 엔터티 ID, 물리 엔드포인트, 논리 역할은 각각 고유해야 합니다. 물리 진단은 `rssi` 같은 별도 채널로 표현하고 자체 고유 역할을 부여하세요. 역할은 계획용 레이블이며 Home Assistant 영역, 레이블, 기기 클래스가 아닙니다. 선언은 측정이 아니며 도구는 하드웨어와 대조해 검증할 수 없습니다.

## 매니페스트

최상위 객체에는 정확히 `version`, `snapshot_sha256`, `sources`, `assignments`, `consumers`가 있습니다. `sources`는 상대 파일 이름을 SHA-256 해시에 매핑합니다. `assignments`는 이미 스냅샷에 있는 물리 엔드포인트를 위한 완전한 교체 엔터티 기록을 포함합니다. 나열하지 않은 엔드포인트는 그대로입니다. 새 기기를 도입하려면 먼저 관찰한 예비 엔드포인트를 스냅샷에 넣으세요. 하드웨어를 암묵적으로 만들거나 지우지 않으며, 이 릴리스는 고유한 역할을 요구합니다.

각 소비자는 `file`과 RFC 6901 `pointer`로 **리터럴 문자열 값**을 식별합니다. `/`는 `~1`로, `~`는 `~0`으로 이스케이프하세요. 목록 인덱스는 0부터 시작하며 선행 0은 허용하지 않습니다. 발견된 모든 참조에는 명시적 정책이 필요합니다.

- `follows_role`: 소스의 논리 역할을 가진 대상을 찾습니다.
- `follows_hardware`: 소스 물리 채널을 유지하고 새 엔터티 ID를 사용합니다.
- `retire`: 참조를 포함하는 명시적 `retire_scope` 객체 제거를 제안합니다.

폐기 이외의 소비자는 `kind`(`action`, `display`, `reference`), 비어 있지 않은 `allowed_roles`, 비어 있어도 되는 `required_capabilities`도 필요합니다. 동작에는 `service_pointer`가 필요합니다. 이 관문은 새로 용도를 바꾼 펌프를 조명 대상으로 쓰는 것을 막습니다. 추론한 의도가 아닌 선언입니다.

폐기 소비자에는 정확히 네 필드 file, pointer, policy, retire_scope가 있습니다. 범위는 루트가 아닌 상위 객체여야 합니다. 같은 폐기 소스에 대한 참조만 포함할 수 있으며 혼합 또는 동적 참조는 차단됩니다. 동작 제거가 잘못된 빈 시퀀스를 남긴다면 오래된 자동화 전체를 선택하세요. 도구는 HA 스키마 검증기를 실행하지 않습니다.

## 도메인 변경

light/switch를 넘나드는 동작에는 `turn_on`, `turn_off`, `toggle`, 해당하는 `homeassistant.*` 서비스만 지원합니다. 자동 서비스 변환에는 비어 있지 않은 `data`나 `data_template`를 허용하지 않습니다. 리터럴 대상이 여럿인 도메인 전용 서비스는 차단됩니다. 서비스 포인터는 해당 동작 아래의 대상을 소유해야 합니다. 표시 도메인 변경에는 언제나 카드 기능의 수동 검토가 필요하며, 스위치가 밝기 제어를 조용히 물려받아서는 안 됩니다.

## 한계

파일당 2 MiB, 소스 파일 합계 16 MiB, 파일 64개, 엔터티·할당·소비자 5,000개, 파일당 JSON 깊이 40과 값 노드 100,000개입니다. 식별자는 최대 256자의 비어 있지 않은 문자열이고, 기능/허용 역할 목록은 최대 64개의 고유 문자열입니다. 상대 소스 경로는 위로 이동할 수 없고 절대 경로이거나 심볼릭 링크를 포함할 수 없습니다. 입력은 일반 파일만 가능합니다.

파일 로더는 같은 정규 경로나 열린 파일 식별자(기기/inode)로 해석되는 두 소스 이름을 거부합니다. 반복된 경로 구분자, 하드 링크, 대소문자를 구분하지 않는 파일 시스템의 대소문자 별칭이 여기에 포함됩니다. 소스 이름 하나만 유지하고 소비자를 갱신하세요. 같은 물리 파일에 별칭을 통해 서로 다른 마이그레이션 정책을 둘 수 없습니다. 내용이 같은 독립 파일은 여전히 유효한 입력입니다. 순수 `plan` API는 파일 시스템 접근이 없으므로 소스 매핑을 직접 만드는 호출자는 호출 전에 이 식별 경계를 강제해야 합니다.
