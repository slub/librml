# Zugang nur innerhalb eines IP-Adressbereichs (z.B. Campusnetz)

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

#### XML

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="iprestricted-444" tenant="https://www.slub-dresden.de/" commercialuse="false" template="IP">
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

#### JSON

```json
{
  "id": "iprestricted-444",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": false,
  "template": "IP",
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
