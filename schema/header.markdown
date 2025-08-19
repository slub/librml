# Header
## Allgemeine Informationen und Haupteinschränkungen

Im **Header** befinden sich Informationen zur eindeutigen Identifikation der LibRML Datei. Ohne eindeutige **ID** kann die Rechtebeschreibung später nicht mit dem zu beschreibenden digitalen Objekts verknüpft werden. Da es vorkommen kann, dass Institutionen interne oder spezifische Entscheidungen treffen müssen zur Verwaltung unterschiedlich lizenzierten Ressourcen, kann die Einrichtung als `tenant` angegeben werden um den nötigen Kontext herzustellen.



| Feld | Beschreibung | Wert |
| :--- | :---------- | :-- |
|**id**| ID zur Identifizierung | String |
|**tenant**| Einrichtung, die die Ressource verwaltet | URI |

Zudem können generelle Einschränkungen und/oder Eigenschaften definiert werden:

| Feld | Beschreibung | Wert |
| :--- | :---------- | :-- |
|**mention**| Ist eine Namensnennung notwendig | true/false|
|**sharealike**| Verpflichtung alle Derivate der Ressource unter denselben Bedingungen zu veröffentlichen | true/false|
|**commercialuse**| Kommerzielle Nutzung erlaubt | true/false|
|**copyright**| Urheberrechtsschutz vorhanden | true/false|


Im Fall einer gebräuchlichen Lizenz ist es möglich die [Vorlage](../tmpl/beispiele.markdown) auf der die Beschreibung aufbaut zu erwähnen, sowie einen Lizenztext zu verlinken. Beim automatischen Generieren aus einer [Vorlage](../tmpl/beispiele.markdown) ist der Wert in der Regel vorausgefüllt.

| Feld | Beschreibung | Wert |
| :--- | :---------- | :-- |
|**template**| Name des eventuell benutzten Templates | String |
|**usageguide**| URL auf der sich die Richtlinien der dazugehörigen Lizenz befinden | URI|

----

### Beispiel

Eine urheberrechtsgeschützt e-Ressource, die im Kontext der SLUB Dresden lizenziert ist. Die e-Ressource erfordert eine Namensnennung, Weiternutzung und Verbreitung unter denselben Einschränkungen wie das Original.
So einer e-Ressource würde folgende LibRML zugewiesen werden. 

**JSON**

```json
    "id": "id-123456",
    "tenant": "http://slub-dresden.de",
    "mention": true,
    "sharealike": true,
    "copyright": true,

```

**XML**


```xml
  <item id="id-123456" tenant="http://slub-dresden.de" mention="true" sharealike="true" copyright="true" />
```
