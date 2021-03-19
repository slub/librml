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
| :------------- | :--------- | :------------------ |
|fromdate| Start-Datum der Einschränkung | Datum<br/><br/>**Format**: ISO8601 (YYYY-MM-DD) |
|todate| End-Datum des Einschränkung | Datum<br/><br/>**Format**: ISO8601 (YYYY-MM-DD) |
|maxresolution| maximal erlaubte Auflösung für den Download einer Ressource | non-negative Integer<br/><br/>**Einheit**: DPI|
|maxbitrate| maximal erlaubte Bitrate für den Download einer Ressource | non-negative Integer<br/><br/>**Einheit**: Bit |
|count| Anzahl der erlaubten Action z.B. die Anzahl der erlaubten Ausleihen | non-negative Integer<br/><br/>**Einheit**: — |
|sessions| Anzahl der erlaubten parallelen Zugriffe auf eine Ressource |  non-negative Integer<br/><br/>**Einheit**: — |
|inside| Nutzung innerhalb eines geographischen Gebiets oder innerhalb einer Institution.<br/><br/>  | in <br/><br/>**Einheit**: — |
|subnet| Innerhalb einer Einrichtung kann der Zugriff über ein Subnetz genauer spezifiziert werden. | IP, IP-Bereiche<br/><br/>**Format**: — |
|outside| Nutzung außerhalb eines geographischen Gebiets oder außerhalb einer Institution. | out <br/><br/>**Einheit**: —|
|commercialuse| Definition, ob eine kommerzielle Nutzung erlaubt ist. | true/false<br/><br/>**Format**: — |
|watermarkvalue| Definition des Wasserzeichens. Das Wasserzeichen muss an einem spezifischen Ort hinterlegt sein der hier verlinkt ist.| URI <br/><br/>|
|duration| Definition der Dauer eines Constraints. | non-negative Integer <br/><br/>**Einheit**: Sekunden |
|minage| Definition des Mindestalters für eine Action. Zum Beispiel zur Beschreibung des Jugendschutzes genutzt. | non-negative Integer <br/><br/>**Einheit**: Jahre|
|maxage| Definition des Maximalalters für eine Action. Zum Beispiel in Einrichtungen genutzt die Kinderbücher für Erwachsene unzugänglich machen. | non-negative Integer <br/><br/>**Einheit**: Jahre|
|required| "Erforderlich" (wird bei der Erforderlichkeit von externen Verträgen benutzt) | true/false<br/><br/>**Format**: — |


## Zusammenhänge mit den verschiedenen Einschränkungen

Um besser zu verstehen wie diese Eigenschaften mit ihren Einschränkungen und letztendlich mit den Nutzungsrechten zusammenhängen, finden sie hier eine Tabelle mit den verschiedenen Zusammenhängen. 

| Attribute | Constraint | Action |
| :--------- | :--------- | :--------- |
| fromdate | date |	alle actions |
| todate | date | alle actions |
|maxresolution | quality | alle actions außer displaymetadata, index, archive and move |
|maxbitrate | quality | alle actions außer displaymetadata, index, archive and move |
|count | count | read, run, lend, download, print and reproduce |
|session | concurrent | read, run und lend |
|inside | location | alle actions |
|outside | location | alle actions |
|commercialuse | commercialuse | alle actions außer displaymetadata und index |
|watermarkvalue | watermark | alle actions außer displaymetadata |
|duration | duration | read, run und lend |
|minage | age | alle actions außer displaymetadata, index, archive and move |
|maxage | age | alle actions außer displaymetadata, index, archive and move |
|required | agreement | alle actions außer displaymetadata und index |
|  | parts | alle actions außer displaymetadata und index |
|  | group | alle actions außer displaymetadata, index, archive and move |

Die constraints parts und group haben keine direkten Attributes sondern "Arrays". Ihre Attributes sind so zu sagen eine Liste.