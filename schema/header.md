# Header

## Allgemeine Informationen und Haupteinschränkungen

Im **Header** sind Informationen zur eindeutigen Identifikation der LibRML-Beschreibung enthalten. Die Erfassung dieser Informationen ist von der [Anwendung](../usage/usage.md) der LibRML-Beschreibung abhängig.

Wird die LibRML-Beschreibung in die Metadaten-Datei des digitalen Objekts eingetragen, in der zum Beispiel bereits Informationen über den `tenant` enthalten sind, muss die Information des `tenant` nicht redundant erfasst werden. In den Beispielen [Anpassung LibRML für Retrodigitalisate](../adjustments/adjustments.md), ist nur das Attribut usageguide eingetragen.

Wird die LibRML-Beschreibung in einem „Rechtemangement-System“ mit LibRML-Beschreibungen aus unterschiedlichen Einrichtungen verwaltet, ist die Information über den `tenant` verpflichtend. Zusätzlich kann die LibRML-Beschreibung ohne eindeutige ID nicht in den zugehörigen digitalen Objekten referenziert werden.

Somit sind im letztgenannten Anwendungsfall einige Informationen im **Header** verpflichtend anzuwenden, auch wenn deren Verpflichtungsgrad generell optional ist.

| Feld | Beschreibung | Wert | Verpflichtungsgrad |
| :--- | :----------- | :--- | :----------------- |
| **id** | ID zur Identifizierung des LibRML-Blocks | String | optional |
| **tenant** | Einrichtung, die das digitale Objekt verwaltet | URI | optional |

Zudem können generelle Einschränkungen und/oder Eigenschaften definiert werden:

| Feld | Beschreibung | Wert | Verpflichtungsgrad |
| :--- | :----------- | :--- | :----------------- |
| **mention** | Ist eine Namensnennung notwendig | true/false | optional |
| **sharealike** | Verpflichtung, alle Derivate des digitalen Objektes unter denselben Bedingungen zu veröffentlichen | true/false | optional |
| **commercialuse** | Kommerzielle Nutzung erlaubt | true/false | optional |
| **derivatives** | Bearbeitungen erlaubt | true/false | optional |
| **copyright** | Urheberrechtsschutz vorhanden | true/false | optional |

Im Fall einer gebräuchlichen Lizenz ist es möglich, die [Vorlage](../templates/templates.md), auf der die Beschreibung aufbaut, zu erwähnen, sowie einen Lizenztext zu verlinken. Beim automatischen Generieren aus einer [Vorlage](../templates/templates.md) ist der Wert in der Regel vorausgefüllt.

| Feld | Beschreibung | Wert | Verpflichtungsgrad |
| :--- | :----------- | :--- | :----------------- |
| **template** | Name der ursprünglich angewendeten [Vorlage](../templates/templates.md) | String | optional |
| **usageguide** | URL, die auf die zugehörigen Nutzungshinweise verweist | URI | optional |

----

### Beispiel

Ein urheberrechtsgeschütztes digitales Objekt, das im Kontext der SLUB Dresden lizenziert ist. Das digitale Objekt erfordert eine Namensnennung; Weiternutzung und Verbreitung unterliegen denselben Einschränkungen wie das Original.\
So einem digitalen Objekt würde folgende LibRML zugewiesen werden.

```xml
<libRML version="0.4" xmlns="http://librml.org/schema">
  <item copyright="true" id="id-123456" mention="true" sharealike="true" tenant="https://www.slub-dresden.de/">
  </item>
</libRML>
```

```json
{
  "id": "id-123456",
  "tenant": "https://www.slub-dresden.de/",
  "mention": true,
  "sharealike": true,
  "copyright": true
}
```
