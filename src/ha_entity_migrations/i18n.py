"""Human-facing text. Stable report keys and diagnostic codes are not translated."""

LANGUAGES = ("en", "ru", "de", "es")
ROWS = {
    "description": (
        "Plan Home Assistant entity migrations without changing anything.",
        "План миграции сущностей Home Assistant без изменений.",
        "Home-Assistant-Entitätsmigrationen ohne Änderungen planen.",
        "Planificar migraciones de entidades de Home Assistant sin modificar nada.",
    ),
    "language": ("Language", "Язык", "Sprache", "Idioma"),
    "plan_help": (
        "Build a read-only plan",
        "Построить план без изменений",
        "Schreibgeschützten Plan erstellen",
        "Crear un plan de solo lectura",
    ),
    "fingerprint_help": (
        "SHA-256 of exact file bytes",
        "SHA-256 точных байтов файла",
        "SHA-256 der exakten Dateibytes",
        "SHA-256 de los bytes exactos del archivo",
    ),
    "manifest_help": (
        "Manifest JSON path",
        "Путь к JSON-манифесту",
        "Pfad zum JSON-Manifest",
        "Ruta del manifiesto JSON",
    ),
    "snapshot_help": (
        "Normalized snapshot JSON path",
        "Путь к нормализованному JSON-снимку",
        "Pfad zum normalisierten JSON-Snapshot",
        "Ruta de la instantánea JSON normalizada",
    ),
    "root_help": (
        "Source-file root directory",
        "Корень исходных файлов",
        "Wurzelverzeichnis der Quelldateien",
        "Directorio raíz de archivos fuente",
    ),
    "format_help": ("Output format", "Формат вывода", "Ausgabeformat", "Formato de salida"),
    "help": ("Show this help", "Показать справку", "Diese Hilfe anzeigen", "Mostrar esta ayuda"),
    "version_help": ("Show version", "Показать версию", "Version anzeigen", "Mostrar versión"),
    "ready": (
        "Ready for review within supplied files; nothing applied.",
        "Готово к проверке в пределах переданных файлов; ничего не применено.",
        "Zur Prüfung der übergebenen Dateien bereit; nichts angewendet.",
        "Listo para revisar los archivos proporcionados; no se aplicó nada.",
    ),
    "blocked": (
        "Plan blocked; resolve every diagnostic before using it.",
        "План заблокирован; устраните все замечания перед использованием.",
        "Plan blockiert; vor Verwendung alle Diagnosen klären.",
        "Plan bloqueado; resuelva todos los diagnósticos antes de usarlo.",
    ),
    "edits": (
        "Proposed edits",
        "Предложенные изменения",
        "Vorgeschlagene Änderungen",
        "Cambios propuestos",
    ),
    "input_error": (
        "Input rejected",
        "Входные данные отклонены",
        "Eingabe abgelehnt",
        "Entrada rechazada",
    ),
    "arguments": (
        "Invalid arguments; see --help.",
        "Неверные аргументы; смотрите --help.",
        "Ungültige Argumente; siehe --help.",
        "Argumentos no válidos; consulte --help.",
    ),
    "unsafe_file": (
        "Expected a regular file, not a symlink or device.",
        "Нужен обычный файл, не ссылка или устройство.",
        "Reguläre Datei statt Verknüpfung oder Gerät erwartet.",
        "Se esperaba un archivo normal, no un enlace o dispositivo.",
    ),
    "size_limit": (
        "Input size limit exceeded.",
        "Превышен предел размера входных данных.",
        "Größenlimit der Eingabe überschritten.",
        "Se superó el límite de tamaño de entrada.",
    ),
    "read_failed": (
        "File could not be read.",
        "Не удалось прочитать файл.",
        "Datei konnte nicht gelesen werden.",
        "No se pudo leer el archivo.",
    ),
    "duplicate_key": (
        "Duplicate JSON key.",
        "Повторный ключ JSON.",
        "Doppelter JSON-Schlüssel.",
        "Clave JSON duplicada.",
    ),
    "duplicate_source": (
        "Two source names refer to one file. Keep one canonical name and update its consumers.",
        "Два имени источника указывают на один файл. Оставьте одно имя и обновите потребителей.",
        "Zwei Quellnamen verweisen auf eine Datei. Einen kanonischen Namen und dessen Verbraucher verwenden.",
        "Dos nombres de origen apuntan al mismo archivo. Conserve un nombre canónico y actualice sus consumidores.",
    ),
    "invalid_json": (
        "Invalid UTF-8 or strict JSON.",
        "Неверный UTF-8 или строгий JSON.",
        "Ungültiges UTF-8 oder striktes JSON.",
        "UTF-8 o JSON estricto no válido.",
    ),
    "structure_limit": (
        "JSON depth or node limit exceeded.",
        "Превышен предел глубины или числа узлов JSON.",
        "JSON-Tiefen- oder Knotenlimit überschritten.",
        "Se superó el límite de profundidad o nodos JSON.",
    ),
    "unsafe_path": (
        "Source path escapes the root or uses a symlink.",
        "Путь выходит за корень или использует ссылку.",
        "Quellpfad verlässt die Wurzel oder verwendet eine Verknüpfung.",
        "La ruta sale de la raíz o usa un enlace.",
    ),
    "invalid_pointer": (
        "JSON pointer does not resolve exactly.",
        "JSON-указатель не указывает на точное значение.",
        "JSON-Zeiger lässt sich nicht exakt auflösen.",
        "El puntero JSON no se resuelve exactamente.",
    ),
    "schema_invalid": (
        "Input does not satisfy the documented schema.",
        "Данные не соответствуют документированной схеме.",
        "Eingabe entspricht nicht dem dokumentierten Schema.",
        "La entrada no cumple el esquema documentado.",
    ),
    "stale_snapshot": (
        "Snapshot fingerprint differs from the manifest.",
        "Отпечаток снимка отличается от манифеста.",
        "Snapshot-Prüfsumme weicht vom Manifest ab.",
        "La huella de la instantánea difiere del manifiesto.",
    ),
    "stale_source": (
        "Source fingerprint differs from the manifest.",
        "Отпечаток исходного файла отличается от манифеста.",
        "Quellprüfsumme weicht vom Manifest ab.",
        "La huella del archivo fuente difiere del manifiesto.",
    ),
    "source_collision": (
        "Duplicate entity, hardware channel or role in snapshot.",
        "Повтор сущности, канала или роли в снимке.",
        "Doppelte Entität, Hardwarekanal oder Rolle im Snapshot.",
        "Entidad, canal físico o función duplicados en la instantánea.",
    ),
    "unknown_hardware": (
        "Assignment refers to absent hardware/channel.",
        "Назначение ссылается на отсутствующий канал устройства.",
        "Zuweisung verweist auf fehlende Hardware/Kanal.",
        "La asignación hace referencia a hardware/canal ausente.",
    ),
    "assignment_collision": (
        "Hardware channel assigned more than once.",
        "Канал назначен несколько раз.",
        "Hardwarekanal mehrfach zugewiesen.",
        "Canal físico asignado más de una vez.",
    ),
    "destination_collision": (
        "Result contains a duplicate entity ID or role.",
        "Результат содержит повтор entity ID или роли.",
        "Ergebnis enthält doppelte Entitäts-ID oder Rolle.",
        "El resultado contiene una ID o función duplicada.",
    ),
    "consumer_collision": (
        "More than one policy for the same reference.",
        "Для одной ссылки задано несколько политик.",
        "Mehrere Richtlinien für dieselbe Referenz.",
        "Más de una política para la misma referencia.",
    ),
    "unsupported_source": (
        "Only JSON sources can be planned; convert other formats explicitly.",
        "Планирование поддерживает только JSON; другие форматы конвертируйте явно.",
        "Nur JSON-Quellen planbar; andere Formate explizit konvertieren.",
        "Solo se planifican fuentes JSON; convierta otros formatos explícitamente.",
    ),
    "unmodeled_reference": (
        "Entity reference is absent from the normalized snapshot.",
        "Ссылка отсутствует в нормализованном снимке.",
        "Entitätsreferenz fehlt im normalisierten Snapshot.",
        "La referencia no está en la instantánea normalizada.",
    ),
    "retire_scope_mixed": (
        "Retirement scope contains other or dynamic references.",
        "Область удаления содержит другие или динамические ссылки.",
        "Entfernungsbereich enthält andere oder dynamische Referenzen.",
        "El ámbito de retirada contiene otras referencias o referencias dinámicas.",
    ),
    "indirect_target": (
        "Device, area or label target requires manual resolution.",
        "Цель device, area или label требует ручного разрешения.",
        "Geräte-, Bereichs- oder Label-Ziel muss manuell aufgelöst werden.",
        "El destino por dispositivo, área o etiqueta requiere resolución manual.",
    ),
    "dynamic_reference": (
        "Dynamic template requires manual review; it was not executed.",
        "Динамический шаблон требует проверки; он не выполнялся.",
        "Dynamische Vorlage manuell prüfen; sie wurde nicht ausgeführt.",
        "La plantilla dinámica requiere revisión; no se ejecutó.",
    ),
    "embedded_reference": (
        "Embedded reference requires manual review.",
        "Встроенная ссылка требует ручной проверки.",
        "Eingebettete Referenz muss manuell geprüft werden.",
        "La referencia integrada requiere revisión manual.",
    ),
    "missing_policy": (
        "Reference has no explicit consumer policy.",
        "Для ссылки не задана явная политика.",
        "Referenz ohne explizite Verbraucherrichtlinie.",
        "La referencia no tiene una política explícita.",
    ),
    "role_retired": (
        "Original role has no destination.",
        "У исходной роли нет назначения.",
        "Ursprüngliche Rolle ohne Ziel.",
        "La función original no tiene destino.",
    ),
    "role_not_allowed": (
        "Destination role is forbidden for this consumer.",
        "Новая роль запрещена для этого потребителя.",
        "Zielrolle für diesen Verbraucher nicht erlaubt.",
        "La función de destino no está permitida para este consumidor.",
    ),
    "capability_missing": (
        "Destination lacks a required capability.",
        "У назначения нет необходимой возможности.",
        "Dem Ziel fehlt eine erforderliche Fähigkeit.",
        "Al destino le falta una capacidad requerida.",
    ),
    "display_domain_review": (
        "Changed display domain requires card/features review.",
        "Смена домена требует проверки карточки и её функций.",
        "Geänderte Anzeigedomäne erfordert Karten-/Funktionsprüfung.",
        "El cambio de dominio requiere revisar la tarjeta y sus funciones.",
    ),
    "service_domain_review": (
        "Service conversion is unsupported; review manually.",
        "Преобразование сервиса не поддержано; проверьте вручную.",
        "Dienstkonvertierung nicht unterstützt; manuell prüfen.",
        "Conversión de servicio no admitida; revise manualmente.",
    ),
    "service_scope_mismatch": (
        "Service pointer does not own this target reference.",
        "Указанный сервис не содержит эту целевую ссылку.",
        "Dienstzeiger gehört nicht zu dieser Zielreferenz.",
        "El puntero de servicio no pertenece a esta referencia de destino.",
    ),
    "service_data_review": (
        "Domain conversion with action data needs manual review.",
        "Смена домена с данными действия требует проверки.",
        "Domänenwechsel mit Aktionsdaten muss manuell geprüft werden.",
        "El cambio de dominio con datos de acción requiere revisión manual.",
    ),
    "mixed_action_targets": (
        "Shared service has multiple targets; do not change its domain blindly.",
        "У общего сервиса несколько целей; нельзя менять домен вслепую.",
        "Gemeinsamer Dienst hat mehrere Ziele; Domäne nicht blind ändern.",
        "El servicio compartido tiene varios destinos; no cambie su dominio a ciegas.",
    ),
    "unused_policy": (
        "Policy did not match an analyzable reference.",
        "Политика не соответствует анализируемой ссылке.",
        "Richtlinie passt zu keiner analysierbaren Referenz.",
        "La política no coincide con una referencia analizable.",
    ),
    "overlapping_edits": (
        "Proposed edit scopes overlap.",
        "Области предложенных изменений пересекаются.",
        "Vorgeschlagene Änderungsbereiche überlappen.",
        "Los ámbitos de los cambios propuestos se superponen.",
    ),
}
CATALOGS = {
    lang: {key: row[index] for key, row in ROWS.items()} for index, lang in enumerate(LANGUAGES)
}


def tr(lang: str, key: str) -> str:
    return CATALOGS[lang][key]
