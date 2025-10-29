# Zugang nur zu Metadaten

| Zugelassene Actions | Constraint | Durch diese Constraint ermöglichte Action |
| :------- | :--------- | :--------- |
| displaymetadata<br/><br/>index | Keine | Keine |

**JSON**

```json
{
  "id": "metaonly-441",
  "tenant": "https://www.slub-dresden.de/",
  "template": "Metadata access only",
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

**XML**

```xml
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.4">
  <item id="metaonly-441" tenant="http://slub-dresden.de" template="Metadata access only">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
  </item>
</libRML>
```
