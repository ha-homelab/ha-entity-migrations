# Architektura i kontrakt raportu

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

[Model](model.md) · [Ograniczenia](limitations.md)

![Przepływ danych tylko do odczytu](../diagrams/pipeline.svg)

`io.py` egzekwuje limity plików, ścieżek i JSON oraz dokładne wskaźniki. `planner.py` sprawdza deklaracje, buduje mapy przed/po, analizuje wartości źródłowe, rozstrzyga jawne zasady i gromadzi diagnostykę. `cli.py` dodaje przetłumaczone komunikaty i wypisuje raport. `i18n.py` zawiera cztery pełne katalogi komunikatów. Ta ścieżka nie zależy od sieci ani Home Assistanta.

Skaner jest celowo zachowawczy. Ciągi będące dokładnymi odwołaniami do encji są sprawdzane względem migawki. Ciągi z osadzonymi odwołaniami pozostają nierozstrzygnięte. Szablony w kluczach lub wartościach i klucze celów urządzenie/obszar/etykieta pozostają nierozstrzygnięte, nawet jeśli interpretacja wydaje się prosta. Zwykłe pola usług nie są traktowane jako identyfikatory encji; dynamiczne usługi pozostają nierozstrzygnięte. Pliki inne niż JSON są rejestrowane jako nieobsługiwane źródła i blokują planowanie. Nie jest to ogólny parser HA.

![Podejmowanie decyzji według zasad](../diagrams/policy.svg)

## Stabilna koperta JSON, wersja schematu 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Dla poprawnych wejść `status` to ready lub blocked. `scope` zawsze ma wartość `supplied_files_only`; `read_only` zawsze true. Błędy wejścia używają mniejszej koperty invalid opisanej w instalacji.

Zmiany mają operację, plik i wskaźnik. `replace_reference` zawiera też before/after/policy; `replace_service` zawiera before/after; `remove_consumer` zawiera wycofywane odwołanie. To **nie są wykonywalne operacje JSON Patch**. Brakuje semantyki transakcji, przesunięć indeksów i cyklu życia HA. Traktuj je jako propozycje do przeglądu; ta wersja celowo nie dostarcza mechanizmu stosowania poprawek.

Diagnostyka zawiera stabilne `code`, `location`, `severity` i przetłumaczone `message`. Zarówno `error`, jak i `unresolved` blokują plan. Raporty `blocked` mogą zawierać kandydatów zmian dla nieobjętych problemem odwołań, ale żaden nie stanowi gotowej transakcji. Nieaktualne lub sprzeczne modele początkowe wstrzymują wszystkie propozycje zmian odwołań. Przypisania zawsze odzwierciedlają model żądany przez użytkownika, nigdy wykonane zmiany.

Raporty sortują źródła, przypisania, zmiany i diagnostykę dla powtarzalności. Nie zawierają bieżących znaczników czasu ani zmyślonych ocen pewności. Skróty bajtów dowodzą, którą wersję wejścia zbadano, a nie jej prawdziwości ani tego, czy urządzenie wykona polecenie.
