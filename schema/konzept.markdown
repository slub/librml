# Konzept


Gerne finden sie hier diverse Details zur libRML, sowie eine detailliertere Erklärung zum Aufbau einer libRML Datei.

Ein konkretes Schema gibt es der Zeit leider noch nicht aber es wird sobald wie möglich hinzugefügt werden. 

### Links : 

Nutzungsrechte und Einschränkungen:

[Actions](actions.markdown) (Nutzungsrechte)

[Constraints](constraints.markdown) (Einschränkungen)

[Attributes](attributes.markdown) (Eigenschaften zu den Einschränkungen)


Beispiele: 

[JSON](json.markdown)

[XML](xmlbeispiel.markdown)

[XSD](xsdschema.markdown)


In der Version 0.2 der LibRML an der wir gerade arbeiten werden die Nutzungsrechte nach Actions organisiert.


Zuerst bekommt die beschriebene eRessource „Attributes“ (Eigenschaften). Damit wird diese Ressource dank einem ID identifiziert und es kann definiert werden von welcher Einrichtung sie verwaltet wird (tenant), der Name der eventuell benutzten „Template“ und die URL auf der sich die Richtlinien der dazu gehörigen Lizenz befinden (usageguide). Dann befinden sich in den Attributen noch zwei eventuelle generelle Einschränkungen: die Namensnennung (mention) und der Verpflichtung alle Derivate der Ressource unter denselben Bedingungen zu veröffentlichen (sharealike).

Danach werden die jeweiligen Actions mit ihren Constraints (Einschränkungen) beschrieben. Actions haben wiederum auch Attributen. Es wird erst der Typ benannt, dann die Genehmigung (hier „Permission“) eingeschaltet (also auf „true“ geschaltet). Zur Erinnerung, es werden in der LibRML keine Genehmigungen schriftlich ausgeschaltet (also auf „False“) da jene Actions die nicht genehmigt sind, weggelassen werden.

Dann werden eventuelle Einschränkungen beschrieben. Diese haben wieder Typ und True/False Schalter und wieder wird das „False“ nicht explizit benutzt, sondern die Einschränkung weggelassen, wenn diese nicht benutzt wird.

Zu den Einschränkungen gehören dann in manchen Fällen eine ganze Serie an Attributen. Diese Attribute sind von einer Einschränkung zur anderen relativ verschieden. Und selbst Einschränkungen die im Text ähnlich klingen könnten wie „von… bis…“ sind im gegebenen Kontext sehr verschieden.

Daher [hier](attributes.markdown) noch eine Liste diese Attribute für Einschränkungen.


