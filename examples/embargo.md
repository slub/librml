# Embargofrist

Aufgrund eines Embargos ist der Zugang zum Digitalisat bis zum 31. Dezember 2028 nur eingeschränkt, d.h. in verminderter Auflösung, möglich.

Ab dem 1. Januar 2029 ist der Zugang dann uneingeschränkt möglich.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexieren)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Ausdrucken)
- print (Herunterladen)

**Art der Einschränkung**:

- quality (Auflösung) mit date (zeitlich)

```xml
<?xml version="1.0" encoding="ASCII"?>
<libRML version="0.4" xmlns="https://librml.org/schema">
  <item commercialuse="false" id="embargo-28" template="IP" tenant="https://www.slub-dresden.de/">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="archive" permission="true"/>
    <action type="read" permission="true">
      <restriction type="quality" maxresolution="72"/>
      <restriction type="date" todate="2028-12-31"/>
    </action>
    <action type="read" permission="true">
      <restriction type="date" fromdate="2029-01-01"/>
    </action>
    <action type="download" permission="true">
      <restriction type="quality" maxresolution="72"/>
      <restriction type="date" todate="2028-12-31"/>
    </action>
    <action type="download" permission="true">
      <restriction type="date" fromdate="2029-01-01"/>
    </action>
    <action type="print" permission="true">
      <restriction type="quality" maxresolution="72"/>
      <restriction type="date" todate="2028-12-31"/>
    </action>
    <action type="print" permission="true">
      <restriction type="date" fromdate="2029-01-01"/>
    </action>
  </item>
</libRML>
```

```json
{
  "id": "embargo-28",
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
          "type": "quality",
          "maxresolution": 72
        },
        {
          "type": "date",
          "todate": "2028-12-31"
        }
      ]
    },
    {
      "type": "read",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2029-01-01"
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "quality",
          "maxresolution": 72
        },
        {
          "type": "date",
          "todate": "2028-12-31"
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2029-01-01"
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "quality",
          "maxresolution": 72
        },
        {
          "type": "date",
          "todate": "2028-12-31"
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2029-01-01"
        }
      ]
    }
  ]
}
```
