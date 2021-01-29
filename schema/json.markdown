# Beispiel
## JSON


Nehmen wir als Beispiel eine e-Ressource die Urheberrecht geschützt ist aber für die die SLUB rechte zur Digitalisierung (inkl. dauerhafter Speicherung, Ablage in Datenbanken und öffentlicher Zugänglichmachung im Internet), mit Ausnahme der Nutzung zu kommerziellen Zwecken bekommen hat. 

{% highlight javascript %}

{
  "id": "DE-611-HS-3665348",
  "tenant": "http://www.slub-dresden.de",
  "copyright": true,
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
    },
    {
      "type": "distribute",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        },
      ]
    },
    {
      "type": "archive",
      "permission": true,
    },
    {
      "type": "move",
      "permission": true,
      "restrictions": [
        {
          "type": "commercialuse",
          "noncommercialuse": true
        },
      ]
    },
  ]
}

{% endhighlight %}