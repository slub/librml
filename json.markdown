# Beispiel
## JSON

{% highlight javascript %}
{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
  "mention": true,
  "sharealike": true,
  "usageguide": "https://nutzungshinweis.slub-dresden.de/il-ma/1.0/",
  "template": "CCBYSA",
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
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2025-02-11"
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2025-02-11"
        },
        {
          "type": "quality",
          "maxresolution": 300
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2030-02-11"
        },
        {
          "type": "quality",
          "maxresolution": 1200
        }
      ]
    },
    {
      "type": "lend",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "2025-02-11"
        },
        {
          "type": "group",
          "groups": [
            "student",
            "employee",
            "kecksesser"
          ]
        },
        {
          "type": "count",
          "count": 3
        },
        {
          "type": "concurrent",
          "sessions": 5
        },
        {
          "type": "location",
          "inside": "in",
          "outside": "out",
          "subnet": [
            "192.168.10.0/24",
            "10.8.0.0/16"
          ],
          "machines": [
            "aa-bb-cc-dd-ee-ff",
            "11-22-33-44-55-66"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        },
        {
          "type": "quality",
          "maxbitrate": 256
        },
        {
          "type": "date",
          "fromdate": "2025-02-11"
        },
        {
          "type": "parts",
          "parts": [
            "datei1.jpg",
            "datei2.jpg",
            "datei3.jpg"
          ]
        },
        {
          "type": "watermark",
          "watermarkvalue": "Thoms war da!"
        },
        {
          "type": "duration",
          "duration": 432000
        }
      ]
    }
  ]
}

{% endhighlight %}