# Limitaciones y límites de la revisión

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

[Arquitectura](architecture.md) · [Seguridad](../../SECURITY.md)

Un plan solo puede ser tan exacto como sus declaraciones físicas/de canales/roles y los archivos proporcionados. La herramienta no descubre paneles omitidos, disparadores de dispositivos, escenas, blueprints, automatizaciones guardadas en otros lugares, filtros Matter, clientes externos ni estados ocultos de integraciones. Un informe listo no es una auditoría completa de Home Assistant. En esta versión cada rol es único; los roles semánticos muchos-a-muchos y los grupos requieren descomposición manual.

Se admiten orígenes de configuración JSON. No se interpretan YAML, inclusiones, alias, anclas, etiquetas ejecutables, componentes personalizados ni plantillas generadas durante la ejecución. La normalización queda fuera de esta versión y puede perder semántica; conserva el original y revisa su equivalencia. Ni siquiera el JSON admitido se comprueba contra el esquema completo de HA. Eliminar un objeto consumidor explícito puede dejar un objeto padre inválido; revísalo y ejecuta el comprobador de configuración de HA durante el proceso habitual de pruebas previas al despliegue.

Capacidades y roles permitidos son restricciones explícitas, no seguridad inferida. La herramienta no sabe si una bomba o un motor de garaje se ha conectado a un enchufe antes inofensivo. El estado comunicado de un relé no demuestra el comportamiento del contacto ni de la carga. No ejecutes scripts de toda la vivienda ni reinicies eléctricamente un aparato en servicio solo para validar nombres. La puesta en marcha física necesita un procedimiento controlado independiente.

Esta versión no aplica planes, renombra entidades del registro, modifica ID únicos, recarga HA, reinicia controladores, retira integraciones ni revierte cambios. Las operaciones devueltas son orientativas y no son JSON Patch ejecutable. Si alguien las aplica manualmente, debe obtener una instantánea nueva y verificar después de cada cambio revisado: índices y versiones pueden haber cambiado. Los hashes no aportan firmas ni control de acceso.

Los informes pueden contener nombres e identificadores privados. No los incluyas en repositorios Git públicos, gestores de incidencias ni artefactos CI. Los ejemplos públicos emplean dispositivos sintéticos y no afirman validación en instalaciones reales. Los diagnósticos bloquean el plan por diseño; no hay opción de forzado, lista de exclusiones ni modo permisivo oculto.
