# Header

## Allgemeine Informationen und Haupteinschränkungen

Im **Header** befinden sich Informationen zur eindeutigen Identifikation der LibRML Datei. Ohne eindeutige **ID** kann die Rechtebeschreibung nicht mit dem zu beschreibenden digitalen Objekt verknüpft werden. Da es vorkommen kann, dass Institutionen interne oder spezifische Entscheidungen zur Verwaltung unterschiedlich lizenzierter digitaler Objekte treffen müssen, kann die Einrichtung als `tenant` angegeben werden, um den nötigen Kontext herzustellen.

| Feld | Beschreibung | Wert | Verpflichtungsgrad |
| :--- | :----------- | :--- | :----------------- |
|**id**| ID zur Identifizierung des LibRML-Blocks | String | optional |
|**tenant**| Einrichtung, die das digitale Objekt verwaltet | URI | optional |

Zudem können generelle Einschränkungen und/oder Eigenschaften definiert werden:

| Feld | Beschreibung | Wert | Verpflichtungsgrad |
| :--- | :----------- | :--- | :----------------- |
|**mention**| Ist eine Namensnennung notwendig | true/false | optional |
|**sharealike**| Verpflichtung, alle Derivate des digitalen Objektes unter denselben Bedingungen zu veröffentlichen | true/false | optional |
|**commercialuse**| Kommerzielle Nutzung erlaubt | true/false | optional |
|**copyright**| Urheberrechtsschutz vorhanden | true/false | optional |

Im Fall einer gebräuchlichen Lizenz ist es möglich, die [Vorlage](../tmpl/templates.md), auf der die Beschreibung aufbaut, zu erwähnen, sowie einen Lizenztext zu verlinken. Beim automatischen Generieren aus einer [Vorlage](../tmpl/templates.md) ist der Wert in der Regel vorausgefüllt.

| Feld | Beschreibung | Wert | Verpflichtungsgrad |
| :--- | :----------- | :--- | :----------------- |
|**template**| Name der ursprünglich angewendeten [Vorlage](../tmpl/templates.md) | String | optional |
|**usageguide**| URL, die auf die zugehörigen Nutzungshinweise verweist | URI | optional |

----

### Beispiel

Ein urheberrechtsgeschütztes digitales Objekt, das im Kontext der SLUB Dresden lizenziert ist. Das digitale Objekt erfordert eine Namensnennung; Weiternutzung und Verbreitung unterliegen denselben Einschränkungen wie das Original.\
So einem digitalen Objekt würde folgende LibRML zugewiesen werden.

```xml
<libRML version="0.4" xmlns="http://librml.org/schema">
  <item id="id-123456" tenant="https://www.slub-dresden.de/" mention="true" sharealike="true" copyright="true">
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
