# Abhängigkeiten zwischen Attributes, Constraints und Actions

## Allgemeine Informationen

Die Einschränkungen (`constraints`) mit ihren zugehörigen Eigenschaften (`attributes`) sind nicht auf alle Nutzungsarten (`actions`) anwendbar.
Folgende Tabelle verschafft einen Überblick, welche Einschränkungen mit welchen Nutzungsarten kombinierbar sind.

| Attribut | Constraint | Action |
| :--------- | :--------- | :--------- |
| fromdate | date | alle actions |
| todate | date | alle actions |
| maxresolution | quality | alle actions außer displaymetadata, index, archive and move |
| maxbitrate | quality | alle actions außer displaymetadata, index, archive and move |
| count | count | read, run, lend, download, print and reproduce |
| sessions | concurrent | read, run und lend |
| inside | location | alle actions |
| subnet | location | alle actions |
| outside | location | alle actions |
| watermarkvalue | watermark | alle actions außer displaymetadata |
| duration | duration | read, run und lend |
| minage | age | alle actions außer displaymetadata, index, archive and move |
| maxage | age | alle actions außer displaymetadata, index, archive and move |
| required | agreement | alle actions außer displaymetadata und index |
| parts | parts | alle actions außer displaymetadata und index |
| groups | group | alle actions außer displaymetadata, index, archive and move |
