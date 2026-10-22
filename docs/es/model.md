# Modelo de entrada

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

[Instalación](installation.md) · [Ejemplos](examples.md)

Todos los documentos usan JSON estricto UTF-8. Se rechazan claves duplicadas, números no finitos y campos de esquema desconocidos. Los ejemplos exactos de `examples/` son la referencia ejecutable. Los campos de versión deben ser el entero `1`, no una cadena ni un booleano.

## Instantánea

El objeto superior contiene únicamente `version` y `entities`. Cada entidad contiene exactamente:

- `entity_id`: ID de dominio/objeto en minúsculas, como `light.workbench`.
- `hardware_id`: identificador privado opaco elegido por el operador.
- `channel`: identificador del canal físico, como cadena.
- `role`: finalidad lógica única, como `workbench` o `pump_enable`.
- `capabilities`: cadenas únicas que describen capacidades, por ejemplo `on_off`.

El par hardware/canal identifica un extremo físico. Los ID de entidad, extremos físicos y roles lógicos deben ser únicos cada uno. Representa un diagnóstico físico mediante un canal distinto, por ejemplo `rssi`, con su propio rol único. Un rol es una etiqueta de planificación, no un área, etiqueta o clase de dispositivo de HA. Estas declaraciones no son mediciones; la herramienta no puede verificarlas contra el hardware.

## Manifiesto

El objeto superior tiene exactamente `version`, `snapshot_sha256`, `sources`, `assignments` y `consumers`. `sources` relaciona nombres de archivo relativos con resúmenes SHA-256. `assignments` contiene registros completos de sustitución para extremos físicos ya presentes en la instantánea. Los extremos no enumerados permanecen iguales. Para añadir un dispositivo, incorpora primero su extremo de reserva observado en la instantánea. No hay creación ni eliminación implícita de hardware y esta versión exige roles únicos.

Cada consumidor identifica un **valor de cadena literal** mediante `file` y un `pointer` RFC 6901. Escapa `/` como `~1` y `~` como `~0`; los índices de listas empiezan en cero y no llevan ceros iniciales. Cada referencia descubierta necesita una política explícita:

- `follows_role`: buscar el destino que posee el rol lógico del origen.
- `follows_hardware`: conservar el canal físico de origen y usar su nuevo ID de entidad.
- `retire`: proponer eliminar el objeto explícito `retire_scope` que contiene la referencia.

Los consumidores no retirados también necesitan `kind` (`action`, `display`, `reference`), `allowed_roles` (no vacío) y `required_capabilities` (posiblemente vacío). Las acciones requieren `service_pointer`. Estas barreras impiden usar una bomba recién reutilizada como destino de iluminación. Son declaraciones, no intención inferida.

Los consumidores retirados tienen exactamente cuatro campos: file, pointer, policy y retire_scope. El alcance debe ser un objeto ancestro distinto de la raíz. Solo puede contener referencias al mismo origen retirado; las referencias mixtas o dinámicas lo bloquean. Selecciona toda una automatización obsoleta cuando quitar una acción dejaría una secuencia vacía inválida. La herramienta no ejecuta el validador de esquema de HA.

## Cambios de dominio

Para una acción que cruza light/switch, solo se admiten `turn_on`, `turn_off`, `toggle` y servicios `homeassistant.*` correspondientes. No se aceptan `data` ni `data_template` no vacíos para convertir servicios automáticamente. Un servicio específico de dominio con varios destinos literales queda bloqueado. El puntero del servicio debe poseer el destino bajo su acción. Los cambios de dominio de visualización siempre exigen revisar manualmente las funciones de la tarjeta; un interruptor no puede heredar silenciosamente controles de brillo.

## Límites

2 MiB por archivo; 16 MiB de orígenes combinados; 64 archivos; 5.000 entidades, asignaciones o consumidores; profundidad JSON de 40 y 100.000 nodos de valor por archivo. Los identificadores son cadenas no vacías de hasta 256 caracteres; las listas de capacidades/roles permitidos tienen hasta 64 cadenas únicas. Las rutas relativas no pueden ascender, ser absolutas ni contener enlaces simbólicos. Solo se aceptan archivos normales.

El cargador rechaza dos nombres de origen que resuelvan a la misma ruta canónica o identidad de archivo abierto (dispositivo/inodo). Esto incluye separadores repetidos, enlaces duros y alias por mayúsculas/minúsculas en sistemas insensibles a ellas. Conserva un nombre y actualiza sus consumidores; los alias no pueden asignar políticas distintas a un mismo archivo físico. Los archivos independientes con contenido idéntico siguen siendo entradas válidas. La API pura `plan` no accede al sistema de archivos: quien construya su propio mapa de orígenes debe imponer este límite de identidad antes de llamarla.
