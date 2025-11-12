# Urheberrechtsschutz + Open Access

## Allgemeine Informationen

Das LibRML kann aus den folgenden Werten abgeleitet werden:

- [Access Status](https://wiki.dnb.de/pages/viewpage.action?pageId=217533654) = [Open Access](http://purl.org/coar/access_right/c_abf2)
- [Rechtehinweis](https://wiki.dnb.de/pages/viewpage.action?pageId=217533656) = [Urheberrechtsschutz 1.0](http://rightsstatements.org/vocab/InC/1.0/)

Hinweis:

- Es wird eine Bereitstellung des Objekts in einem Open Access-Repositorium angenommen, die frei zugänglich und speicherbar ist. Die Weiterverwendung und Anpassung ist nur in Abstimmung mit dem Urheber oder der Urheberin möglich. Schranken des Urheberechts werden nicht berücksichtigt.
- Es wird keine Garantie für die juristische Korrektheit gegeben.

#### XML

```xml
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.4" xmlns:libRML="https://librml.org/schema">
  <item id="copyright-oa-100" tenant="https://slub-dresden.de/" usageguide="http://librml.org/examples/copyright_openaccess"  template="LibRML Copyright - Open Access">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="read" permission="true"/>
    <action type="download" permission="true"/>
    <action type="print" permission="true"/>
    <action type="archive" permission="true"/>
  </item>
</libRML>
```

#### JSON

```json
{
  "id": "copyright-oa-100",
  "tenant": "https://www.slub-dresden.de/",
  "usageguide": "https://librml.org/examples/copyright_openaccess",
  "template": "LibRML Copyright - Open Access",
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
      "type": "download",
      "permission": true
    },
    {
      "type": "print",
      "permission": true
    },
    {
      "type": "archive",
      "permission": true
    }
  ]
}
```
