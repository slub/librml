# Konzept


Gerne finden sie hier diverse Details zur LibRML, sowie eine detailliertere Beschreibung zum Aufbau einer LibRML Datei.

Ein konkretes Schema ist derzeit leider noch nicht verfügbar aber es wird sobald wie möglich hinzugefügt. 


Eine LibRML Datei besteht aus:

- **Header** (Allgemeine Informationen)

- [**Actions**](actions.markdown) (Nutzungsrechte)

- [**Constraints**](constraints.markdown) (Einschränkungen)

- [**Attributes**](attributes.markdown) (Eigenschaften zu den Einschränkungen)


In der Version 0.2 der LibRML an der wir gerade arbeiten werden die Nutzungsrechte nach Actions organisiert.


Zuerst werden im **Header** für die beschriebene eRessource **„Attributes“** (Eigenschaften) vergeben. (Nicht zu verwechseln mit den ["**Attributes**"](attributes.markdown) die zur Beschreibung von Eigenschaften der verschiedenen Einschränkungen benutzt werden)

- **id**: ID zur Identifizierung der Ressource
- **tenant**: Einrichtung, die die Ressource verwaltet
- **template**: Name des eventuell benutzten Templates
- **usageguide**: URL auf der sich die Richtlinien der dazugehörigen Lizenz befinden 

Zudem können in den Attributen noch zwei generelle Einschränkungen definiert werden:

- **mention**: die Namensnennung
- **sharealike**: Verpflichtung alle Derivate der Ressource unter denselben Bedingungen zu veröffentlichen


Nach diesem **Header** werden die jeweiligen **Actions** beschrieben. Diese werden durch **Constraints** und **Attributes** ergänzt. Es wird erst der Typ benannt, dann die Genehmigung (hier „Permission“) eingeschaltet (also auf „true“ geschaltet). Zur Erinnerung, es werden in der LibRML keine Genehmigungen explizit ausgeschaltet (also auf „false“) da jene Actions die nicht genehmigt sind, weggelassen werden.

Dann werden eventuelle Einschränkungen beschrieben. Diese haben wieder Typ und True/False Schalter und wieder wird das „False“ nicht explizit benutzt, sondern die Einschränkung weggelassen, wenn diese nicht benutzt wird.

Zu den Einschränkungen gehören dann in manchen Fällen eine ganze Serie an Attributen. Diese Attribute sind von einer Einschränkung zur anderen relativ verschieden. Und selbst Einschränkungen, die im Text ähnlich klingen könnten wie „von… bis…“ sind im gegebenen Kontext sehr verschieden.

Daher [**hier**](attributes.markdown) noch eine Liste diese Attribute für Einschränkungen.



Hier finden sie Beispiele für Vorlagen: 

- [**Vorlagen**](/tmpl/beispiele.html)

Und andere Beispiele: 
- [**JSON**](json.markdown)
- [**XML**](xmlbeispiel.markdown)
- [**XSD**](xsdschema.markdown)