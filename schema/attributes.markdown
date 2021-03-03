# Attributes
## Eigenschaften der verschiedenen Einschränkungen

Eigenschaften (`attributes`) spezifizieren die Einschränkungen (`constraints`) einer Ressource. Jedem Attribut **muss** ein Wert zugewiesen werden. Einschränkungen können mehreren Eigenschaften besitzen.

**JSON**

{% highlight javascript %}
"restrictions": [{
    "type": "CONSTRAINT-NAME",
    "ATTRIBUTE-NAME": "VALUE",
 }]
{% endhighlight %}

**XML**
{% highlight xml %}
<restriction type="CONSTRAINT-NAME" ATTRIBUTE="VALUE"/>
{% endhighlight %}

In der LibRML stehen folgende `Attributes` zur genaueren Beschreibung der `Constraints` zur Verfügung.

| Attribute-Name | Beschreibung | Wert&nbsp;+&nbsp;Einheit&nbsp;/&nbsp;Format |
| :-------------:| :---------: | :------------------: |
|fromdate| Start-Datum der Einschränkung | Datum<br/><br/>**Format**: ISO8601 (YYYY-MM-DD) |
|todate| End-Datum des Einschränkung | Datum<br/><br/>**Format**: ISO8601 (YYYY-MM-DD) |
|maxresolution| maximal erlaubte Auflösung für den Download einer Ressource | non-negative Integer<br/><br/>**Einheit**: DPI|
|maxbitrate| maximal erlaubte Bitrate für den Download einer Ressource | non-negative Integer<br/><br/>**Einheit**: Bit |
|count| Anzahl der erlaubten Action z.B. die Anzahl der erlaubten Ausleihen | non-negative Integer<br/><br/>**Einheit**: — |
|sessions| Anzahl der erlaubten parallelen Zugriffe auf eine Ressource |  non-negative Integer<br/><br/>**Einheit**: — |
|inside| Nutzung innerhalb eines geographischen Gebiets oder innerhalb einer Institution.<br/><br/>  | in <br/><br/>**Einheit**: — |
|subnet| Innerhalb einer Einrichtung kann der Zugriff über ein Subnetz genauer spezifiziert werden. | IP, IP-Bereiche |
|outside| Nutzung außerhalb eines geographischen Gebiets oder außerhalb einer Institution. | out <br/><br/>**Einheit**: —|
|noncommercialuse| Definition, ob eine nicht-kommerziellen Nutzung erlaubt ist. | true/false|
|commercialuse| Definition, ob eine kommerzielle Nutzung erlaubt ist. | true/false |
|watermarkvalue| Definition des Wasserzeichens. Das Wasserzeichen muss an einem spezifischen Ort hinterlegt sein der hier verlinkt ist.| URI <br/><br/>|
|duration| Definition der Dauer eines Constraints. | non-negative Integer <br/><br/>**Einheit**: Sekunden |
|minage| Definition des Mindestalters für eine Action. Zum Beispiel zur Beschreibung des Jugendschutzes genutzt. | non-negative Integer <br/><br/>**Einheit**: Jahre|
|required| "Erforderlich" (wird bei der Erforderlichkeit von externen Verträgen benutzt) | true/false|
