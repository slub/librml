# Header
## Allgemeine Informationen und Haupteinschränkungen

Im **Header** befinden sich Informationen zur eindeutigen Identifikation des zu beschreibenden digitalen Objekts. Ohne eindeutige **id** kann die Rechtebeschreibung nicht mit dem konkreten Objekt verknüpft werden. Da es vorkommen kann, dass Institutionen die gleiche Ressource unterschiedlich lizenziert haben, wird die Einrichtung als `tenant` angegeben um den nötigen Kontext herzustellen. Analog kann es verschiedene Identifier zur gleichen e-Ressourcen geben, die als verwandte IDs als `relatedids` abgelegt werden können.



| Feld | Beschreibung | Wert |
| :---:| :----------: | :--: |
|**id**| ID zur Identifizierung der Ressource | String |
|**relatedids**| Verwandte IDs im Falle einer Ressource mit mehreren IDs (mehr als einmal im Katalog vorhanden) und/oder mehreren Verträgen (unter unterschiedlichen Lizenzen) | \[String\] |
|**tenant**| Einrichtung, die die Ressource verwaltet | URI |

Zudem können generelle Einschränkungen der e-Ressournce definiert werden:

| Feld | Beschreibung | Wert |
| :---:| :----------: | :--: |
|**mention**| Ist eine Namensnennung notwendig | true/false|
|**sharealike**| Verpflichtung alle Derivate der Ressource unter denselben Bedingungen zu veröffentlichen | true/false|
|**copyright**| Urheberrechtsschutz vorhanden | true/false|


Im Fall einer gebräuchlichen Lizenz ist es möglich die [Vorlage](../tmpl/beispiele.markdown) auf der die Beschreibung aufbaut zu erwähnen, sowie einen Lizenztext zu verlinken. Beim automatischen Generieren aus einer einer [Vorlage](../tmpl/beispiele.markdown) ist der Wert in der Regel vorausgefüllt.

| Feld | Beschreibung | Wert |
| :---:| :----------: | :--: |
|**template**| Name des eventuell benutzten Templates | true/false|
|**usageguide**| URL auf der sich die Richtlinien der dazugehörigen Lizenz befinden | true/false|

----

### Beispiel

Eine urheberrechtsgeschützt e-Ressource mit zwei verwandten IDs, die im Kontext der SLUB Dresden lizenziert ist. Die e-Ressource erfordert eine Namensnennung, Weiternutzung und Verbreitung unter denselben Einschränkungen wie das Original.

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
  </item>
{% endhighlight %}
