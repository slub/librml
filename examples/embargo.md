# Embargofrist

Aufgrund eines Embargos ist der Zugang zum Digitalisat bis zum 31. Dezember 2028 nur eingeschränkt, d.h. in verminderter Auflösung, möglich.

Ab dem 1. Januar 2029 ist der Zugang dann uneingeschränkt möglich.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- index (Indexnutzung)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- read (Lesen)
- download (Ausdrucken)
- print (Herunterladen)

**Art der Einschränkung**:

- quality (Auflösung) mit date (zeitlich)

{% highlight xml %}
{% include_relative embargo.xml %}
{% endhighlight %}

```json
{
  "commercialuse": false,
  "id": "embargo-28",
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
          "type": "quality",
          "maxresolution": "72"
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
          "maxresolution": "72"
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
          "maxresolution": "72"
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
