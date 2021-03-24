# LibRML Konzept
## Aufbau
Eine LibRML Datei besteht aus:

- Allgemeinen Informationen ([**Header**](header.markdown))

- Nutzungsrechten ([**Actions**](actions.markdown))

  - Einschränkungen ([**Constraints**](constraints.markdown))

  - Eigenschaften ([**Attributes**](attributes.markdown))

----

Zunächst werden im [**Header**](header.markdown) allgemeine Informationen zur Beschreibung der e-Ressource vergeben.

Nach dem [**Header**](header.markdown) werden die [**Nutzungsrechte**](actions.markdown) beschrieben. Diese Nutzungsrechte werden durch [**Einschränkungen**](constraints.markdown) und [**Eigenschaften**](attributes.markdown) ergänzt. In LibRML wird nur die **erlaubte Nutzung** beschrieben. Nutzungsrechte die **nicht** in der LibRML-Beschreibung der e-Ressource vorkommen gelten implizit als **verboten** und können weggelassen werden.

----

## Beispiel

Eine urheberrechtsbehaftete e-Ressource der [SLUB Dresden](https://www.slub-dresden.de), die im Rahmen der Digitalisierung die dauerhafte Speicherung, Ablage in Datenbanken, und dem öffentlicher Zugriff erlaubt. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken. **Nicht erlaubt** ist das herunterladen, ausdrucken, vervielfältigen, bearbeiten, wiederverwenden und veröffentlichen der e-Ressource.

{% highlight javascript %}

{
  "id": "DE-611-HS-3665348",
  "tenant": "https://www.slub-dresden.de",
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
	  "permission": true,
	},
	{
	  "type": "distribute",
	  "permission": true,
	  "restrictions": [
		{
		  "type": "commercialuse",
		  "noncommercialuse": true
		},
	  ]
	},
	{
	  "type": "archive",
	  "permission": true,
	},
	{
	  "type": "move",
	  "permission": true,
	  "restrictions": [
		{
		  "type": "commercialuse",
		  "noncommercialuse": true
		},
	  ]
	},
  ]
}

{% endhighlight %}

----

### Vorlagen

Häufig kommt es vor, dass e-Ressourcen fest definierten Lizenzen unterliegen aus der sich die Nutzung ableiten lässt (z.B. Public Domain oder CC-Lizenzen). Für solche Fälle stehen fertige [**Vorlagen**](../tmpl/beispiele.markdown) bereit, die die Nutzungsrechte vollständig definieren und nachgenutzt werden können.

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
