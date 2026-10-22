# Model wejścia

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

[Instalacja](installation.md) · [Przykłady](examples.md)

Wszystkie dokumenty używają ścisłego JSON UTF-8. Powtórzone klucze, liczby nieskończone i wartości NaN i nieznane pola schematu są odrzucane. Dokładne przykłady w `examples/` stanowią wykonywalny wzorzec. Pola wersji muszą być liczbą całkowitą `1`, nie tekstem ani wartością logiczną.

## Migawka

Obiekt główny zawiera tylko `version` i `entities`. Każda encja zawiera dokładnie:

- `entity_id`: ID domeny/obiektu małymi literami, np. `light.workbench`.
- `hardware_id`: prywatny nieprzezroczysty identyfikator wybrany przez operatora.
- `channel`: identyfikator fizycznego kanału jako tekst.
- `role`: unikalne logiczne przeznaczenie, np. `workbench` lub `pump_enable`.
- `capabilities`: unikalne ciągi opisujące możliwości, np. `on_off`.

Para sprzęt/kanał identyfikuje fizyczny punkt końcowy. ID encji, fizyczne punkty i role logiczne muszą być każdy z osobna unikalne. Diagnostykę fizyczną przedstaw jako inny kanał, np. `rssi`, z własną unikalną rolą. Rola to etykieta planowania, nie obszar, etykieta ani klasa urządzenia HA. Te deklaracje nie są pomiarami; narzędzie nie może porównać ich ze sprzętem.

## Manifest

Obiekt główny ma dokładnie `version`, `snapshot_sha256`, `sources`, `assignments` i `consumers`. `sources` przypisuje względnym nazwom plików skróty SHA-256. `assignments` zawiera pełne zastępcze rekordy encji dla punktów fizycznych już obecnych w migawce. Niewymienione punkty się nie zmieniają. Nowe urządzenie wprowadź najpierw jako zaobserwowany rezerwowy punkt w migawce. Nie ma niejawnego tworzenia ani usuwania sprzętu; ta wersja wymaga unikalnych ról.

Każdy konsument wskazuje **literalną wartość tekstową** przez `file` i `pointer` RFC 6901. Koduj `/` jako `~1`, a `~` jako `~0`; indeksy list zaczynają się od zera i nie mają zer wiodących. Każde wykryte odwołanie wymaga jawnej zasady:

- `follows_role`: znajdź cel posiadający logiczną rolę źródła.
- `follows_hardware`: zachowaj fizyczny kanał źródłowy i użyj jego nowego ID encji.
- `retire`: zaproponuj usunięcie jawnego obiektu `retire_scope` zawierającego odwołanie.

Niewycofywani konsumenci wymagają też `kind` (`action`, `display`, `reference`), `allowed_roles` (niepuste) i `required_capabilities` (mogą być puste). Akcje wymagają `service_pointer`. Te bariery chronią przed użyciem pompy o nowym przeznaczeniu jako celu oświetlenia. To deklaracje, a nie wnioskowana intencja.

Wycofywani konsumenci mają dokładnie cztery pola: file, pointer, policy i retire_scope. Zakres musi być obiektem przodka innym niż korzeń. Może zawierać wyłącznie odwołania do tego samego wycofywanego źródła; mieszane i dynamiczne odwołania go blokują. Wybierz całą przestarzałą automatyzację, gdy usunięcie akcji pozostawiłoby niepoprawną pustą sekwencję. Narzędzie nie uruchamia walidatora schematu HA.

## Zmiany domen

Dla akcji przechodzącej między light/switch obsługiwane są tylko `turn_on`, `turn_off`, `toggle` i odpowiednie usługi `homeassistant.*`. Niepuste `data` lub `data_template` nie są akceptowane w automatycznej konwersji. Usługa specyficzna dla domeny z wieloma literalnymi celami jest blokowana. Wskaźnik usługi musi posiadać cel pod własną akcją. Zmiany domeny wyświetlania zawsze wymagają ręcznej oceny funkcji karty; przełącznik nie może po cichu odziedziczyć regulacji jasności.

## Limity

2 MiB na plik; łącznie 16 MiB plików źródłowych; 64 pliki; 5000 encji, przypisań lub konsumentów; głębokość JSON 40 i 100 000 węzłów wartości na plik. Identyfikatory są niepustymi ciągami do 256 znaków, listy możliwości/dozwolonych ról mają do 64 unikalnych ciągów. Względne ścieżki nie mogą wychodzić w górę, być bezwzględne ani zawierać dowiązań symbolicznych. Wejścia to tylko zwykłe pliki.

Loader odrzuca dwie nazwy źródeł wskazujące tę samą ścieżkę kanoniczną lub tożsamość otwartego pliku (urządzenie/inode). Obejmuje to powtórzone separatory, dowiązania twarde i aliasy wielkości liter w niewrażliwych na nią systemach. Zachowaj jedną nazwę i zaktualizuj konsumentów; aliasy nie mogą przypisywać różnych zasad migracji jednemu plikowi fizycznemu. Niezależne pliki o identycznej treści są nadal poprawne. Czyste API `plan` nie ma dostępu do systemu plików: wywołujący budujący mapę źródeł samodzielnie musi egzekwować tę granicę tożsamości przed wywołaniem.
