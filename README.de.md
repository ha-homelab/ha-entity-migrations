# Home Assistant Entity Migrations

**Eine logische Rolle auf neue Hardware übertragen, ohne alte Automationen versehentlich auf ein anderes Gerät umzulenken.** Dieses lokale Python-CLI erstellt einen prüfbaren Plan aus einem expliziten Inventar und Referenzrichtlinien. Es verbindet sich nicht mit Home Assistant und wendet keine Änderungen an.

[English](README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Ausführliches Handbuch auf Englisch](docs/en/installation.md)

![Synthetische Übertragung einer Rolle](docs/diagrams/role-transfer.svg)

Eine Steckdose versorgte eine Lampe und wird nun für eine Pumpe verwendet. Die Lampenrolle zieht zu einer anderen Steckdose um. `follows_role` folgt der Lampe; `follows_hardware` folgt dem physischen Kanal, prüft aber die erlaubten Rollen. Eine Lichtautomation darf dadurch nicht unbemerkt die Pumpe ausschalten. `retire` schlägt das Entfernen eines ausdrücklich ausgewählten Verbrauchercontainers vor.

## Installation und Beispiel

Python 3.11 oder neuer; keine Laufzeitabhängigkeiten. Im Quellverzeichnis:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
ha-entity-migrations --lang de plan --manifest examples/role-swap/manifest.json --snapshot examples/role-swap/snapshot.json --root examples/role-swap
```

Das Beispiel ist vollständig synthetisch. `ready` und Exitcode 0 bedeuten einen zur Prüfung geeigneten Plan im angegebenen Umfang, keine ausgeführte Migration. `examples/domain-change` zeigt die gemeinsame Umstellung von `light.table` und `light.turn_off`. `examples/blocked-template` liefert `blocked` und Exitcode 3. Ungültige Eingaben ergeben Exitcode 2. `--format text` nach `plan` zeigt Text; JSON-Schlüssel und Diagnosecodes bleiben in jeder Sprache gleich.

## Umfang

Explizite Hardware-/Kanal-/Rollenbindungen, deklarierte Fähigkeiten, erlaubte Rollen, JSON-Zeiger, Kollisionsprüfung und SHA-256 der exakten Dateibytes. Die einfache light/switch-Dienstumstellung unterstützt ein einzelnes literales Ziel ohne Aktionsdaten. Dynamische Jinja-Ausdrücke, indirekte Geräte-/Bereichs-/Label-Ziele, unbekannte Referenzen und nicht unterstützte Formate blockieren den Plan.

YAML muss ausdrücklich nach JSON normalisiert und geprüft werden. Kommentare, Anker und Formatierung werden nicht übernommen. `ready` bestätigt weder die Vollständigkeit einer HA-Prüfung noch die tatsächliche Verdrahtung. Version 0.1.0 hat keinen Netzwerkclient und keinen apply-Befehl.

[Modell](docs/en/model.md) · [Beispiele](docs/en/examples.md) · [Architektur](docs/en/architecture.md) · [Fehlerbehebung](docs/en/troubleshooting.md) · [Grenzen](docs/en/limitations.md) · [Sicherheit](SECURITY.md) · [Wiki-Quelldateien](wiki/Home.md)

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 tools/generate_examples.py
python3 tools/render_diagrams.py
```

Tests verwenden keine realen Geräte. Die reproduzierbaren SVGs sind synthetische Diagramme, keine Messkurven oder Fotos. Ausführliche Handbücher liegen auf Englisch und Russisch vor; CLI und README unterstützen alle vier Sprachen. MIT-Lizenz.
