# Actions
## Nutzungsrechte

Actions beschreiben die Nutzungsmöglichkeiten von Ressourcen. Alle Nutzungsmöglichkeiten sind generell nicht zulässig, solange sie nicht in der Rechtebeschreibung auftauchen [(siehe LibRML Konzept)](concept.markdown).

```json
{
  "id": "ID-NAME",
  "actions": [{
    "type": "ACTION-NAME",
    "permission": true
  }]
}
```


Um eine Nutzungsmöglichkeit zu gewähren, muss die entsprechende Action in der LibRML-Beschreibung aufgeführt werden. Jede Action wird dafür mit dem zugehörigen `type` eingeleitet, der die Art der Nutzung beschreibt. Mit `"permission": true"`{:.highlight .json} wird sie explizit als erlaubt gekennzeichnet.


Alle Actions können zusätzlich durch Einschränkungen [(siehe Constraints)](constraints.markdown) und Attributen [(siehe Attributes)](attributes.markdown) feiner spezifiziert werden.


In der LibRML stehen folgende Actions zur Beschreibung von Nutzungsrechten zur Verfügung.

| Action-Name | Übersetzung | Beschreibung |
| :---------- | :--------- | :----------- |
| **displaymetadata** | Anzeigen der Metadaten | Erlaubt ausschließlich die Anzeige der Metadaten im Katalog. |
| **read** | „Lesen“ der Datei | Erlaubt das Öffnen und Lesen der Ressource. |
| **run** |  Ausführen | Erlaubt das Ausführen der Ressource z. B. einer Anwendung |
| **lend** | Verleih | Erlaubt den Verleih der Ressource.<br/><br/>Auf Einrichtungen bezogen. |
| **download** | Herunterladen | Erlaubt das Herunterladen einer Datei auf einen Computer oder auf jeglichen anderen Datenträger. |
| **print** | Ausdrucken | Erlaubt das Ausdrucken des Werkes. |
| **reproduce** | Vervielfältigen | Erlaubt die private und öffentliche Vervielfältigung der Ressource, unabhängig davon, ob sie verbreitet wird oder nicht. |
| **modify** | Bearbeiten | Erlaubt jede Art der Bearbeitung, Übersetzung, Umarbeitung. |
| **reuse** | Wiederverwenden | Erlaubt die Wiederverwendung des ganzen Werkes oder Teile des Werkes |
| **distribute** | (Ver)teilen | Erlaubt das nicht-öffentliche Verbreiten der Ressource, wie zum Beispiel durch die Weitergabe der Ressource im Bekanntenkreis. |
| **publish** | Veröffentlichen oder vorführen |  Erlaubt das öffentliche Verbreiten oder Vorführen der Ressource, wie zum Beispiel durch eine Verlagsveröffentlichung oder eine öffentliche Vorlesung. |
| **archive** | Archivieren | Erlaubt die Speicherung der Ressource zum Zweck der Archivierung.<br/><br/>Auf Einrichtungen bezogen.  |
| **index** | Indexieren | Erlaubt die Erzeugung und/oder das Einfügen von Metadaten in einen Index, zum Beispiel für einen Katalog.<br/><br/>Auf Einrichtungen bezogen. |
| **move** | Übertragen der Daten | Erlaubt die Übertragung der Ressource zwischen Datenbanken, oder das interne Speichern einer Ressource, die in einer externen Datenbank des Anbieters verfügbar ist.<br/><br/>Auf Einrichtungen bezogen. |
