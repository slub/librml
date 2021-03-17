# Read only
## 5. Zugang nur zur Ansicht, aber keine Speicherungs-/Druckmöglichkeit

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive<br/><br/>read | Keine | Keine |

{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
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

{% endhighlight %}