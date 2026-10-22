# Rozwiązywanie problemów

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

[Instalacja](installation.md) · [Ograniczenia](limitations.md)

**Nie znaleziono polecenia:** aktywuj środowisko wirtualne użyte do instalacji. Spróbuj `python3 -m ha_entity_migrations --version`; nie instaluj w systemowym Pythonie tylko po to, by ominąć błędną ścieżkę.

**Wyjście 2, schema_invalid:** porównaj klucze z wykonywalnym przykładem i [modelem wejścia](model.md). Nieznane pola są błędami. Wersje to liczba całkowita 1; identyfikatory kanałów to tekst. Każda zasada akcji potrzebuje wskaźnika usługi. Migawka ma encje, manifest przypisania i konsumentów. To nie są zamienne pliki.

**Wyjście 2, duplicate_source:** dwie nazwy oznaczają jeden plik fizyczny. Zostaw jedną nazwę kanoniczną w `sources` i zmień wszystkie pola `file` konsumentów. Usuń podwójne separatory lub aliasy dowiązań twardych/wielkości liter; nie dawaj aliasowi drugiej zasady. Osobne pliki o identycznej treści pozostają obsługiwane.

**stale_snapshot / stale_source:** porównaj rzeczywiste zmiany z zatwierdzonym źródłem. Użyj fingerprint dopiero po ich ocenie. Białe znaki zmieniają skrót. Nie wskazuj starej kopii tylko po to, by pasował dawny hash.

**source_collision / destination_collision:** kanał fizyczny, rola lub ID encji jest powtórzone. Jawnie przedstaw obie strony zamiany ról i sprawdź, czy niezmieniony punkt nie zachowuje pożądanego ID docelowego.

**role_not_allowed / capability_missing:** konsument trafiłby do niewłaściwego obciążenia lub utracił możliwość. Potwierdź, czy ma podążać za rolą czy sprzętem. Nie rozszerzaj automatycznie allowed_roles i nie deklaruj możliwości nieobecnych w sprzęcie. Światło zastąpione przekaźnikiem włącz/wyłącz nie oferuje ściemniania.

**missing_policy / unmodeled_reference:** zinwentaryzuj wskazany punkt i dodaj jawną deklarację konsumenta dopiero po potwierdzeniu celu. Stary wpis historii może nie należeć do aktywnego zakresu; świadomie wyklucz ten plik, opisz wykluczenie i wygeneruj ponownie kontrakt źródeł.

**dynamic_reference / embedded_reference / indirect_target:** ta wersja nie może dowieść mapowania. Sprawdź osobno Jinja lub zachowanie grup/obszarów/etykiet albo dostarcz jawną znormalizowaną konfigurację literalną. Program nigdy nie wykonuje szablonu.

**display_domain_review / service_data_review / mixed_action_targets:** sprawdź funkcje kart, parametry akcji i grupy celów. Podziel akcję wielodomenową w oddzielnie ocenionej zmianie źródła; nie zmieniaj tylko domeny usługi.

**retire_scope_mixed / overlapping_edits:** wybierz spójny przestarzały obiekt konsumenta bez obcych odwołań. Nie usuwaj jedynie entity_id z akcji: może to stworzyć szeroki cel lub niepoprawną konfigurację. Program nie wykonuje automatycznego wycofywania.

**unsupported_source:** planować można tylko JSON. YAML, pliki binarne i inne nie są po cichu pomijane. Jawnie znormalizowana kopia JSON może pomóc analizie, ale przed rzeczywistą edycją musi zostać porównana z oryginałem.

Zgłaszaj błędy z minimalnym wejściem syntetycznym, wersjami narzędzia/Pythona, kodem wyjścia i kodami diagnostycznymi. Nigdy nie załączaj surowego eksportu domu ani poświadczeń API.
