# Limited concurrent uses 
## 6. Beschränkung auf eine bestimmte Menge gleichzeitiger Zugänge

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