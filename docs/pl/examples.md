# Omówione przykłady

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

[Model wejścia](model.md) · [Architektura](architecture.md)

Cały sprzęt i wszystkie role w przykładach są syntetyczne. Odtwórz identyczne wejścia poleceniem `python3 tools/generate_examples.py`. Żadne polecenie nie łączy się z Home Assistantem.

## Rola lampy opuszcza gniazdko o nowym przeznaczeniu

Wykonaj polecenie z README dla `examples/role-swap`. Początkowo `plug-a/1` posiada `light.workbench`, a `plug-b/1` posiada `switch.spare`. Manifest przypisuje rolę pompy do gniazdka A, a rolę stołu roboczego do B. Automatyzacja oświetlenia używa `follows_role` i dopuszcza wyłącznie `workbench`. Jej odwołanie pozostaje `light.workbench`, mimo zmiany sprzętu docelowego. Brak zmiany tekstowej jest zamierzony, nie oznacza pominiętej migracji. Pole `assignments` raportu zawiera zmiany sprzętowe do oceny przez człowieka.

Stary rezerwowy konsument jest wycofywany pod `/1`, czyli jako cały drugi obiekt automatyzacji. Nie pozostawia to pustej sekwencji akcji. Raport jest doradczy; program nie usuwa elementów tablicy JSON. Przy ręcznym stosowaniu wielu proponowanych usunięć uwzględnij przesunięcia indeksów i uruchom ponownie na świeżej migawce.

Zmień pierwszą zasadę na `follows_hardware`, pozostawiając dozwoloną rolę `workbench`: plan blokuje `role_not_allowed`. Rozszerzenie listy o pompę jest jawną, niebezpieczną zmianą intencji, a nie zwykłą metodą usuwania błędu. Przywróć właściwą zasadę.

## Przekaźnik zmienia domenę z light na switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Dwie proponowane zmiany modyfikują cel i jego usługę `light.turn_off`. Dodaj dane jasności do akcji źródłowej, zaktualizuj zatwierdzony odcisk źródła i uruchom ponownie: `service_data_review` blokuje automatyczną konwersję. Nie usuwaj ustawień jasności tylko po to, by przejść kontrolę; oceń oczekiwane zachowanie.

## Nierozstrzygnięty szablon

Wykonaj to samo polecenie z `examples/blocked-template`. Cel jest dynamicznym Jinja. Narzędzie nie oblicza go i zwraca kod 3. Pełny obsługiwany plan wymaga jawnej konfiguracji z możliwymi do wykazania celami literalnymi; inaczej zachowaj tę część jako udokumentowaną ręczną migrację poza gotowym zakresem. Ignorowanie kodu wyjścia nie rozstrzyga szablonu.

## Rozbieżności i powtarzalność

Zmiana źródła bez zmiany skrótu w manifeście powoduje `stale_source`. Zmiana migawki powoduje `stale_snapshot`. Dla takich nieaktualnych modeli nie powstają propozycje zmian odwołań. Dla niezmienionych plików wynik JSON jest deterministyczny poza wybranym językiem. Pliki źródłowe pozostają identyczne bajt po bajcie.

Dla rzeczywistego projektu skopiuj format do prywatnego folderu, zweryfikuj fizyczne tożsamości, zinwentaryzuj konsumentów i uruchom planer. Przejrzyj wszystkie przypisania i zmiany, wykonaj kontrole HA w ustalonym procesie wdrożenia, a następnie utwórz nową migawkę tylko do odczytu, aby zweryfikować wynik. Projekt nie implementuje tego wdrożenia ani mechanizmu wycofywania zmian.
