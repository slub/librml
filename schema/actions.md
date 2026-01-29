# Actions - Nutzungsarten

## Allgemeine Informationen

Nutzungsarten (`actions`) beschreiben die Nutzungsmöglichkeiten eines digitalen Objekts, die bei Bedarf eingeschränkt werden sollen.
Sie müssen in der LibRML-Beschreibung enthalten sein [(siehe LibRML Konzept)](concept.md), ansonsten ist die Nutzungsart nicht erlaubt. Jede `action` wird durch `type` eindeutig in ihrer Nutzungsart bestimmt. Die `permission` kennzeichnet mittels des Wertes `true` die `action` als eine erlaubte Nutzungsart.

`actions` können zusätzlich durch Einschränkungen [(siehe Constraints)](constraints.md) und Eigenschaften [(siehe Attributes)](attributes.md) spezifiziert werden.

```xml
<libRML version="0.4" xmlns="http://librml.org/schema">
  <item id="ID-NAME">
    <action type="ACTION-NAME" permission="true" />
  </item>
</libRML>
```

```json
{
  "id": "ID-NAME",
  "actions": [{
    "type": "ACTION-NAME",
    "permission": true
  }]
}
```

## Liste

In LibRML stehen folgende Nutzungsarten zur Verfügung.

| Action-Name | Übersetzung | Beschreibung |
| :---------- | :--------- | :----------- |
| **displaymetadata** | Anzeigen der Metadaten | Erlaubt ausschließlich die Anzeige der Metadaten im Katalog. |
| **read** | „Lesen“ der Datei | Erlaubt das Öffnen und Lesen des digitalen Objekts. |
| **run** | Ausführen | Erlaubt das Ausführen des digitalen Objekts z. B. einer Anwendung. |
| **lend** | Verleih | Erlaubt den Verleih des digitalen Objekts.<br/><br/>Auf Einrichtungen bezogen. |
| **download** | Herunterladen | Erlaubt das Herunterladen einer Datei auf einen Computer oder auf jeglichen anderen Datenträger. |
| **print** | Ausdrucken | Erlaubt das Ausdrucken des Werkes. |
| **reproduce** | Vervielfältigen | Erlaubt die private und öffentliche Vervielfältigung des digitalen Objekts, unabhängig davon, ob sie verbreitet wird oder nicht. |
| **modify** | Bearbeiten | Erlaubt jede Art der Bearbeitung, Übersetzung, Umarbeitung. |
| **reuse** | Wiederverwenden | Erlaubt die Wiederverwendung des ganzen Werkes oder Teile des Werkes. |
| **distribute** | (Ver)teilen | Erlaubt das nicht-öffentliche Verbreiten des digitalen Objekts, wie zum Beispiel durch die Weitergabe des digitalen Objekts im Bekanntenkreis. |
| **publish** | Veröffentlichen oder vorführen | Erlaubt das öffentliche Verbreiten oder Vorführen des digitalen Objekts, wie zum Beispiel durch eine Verlagsveröffentlichung oder eine öffentliche Vorlesung. |
| **archive** | Archivieren | Erlaubt die Speicherung des digitalen Objekts zum Zweck der Archivierung.<br/><br/>Auf Einrichtungen bezogen. |
| **index** | Indexieren | Erlaubt die Erzeugung und/oder das Einfügen von Metadaten in einen Index, zum Beispiel für einen Katalog.<br/><br/>Auf Einrichtungen bezogen. |
| **move** | Übertragen der Daten | Erlaubt die Übertragung des digitalen Objekts zwischen Datenbanken, oder das interne Speichern eines digitalen Objekts, die in einer externen Datenbank des Anbieters verfügbar ist.<br/><br/>Auf Einrichtungen bezogen. |
