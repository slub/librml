# Abhängigkeiten zwischen Constraints und Actions

Die Einschränkungen (`constraints`) mit ihren zugehörigen Eigenschaften (`attributes`) sind nicht auf alle Nutzungsarten (`actions`) anwendbar.

In der folgendenden Tabelle sind die erlaubten Kombinationen von Einschränkungen und Nutzungsarten enthalten.

| Constraint | Attributes | Actions |
| :--------- | :--------- | :--------- |
| age | maxage <br> minage | alle außer `archive` `displaymetadata` `move` |
| agreement | required | alle außer `displaymetadata` |
| concurrent | sessions | nur `lend` `read` `run` |
| count | count | nur `download` `lend` `print` `read` `reproduce` `run` |
| date | fromdate <br> todate | alle |
| duration | maxduration <br> percentage | nur `lend` `read` `run` |
| group | groups | alle außer `archive` `displaymetadata` `move` |
| location | inside <br> outside <br> subnet | alle |
| parts | percentage | alle außer `displaymetadata` `index` |
| quality | maxbitrate <br> maxresolution | alle außer `archive` `displaymetadata` `index` `move` |
| watermark | watermarkvalue | alle außer `displaymetadata` |
