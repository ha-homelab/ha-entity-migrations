# Instalacja i CLI

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

[Indeks dokumentacji](../../README.md#documentation)

Użyj Pythona 3.11 lub nowszego. Utwórz i aktywuj osobne środowisko wirtualne, a w kopii repozytorium wykonaj `python3 -m pip install -e .`. Pakiet nie ma zależności wykonawczych; pip może pobrać zaplecze budowania. Dla komputera offline przygotuj wcześniej wheel i zależności budowania. Wybraną instalację sprawdź przez `ha-entity-migrations --version`; polecenie podaje zainstalowaną wersję pakietu.

CLI ma dwa polecenia; globalna opcja języka poprzedza polecenie:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` wypisuje SHA-256 dokładnych bajtów pliku małymi literami. Nie sprawdza poprawności pliku jako JSON. Odciski migawki i źródeł w manifeście muszą dokładnie odpowiadać plikom, łącznie z białymi znakami. Nie odświeżaj odcisku tylko po to, by ukryć nieoczekiwaną rozbieżność; najpierw porównaj i zatwierdź nowe wejście.

`plan` czyta manifest JSON, znormalizowaną migawkę JSON i tylko pliki jawnie wskazane w `manifest.sources`, względem `--root`. Nie przeszukuje rekursywnie katalogów ani folderu domowego. Domyślny wynik to JSON. Dla `--lang en|ru|de|es` zmieniają się tylko komunikaty dla ludzi; nazwy pól i kody diagnostyczne pozostają stabilne. `--help` jest dostępne na poziomie głównym i dla każdego polecenia. Nie ma poleceń stosowania, wysyłania, wykrywania ani uwierzytelniania.

Status wyjścia:

- **0:** obsługiwany zakres wejścia jest wewnętrznie spójny i gotowy do przeglądu.
- **2:** błędne argumenty/wejście, nieczytelny plik albo naruszenie schematu/limitu.
- **3:** strukturalnie poprawne wejście dało plan zablokowany przez konflikt lub nierozstrzygnięty zakres.

Błędy wejścia po analizie argumentów generują kopertę JSON na stdout z `status: invalid`. Błędy argumentów wypisują zlokalizowaną pomoc na stderr. Poprawne obliczenie odcisku wypisuje tylko skrót. W trybie tekstowym proponowane zmiany zachowują maszynowe nazwy pól, a wyjaśnienia są tłumaczone.

Pliki operacyjne trzymaj w prywatnym katalogu. Przekierowanie stdout tworzy własny raport, mogący zawierać identyfikujące nazwy encji i ścieżki. Samo narzędzie niczego nie zapisuje. Odinstaluj przez `python3 -m pip uninstall ha-entity-migrations`. Kontrole programistyczne opisuje [CONTRIBUTING](../../CONTRIBUTING.md).
