# Zugang nur innerhalb eines IP-Adressbereichs (z.B. Campusnetz)

| Zugelassene Actions | Constraint | Durch diese Constraint ermöglichte Action |
| :------- | :--------- | :--------- |
| displaymetadata<br/><br/>index<br/><br/>archive | Einrichtung (IP-Bereich)| read<br/><br/>download<br/><br/>print |

**JSON**

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
          "subnet": [
            "192.168.10.0/24"
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
          "subnet": [
            "192.168.10.0/24"
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
          "subnet": [
            "192.168.10.0/24"
          ]
        }
      ]
    }
  ]
}
```

**XML**

```xml
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.3">
  <item id="iprestricted-444" tenant="http://slub-dresden.de" commercialuse="false" template="IP">
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
