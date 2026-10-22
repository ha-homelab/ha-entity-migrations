# Modèle d'entrée

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

[Installation](installation.md) · [Exemples](examples.md)

Tous les documents utilisent du JSON UTF-8 strict. Clés dupliquées, nombres non finis et champs inconnus du schéma sont rejetés. Les exemples exacts de `examples/` constituent la référence exécutable. Les champs de version doivent être l'entier `1`, pas une chaîne ni un booléen.

## Instantané

L'objet racine contient uniquement `version` et `entities`. Chaque entité contient exactement :

- `entity_id` : identifiant domaine/objet en minuscules, par exemple `light.workbench`.
- `hardware_id` : identifiant privé opaque choisi par l'opérateur.
- `channel` : identifiant de canal physique sous forme de chaîne.
- `role` : fonction logique unique, par exemple `workbench` ou `pump_enable`.
- `capabilities` : chaînes uniques décrivant les capacités, par exemple `on_off`.

Le couple matériel/canal identifie une terminaison physique. Les identifiants d'entité, terminaisons physiques et rôles logiques doivent chacun être uniques. Représentez un diagnostic physique par un canal différent, par exemple `rssi`, avec son propre rôle unique. Un rôle est une désignation de planification, pas une zone, étiquette ou classe d'appareil HA. Ces déclarations ne sont pas des mesures ; l'outil ne peut pas les vérifier sur le matériel.

## Manifeste

L'objet racine contient exactement `version`, `snapshot_sha256`, `sources`, `assignments` et `consumers`. `sources` associe les noms de fichiers relatifs aux condensats SHA-256. `assignments` contient les enregistrements complets de remplacement des terminaisons physiques déjà présentes dans l'instantané. Les terminaisons absentes de cette liste restent inchangées. Pour introduire un appareil, incluez d'abord sa terminaison de réserve observée dans l'instantané. Il n'y a pas de création/suppression implicite de matériel ; les rôles doivent être uniques.

Chaque consommateur identifie une **valeur de chaîne littérale** par `file` et un `pointer` RFC 6901. Échappez `/` en `~1` et `~` en `~0` ; les indices commencent à zéro, sans zéros initiaux. Toute référence découverte exige une politique explicite :

- `follows_role` : trouver la destination possédant le rôle logique de la source.
- `follows_hardware` : conserver le canal physique source et utiliser son nouvel identifiant d'entité.
- `retire` : proposer la suppression de l'objet explicite `retire_scope` contenant la référence.

Les consommateurs non retirés nécessitent aussi `kind` (`action`, `display`, `reference`), `allowed_roles` (non vide) et `required_capabilities` (éventuellement vide). Les actions nécessitent `service_pointer`. Ces barrières empêchent d'utiliser une pompe réaffectée comme cible d'éclairage. Ce sont des déclarations, pas une intention déduite.

Les consommateurs retirés ont exactement quatre champs : file, pointer, policy et retire_scope. Le périmètre doit être un objet ancêtre autre que la racine. Il ne peut contenir que des références à la même source retirée ; des références mixtes ou dynamiques le bloquent. Choisissez une automatisation obsolète entière si retirer une action laisserait une séquence vide invalide. L'outil n'exécute pas le validateur de schéma HA.

## Changements de domaine

Pour une action traversant light/switch, seuls `turn_on`, `turn_off`, `toggle` et les services `homeassistant.*` correspondants sont acceptés. Aucune valeur non vide de `data` ou `data_template` n'est admise pour la conversion automatique. Un service propre à un domaine avec plusieurs cibles littérales est bloqué. Le pointeur de service doit posséder la cible sous son action. Un changement de domaine d'affichage exige toujours une vérification manuelle des fonctions de carte ; un interrupteur ne peut hériter silencieusement des commandes de luminosité.

## Bornes

2 MiB par fichier ; 16 MiB de sources cumulées ; 64 fichiers ; 5 000 entités, affectations ou consommateurs ; profondeur JSON de 40 et 100 000 nœuds de valeur par fichier. Les identifiants sont des chaînes non vides de 256 caractères maximum ; les listes de capacités/rôles autorisés ont au plus 64 chaînes uniques. Les chemins relatifs ne peuvent remonter, être absolus ni contenir de liens symboliques. Seuls les fichiers ordinaires sont acceptés.

Le chargeur rejette deux noms de source désignant le même chemin canonique ou la même identité de fichier ouvert (périphérique/inode). Cela inclut les séparateurs répétés, liens physiques et alias de casse sur les systèmes insensibles à la casse. Gardez un nom unique et actualisez ses consommateurs ; les alias ne peuvent porter différentes politiques pour un fichier physique. Des fichiers indépendants au contenu identique restent valides. L'API pure `plan` n'accède pas au système de fichiers : les appelants construisant eux-mêmes leur correspondance doivent imposer cette frontière d'identité avant l'appel.
