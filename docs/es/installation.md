# Instalación y CLI

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

[Índice de documentación](../../README.md#documentation)

Utiliza Python 3.11 o posterior. Crea y activa un entorno virtual dedicado y ejecuta `python3 -m pip install -e .` desde el repositorio descargado. El paquete no tiene dependencias de ejecución; pip puede descargar su motor de compilación. Para una máquina sin conexión, prepara de antemano el wheel y las dependencias de compilación. Verifica la instalación seleccionada con `ha-entity-migrations --version`, que muestra la versión del paquete instalado.

La CLI tiene dos órdenes, con la opción global de idioma antes de la orden:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` imprime el SHA-256 en minúsculas de los bytes exactos del archivo. No valida su contenido como JSON. Las huellas de instantánea y orígenes del manifiesto deben corresponder a esos archivos exactos, incluidos espacios en blanco. No renueves una huella solo para descartar una desviación inesperada; compara y aprueba primero la entrada nueva.

`plan` lee un manifiesto JSON, una instantánea JSON normalizada y únicamente los archivos indicados explícitamente en `manifest.sources`, relativos a `--root`. No recorre directorios recursivamente ni busca en tu carpeta personal. La salida predeterminada es JSON. Con `--lang en|ru|de|es` solo cambian los mensajes humanos; nombres de campos y códigos diagnósticos permanecen estables. `--help` está disponible en el nivel superior y para cada orden. No existen órdenes para aplicar, subir, descubrir ni autenticar.

Estado de salida:

- **0:** el alcance de entrada admitido es coherente internamente y está listo para revisión.
- **2:** argumentos/entrada inválidos, archivo ilegible o infracción de esquema/límites.
- **3:** una entrada estructuralmente válida produjo un plan bloqueado por conflicto o alcance sin resolver.

Los fallos de entrada posteriores al análisis de argumentos generan un envoltorio JSON en stdout con `status: invalid`. Los errores de argumentos imprimen instrucciones localizadas en stderr. Una huella calculada correctamente imprime solo el resumen. En modo texto, las ediciones propuestas conservan los nombres de campo de máquina y traducen las explicaciones.

Guarda los archivos operativos en un directorio privado. Al redirigir stdout creas tu propio informe, que puede contener nombres identificativos de entidades y rutas. La herramienta no escribe nada por sí misma. Desinstala con `python3 -m pip uninstall ha-entity-migrations`. Para comprobaciones de desarrollo, consulta [CONTRIBUTING](../../CONTRIBUTING.md).
