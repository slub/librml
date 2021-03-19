# Location
## 4. Zugang nur innerhalb einer Einrichtung/eines Campus/eines IP-Adressbereichs

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive | Einrichtung | read<br/><br/>download<br/><br/>print |


**JSON**
{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
  "template": "IP",
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
          "type": "location",
          "subnet": [
            "192.168.10.0/24"
          ]
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "location",
          "subnet": [
            "192.168.10.0/24"
          ]
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "location",
          "subnet": [
            "192.168.10.0/24"
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


**XML**
{% highlight xml %}
<?xml version='1.0' encoding='ASCII'?>
<libRML version="0.3">
  <item id="doi:10.1371/journal.pbio.0020447" tenant="http://slub-dresden.de" template="Authentification">
    <action type="displaymetadata" permission="true"/>
    <action type="index" permission="true"/>
    <action type="read" permission="true">
      <restriction type="location" subnet="192.168.10.0/24"/>
    </action>
    <action type="download" permission="true">
      <restriction type="location" subnet="192.168.10.0/24"/>
    </action>
    <action type="print" permission="true">
      <restriction type="location" subnet="192.168.10.0/24"/>
    </action>
    <action type="archive" permission="true"/>
  </item>
</libRML>
{% endhighlight %}