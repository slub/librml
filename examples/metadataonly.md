# Anzeige der Metadaten

Zugang nur zu Metadaten, eine weitere Nutzung (z.B. Ansicht und Download) des digitalen Objekts ist nicht möglich.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)

**Eingeschränkte Nutzungsarten**:

- Keine

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.6" xmlns="http://librml.org/schema">
  <item id="metaonly-441" template="Metadata access only" tenant="https://www.slub-dresden.de/">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
  </item>
</libRML>
```

```json
{
  "id": "metaonly-441",
  "template": "Metadata access only",
  "tenant": "https://www.slub-dresden.de/",
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
