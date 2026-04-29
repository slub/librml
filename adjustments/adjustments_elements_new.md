# Neue Elemente für Retrodigitalisate

## Allgemeine Informationen

Grundlage der Dokumentation ist: [Untersuchung - 02-02 LibRML  Neue Elemente für Retrodigitalisate](https://wiki.dnb.de/x/bNgtFw).
Ziel ist unter anderem die Anpassung des LibRML-Modells und die Erstellung eines Anwendungsprofils für Retrodigitalisate entsprechend [AP 5 Anpassung LibRML](https://wiki.dnb.de/x/VhmpG).

## Constraints

### mets

Bestandteile der METS-Dateien, die zur Beschreibung der Beschränkungen in LibRML benötigt sind, werden in dem constraint `mets` beschrieben und in Attributen spezifiziert.

Anwendbar in den folgenden [Actions](/schema/actions.md):

* `download`
* `index`
* `read`

### interface

Die Verfügbarkeit des Objekts an Schnittstellen wird in dem constraint `interface` beschrieben.

Anwendbar in den folgenden [Actions](/schema/actions.md):

* `publish`

## Attributes

### filegroups

Werte, die in dem Attribut `USE` in `<mets:fileGrp>` enthalten sind.

Die Werte können zur Steuerung der Anzeige oder des Download des Objekts (Metadaten oder Mediendaten) ausgewertet werden.

Werte:

* [METS-Anwendungsprofil](https://dfg-viewer.de/fileadmin/groups/dfgviewer/METS-Anwendungsprofil_2.3.1.pdf)
  * DEFAULT
  * DOWNLOAD
  * THUMBS
  * TEASER
  * AUDIO
  * FULLTEXT
* SLUB-spezifisch
  * ORIGINAL
  * VIDEO
  * WAVEFORM
* früheres METS-Anwendungsprofil
  * MIN
  * MAX
  * SPECIAL

Anwendungsbeispiel SLUB

In der SLUB Dresden werden spezifische Vorgaben definiert, die von Kitodo.Presentation ausgewertet und interpretiert werden.

* "THUMBS" (action: `read`):
  * Nur Anzeige der Thumbnails in der Listenansicht, Vorschaubilder
  * Keine Ansicht der Derivate in der Vollansicht

* "DEFAULT FULLTEXT THUMBS" (action: `read`):
  * Anzeige der Thumbnails in der Listenansicht,
  * Anzeige der Derivate DEFAULT und FULLTEXT in der Vollansicht
  * ORIGINAL: Anzeige

Anwendbar in den folgenden [Constraints](/schema/constraints.md):

* `mets`

### fileformats

Werte, die in der METS-Datei enthalten sind oder davon abgeleitet werden, um Präsentation-Funktionen zu ermöglichen.

Die Werte können zur Steuerung der Anzeige oder des Download des Objekts (Metadaten oder Mediendaten) ausgewertet werden.

Werte:

* SLUB-spezifisch
  * FULLDOWNLOAD
  * FULLTEXT-TXT
  * FULLTEXT-XML
  * IIIF-JSON
  * METS-XML

Weitere Informationen:

* Dateien, die das digitale Objekt beschreiben:
  * IIIF-JSON
  * METS-XML
* Aggregierte Derivate aus METS-fileGroup:
  * FULLDOWNLOAD
    * `mets:fileGrp[@USE="DOWNLOAD"]/mets:file[@ID="FULLDOWNLOAD"]`

* Abgeleitete Derivate einer METS-fileGroup:
  * FULLTEXT-TXT
  * FULLTEXT-XML

Anwendbar in den folgenden [Constraints](/schema/constraints.md):

* `mets`

### OAI-PMH

Verfügbarkeit der Objekte an der OAI-Schnittstelle.

Werte:

* internal
* external

Weitere Informationen:

* internal =
  Bereitstellung für administrative Zwecke für das Personal innerhalb einer Einrichtung.
* external =
  Bereitstellung ohne Einschränkung.

Anwendbar in den folgenden [Constraints](/schema/constraints.md):

* `interface`

### IIIF

Verfügbarkeit der Objekte als IIIF-Manifest.

Weitere Informationen:

Werte:

* internal
* external

Weitere Informationen:

* internal =
  Bereitstellung für administrative Zwecke für das Personal innerhalb einer Einrichtung.
* external =
  Bereitstellung ohne Einschränkung.

Anwendbar in den folgenden [Constraints](/schema/constraints.md):

* `interface`
