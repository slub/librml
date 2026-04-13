# Actions - Nutzungsarten

## Allgemeine Informationen

Nutzungsarten (`actions`) beschreiben die Nutzungsmöglichkeiten eines digitalen Objekts.

In einer LibRML-Beschreibung muss jede erlaubte `action` ausdrücklich aufgeführt werden [(siehe LibRML Konzept)](concept.md). Jede `action`, die nicht enthalten ist, wird vom System als untersagt interpretiert. Jede `action` wird über das Attribut `type` eindeutig identifiziert. Das Attribut `permission="true"` kennzeichnet die `action` formal als erlaubt.

`action` können durch Einschränkungen [(siehe `Constraints`)](constraints.md) und Eigenschaften [(siehe `Attributes`)](attributes.md) spezifiziert werden.

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

In LibRML stehen die folgenden Nutzungsarten zur Verfügung. Es wird zwischen technisch durchsetzbaren Nutzungsarten (Download, Zugang, etc.) und informativen Nutzungsarten (Nachnutzung in anderen Veröffentlichungen, etc.) unterschieden.

| Action-Name | Übersetzung | Beschreibung |
| :---------- | :--------- | :----------- |
| **archive** | Archivieren | Erlaubt die Speicherung des digitalen Objekts zum Zweck der Archivierung.<br/> _einrichtungsinterne Nutzungsart_ |
| **displaymetadata** | Anzeigen der Metadaten | Erlaubt ausschließlich die Anzeige der Metadaten im Katalog. |
| **distribute** | (Ver)teilen | Erlaubt das nicht-öffentliche Verbreiten des digitalen Objekts, wie zum Beispiel durch die Weitergabe des digitalen Objekts im Bekanntenkreis.<br/> _technisch nicht durchsetzbar_ |
| **download** | Herunterladen | Erlaubt das Herunterladen einer Datei auf einen Computer oder auf jeglichen anderen Datenträger. |
| **index** | Indexieren | Erlaubt die Erzeugung und/oder das Einfügen von Metadaten in einen Index, zum Beispiel für einen Katalog.<br/> _einrichtungsinterne Nutzungsart_ |
| **lend** | Verleih | Erlaubt den Verleih des digitalen Objekts.<br/> _einrichtungsinterne Nutzungsart_ |
| **modify** | Bearbeiten | Erlaubt jede Art der Bearbeitung, Übersetzung, Umarbeitung.<br/> _technisch nicht durchsetzbar_ |
| **move** | Übertragen der Daten | Erlaubt die Übertragung des digitalen Objekts zwischen Datenbanken, oder das interne Speichern eines digitalen Objekts, die in einer externen Datenbank des Anbieters verfügbar ist.<br/> _einrichtungsinterne Nutzungsart_ |
| **print** | Ausdrucken | Erlaubt das Ausdrucken des Werkes. |
| **publish** | Veröffentlichen oder vorführen | Erlaubt das öffentliche Verbreiten oder Vorführen des digitalen Objekts, wie zum Beispiel durch eine Verlagsveröffentlichung oder eine öffentliche Vorlesung.<br/> _technisch nicht durchsetzbar_ <br/> Öffentliches Verbreiten des Objektes, beispielsweise über entsprechende Schnittstellen. |
| **read** | „Lesen“ der Datei | Erlaubt das Öffnen und Lesen des digitalen Objekts. |
| **reproduce** | Vervielfältigen | Erlaubt die private und öffentliche Vervielfältigung des digitalen Objekts, unabhängig davon, ob sie verbreitet wird oder nicht.<br/> _technisch nicht durchsetzbar_ |
| **reuse** | Wiederverwenden | Erlaubt die Wiederverwendung des ganzen Werkes oder Teile des Werkes.<br/> _technisch nicht durchsetzbar_ |
| **run** | Ausführen | Erlaubt das Ausführen des digitalen Objekts z. B. einer Anwendung. |
