# Home Assistant Entity Migrations

**Beta 0.1.1b1:** versión preliminar para evaluar el software; no implica la aceptación de dispositivos físicos.

**Traslade una función a nuevo hardware sin dirigir accidentalmente sus automatizaciones al aparato equivocado.** Esta CLI local de Python genera un plan revisable a partir de un inventario explícito y políticas de referencias. No se conecta a Home Assistant ni aplica cambios.

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Manual completo en inglés](docs/en/installation.md)

![Transferencia sintética de una función](docs/diagrams/role-transfer.svg)

Un enchufe antes alimentaba una lámpara y ahora alimentará una bomba. La función de iluminación pasa a otro enchufe. `follows_role` sigue la lámpara; `follows_hardware` sigue el canal físico, pero comprueba las funciones permitidas. Una automatización de luces no debe acabar apagando la bomba. `retire` propone eliminar un contenedor de consumidor seleccionado explícitamente.

## Instalación y ejemplo

Python 3.11 o posterior; sin dependencias en tiempo de ejecución. Desde el directorio fuente:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
ha-entity-migrations --lang es plan --manifest examples/role-swap/manifest.json --snapshot examples/role-swap/snapshot.json --root examples/role-swap
```

El ejemplo es completamente sintético. `ready` y código 0 indican un plan listo para revisar dentro del ámbito suministrado, no una migración aplicada. `examples/domain-change` muestra la conversión conjunta de `light.table` y `light.turn_off`. `examples/blocked-template` devuelve `blocked`, código 3. Las entradas inválidas devuelven código 2. Añada `--format text` después de `plan` para texto; las claves JSON y los códigos de diagnóstico no cambian con el idioma.

## Alcance

Hardware/canal/función explícitos, capacidades declaradas, funciones permitidas, punteros JSON, colisiones y SHA-256 de los bytes exactos. La conversión sencilla entre light y switch admite un único destino literal sin datos de acción. Jinja dinámico, destinos indirectos por dispositivo/área/etiqueta, referencias desconocidas y formatos no admitidos bloquean el plan.

Normalice YAML a JSON de forma explícita y revise la representación. No se conservan comentarios, anclas ni formato. `ready` no certifica una auditoría completa de HA ni el cableado real. Esta versión no incluye cliente de red ni comando apply.

[Modelo](docs/en/model.md) · [Ejemplos](docs/en/examples.md) · [Arquitectura](docs/en/architecture.md) · [Diagnóstico](docs/en/troubleshooting.md) · [Límites](docs/en/limitations.md) · [Seguridad](SECURITY.md) · [Fuentes de la wiki](wiki/Home.md)

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 tools/generate_examples.py
python3 tools/render_diagrams.py
```

Las pruebas no utilizan dispositivos reales. Los SVG reproducibles son diagramas sintéticos, no fotografías ni resultados medidos. Manuales completos en inglés y ruso; CLI y README en los cuatro idiomas. Versión 0.1.1b1, licencia MIT.
