# Konzept

## Allgemeine Informationen

LibRML kann grundsätzlich in zwei Anwendungsszenarien eingesetzt werden:

1. **Eingebettete Beschreibung**: Die LibRML-Beschreibung wird direkt in die Metadatendatei eines digitalen Objekts eingebettet.
1. **Referenzierte Beschreibung**: Die LibRML-Beschreibung wird als eigenständiges Objekt in einem zentralen Rechteverwaltungssystem verwaltet. Die Verknüpfung erfolgt über eine eindeutige ID (Referenz-ID), die in den Metadaten des digitalen Objekts hinterlegt wird.

Weitere Informationen finden Sie unter [Anwendungsszenarien](../usage/usage.md).

Während im vorangegangenen EFRE-Projekt die Verwaltung in zentralen Rechteverwaltungssystemen im Fokus stand, liegt der Schwerpunkt des DFG-Projekts auf der Einbettung der LibRML-Beschreibung in die Metadatendateien (siehe Rechtebeschreibung mit LibRML). 

Je nach gewähltem Szenario kommen die im Folgenden erläuterten Elemente unterschiedlich zum Einsatz.

## Aufbau

Eine LibRML-Beschreibung ist hierarchisch strukturiert und besteht aus folgenden Elementen:

- Allgemeinen Informationen ([**Header**](header.md))
- Nutzungsarten ([**Actions**](actions.md))
  - Einschränkungen ([**Constraints**](constraints.md))
  - Eigenschaften ([**Attributes**](attributes.md))

Im [**Header**](header.md) werden Metadaten zur Beschreibung selbst sowie allgemeine Eigenschaften des Objekts definiert. Darauf folgen die [**Nutzungsarten**](actions.md), die durch [**Einschränkungen**](constraints.md) und [**Eigenschaften**](attributes.md) präzisiert werden können.
In LibRML gilt das Prinzip der Exklusivität: Es werden ausschließlich erlaubte Nutzungsarten ausdrücklich beschrieben. Jede Nutzungsart, die nicht ausdrücklich in der LibRML-Beschreibung aufgeführt ist, gilt als verboten.

Die aktuellen Schemata für die XML- und JSON-Repräsentationen können [hier](schemas.md) eingesehen werden.

## Beispiel

Ein urheberrechtlich geschütztes digitales Objekt der [SLUB Dresden](https://www.slub-dresden.de/) darf unter anderem indexiert, archiviert und gelesen werden. Eine Nutzung zu kommerziellen Zwecken ist hingegen ausgeschlossen. Da alle nicht genannten Aktionen untersagt sind, ist damit auch das Herunterladen, Ausdrucken, Vervielfältigen, Bearbeiten oder Veröffentlichen nicht gestattet.

Diesem digitalen Objekt würde folgende LibRML-Beschreibung zugewiesen werden.

```xml
<libRML version="0.4" xmlns="http://librml.org/schema">
  <item commercialuse="false" copyright="true" id="access-0815" tenant="https://www.slub-dresden.de/">
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

Nutzungsmöglichkeiten leiten sich auch aus Standard-Lizenzen wie Creative Commons ab. Um die Erstellung der LibRML-Beschreibung zu erleichtern, stehen für diese Anwendungsfälle die [**Vorlagen**](../templates/templates.md) zur Verfügung.
