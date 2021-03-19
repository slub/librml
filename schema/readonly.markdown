# Read only
## 5. Zugang nur zur Ansicht, aber keine Speicherungs-/Druckmöglichkeit

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive<br/><br/>read | Keine | Keine |


**JSON**
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

**XML**
{% highlight xml %}
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.3">
  <item id="doi:10.1371/journal.pbio.0020447" tenant="http://slub-dresden.de" template="Metadata access only">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="read" permission="true"/>
    <action type="archive" permission="true"/>
  </item>
</libRML>
{% endhighlight %}