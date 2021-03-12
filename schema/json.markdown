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


| Beispiel Benennung | Zugelassene Actions | Eventuelle Einschränkung | Durch diese Einschränkung ermöglichte Action | Link zum JSON |
| :--------:| :-------: | :---------: | :---------: | :---------: |
| **Zugang nur zu Metadaten** | displaymetadata<br/><br/>index | Keine | Keine | [Metadata only](metadataonly.markdown) |
| **Zugang nur nach Authentifizierung** | displaymetadata<br/><br/>index<br/><br/>archive | Authentifizierung | read<br/><br/>download<br/><br/>print | [Authentification](authentification.markdown) |
| **Zugang nur nach Abschluss eines Nutzungsvertrags** | displaymetadata<br/><br/>index<br/><br/>archive | Nutzungsvertrag | read<br/><br/>download<br/><br/>print<br/><br/>reproduce<br/><br/>modify<br/><br/>reuse<br/><br/>distribute<br/><br/>publish<br/><br/>move | [Agreement](agreement.markdown) |
| **Zugang nur innerhalb einer Einrichtung/eines IP-Adressbereichs** | displaymetadata<br/><br/>index<br/><br/>archive | Einrichtung | read<br/><br/>download<br/><br/>print | [location](location.markdown) |
| **Zugang nur zur Ansicht, aber keine Speicherungs-/Druckmöglichkeit** | displaymetadata<br/><br/>index<br/><br/>archive<br/><br/>read | Keine | Keine | [Read only](readonly.markdown) |
| **Beschränkung auf eine bestimmte Menge gleichzeitiger Zugänge** | displaymetadata<br/><br/>index<br/><br/>archive | Limitierte gleichzeitige Zugänge | read<br/><br/>download<br/><br/>print | [Limited concurrent uses](concurrent.markdown) |

