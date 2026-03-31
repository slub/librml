# Erweiterungen von LibRML für Retrodigitalisate

## Allgemeine Informationen

In dieser Diskussion wird untersucht, ob und wie LibRML für Retrodigitalisate angepasst werden kann.

Der Schwerpunkt dieser Diskussion besteht in der Erstellung und dem Vergleich von Beispielen, um die Anwendbarkeit zu prüfen. Aspekte der Prüfung sind:

* Vereinbarkeit mit dem bestehenden LibRML-Konzept
* Abbildung der notwendigen Eigenschaften, um Schnittstellenverfügbarkeit, Qualität der angezeigten, herunterladbaren Derivate, …
* Flexibilität hinsichtlich der angewendeten Werte
* Erweiterbarkeit

## Beispiele

* [Künstlerbücher](kuenstlerbuecher.md)
* [Sächsische Zeitung](saechsischezeitung.md)
* [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht](persrecht.md)
* [Eingeschränkter Zugang - Arbeitsplätze Mediathek](mediathek.md)
* [Eingeschränkte Nutzung - Mediathek - Nur Ansicht](ansicht.md)
* [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](aufsicht.md)
* [Gebrauchs- und Reklamegrafik](grafik.md)

## Dokumentation

### Grundlage

Grundlage der Dokumentation der Anpassungen ist: [Untersuchung - LibRML - Anforderungen für Retrodigitalisate (SLUB Dresden)](https://wiki.dnb.de/x/XdgtFw), insbesondere [Untersuchung - 02-02 LibRML  Neue Elemente für Retrodigitalisate](https://wiki.dnb.de/x/bNgtFw).

### Constraints

| Bezeichnung | Beschreibung | Beispiel | Bemerkung |
| --- | --- | --- | --- |
| mets | Bestandteile der METS-Dateien, die zur Beschreibung der Beschränkungen in LibRML benötigt sind, werden in dem constraint `mets` beschrieben und in Attributen spezifiziert.<br/> | - | Anwendbar in Actions: {::nomarkdown}<ul><li>displaymetadata</li><li>download</li><li>index</li><li>read</li></ul>{:/} |
| interface | Die Verfügbarkeit des Objekts an Schnittstellen wird in dem constraint `interface` beschrieben.  | - | Anwendbar in Actions: {::nomarkdown}<ul><li>publish</li></ul>{:/} |

### Attributes

| Bezeichnung | Beschreibung | Wert | Einheit / Format | Bemerkung |
| --- | --- | --- | --- | --- |
| filegroups | Werte, die in dem Attribut `USE` in `<mets:fileGrp>` enthalten sind.<br/>Die Werte können zur Steuerung der Anzeige oder des Download des Objekts (Metadaten oder Mediendaten) ausgewertet werden. {::nomarkdown}<br/>Werte:<ul><li>METS-Anwendungsprofil<ul><li>DEFAULT</li><li>DOWNLOAD</li><li>FULLTEXT</li><li>THUMBS</ul></li><li>SLUB-spezifisch<ul><li>AUDIO</li><li>ORIGINAL</li><li>VIDEO</li><li>WAVEFORM</ul><li>früheres METS-Anwendungsprofil<ul><li>MIN</li><li>MAX</li></ul></ul>Anwendungsbeispiel SLUB:<ul><li>In der SLUB Dresden werden spezifische Vorgaben definiert, die von Kitodo.Presentation ausgewertet und interpretiert werden.<ul><li>THUMBS (action= read):<br/>Nur Anzeige der Thumbnails in der Listenansicht, Vorschaubilder<br/>Keine Ansicht der Derivate in der Vollansicht</li><li>DEFAULT</li><li>FULLTEXT</li><li>THUMBS (action= read):<br/>Anzeige der Thumbnails in der Listenansicht,<br/>Anzeige der Derivate DEFAULT und FULLTEXT in der Vollansicht</li><li>ORIGINAL: Anzeige</li></ul></ul>{:/} | Tokenliste | Einheit: — | Anwendbar in Constraints:<br/> `mets` |
| fileformats | Werte, die in der METS-Datei enthalten sind oder davon abgeleitet werden, um Präsentation-Funktionen zu ermöglichen.<br/>Die Werte können zur Steuerung der Anzeige oder des Download des Objekts (Metadaten oder Mediendaten) ausgewertet werden.<br/>Werte: {::nomarkdown}<ul><li>SLUB-spezifisch:<ul><li>FULLDOWNLOAD</li><li>FULLTEXT-TXT</li><li>FULLTEXT-XML</li><li>IIIF-JSON</li><li>METS-XML</li></ul> Weitere Informationen: <ul><li>Dateien, die das digitale Objekt beschreiben:<br/>IIIF-JSON, METS-XML</li><li>Aggregierte Derivate aus METS-fileGroup:<br/>FULLDOWNLOAD<br/>mets:fileGrp[@USE="DOWNLOAD"]/mets:file[@ID="FULLDOWNLOAD"]</li><li>Abgeleitete Derivate einer METS-fileGroup:<br/>FULLTEXT-TXT, FULLTEXT-XML</li></ul>{:/} | Tokenliste | Einheit: — | Anwendbar in Constraints: <br/> `mets` |
| OAI-PMH | Verfügbarkeit der Objekte an der OAI-Schnittstelle.<br/>Weitere Informationen: {::nomarkdown}<ul><li>internal: Bereitstellung für administrative Zwecke für das Personal innerhalb einer Einrichtung.</li><li>external: Bereitstellung ohne Einschränkung.</li></ul>{:/} | `internal`<br/>`external` | Einheit: — | Anwendbar in Constraints:<br/>`interface` |
| IIIF | Verfügbarkeit der Objekte als IIIF-Manifest.<br/>Weitere Informationen: {::nomarkdown}<ul><li>internal Bereitstellung für administrative Zwecke für das Personal innerhalb einer Einrichtung.</li><li>external: Bereitstellung ohne Einschränkung.</li></ul>{:/} | `internal`<br/>`external` | Einheit: — | Anwendbar in Constraints:<br/>`interface` |
