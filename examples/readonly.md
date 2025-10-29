# Nur zur Ansicht, aber keine Speicher- oder Druckmöglichkeit

| Zugelassene Actions | Constraint | Durch diese Constraint ermöglichte Action |
| :------- | :--------- | :--------- |
| displaymetadata<br/><br/>index<br/><br/>read<br/><br/>archive | Keine | Keine |

**JSON**

```json
{
  "id": "readonly-449",
  "tenant": "https://www.slub-dresden.de/",
  "template": "Read Only",
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
      "type": "read",
      "permission": true
    },
    {
      "type": "archive",
      "permission": true
    }
  ]
}
```

**XML**

```xml
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.4">
  <item id="readonly-449" tenant="http://slub-dresden.de" template="Read only">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="read" permission="true"/>
    <action type="archive" permission="true"/>
  </item>
</libRML>
```
