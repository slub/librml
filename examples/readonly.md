# Anzeige des Objekts

Zugang zum Objekt zur Ansicht ohne weitere Nutzungsmöglichkeiten, wie Speichern oder Drucken. 

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- read (Lesen)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- Keine

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="readonly-449" tenant="https://www.slub-dresden.de/" template="Read only">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="read" permission="true"/>
    <action type="archive" permission="true"/>
  </item>
</libRML>
```

```json
{
  "id": "readonly-449",
  "tenant": "https://www.slub-dresden.de/",
  "template": "Read Only",
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
      "permission": true
    },
    {
      "type": "archive",
      "permission": true
    }
  ]
}
```
