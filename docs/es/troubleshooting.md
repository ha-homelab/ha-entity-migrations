# Solución de problemas

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

[Instalación](installation.md) · [Limitaciones](limitations.md)

**Orden no encontrada:** activa el mismo entorno virtual usado al instalar. Prueba `python3 -m ha_entity_migrations --version`; no instales en el Python del sistema solo para sortear una discrepancia de rutas.

**Salida 2, schema_invalid:** compara tus claves con el ejemplo ejecutable y el [modelo de entrada](model.md). Los campos desconocidos son errores. Las versiones son el entero 1; los identificadores de canal son cadenas. Cada política de acción necesita su puntero de servicio. Una instantánea tiene entidades; un manifiesto tiene asignaciones y consumidores. Los archivos no son intercambiables.

**Salida 2, duplicate_source:** dos nombres identifican un archivo físico. Mantén un único nombre canónico en `sources` y actualiza todos los campos `file` de consumidores. Elimina separadores duplicados y alias por enlaces duros o mayúsculas; no concedas una segunda política al alias. Se siguen admitiendo archivos separados con contenido idéntico.

**stale_snapshot / stale_source:** compara los cambios reales con el origen aprobado. Usa fingerprint solo después de revisarlos. Los cambios de espacios afectan al hash. No apuntes a una copia obsoleta solo para satisfacer el hash antiguo.

**source_collision / destination_collision:** un canal físico, rol o ID de entidad está duplicado. Expresa explícitamente ambos lados de un intercambio de roles y comprueba que ningún extremo sin cambios conserve el ID de destino deseado.

**role_not_allowed / capability_missing:** el consumidor alcanzaría una carga inadecuada o perdería una capacidad. Confirma si debe seguir el rol o el hardware. No amplíes automáticamente allowed_roles ni declares capacidades inexistentes. Una luz sustituida por un relé de encendido/apagado no puede regular brillo.

**missing_policy / unmodeled_reference:** inventaría el extremo referenciado y añade una declaración explícita de consumidor solo tras confirmar su finalidad. Una cadena de historial antigua puede quedar fuera del alcance activo; retira deliberadamente ese archivo del alcance, documenta la exclusión y regenera el contrato de orígenes.

**dynamic_reference / embedded_reference / indirect_target:** esta versión no puede demostrar la correspondencia. Revisa Jinja o el comportamiento de grupos/áreas/etiquetas por separado o proporciona configuración literal normalizada explícita. El programa nunca ejecuta plantillas.

**display_domain_review / service_data_review / mixed_action_targets:** inspecciona funciones de tarjetas, parámetros de acciones y lotes de destinos. Divide una acción multidominio en un cambio de origen revisado por separado; no cambies solo el dominio del servicio.

**retire_scope_mixed / overlapping_edits:** elige un objeto consumidor obsoleto coherente sin referencias ajenas. No elimines solo entity_id de una acción: podrías crear un destino demasiado amplio o configuración inválida. Este programa no aplica retiradas automáticas.

**unsupported_source:** solo se puede planificar JSON. YAML, binarios y otros archivos no se omiten silenciosamente. Una copia JSON normalizada explícitamente puede ayudar al análisis, pero debe compararse con el original antes de cualquier edición real.

Informa de errores con una entrada sintética mínima, las versiones de herramienta/Python, el código de salida y los códigos diagnósticos. Nunca adjuntes una exportación doméstica sin depurar ni credenciales API.
