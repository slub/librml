# Das Konzept von LibRML

## Allgemeine Informationen

LibRML kann in unterschiedlichen [Anwendungsszenarien](../usage/usage.md) eingesetzt werden. Zum einen kann eine LibRML-Beschreibung in die Metadatendatei eines digitalen Objekts eingetragen werden. Zum anderen kann eine LibRML-Beschreibung als eigenständiges Objekt in Rechteverwaltungssystemen verwaltet werden. In diesen Fällen wird die Verknüpfung zwischen dem digitalen Objekt und der LibRML-Beschreibung durch eine ID ermöglicht, die in die Metadatendatei des digitalen Objekts eingetragen wird.

Im EFRE-Projekt wurde zunächst die Anwendung in Rechteverwaltungssystemen verfolgt.
Im DFG-Projekt wird hauptsächlich die Anwendung der LibRML-Beschreibung in der Metadatendatei verfolgt (siehe [Rechtebeschreibung mit LibRML](../index.md)).
Abhängig von der Anwendung werden die im folgenden erläuterten Bestandteile des LibRML angewendet.

## Aufbau

Eine LibRML-Beschreibung besteht aus folgenden Elementen:

- Allgemeinen Informationen ([**Header**](header.md))

- Nutzungsarten ([**Actions**](actions.md))

  - Einschränkungen ([**Constraints**](constraints.md))

  - Eigenschaften ([**Attributes**](attributes.md))

Im [**Header**](header.md) werden allgemeine Informationen und allgemeine Eigenschaften eingetragen.

Nach dem [**Header**](header.md) werden die [**Nutzungsarten**](actions.md) beschrieben, die durch [**Einschränkungen**](constraints.md) und [**Eigenschaften**](attributes.md) spezifiziert werden. In LibRML werden nur **erlaubte Nutzungsarten** beschrieben. Nutzungsarten, die nicht in der LibRML-Beschreibung des digitalen Objekts enthalten sind, sind **verboten**.

## Beispiel

Ein urheberrechtlich geschütztes digitales Objekt der [SLUB Dresden](https://www.slub-dresden.de/) darf unter anderem indexiert, archiviert und gelesen werden. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken. Nicht erlaubt ist das Herunterladen, Ausdrucken, Vervielfältigen, Bearbeiten, Wiederverwenden und Veröffentlichen des digitalen Objekts.
Diesem digitalen Objekt würde folgende LibRML-Beschreibung zugewiesen werden.

```xml
<libRML version="0.4" xmlns="http://librml.org/schema">
  <item id="access-0815" tenant="https://www.slub-dresden.de/" commercialuse="false" copyright="true">
    <action type="displaymetadata" permission="true" />
    <action type="index" permission="true" />
    <action type="read" permission="true" />
    <action type="distribute" permission="true" />
    <action type="archive" permission="true" />
    <action type="move" permission="true" />
  </item>
</libRML>
```

```json
{
  "id": "access-0815",
  "tenant": "https://www.slub-dresden.de/",
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

## Vorlagen

Digitale Objekte können Creative-Commons-Lizenzen unterliegen, aus denen sich die Nutzungsmöglichkeiten ableiten. Für diese Anwendungsfälle stehen [**Vorlagen**](.. /templates/templates.md) zur Verfügung.
