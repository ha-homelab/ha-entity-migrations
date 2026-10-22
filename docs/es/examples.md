# Ejemplos desarrollados

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

[Modelo de entrada](model.md) · [Arquitectura](architecture.md)

Todo el hardware y los roles de estos ejemplos son sintéticos. Recrea entradas idénticas con `python3 tools/generate_examples.py`. Ninguna orden conecta con Home Assistant.

## El rol de una lámpara abandona un enchufe reutilizado

Ejecuta la orden del README para `examples/role-swap`. Inicialmente, `plug-a/1` posee `light.workbench` y `plug-b/1` posee `switch.spare`. El manifiesto asigna el rol de bomba al enchufe A y el de banco de trabajo al B. La automatización de iluminación utiliza `follows_role` y solo permite `workbench`. Su referencia sigue siendo `light.workbench` mientras cambia el hardware de destino. La ausencia de una edición textual es el resultado previsto, no una migración pendiente. `assignments` en el informe contiene los cambios de hardware para revisión humana.

El consumidor de reserva anterior se retira en `/1`, todo el segundo objeto de automatización. Así no queda una secuencia de acciones vacía. El informe es orientativo; el programa no elimina elementos del array JSON. Si aplicas manualmente varias eliminaciones propuestas, ten en cuenta el desplazamiento de índices y repite el análisis desde una instantánea nueva.

Cambia la primera política a `follows_hardware` manteniendo `workbench` como rol permitido: el plan se bloquea con `role_not_allowed`. Ampliar la lista para incluir una bomba cambia explícitamente la intención de forma peligrosa; no es un modo rutinario de eliminar el error. Restaura la política correcta.

## Un relé pasa de light a switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Las dos ediciones propuestas cambian el destino y su servicio `light.turn_off`. Añade datos de brillo a la acción de origen, actualiza la huella aprobada y repite: `service_data_review` bloquea la conversión automática. No descartes los ajustes de brillo solo para satisfacer la herramienta; revisa el comportamiento deseado.

## Una plantilla sin resolver

Ejecuta la misma orden con `examples/blocked-template`. El destino es Jinja dinámico. La herramienta no lo evalúa y devuelve el código 3. Un plan completo admitido necesita configuración explícita con destinos literales demostrables; de lo contrario, documenta esta parte como migración manual fuera del alcance listo. Ignorar el código de salida no resuelve la plantilla.

## Desviaciones y repetibilidad

Editar un origen sin cambiar su hash en el manifiesto produce `stale_source`. Editar la instantánea produce `stale_snapshot`. Estos modelos obsoletos no generan ediciones candidatas de referencias. Con archivos sin cambios, el resultado JSON es determinista salvo por el idioma seleccionado. Los archivos de origen permanecen idénticos byte a byte.

Para un proyecto real, copia el formato en una carpeta privada, verifica identidades físicas, enumera los consumidores y ejecuta el planificador. Revisa todas las asignaciones y ediciones, realiza las comprobaciones propias de HA dentro del despliegue establecido y crea después una nueva instantánea de solo lectura para verificar el resultado. Este proyecto no implementa ese despliegue ni un ejecutor de reversión.
