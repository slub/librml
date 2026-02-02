# Digitales Objekt zur Präsentation und nicht-kommerziellen Nutzung

Ein urheberrechtsbehaftetes digitales Objekt der [SLUB Dresden](https://www.slub-dresden.de), die im Rahmen der Digitalisierung die dauerhafte Speicherung, Ablage in Datenbanken, und dem öffentlicher Zugriff erlaubt. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken. **Nicht erlaubt** ist das herunterladen, ausdrucken, vervielfältigen, bearbeiten, wiederverwenden und veröffentlichen des digitalen Objektes.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- read (Lesen)
- archive (Archivieren)
- distribute ((Ver)teilen)
- move (Übertragen der Daten)

**Eingeschränkte Nutzungsarten**:

- Keine

#### XML

```xml
<?xml version="1.0" ?>
<libRML version="0.4" xmlns="https://librml.org/schema">
    <item id="DE-611-HS-3665348" tenant="https://www.slub-dresden.de/" commercialuse="false" copyright="true">
        <action type="displaymetadata" permission="true"/>
        <action type="index" permission="true"/>
        <action type="read" permission="true"/>
        <action type="archive" permission="true"/>
        <action type="distribute" permission="true"/>
        <action type="move" permission="true"/>
    </item>
</libRML>
```

#### JSON

```json
{
  "id": "digitisation-500",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": false,
  "copyright": true,
  "actions": [
    {
      "type": "displaymetadata",
      "permission": true
    },
    {
      "type": "index",
      "permission": true
    },
    {
      "type": "read",
      "permission": true,
    },
    {
      "type": "archive",
      "permission": true,
    },
    {
      "type": "distribute",
      "permission": true
    },
    {
      "type": "move",
      "permission": true
    },
  ]
}
```
