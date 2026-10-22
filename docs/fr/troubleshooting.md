# Dépannage

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

[Installation](installation.md) · [Limites](limitations.md)

**Commande introuvable :** activez l'environnement virtuel utilisé à l'installation. Essayez `python3 -m ha_entity_migrations --version` ; n'installez pas dans le Python système pour contourner un mauvais chemin.

**Sortie 2, schema_invalid :** comparez vos clés à l'exemple exécutable et au [modèle d'entrée](model.md). Les champs inconnus sont des erreurs. Les versions sont l'entier 1 ; les identifiants de canal sont des chaînes. Toute politique d'action exige son pointeur de service. L'instantané contient des entités, le manifeste des affectations et consommateurs : ces fichiers ne sont pas interchangeables.

**Sortie 2, duplicate_source :** deux noms désignent un fichier physique. Gardez un nom canonique dans `sources` et actualisez tous les champs `file` des consommateurs. Supprimez les séparateurs en double ou alias de lien physique/casse ; n'attribuez pas une deuxième politique à un alias. Les fichiers séparés au contenu identique restent acceptés.

**stale_snapshot / stale_source :** comparez les changements réels à la source approuvée. N'utilisez la commande fingerprint qu'après vérification. Les espaces modifient l'empreinte. Ne pointez pas vers une copie périmée simplement pour satisfaire l'ancienne empreinte.

**source_collision / destination_collision :** un canal physique, rôle ou identifiant d'entité est dupliqué. Décrivez explicitement les deux côtés d'un échange de rôles et vérifiez qu'une terminaison inchangée ne conserve pas l'identifiant de destination souhaité.

**role_not_allowed / capability_missing :** le consommateur atteindrait une charge inappropriée ou perdrait une capacité. Confirmez s'il doit suivre le rôle ou le matériel. N'élargissez pas automatiquement allowed_roles et ne déclarez pas des capacités absentes. Une lampe remplacée par un relais tout-ou-rien ne peut plus varier en luminosité.

**missing_policy / unmodeled_reference :** recensez la terminaison référencée et n'ajoutez une déclaration de consommateur qu'après avoir confirmé sa fonction. Une ancienne chaîne d'historique peut être hors du périmètre actif ; excluez délibérément ce fichier, documentez l'exclusion et régénérez le contrat des sources.

**dynamic_reference / embedded_reference / indirect_target :** cette version ne peut prouver la correspondance. Examinez séparément Jinja ou le comportement groupe/zone/étiquette, ou fournissez une configuration littérale normalisée explicite. Le programme n'exécute jamais de modèle.

**display_domain_review / service_data_review / mixed_action_targets :** examinez fonctions des cartes, paramètres d'action et lots de cibles. Séparez une action multidomaine dans une modification de source examinée à part ; ne changez pas seulement le domaine du service.

**retire_scope_mixed / overlapping_edits :** choisissez un objet consommateur obsolète cohérent, sans références étrangères. Ne supprimez pas seulement entity_id d'une action : cela pourrait élargir la cible ou rendre la configuration invalide. Le programme n'applique aucun retrait automatique.

**unsupported_source :** seul JSON peut être planifié. YAML, fichiers binaires et autres ne sont pas ignorés silencieusement. Une copie JSON explicitement normalisée peut aider l'analyse, mais doit être comparée à l'original avant toute modification réelle.

Signalez un bogue avec une entrée synthétique minimale, les versions outil/Python, le code de sortie et les codes de diagnostic. Ne joignez jamais un export domestique brut ni des identifiants API.
