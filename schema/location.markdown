# Location
## 4. Zugang nur innerhalb einer Einrichtung/eines Campus/eines IP-Adressbereichs

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
