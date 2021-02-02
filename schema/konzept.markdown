# Konzept


Gerne finden sie hier diverse Details zur LibRML, sowie eine detailliertere Beschreibung zum Aufbau einer LibRML Datei. 

Eine LibRML Datei besteht aus:

- [**Header**](header.markdown) (Allgemeine Informationen)

- [**Actions**](actions.markdown) (Nutzungsrechte)

- [**Constraints**](constraints.markdown) (Einschränkungen)

- [**Attributes**](attributes.markdown) (Eigenschaften zu den Einschränkungen)


In der Version 0.3 der LibRML an der wir gerade arbeiten werden die Nutzungsrechte nach Actions organisiert.


Zuerst werden im **Header** für die beschriebene eRessource **„Attributes“** (Eigenschaften) vergeben. (Nicht zu verwechseln mit den ["**Attributes**"](attributes.markdown) die zur Beschreibung von Eigenschaften der verschiedenen Einschränkungen benutzt werden)

Nach diesem **Header** werden die jeweiligen **Actions** beschrieben. Diese werden durch **Constraints** und **Attributes** ergänzt. Es wird erst der Typ benannt, dann die Genehmigung (hier „Permission“) eingeschaltet (also auf „true“ geschaltet). Zur Erinnerung, es werden in der LibRML keine Genehmigungen explizit ausgeschaltet (also auf „false“) da jene Actions die nicht genehmigt sind, weggelassen werden.

Dann werden eventuelle Einschränkungen beschrieben. Diese haben wieder Typ und True/False Schalter und wieder wird das „False“ nicht explizit benutzt, sondern die Einschränkung weggelassen, wenn diese nicht benutzt wird.

Zu den Einschränkungen gehören dann in manchen Fällen eine ganze Serie an Attributen. Diese Attribute sind von einer Einschränkung zur anderen relativ verschieden. Und selbst Einschränkungen, die im Text ähnlich klingen könnten wie „von… bis…“ sind im gegebenen Kontext sehr verschieden.

Daher [**hier**](attributes.markdown) noch eine Liste dieser Attributes für Einschränkungen.

Hier finden sie Beispiele für Vorlagen: 

- [**Vorlagen**](../tmpl/beispiele.markdown)

Und andere Beispiele: 
- [**JSON**](json.markdown)
- [**XML**](xmlbeispiel.markdown)

Eine XSD gibt es im Moment nur als Entwurf zur Version 0.2: 
*(Dieser Entwurf würd andauerd verändert. Daher wird erst zur Version 1.0 ein Update hier veröffentlicht)*

- [**XSD**](xsdschema.markdown)
