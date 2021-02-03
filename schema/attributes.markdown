# Attributes
## Eigenschaften der verschiedenen Einschränkungen

Hier finden sie alle Attributes (sogenannte Eigenschaften) die, die in der LibRML beschrieben Einschränkungen beeinflussen können. 


- fromdate
    - Ab gegebenem Datum
    - Angabe nach ISO-Standard (YYYY-MM-DD) 

- todate 
    - Bis gegebenem Datum 
    - Angabe nach ISO-Standard (YYYY-MM-DD)

- maxresolution 
    - Maximale Auflösung
    - Angabe in DPI

- maxbitrate
    - Maximale Größe
    - Angabe in Bit

- count 
    - Anzahl (z.B. für die Anzahl an Ausleihen)
    - Angabe als Zahl - Integer

- sessions 
    - z.B. im Falle einer Ressource die nicht gleichzeitig auf zwei Rechnern angesehen werden darf
    - Angabe als Zahl - Integer

- inside 
    - Innerhalb (Wird für Geographische Einschränkungen oder Einschränkungen bezüglich der Einrichtung benutzt)
    - Angabe: "in"

- outside 
    - Außerhalb (Wird für Geographische Einschränkungen oder Einschränkungen bezüglich der Einrichtung benutzt)
    - Angabe: "out"

    > Im falle der Einschränkung bezüglich einer Einrichtung kann diese z.B. über das Subnet (Eine Gruppierung von IP Adressen die einem Teil des Netzwerks angehören) geschehen wofür das *Restriction Type* **Subnet** benutzt werden kann. 


- noncommercialuse 
    - Nicht kommerzielle Nutzung
    - Angabe: "true"/"false"

- commercialuse
    - Kommerzielle Nutzung
    - Angabe: "true"/"false"

- watermarkvalue 
    - Bezeichnung des Wasserzeichens
    - Das *Watermark* muss an einem spezifischen Ort hinterlegt sein der hier verlinkt ist

- duration 
    - Dauer
    - Angabe in non-negative Integer (Sekunden)

- minage 
    - Mindestalter (Wird für Jugendschutz und dergleichen benutzt)
    - Angabe als Zahl - Integer

- required
    - "Erforderlich" (wird bei der Erforderlichkeit von externen Verträgen benutzt)
    - Angabe: "true"/"false"


### Anwendung

**JSON**

Einschränkungen werden in LibRML in das jeweilige Element mit dem zugehörigen Attribut eingetragen.

{% highlight javascript %}
"restrictions": [

  {

    "type": "date",

    "fromdate": "2025-02-11"

  },

{% endhighlight %}




**XML**

Einschränkungen werden in LibRML in dem Element restrictions in das jeweilige Attribut mit dem zugehörigen Wert eingetragen.

{% highlight xml %}
<restriction type="date" fromdate="2025-02-11"/>
{% endhighlight %}
