# Arquitectura y contrato del informe

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

[Modelo](model.md) · [Limitaciones](limitations.md)

![Flujo de datos de solo lectura](../diagrams/pipeline.svg)

`io.py` impone límites a archivos, rutas y JSON, y punteros exactos. `planner.py` valida las declaraciones, construye los mapas anterior/posterior, examina los valores de origen, resuelve las políticas explícitas y acumula diagnósticos. `cli.py` añade mensajes traducidos e imprime el informe. `i18n.py` contiene cuatro catálogos completos de mensajes. Este recorrido no depende de la red ni de Home Assistant.

El analizador es conservador deliberadamente. Comprueba las cadenas que parecen referencias exactas a entidades contra la instantánea. Las cadenas con referencias incrustadas quedan sin resolver. Las plantillas en claves o valores y las claves de destino de dispositivo/área/etiqueta quedan sin resolver aunque parezcan fáciles de adivinar. Los campos simples de servicio no se consideran ID de entidad; los servicios dinámicos siguen sin resolverse. Los archivos que no son JSON se registran como orígenes no admitidos y bloquean la planificación. No es un analizador general de HA.

![Flujo de decisiones de las políticas](../diagrams/policy.svg)

## Envoltorio JSON estable, versión 1 del esquema

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Con entradas válidas, `status` es ready o blocked. `scope` siempre es `supplied_files_only`; `read_only` siempre es true. Los errores de entrada utilizan el envoltorio invalid más pequeño descrito en la instalación.

Las ediciones tienen una operación, un archivo y un puntero. `replace_reference` incluye también before/after/policy; `replace_service` incluye before/after; `remove_consumer` incluye la referencia retirada. **No son un JSON Patch ejecutable**. Carecen de semántica de transacción, desplazamiento de índices y ciclo de vida de HA. Revísalas como propuestas; esta versión no proporciona aplicador de parches deliberadamente.

Los diagnósticos contienen `code`, `location`, `severity` estables y `message` traducido. Tanto `error` como `unresolved` bloquean el plan. Los informes `blocked` pueden contener ediciones candidatas de referencias no afectadas, pero ninguna constituye una transacción lista. Los modelos iniciales obsoletos o contradictorios suprimen todas las ediciones candidatas de referencias. Las asignaciones siempre reflejan el modelo solicitado por el usuario, nunca cambios completados.

Los informes ordenan orígenes, asignaciones, ediciones y diagnósticos para ser reproducibles. No incluyen fechas actuales ni puntuaciones de confianza inventadas. Los hashes de bytes prueban qué versión de entrada se analizó, no si era verdadera ni si un dispositivo obedecerá una orden.
