# Anzeige der Metadaten

Zugang nur zu Metadaten. Nutzung (Ansicht, Download, ...) des digitalen Objekts ist nicht möglich. 

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)

**Eingeschränkte Nutzungsarten**:

- Keine

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="metaonly-441" tenant="https://www.slub-dresden.de/" template="Metadata access only">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
  </item>
</libRML>
```

```json
{
  "id": "metaonly-441",
  "tenant": "https://www.slub-dresden.de/",
  "template": "Metadata access only",
  "actions": [
    {
      "type": "displaymetadata",
      "permission": true
    },
    {
      "type": "index",
      "permission": true
    }
  ]
}
```
