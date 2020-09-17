# CC BY-NC-ND 4.0
## Creative Commons mit Namensnennung, nicht kommerziell und keine Veränderungen/Ableitungen


{% highlight javascript %}

{
  "id": "demo-mit-CCBYNCND",
  "tenant": "http://www.slub-dresden.de",
  "mention": true,
  "usageguide": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
  "template": "CCBYNCND-V4.0",
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
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    },
    {
      "type": "reproduce",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    },
    {
      "type": "distribute",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    },
    {
      "type": "publish",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    },
    {
      "type": "archive",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    },
    {
      "type": "move",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        }
      ]
    }
  ]
}

{% endhighlight %}