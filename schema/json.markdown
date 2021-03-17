# Beispiel
## JSON


Eine urheberrechtsbehaftete e-Ressource der [SLUB Dresden](https://www.slub-dresden.de), die im Rahmen der Digitalisierung die dauerhafte Speicherung, Ablage in Datenbanken, und dem öffentlicher Zugriff erlaubt. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken. **Nicht erlaubt** ist das herunterladen, ausdrucken, vervielfältigen, bearbeiten, wiederverwenden und veröffentlichen der e-Ressource.

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

### Weitere Beispiele

Zur besseren Verständigung und damit jeder sich jeder vorstellen kann wie eine LibRML in unterschiedlien Situationen aussehen soll, finden sie hier eine Liste von Beispiele die uns von André Hohmann vorgeschlagen wurden. 


| Beispiel Benennung | Link zum JSON |
| :--------: | :---------: |
| **Zugang nur zu Metadaten** | [Metadata only](metadataonly.markdown) |
| **Zugang nur nach Authentifizierung** | [Authentification](authentification.markdown) |
| **Zugang nur nach Abschluss eines Nutzungsvertrags** | [Agreement](agreement.markdown) |
| **Zugang nur innerhalb einer Einrichtung/eines IP-Adressbereichs** | [location](location.markdown) |
| **Zugang nur zur Ansicht, aber keine Speicherungs-/Druckmöglichkeit** | [Read only](readonly.markdown) |
| **Beschränkung auf eine bestimmte Menge gleichzeitiger Zugänge** | [Limited concurrent uses](concurrent.markdown) |
