# Authentifizierung

Zugang und Nutzung nur nach Authentifizierung. In LibRML wird dies durch Zugehörigkeit zu einer Gruppe beschrieben. 

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Herunterladen)
- print (Ausdrucken)

**Art der Einschränkung**:

- group (Gruppe)

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="auth-DE-442" tenant="https://www.slub-dresden.de/" commercialuse="true" template="Authentification">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="archive" permission="true"/>
    <action type="read" permission="true">
      <restriction type="group" groups="registered"/>
    </action>
    <action type="download" permission="true">
      <restriction type="group" groups="registered"/>
    </action>
    <action type="print" permission="true">
      <restriction type="group" groups="registered"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "auth-DE-442",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": true,
  "template": "Authentification",
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
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    }
  ]
}
```
