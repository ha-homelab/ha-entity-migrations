# Installation et interface en ligne de commande

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

[Index de la documentation](../../README.md#documentation)

Utilisez Python 3.11 ou ultérieur. Créez et activez un environnement virtuel dédié, puis exécutez `python3 -m pip install -e .` depuis le dépôt extrait. Le paquet n'a pas de dépendance d'exécution ; pip peut télécharger son moteur de construction. Pour une machine hors ligne, préparez à l'avance le wheel et les dépendances de construction. Vérifiez l'installation sélectionnée avec `ha-entity-migrations --version`, qui indique la version installée.

La CLI propose deux commandes, avec une option de langue globale placée avant la commande :

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` affiche le SHA-256 en minuscules des octets exacts du fichier. Il ne valide pas le fichier en tant que JSON. Les empreintes d'instantané et de sources du manifeste doivent correspondre exactement aux fichiers, espaces compris. Ne renouvelez pas une empreinte uniquement pour écarter une dérive inattendue ; comparez et approuvez d'abord la nouvelle entrée.

`plan` lit un manifeste JSON, un instantané JSON normalisé et uniquement les fichiers nommés explicitement dans `manifest.sources`, relativement à `--root`. Il ne parcourt pas récursivement un répertoire et ne fouille pas votre dossier personnel. La sortie par défaut est JSON. Seuls les messages destinés aux humains changent avec `--lang en|ru|de|es` ; les noms de champs et codes de diagnostic restent stables. `--help` existe au niveau supérieur et pour chaque commande. Aucune commande n'applique, ne téléverse, ne découvre ni n'authentifie quoi que ce soit.

Codes de sortie :

- **0 :** le périmètre d'entrée pris en charge est cohérent et prêt à être examiné.
- **2 :** arguments/entrée invalides, fichier illisible ou violation de schéma/limite.
- **3 :** une entrée structurellement valide produit un plan bloqué par conflit ou périmètre non résolu.

Les erreurs d'entrée après analyse des arguments produisent une enveloppe JSON sur stdout avec `status: invalid`. Les erreurs d'arguments affichent une aide localisée sur stderr. Une empreinte calculée avec succès n'affiche que le condensat. En mode texte, les modifications proposées gardent leurs noms de champs machine ; les explications sont traduites.

Conservez les fichiers opérationnels dans un répertoire privé. Rediriger stdout crée votre propre rapport, qui peut contenir des noms d'entités identifiants et des chemins. L'outil lui-même n'écrit rien. Désinstallez avec `python3 -m pip uninstall ha-entity-migrations`. Pour les contrôles de développement, consultez [CONTRIBUTING](../../CONTRIBUTING.md).
