# Limited concurrent uses 
## 6. Beschränkung auf eine bestimmte Menge gleichzeitiger Zugänge

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive | Limitierte gleichzeitige Zugänge | read<br/><br/>download<br/><br/>print |

{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
  "template": "TermsOfUse",
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

{% endhighlight %}