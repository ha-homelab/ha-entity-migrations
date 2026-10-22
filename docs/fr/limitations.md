# Limites et périmètre de vérification

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

[Architecture](architecture.md) · [Sécurité](../../SECURITY.md)

Un plan ne peut être plus exact que ses déclarations physiques/de canaux/de rôles et les fichiers fournis. L'outil ne découvre pas les tableaux de bord omis, déclencheurs d'appareils, scènes, blueprints, automatisations stockées ailleurs, filtres Matter, clients externes ou états cachés d'intégrations. Un rapport prêt n'est pas un audit complet de Home Assistant. Chaque rôle est unique dans cette version ; les rôles sémantiques plusieurs-à-plusieurs et groupes nécessitent une décomposition manuelle.

Les sources de configuration JSON sont prises en charge. YAML lui-même, inclusions, alias, ancres, balises exécutables, composants personnalisés et modèles générés à l'exécution ne sont pas interprétés. La normalisation est hors du périmètre de cette version et peut perdre de la sémantique ; conservez l'original et vérifiez l'équivalence. Même le JSON accepté n'est pas contrôlé contre le schéma complet de configuration HA. Supprimer un objet consommateur explicite peut laisser un parent invalide ; vérifiez ce parent et lancez le contrôleur de configuration HA dans votre procédure habituelle de préproduction.

Capacités et rôles autorisés sont des contraintes explicites, pas une sécurité déduite. L'outil ignore qu'une pompe ou une motorisation de garage a remplacé une charge anodine sur une prise. L'état signalé d'un relais ne prouve pas le comportement du contact/de la charge. Ne lancez pas de scripts pour toute la maison et ne coupez pas l'alimentation d'un appareil en service uniquement pour valider des noms. La mise en service physique relève d'une procédure contrôlée distincte.

Cette version n'applique pas de plan, ne renomme pas d'entité du registre, ne modifie pas d'identifiant unique, ne recharge pas HA, ne redémarre pas de contrôleur, ne retire pas d'intégration et n'annule pas de changement. Les opérations sont indicatives, pas des JSON Patch exécutables. En cas d'application manuelle, prenez un nouvel instantané et vérifiez après chaque modification examinée ; indices et versions peuvent avoir changé. Les empreintes n'offrent ni signature ni contrôle d'accès.

Les rapports peuvent contenir noms et identifiants privés. Ne les mettez pas dans Git public, les gestionnaires de tickets ou les artefacts CI. Les exemples publics sont synthétiques et ne prétendent pas avoir été validés sur le terrain. Les diagnostics bloquent volontairement le plan ; aucun drapeau de forçage, liste d'exclusion ou mode permissif caché n'existe.
