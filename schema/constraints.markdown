# Constraints
## Einschränkungen

Eingeschränkte Nutzungsmöglichkeiten werden in der LibRML an den konkreten `Actions` festgelegt. Die Einschränkungen (`Constraints`) gelten explizit nur für die Aktion an der sie hinterlegt sind, um die maschinelle Auswertbarkeit zu gewährleisten. Einschränkungen die sich auf mehrere Aktionen auswirken, müssen entsprechend wiederholt werden. Für die vereinfachte Bearbeitung können systematische Einschränkungen einmalig definiert und wiederverwendet werden (siehe Templates).

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
| :--------------:| :---------: | :----------: |:-------: |
| parts | Teile | Einschränkung der Action auf bestimmte Teile der Ressource. | |
| group | Nutzergruppe | Einschränkung der Action auf bestimmte Personen oder Personengruppen. | |
| age | Alter | Einschränkung der Action auf Nutzer eines bestimmten Alters. | |
| location | Ort | Geographisch (ein bestimmtes Gebiet z.B. Deutschland)<br/><br/>Institutionell (eine bestimmte Einrichtung z.B. SLUB Dresden) | |
| date | Zeitpunkt | Einschränkung der Action ab oder bis zu einem bestimmten Zeitpunkt (Embargo). | |
| duration | Dauer | Einschränkung der Action auf eine bestimmte Zeitdauer. | |
| count | Anzahl | Einschränkung der Action auf eine bestimmte Anzahl an Ausführungen, Benutzungen, ... | |
| concurrent | Gleichzeitig | Einschränkung der Action auf eine bestimmte Anzahl an gleichzeitigen Ausführungen, Benutzungen, ... | |
| watermark | Wasserzeichen | Einschränkung der Action auf eine Kennzeichnung der Ressource mit einem Wasserzeichen oder einer anderer Markierung. | |
| commercialuse | Kommerzielle Nutzung | `commercial use` (Kommerzielle Nutzung)<br/><br/>`non commercial use` (Nicht-kommerzielle Nutzung)<br/><br/>Eine zukünftige Erweiterung ist möglich, wie zum Beispiel um den Wert `academical` für akademische Zwecke. Freitext-Eingaben werden jedoch nicht angeboten. | |
| quality | Qualität | Einschränkung der Action auf eine maximale Qualität. | |
| agreement | Einwilligung | Einschränkung der Action hinsichtlich eines Vertrags oder Zustimmung zu Nutzungsbedingungen. | |
