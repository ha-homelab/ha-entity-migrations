# Ograniczenia i granice przeglądu

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

[Architektura](architecture.md) · [Bezpieczeństwo](../../SECURITY.md)

Dokładność planu zależy od deklaracji sprzętu/kanałów/ról i dostarczonych plików. Narzędzie nie wykrywa pominiętych paneli, wyzwalaczy urządzeń, scen, blueprintów, automatyzacji zapisanych gdzie indziej, filtrów Matter, klientów zewnętrznych ani ukrytych stanów integracji. Gotowy raport nie jest pełnym audytem Home Assistanta. W tej wersji role są unikalne; role semantyczne wiele-do-wielu i grupy wymagają ręcznego rozłożenia.

Obsługiwane są źródła konfiguracji JSON. YAML, dołączenia, aliasy, kotwice, wykonywalne znaczniki, komponenty własne i szablony generowane podczas działania nie są interpretowane. Normalizacja jest poza tą wersją i może utracić semantykę; zachowaj oryginał i sprawdź równoważność. Nawet obsługiwany JSON nie jest sprawdzany względem pełnego schematu HA. Usunięcie jawnego obiektu konsumenta może pozostawić niepoprawny obiekt nadrzędny; sprawdź go i uruchom walidację konfiguracji HA w zwykłym procesie testowym przed wdrożeniem.

Możliwości i dozwolone role są jawnymi ograniczeniami, nie wywnioskowanym bezpieczeństwem. Narzędzie nie wie, że do wcześniej nieszkodliwego gniazdka podłączono pompę albo napęd garażu. Raportowany stan przekaźnika nie dowodzi zachowania styku/obciążenia. Nie uruchamiaj skryptów dla całego domu ani nie odłączaj i nie włączaj pracującego sprzętu jedynie dla sprawdzenia nazw. Fizyczne uruchomienie wymaga osobnej kontrolowanej procedury.

Ta wersja nie stosuje planów, nie zmienia nazw encji rejestru, unikalnych ID, nie przeładowuje HA, nie restartuje kontrolerów, nie wycofuje integracji i nie cofa zmian. Zwracane operacje są doradcze, nie są wykonywalnym JSON Patch. Przy ręcznym użyciu uzyskaj świeżą migawkę i sprawdzaj stan po każdej przejrzanej zmianie; indeksy i wersje mogły się zmienić. Skróty nie zapewniają podpisów ani kontroli dostępu.

Raporty mogą zawierać prywatne nazwy i identyfikatory. Nie umieszczaj ich w publicznym Git, trackerach zgłoszeń ani artefaktach CI. Publiczne przykłady używają syntetycznych urządzeń i nie deklarują walidacji w terenie. Diagnostyka celowo blokuje plan; nie ma flagi wymuszania, listy ignorowania ani ukrytego liberalnego trybu.
