# Exemples détaillés

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

[Modèle d'entrée](model.md) · [Architecture](architecture.md)

Tout le matériel et tous les rôles présentés ici sont synthétiques. Recréez des entrées identiques avec `python3 tools/generate_examples.py`. Aucune commande ne se connecte à Home Assistant.

## Le rôle de lampe quitte une prise réaffectée

Exécutez la commande du README pour `examples/role-swap`. Au départ, `plug-a/1` possède `light.workbench` et `plug-b/1` possède `switch.spare`. Le manifeste affecte le rôle de pompe à la prise A et celui d'établi à B. L'automatisation d'éclairage utilise `follows_role` et n'autorise que `workbench`. Sa référence reste `light.workbench` alors que le matériel de destination change. Cette absence de modification textuelle est intentionnelle, ce n'est pas une migration manquante. Le champ `assignments` du rapport contient les changements matériels à examiner.

L'ancien consommateur de réserve est retiré à `/1`, soit tout le deuxième objet d'automatisation. Cela ne laisse pas de séquence d'actions vide. Le rapport est indicatif ; le programme ne supprime aucun élément de tableau JSON. Si vous appliquez manuellement plusieurs suppressions proposées, tenez compte des indices décalés et relancez depuis un nouvel instantané.

Passez la première politique à `follows_hardware` en gardant `workbench` comme rôle autorisé : le plan bloque avec `role_not_allowed`. Élargir cette liste pour inclure une pompe change explicitement et dangereusement l'intention ; ce n'est pas une correction habituelle de l'erreur. Rétablissez plutôt la bonne politique.

## Un relais passe de light à switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Les deux modifications proposées changent la cible et son service `light.turn_off`. Ajoutez des données de luminosité à l'action source, actualisez l'empreinte source approuvée et relancez : `service_data_review` bloque la conversion automatique. Ne supprimez pas les réglages de luminosité simplement pour satisfaire l'outil ; examinez le comportement souhaité.

## Un modèle non résolu

Exécutez la même commande avec `examples/blocked-template`. La cible est du Jinja dynamique. L'outil ne l'évalue pas et renvoie le code 3. Un plan complet pris en charge exige une configuration explicite avec des cibles littérales démontrables ; sinon, conservez cette partie comme migration manuelle documentée hors du périmètre prêt. Ignorer le code de sortie ne résout pas le modèle.

## Dérive et répétabilité

Modifier une source sans changer son empreinte dans le manifeste produit `stale_source`. Modifier l'instantané produit `stale_snapshot`. Aucune modification candidate de référence n'est émise pour ces modèles périmés. À fichiers identiques, le résultat JSON est déterministe sauf pour la langue choisie. Les fichiers sources restent inchangés octet par octet.

Pour un vrai projet, copiez le format dans un dossier privé, vérifiez les identités physiques, recensez les consommateurs et lancez le planificateur. Examinez toutes les affectations et modifications, effectuez les contrôles propres à HA dans votre procédure habituelle de déploiement, puis créez un nouvel instantané en lecture seule pour vérifier le résultat. Ce projet n'implémente ni ce déploiement ni un exécuteur de retour arrière.
