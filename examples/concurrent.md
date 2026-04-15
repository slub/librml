# Gleichzeitiger Zugriff

Zugang und Nutzung ist auf eine bestimmte Menge gleichzeitiger Zugriffe beschränkt.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- index (Indexnutzung)
- read (Lesen)
- download (Herunterladen)
- print (Ausdrucken)

**Art der Einschränkung**:

- concurrent (Gleichzeitig)

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="http://librml.org/schema">
  <item commercialuse="true" id="concuracc-440" template="ConcurrentAccess" tenant="https://www.slub-dresden.de/">
    <action type="displaymetadata" permission="true"/>
    <action type="archive" permission="true"/>
    <action type="index" permission="true">
      <restriction type="concurrent" sessions="5"/>
    </action>
    <action type="read" permission="true">
      <restriction type="concurrent" sessions="5"/>
    </action>
    <action type="download" permission="true">
      <restriction type="concurrent" sessions="5"/>
    </action>
    <action type="print" permission="true">
      <restriction type="concurrent" sessions="5"/>
    </action>
  </item>
</libRML>
```

```json
{
  "commercialuse": true,
  "id": "concuracc-440",
  "template": "ConcurrentAccess",
  "tenant": "https://www.slub-dresden.de/",
  "actions": [
    {
      "type": "displaymetadata",
      "permission": true
    },
    {
      "type": "archive",
      "permission": true
    },
    {
      "type": "index",
      "permission": true,
      "restrictions": [
        {
          "type": "concurrent",
          "sessions": 5
        }
      ]
    },
    {
      "type": "read",
      "permission": true,
      "restrictions": [
        {
          "type": "concurrent",
          "sessions": 5
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "concurrent",
          "sessions": 5
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "concurrent",
          "sessions": 5
        }
      ]
    }
  ]
}
```
