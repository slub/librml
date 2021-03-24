# Zugang nur nach Authentifizierung

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :------- | :--------- | :--------- |
| displaymetadata<br/><br/>index<br/><br/>archive | Authentifizierung | read<br/><br/>download<br/><br/>print |

**JSON**
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
      "type": "archive",
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
    }
  ]
}


{% endhighlight %}

**XML**
{% highlight xml %}
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.3">
  <item id="doi:10.1371/journal.pbio.0020447" tenant="http://slub-dresden.de" template="Authentification">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="archive" permission="true"/>
    <action type="read" permission="true">
      <restriction type="group" groups="registered"/>
    </action>
    <action type="download" permission="true">
      <restriction type="group" groups="registered"/>
    </action>
    <action type="print" permission="true">
      <restriction type="group" groups="registered"/>
    </action>

  </item>
</libRML>
{% endhighlight %}
