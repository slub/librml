# Authentification
## 2. Zugang nur nach Authentifizierung

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive | Authentifizierung | read<br/><br/>download<br/><br/>print |

{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
  "template": "Authentification",
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
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "group",
          "groups": [
            "registered"
          ]
        }
      ]
    },
    {
      "type": "archive",
      "permission": true
    }
  ]
}


{% endhighlight %}