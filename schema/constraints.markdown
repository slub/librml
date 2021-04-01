# Constraints
## Einschränkungen

Eingeschränkte Nutzungsmöglichkeiten werden in der LibRML an den konkreten `Actions` festgelegt. Die Einschränkungen (`Constraints`) gelten explizit nur für die Aktion an der sie hinterlegt sind, um die maschinelle Auswertbarkeit zu gewährleisten. Einschränkungen, die sich auf mehrere Nutzungsrechte auswirken, müssen entsprechend wiederholt werden. Für die vereinfachte Bearbeitung können systematische Einschränkungen einmalig definiert und wiederverwendet werden (siehe Templates).

Einige `Constraints` werden durch `Attribute` [(Siehe Attribute)](attributes.markdown) näher spezifiziert.

**JSON**

{% highlight javascript %}
"actions": [{
    "type": "ACTION-NAME",
    "permission": true,
    "restrictions": [{
        "type": "CONSTRAINT-NAME",
        "ATTRIBUTE": "X"
     }]
}]
{% endhighlight %}

**XML**
{% highlight xml %}
<action type="ACTION-NAME" permission="true">
  <restriction type="CONSTRAINT-NAME" ATTRIBUTE="X"/>
</action>
{% endhighlight %}

In der LibRML stehen folgende `Constraints` zur Einschränkung der `Actions` zur Verfügung.

| Constraint-Name | Übersetzung | Beschreibung | Beispiel |
| :-------------- | :--------- | :---------- |:------- |
| parts | Teile | Einschränkung der Action auf bestimmte Teile der Ressource. | [→&nbsp;Parts](#parts) |
| group | Nutzergruppe | Einschränkung der Action auf bestimmte Personen oder Personengruppen. | [→&nbsp;Group](#group)|
| age | Alter | Einschränkung der Action auf Nutzer eines bestimmten Alters. | [→&nbsp;Age](#age) |
| location | Ort | Geographisch (ein bestimmtes Gebiet z. B. Deutschland)<br/><br/>Institutionell (eine bestimmte Einrichtung z. B. SLUB Dresden) | [→&nbsp;Location](#location)|
| date | Zeitpunkt | Einschränkung der Action ab oder bis zu einem bestimmten Zeitpunkt (Embargo). | [→&nbsp;Date](#date)|
| duration | Dauer | Einschränkung der Action auf eine bestimmte Zeitdauer. | [→&nbsp;Duration](#duration) |
| count | Anzahl | Einschränkung der Action auf eine bestimmte Anzahl an Ausführungen, Benutzungen, ... | [→&nbsp;Count](#count)|
| concurrent | Gleichzeitig | Einschränkung der Action auf eine bestimmte Anzahl an gleichzeitigen Ausführungen, Benutzungen, ... | [→&nbsp;Concurrent](#concurrent) |
| watermark | Wasserzeichen | Einschränkung der Action auf eine Kennzeichnung der Ressource mit einem Wasserzeichen oder einer anderer Markierung. | [→&nbsp;Watermark](#watermark)|
| commercialuse | Kommerzielle Nutzung | `commercial use` (Kommerzielle Nutzung)<br/><br/>`non commercial use` (Nicht-kommerzielle Nutzung)<br/><br/>Eine zukünftige Erweiterung ist möglich, wie zum Beispiel um den Wert `academical` für akademische Zwecke. Freitext-Eingaben werden jedoch nicht angeboten. | [→&nbsp;Commercialuse](#commercialuse)|
| quality | Qualität | Einschränkung der Action auf eine maximale Qualität. | [→&nbsp;Quality](#quality)|
| agreement | Einwilligung | Einschränkung der Action hinsichtlich eines Vertrags oder Zustimmung zu Nutzungsbedingungen. | [→&nbsp;Agreement](#agreement)|


## Beispiele

### Parts

{% highlight javascript %}
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "parts",
      "parts": "1"
    },
{% endhighlight %}

### Group

{% highlight javascript %}
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "group",
      "groups": [
        "registered",
        "employee",
      ]
    },
{% endhighlight %}

### Age
{% highlight javascript %}
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "age",
      "minage": "18"
    },
{% endhighlight %}

### Location

{% highlight javascript %}
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "location",
      "subnet": "192.168.0.0/16"
    },
{% endhighlight %}

### Date

{% highlight javascript %}
  "type": "distribute",
  "permission": true,
  "restrictions": [
    {
      "type": "date",
      "fromdate": "2035-01-01"
    },
{% endhighlight %}

### Duration

{% highlight javascript %}
  "type": "run",
  "permission": true,
  "restrictions": [
    {
      "type": "duration",
      "duration": 86400
    },
{% endhighlight %}

### Count

{% highlight javascript %}
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "count",
      "count": 10
    },
{% endhighlight %}

### Concurrent

{% highlight javascript %}
  "type": "lend",
  "permission": true,
  "restrictions": [
    {
      "type": "concurrent",
      "sessions": 4
    },
{% endhighlight %}

### Watermark

{% highlight javascript %}
  "type": "distribute",
  "permission": true,
  "restrictions": [
    {
      "type": "watermark",
      "watermarkvalue": "https://domain/watermark.png"
    },
{% endhighlight %}

### Commercialuse

{% highlight javascript %}
  "type": "publish",
  "permission": true,
  "restrictions": [
    {
      "type": "commercialuse",
      "commercialuse": false
    },
{% endhighlight %}

### Quality

{% highlight javascript %}
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "quality",
      "maxresolution": 300
    },
{% endhighlight %}

### Agreement

{% highlight javascript %}
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "agreement",
      "required": true
    },
{% endhighlight %}
