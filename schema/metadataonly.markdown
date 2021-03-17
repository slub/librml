# Metadata Only
## 1. Zugang nur zu Metadaten

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index | Keine | Keine |

{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
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

{% endhighlight %}