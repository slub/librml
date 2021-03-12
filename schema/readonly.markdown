# Read only
## 5. Zugang nur zur Ansicht, aber keine Speicherungs-/Druckmöglichkeit

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