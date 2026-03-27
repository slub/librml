# Begrenztes Abspielen des Objekts

Die Wiedergabe der Audio-/Videodatei ist ausschnittsweise erlaubt, jedoch maximal auf zwei Minuten beschränkt.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- run (Ausführen)

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="readonly-449" template="Read only" tenant="https://www.slub-dresden.de/">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="archive" permission="true"/>
    <action type="read" permission="true">
      <restriction type="duration" percentage="10"/>
      <restriction type="duration" maxduration="120"/>
    </action>
    <action type="run" permission="true">
      <restriction type="duration" percentage="10"/>
      <restriction type="duration" maxduration="120"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "readonly-449",
  "template": "Read Only",
  "tenant": "https://www.slub-dresden.de/",
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
      "type": "archive",
      "permission": true
    },
    {
      "type": "read",
      "permission": true,
      "restrictions": [
        {
          "type": "duration",
          "percentage": "10"
        },
        {
          "type": "duration",
          "maxduration": "120"
        }
      ]
    }
    {
      "type": "run",
      "permission": true,
      "restrictions": [
        {
          "type": "duration",
          "percentage": "10"
        },
        {
          "type": "duration",
          "maxduration": "120"
        }
      ]
    }
  ]
}
```
