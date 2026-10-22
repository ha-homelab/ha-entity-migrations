# 설치와 CLI

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

[문서 색인](../../README.md#documentation)

Python 3.11 이상을 사용하세요. 전용 가상 환경을 만들고 활성화한 뒤 체크아웃에서 `python3 -m pip install -e .`를 실행하세요. 패키지에는 런타임 의존성이 없지만 pip가 빌드 백엔드를 받을 수 있습니다. 오프라인 컴퓨터는 wheel과 빌드 의존성을 미리 준비하세요. `ha-entity-migrations --version`으로 선택한 설치를 확인하면 설치된 패키지 버전을 표시합니다.

CLI에는 명령 두 개가 있고 전역 언어 옵션은 명령 앞에 둡니다.

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint`는 정확한 파일 바이트의 SHA-256을 소문자로 출력합니다. 파일이 JSON으로 유효한지는 검사하지 않습니다. 매니페스트의 스냅샷 및 소스 지문은 공백을 포함해 정확히 그 파일과 일치해야 합니다. 예상하지 못한 드리프트를 없애려고 지문만 갱신하지 말고 새 입력을 먼저 비교하고 승인하세요.

`plan`은 JSON 매니페스트, 정규화된 JSON 스냅샷, 그리고 `--root` 기준으로 `manifest.sources`에 명시된 파일만 읽습니다. 디렉터리를 재귀 탐색하거나 홈을 검색하지 않습니다. 기본 출력은 JSON입니다. `--lang en|ru|de|es`는 사람이 읽는 메시지만 바꾸며, 필드 이름과 진단 코드는 안정적입니다. 최상위와 각 명령에서 `--help`를 사용할 수 있습니다. 적용, 업로드, 탐색, 인증 명령은 없습니다.

종료 상태:

- **0:** 지원되는 입력 범위가 내부적으로 일관되어 검토할 준비가 되었습니다.
- **2:** 잘못된 인자/입력, 읽을 수 없는 파일, 스키마/한계 위반입니다.
- **3:** 구조적으로 유효한 입력이 충돌이나 미해결 범위 등으로 차단된 계획을 만들었습니다.

인자 파싱 후 입력 실패는 `status: invalid`를 담은 JSON 외곽 구조를 stdout에 출력합니다. 인자 오류는 번역된 사용법을 stderr에 출력합니다. 지문 생성 성공 시에는 해시만 출력합니다. 텍스트 모드에서도 편집 제안 기록은 기계용 필드 이름을 유지하고 설명만 번역합니다.

운영 파일은 비공개 디렉터리에 보관하세요. stdout을 리다이렉트하면 자신의 보고서가 생기며, 식별 가능한 엔터티 이름과 경로가 들어갈 수 있습니다. 도구 자체는 아무것도 쓰지 않습니다. `python3 -m pip uninstall ha-entity-migrations`로 제거하세요. 개발자 검사는 [CONTRIBUTING](../../CONTRIBUTING.md)을 참고하세요.
