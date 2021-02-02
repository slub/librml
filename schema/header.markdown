# Header
## Allgemeine Informationen und Haupteinschränkungen

Im **Header** befinden sich wichtige Informationen zum Objekt die unter anderem der Verknüpfung mit besagtem Objekt aber auch mit eventuellen anderen Versionen desselben dienen, sowie mit der Einrichtung die diese Ressourcen verwalten und eventuelle Richtlinien und Lizenzen.

Des Weiteren werden auch hier allgemeine Einschränkungen beschrieben die für alle Nutzungsrechte bezüglich dieses Objekts gelten.

Die wichtigste Information in diesem **Header** die auf keinem Fall fehlen darf ist dabei die **id**. Ohne Identifizierung kann die LibRML nicht mit dem Objekt verknüpft werden.

Die Felder **relatedids** (wenn zutreffend) und **tenant** sollten ebenfalls ausgefüllt werden. Zum einen um eventuelle Fehler zu vermeiden und Klarheit zu schaffen, falls es andere Vorkommnisse desselben Objekts gibt, zum anderen um Klar zu stellen, wer für die Verwaltung zuständig ist.
Alle anderen Felder sind Fakultativ. Jedoch sollten sie ausgefüllt werden, wenn zutreffend.


- **id**: ID zur Identifizierung der Ressource
- **relatedids**: Andere IDs im Falle einer Ressource mit mehreren IDs (mehr als einmal im Katalog vorhanden) und/oder mehreren Verträgen (unter unterschiedlichen Lizenzen)
- **tenant**: Einrichtung, die die Ressource verwaltet
- **template**: Name des eventuell benutzten Templates (wird automatisch beim aussuchen einer Vorlage ausgefüllt)
- **usageguide**: URL auf der sich die Richtlinien der dazugehörigen Lizenz befinden 

Zudem können in den Attributen noch zwei generelle Einschränkungen definiert werden:

- **mention**: die Namensnennung
- **sharealike**: Verpflichtung alle Derivate der Ressource unter denselben Bedingungen zu veröffentlichen
- **copyright**: das Bestehen oder nicht eines Urheberrechtschutzes

### Ein Beispiel

Ein Objekt mit zwei anderen IDs, von der SLUB verwaltet mit Namensnennung, Wiederbenutzung und Weiterverbreitung unter denselben Einschränkungen wie das Original und Urheberrechtsgeschützt.

**JSON**

{% highlight javascript %}

    "id": "id-123456",
    "relatedids": [
        "A-id-123456",
        "B-id-123456"
    ],
    "tenant": "http://slub-dresden.de",
    "mention": true,
    "sharealike": true,
    "copyright": true,

{% endhighlight %}

**XML**


{% highlight xml %}
  <item id="id-123456" tenant="http://slub-dresden.de" mention="true" sharealike="true" copyright="true">
    <relatedid id="A-id-123456"/>
    <relatedid id="B-id-123456"/>
{% endhighlight %}