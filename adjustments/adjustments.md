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

#### mets

Bestandteile der METS-Dateien, die zur Beschreibung der Beschränkungen in LibRML benötigt sind, werden in dem constraint `mets` beschrieben und in Attributen spezifiziert.

Anwendbar in den folgenden [Actions](/schema/actions.md):

* `displaymetadata`
* `download`
* `index`
* `read`

#### interface

Die Verfügbarkeit des Objekts an Schnittstellen wird in dem constraint `interface` beschrieben.

Anwendbar in den folgenden [Actions](/schema/actions.md):

* `publish`

### Attributes

#### filegroups

Werte, die in dem Attribut `USE` in `<mets:fileGrp>` enthalten sind.

Die Werte können zur Steuerung der Anzeige oder des Download des Objekts (Metadaten oder Mediendaten) ausgewertet werden.

Werte:

* METS-Anwendungsprofil
  * DEFAULT
  * DOWNLOAD
  * FULLTEXT
  * THUMBS
* SLUB-spezifisch
  * AUDIO
  * ORIGINAL
  * VIDEO
  * WAVEFORM
* früheres METS-Anwendungsprofil
  * MIN
  * MAX

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

#### fileformats

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

#### OAI-PMH

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

#### IIIF

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
