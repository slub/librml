# Das Konzept hinter LibRML
## Aufbau
Eine LibRML Datei besteht aus:

- Allgemeinen Informationen ([**Header**](header.markdown))

- Nutzungsrechten ([**Actions**](actions.markdown))

  - Einschränkungen ([**Constraints**](constraints.markdown))

  - Eigenschaften ([**Attributes**](attributes.markdown))

----

Im [**Header**](header.markdown) werden allgemeine Informationen wie die ID oder generellen Eigenschaften eingetragen.

Nach dem [**Header**](header.markdown) werden die [**Nutzungsrechte**](actions.markdown) beschrieben. Diese Nutzungsrechte werden durch [**Einschränkungen**](constraints.markdown) und [**Eigenschaften**](attributes.markdown) ergänzt. In LibRML werden nur **erlaubte Nutzungsrechte** beschrieben. Nutzungsrechte die **nicht** in der LibRML-Beschreibung der e-Ressource  enthalten sind, sind implizit **verboten**.

----

## Beispiel

Eine urheberrechtsbehaftete e-Ressource der [SLUB Dresden](https://www.slub-dresden.de), die im Rahmen der Digitalisierung die dauerhafte Speicherung, Ablage in Datenbanken, und den öffentlichen Zugriff erlaubt. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken (In diesem Fall schreiben wir aus Vorzeige-Gründen aktiv das *"false"* zur *"commercialuse"* in den Beispiel-Code). **Nicht erlaubt** ist das herunterladen, ausdrucken, vervielfältigen, bearbeiten, wiederverwenden und veröffentlichen der e-Ressource.
So einer e-Ressource würde folgende LibRML zugewiesen werden. 

{% highlight javascript %}

{
  "id": "DE-611-HS-3665348",
  "tenant": "https://www.slub-dresden.de",
  "commercialuse": false,
  "copyright": true,
  "actions": [
	{
	  "type": "displaymetadata",
	  "permission": true
	},
	{
	  "type": "index",
	  "permission": true
	},
	{
	  "type": "read",
	  "permission": true
	},
	{
	  "type": "distribute",
	  "permission": true
	},
	{
	  "type": "archive",
	  "permission": true
	},
	{
	  "type": "move",
	  "permission": true
	},
  ]
}

{% endhighlight %}

----

### Vorlagen

E-Ressourcen können fest definierten Lizenzen unterliegen, aus der sich die Nutzung ableiten lässt, zum Beispiel Creative Commons-Lizenzen. Für solche Fälle stehen [**Vorlagen**](../tmpl/beispiele.markdown) bereit, die die Nutzungsrechte vollständig definieren und nachgenutzt werden können.

----

Ausführlichere Informationen zu den Bestandteilen einer LibRML-Beschreibung finden Sie auf den folgenden Seiten:

- [**Header**](header.markdown)
- [**Nutzungsrechte**](actions.markdown)
- [**Einschränkungen**](constraints.markdown)
- [**Eigenschaften**](attributes.markdown)

Beispiele:
- [**JSON**](json.markdown)
- [**XML**](xmlbeispiel.markdown)

Validierung:

Eine XSD gibt es im Moment nur als Entwurf in Version 0.2:
*(Dieser Entwurf wird kontinuierlich verändert. Eine finale Version wird erst mit Version 1.0 veröffentlicht.)*
- [**XSD**](xsdschema.markdown)


Häufig vorkommende Lizenzen in LibRML
- [**Vorlagen**](../tmpl/beispiele.markdown)
