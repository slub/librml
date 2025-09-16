# Das Konzept hinter LibRML

## Aufbau

Eine LibRML Datei besteht aus:

- Allgemeinen Informationen ([**Header**](header.md))

- Nutzungsrechten ([**Actions**](actions.md))

  - Einschränkungen ([**Constraints**](constraints.md))

  - Eigenschaften ([**Attributes**](attributes.md))

---

Im [**Header**](header.md) werden allgemeine Informationen wie die ID oder generellen Eigenschaften eingetragen.

Nach dem [**Header**](header.md) werden die [**Nutzungsrechte**](actions.md) beschrieben. Diese Nutzungsrechte werden durch [**Einschränkungen**](constraints.md) und [**Eigenschaften**](attributes.md) ergänzt. In LibRML werden nur **erlaubte Nutzungsrechte** beschrieben. Nutzungsrechte die **nicht** in der LibRML-Beschreibung der e-Ressource  enthalten sind, sind implizit **verboten**.

---

## Beispiel

Eine urheberrechtsbehaftete e-Ressource der [SLUB Dresden](https://www.slub-dresden.de/), die im Rahmen der Digitalisierung die dauerhafte Speicherung, Ablage in Datenbanken, und den öffentlichen Zugriff erlaubt. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken (In diesem Fall schreiben wir zur besseren Verständlichkeit aktiv das `false` zur `"commercialuse"` in das JSON). **Nicht erlaubt** ist das herunterladen, ausdrucken, vervielfältigen, bearbeiten, wiederverwenden und veröffentlichen der e-Ressource.\
So einer e-Ressource würde folgende LibRML zugewiesen werden.

```json
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
    }
  ]
}
```

---

### Vorlagen

E-Ressourcen können fest definierten Lizenzen unterliegen, aus der sich die Nutzung ableiten lässt, zum Beispiel Creative Commons-Lizenzen. Für solche Fälle stehen [**Vorlagen**](../tmpl/beispiele.md) bereit, die die Nutzungsrechte vollständig definieren und nachgenutzt werden können.

---

Ausführlichere Informationen zu den Bestandteilen einer LibRML-Beschreibung finden Sie auf den folgenden Seiten:

- [**Header**](header.md)
- [**Nutzungsrechte**](actions.md)
- [**Einschränkungen**](constraints.md)
- [**Eigenschaften**](attributes.md)

Häufig vorkommende Lizenzen in LibRML

- [**Vorlagen**](../tmpl/beispiele.md)
