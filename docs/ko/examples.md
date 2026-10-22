# 자세한 예제

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

[입력 모델](model.md) · [아키텍처](architecture.md)

여기의 하드웨어와 역할은 모두 합성 예제입니다. `python3 tools/generate_examples.py`로 같은 입력을 다시 만듭니다. 어떤 명령도 Home Assistant에 연결하지 않습니다.

## 용도를 바꾼 플러그에서 램프 역할 옮기기

`examples/role-swap`에 대한 README 명령을 실행하세요. 처음에 `plug-a/1`은 `light.workbench`를, `plug-b/1`은 `switch.spare`를 소유합니다. 매니페스트는 플러그 A에 펌프 역할을, 플러그 B에 작업대 역할을 할당합니다. 조명 자동화는 `follows_role`을 사용하고 `workbench`만 허용합니다. 대상 하드웨어는 바뀌지만 엔터티 참조는 `light.workbench`로 유지됩니다. 텍스트 편집이 없는 것이 의도한 결과이며 누락된 마이그레이션이 아닙니다. 보고서의 `assignments`에는 사람이 검토할 하드웨어 변경이 들어 있습니다.

이전 예비 소비자는 `/1`, 즉 두 번째 자동화 객체 전체에서 폐기됩니다. 빈 동작 시퀀스를 남기지 않습니다. 보고서는 조언일 뿐 프로그램이 JSON 배열 요소를 삭제하지 않습니다. 제안된 여러 배열 삭제를 수동 적용한다면 이동하는 인덱스를 고려하고 새 스냅샷에서 다시 실행하세요.

첫 정책을 `follows_hardware`로 바꾸고 허용 역할을 `workbench`로 유지하면 계획은 `role_not_allowed`로 차단됩니다. 허용 역할 목록에 펌프를 추가하는 것은 명시적이고 위험한 의도 변경이며, 오류를 없애는 일반적인 방법이 아닙니다. 올바른 정책을 복원하세요.

## 릴레이를 light에서 switch로 바꾸기

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

제안된 두 편집은 대상과 그 `light.turn_off` 서비스를 바꿉니다. 소스 동작에 밝기 데이터를 추가하고 승인된 소스 지문을 갱신한 뒤 다시 실행하면 `service_data_review`가 자동 변환을 차단합니다. 도구를 통과시키려고 밝기 설정을 버리지 말고 원하는 동작을 검토하세요.

## 해결되지 않은 템플릿

`examples/blocked-template`에 같은 명령을 실행하세요. 대상은 동적 Jinja입니다. 도구는 평가하지 않으며 코드 3을 반환합니다. 완전하고 지원되는 계획은 입증 가능한 리터럴 대상이 있는 명시적 설정을 요구합니다. 그렇지 않으면 준비된 범위 밖의 문서화된 수동 마이그레이션으로 남겨 두세요. 종료 코드를 무시해도 템플릿이 해결되지는 않습니다.

## 드리프트와 반복 가능성

매니페스트 해시를 바꾸지 않고 소스를 편집하면 `stale_source`가 발생합니다. 스냅샷을 편집하면 `stale_snapshot`이 발생합니다. 이런 오래된 모델에는 참조 편집 후보를 출력하지 않습니다. 파일이 같다면 선택한 언어를 제외하고 JSON 결과는 결정적입니다. 소스 파일은 바이트 단위로 그대로 유지됩니다.

실제 프로젝트에서는 형식을 비공개 폴더에 복사하고 물리 식별을 검증하고 소비자를 열거한 뒤 계획기를 실행하세요. 모든 할당과 편집을 검토하고 기존 배포 절차에서 HA 자체 검사를 수행한 다음, 새 읽기 전용 스냅샷을 만들어 결과를 검증하세요. 이 프로젝트는 그 배포나 롤백 실행기를 구현하지 않습니다.
