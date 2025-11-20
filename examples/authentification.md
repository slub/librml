# Zugang nur nach Authentifizierung

| Zugelassene Actions | Constraint | Durch diese Constraint ermöglichte Action |
| :------- | :--------- | :--------- |
| displaymetadata<br/><br/>index<br/><br/>archive | Authentifizierung | read<br/><br/>download<br/><br/>print |

#### XML

```xml
<?xml version='1.0' encoding='ASCII'?>
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

#### JSON

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
