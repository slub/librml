# IP-Adressbereich

Zugang und Nutzung nur innerhalb eines IP-Adressbereichs, wie zum Beispiel Campusnetz.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Ausdrucken)
- print (Herunterladen)

**Art der Einschränkung**:

- location (ortsspezifisch)

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.6" xmlns="http://librml.org/schema">
  <item commercialuse="false" id="iprestricted-444" template="IP" tenant="https://www.slub-dresden.de/">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="archive" permission="true"/>
    <action type="read" permission="true">
      <restriction type="location" subnet="192.168.10.0/24"/>
    </action>
    <action type="download" permission="true">
      <restriction type="location" subnet="192.168.10.0/24"/>
    </action>
    <action type="print" permission="true">
      <restriction type="location" subnet="192.168.10.0/24"/>
    </action>
  </item>
</libRML>
```

```json
{
  "commercialuse": false,
  "id": "iprestricted-444",
  "template": "IP",
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
          "type": "location",
          "inside": [
            "library"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "location",
          "inside": [
            "library"
          ]
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "location",
          "inside": [
            "library"
          ]
        }
      ]
    }
  ]
}
```
