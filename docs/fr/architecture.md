# Architecture et contrat du rapport

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

[Modèle](model.md) · [Limites](limitations.md)

![Flux de données en lecture seule](../diagrams/pipeline.svg)

`io.py` impose les limites de fichiers, chemins et JSON, ainsi que des pointeurs exacts. `planner.py` valide les déclarations, construit les correspondances avant/après, examine les valeurs sources, résout les politiques explicites et rassemble les diagnostics. `cli.py` ajoute les messages traduits et affiche le rapport. `i18n.py` contient quatre catalogues complets de messages. Ce parcours ne dépend ni du réseau ni de Home Assistant.

L'analyseur est volontairement prudent. Les chaînes correspondant exactement à une référence d'entité sont vérifiées contre l'instantané. Les chaînes contenant des références incorporées restent non résolues. Les modèles dans les clés ou valeurs et les clés de cible appareil/zone/étiquette restent non résolus, même lorsque leur interprétation semble évidente. Les champs de service simples ne sont pas traités comme des identifiants d'entité ; les services dynamiques restent non résolus. Les fichiers non JSON sont enregistrés comme sources non prises en charge et bloquent la planification. Ce n'est pas un analyseur HA généraliste.

![Décisions des politiques](../diagrams/policy.svg)

## Enveloppe JSON stable, version 1 du schéma

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Pour des entrées valides, `status` vaut ready ou blocked. `scope` vaut toujours `supplied_files_only` et `read_only` toujours true. Les erreurs d'entrée utilisent l'enveloppe invalid plus petite décrite dans l'installation.

Les modifications ont une opération, un fichier et un pointeur. `replace_reference` contient aussi before/after/policy ; `replace_service` contient before/after ; `remove_consumer` contient la référence retirée. Ce ne sont **pas des JSON Patch exécutables**. Il leur manque les sémantiques de transaction, de décalage d'indice et de cycle de vie HA. Examinez-les comme des propositions ; cette version ne fournit délibérément aucun outil d'application de correctifs.

Les diagnostics contiennent les champs stables `code`, `location`, `severity` et un `message` traduit. `error` et `unresolved` bloquent tous deux un plan. Les rapports `blocked` peuvent contenir des modifications candidates pour les références non touchées, mais aucune ne constitue une transaction prête. Les modèles initiaux périmés ou contradictoires suppriment toutes les modifications candidates de références. Les affectations reflètent toujours le modèle demandé par l'utilisateur, jamais des changements déjà effectués.

Les rapports trient sources, affectations, modifications et diagnostics pour être reproductibles. Il n'y a ni horodatage courant ni score de confiance inventé. Les empreintes des octets prouvent quelle version d'entrée a été analysée, pas sa véracité ni l'obéissance d'un appareil à une commande.
