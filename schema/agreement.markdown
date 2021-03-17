# Agreement
## 3. Zugang nur nach Abschluss eines Nutzungsvertrags

| Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action |
| :-------: | :---------: | :---------: |
| displaymetadata<br/><br/>index<br/><br/>archive | Nutzungsvertrag | read<br/><br/>download<br/><br/>print<br/><br/>reproduce<br/><br/>modify<br/><br/>reuse<br/><br/>distribute<br/><br/>publish<br/><br/>move |

{% highlight javascript %}

{
  "id": "doi:10.1371/journal.pbio.0020447",
  "tenant": "http://www.slub-dresden.de",
  "template": "Only Metadata Access",
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
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "download",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "reproduce",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "modify",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "reuse",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "distribute",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "publish",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
    {
      "type": "move",
      "permission": true,
      "restrictions": [
        {
          "type": "agreement",
          "required": true
        }
      ]
    },
  ]
}

{% endhighlight %}