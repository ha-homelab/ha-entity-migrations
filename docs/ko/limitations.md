# 제한과 검토 경계

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

[아키텍처](architecture.md) · [보안](../../SECURITY.md)

계획의 정확성은 물리 기기/채널/역할 선언과 제공한 파일에 달려 있습니다. 이 도구는 빠진 대시보드, 기기 트리거, 장면, 블루프린트, 다른 곳의 자동화, Matter 필터, 외부 클라이언트, 숨겨진 통합 상태를 발견하지 않습니다. 준비된 보고서를 완전한 Home Assistant 감사라고 부르지 마세요. 이 릴리스에서 역할은 고유해야 하며, 다대다 의미 역할과 그룹은 수동으로 분해해야 합니다.

JSON 설정 소스를 지원합니다. YAML 자체, include, 별칭, 앵커, 실행 가능한 태그, 사용자 정의 구성 요소, 런타임 생성 템플릿은 해석하지 않습니다. 정규화는 이 릴리스 밖의 작업이며 의미를 잃을 수 있습니다. 원본을 보존하고 동등성을 검토하세요. 지원되는 JSON도 Home Assistant의 전체 설정 스키마와 대조하지 않습니다. 명시적 소비자 객체를 지우면 잘못된 부모가 남을 수 있습니다. 그 부모를 검토하고 일반 스테이징 과정에서 HA 설정 검사기를 실행하세요.

기능과 허용 역할은 명시적 제약이지 추론된 안전성이 아닙니다. 도구는 이전에 무해했던 콘센트에 펌프나 차고 구동 장치가 꽂혔는지 알 수 없습니다. 보고된 릴레이 상태는 접점/부하 동작을 입증하지 않습니다. 이름 확인만 하려고 집 전체 스크립트를 실행하거나 작동 중인 가전의 전원을 껐다 켜지 마세요. 물리적 시운전은 별도로 통제된 절차에 속합니다.

이 릴리스는 계획 적용, 레지스트리 엔터티 이름 변경, 고유 ID 변경, HA 다시 로드, 컨트롤러 재시작, 통합 폐기, 변경 롤백을 수행하지 않습니다. 반환 연산은 조언이며 실행 가능한 JSON Patch가 아닙니다. 수동 적용한다면 새 스냅샷을 확보하고 검토한 변경마다 이후를 검증하세요. 인덱스와 버전이 달라졌을 수 있습니다. 해시는 서명이나 접근 제어를 제공하지 않습니다.

보고서에는 비공개 이름과 식별자가 들어갈 수 있습니다. 공개 Git, 이슈 트래커, CI 산출물에서 제외하세요. 공개 예제는 합성 기기를 사용하며 현장 검증을 주장하지 않습니다. 진단은 설계상 계획을 차단합니다. 강제 플래그, 무시 목록, 숨겨진 허용 모드는 없습니다.
