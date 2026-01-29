# Beschränkung auf eine bestimmte Menge gleichzeitiger Zugänge

| Zugelassene Actions | Constraint | Durch diese Constraint ermöglichte Action |
| :------- | :--------- | :--------- |
| displaymetadata<br/><br/>index<br/><br/>archive | Limitierte gleichzeitige Zugänge | read<br/><br/>download<br/><br/>print |

#### XML

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item id="concuracc-440" tenant="https://www.slub-dresden.de/" commercialuse="true" template="ConcurrentAccess">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="archive" permission="true"/>
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

#### JSON

```json
{
  "id": "concuracc-440",
  "tenant": "https://www.slub-dresden.de/",
  "commercialuse": true,
  "template": "ConcurrentAccess",
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
