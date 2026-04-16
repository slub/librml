# Attributes - Eigenschaften

## Allgemeine Informationen

Eigenschaften (`attributes`) spezifizieren die Einschränkungen (`constraints`) von Nutzungsarten (`actions`). Während ein `Constraint` den Typ der Einschränkung festlegt (z. B. Ort oder Zeit), definieren die Attribute die konkreten Parameter.

Jeder Eigenschaft **muss** ein Wert zugewiesen werden. Eine Einschränkung kann  durch mehrere Eigenschaften spezifiziert werden.

```xml
<restriction type="CONSTRAINT-NAME" ATTRIBUT-NAME="WERT"/>
```

```json
"restrictions": [{
    "type": "CONSTRAINT-NAME",
    "ATTRIBUT-NAME": "WERT",
 }]
```

## Liste

In LibRML stehen folgende Eigenschaften zur Verfügung.

| Attribut-Name | Beschreibung | Wert | Einheit&nbsp;/&nbsp;Format |
| :------------- | :--------- | :--------- | :------------------ |
| count | Anzahl der erlaubten Action, z. B. die Anzahl der erlaubten Ausleihen | positive integer | |
| fromdate | Start-Datum der Einschränkung | Datum | **Format**: ISO8601 (YYYY-MM-DD) |
| groups | Gruppen, auf die eine Constraint zutrifft. | Tokenliste  | |
| inside | Nutzung innerhalb eines geographischen Gebiets oder innerhalb einer Institution | Name | |
| maxage | Maximalalter für eine Action. Zum Beispiel in Einrichtungen genutzt, die Kinderbücher für Erwachsene unzugänglich machen. | positive integer | **Einheit**: Jahre |
| maxbitrate | Maximal erlaubte Bitrate für den Download eines digitalen Objekts | positive integer | **Einheit**: Bit |
| maxduration | Maximale Dauer eines Constraints | positive integer | **Einheit**: Sekunden |
| maxresolution | Maximal erlaubte Auflösung für die Anzeige und den Download eines digitalen Objekts | positive integer | **Einheit**: DPI <br> Die Einheit kann auch angegeben werden, z.B. 150dpi, oder eine entsprechende Zeilenzahl für Videos festgelegt werden, z.B. 1080p oder 720i |
| minage | Mindestalter für eine Action. Zum Beispiel zur Beschreibung des Jugendschutzes genutzt. | positive integer | **Einheit**: Jahre |
| outside | Nutzung außerhalb eines geographischen Gebiets oder außerhalb einer Institution | Name | |
| percentage | Teile des digitalen Objekts in Prozent. | nicht-negative integer | |
| required | "Erforderlich" (wird bei der Erforderlichkeit von externen Verträgen benutzt) | Boolean | true/false |
| sessions | Anzahl der erlaubten parallelen Zugriffe auf ein digitalen Objekt | positive integer | |
| subnet | Innerhalb einer Einrichtung kann der Zugriff über ein Subnetz genauer spezifiziert werden. | IP-Bereiche | **Format:**: [CIDR-Notation](https://de.wikipedia.org/wiki/CIDR) |
| todate | End-Datum der Einschränkung | Datum | **Format**: ISO8601 (YYYY-MM-DD) |
| watermarkvalue | Definition des Wasserzeichens. Das Wasserzeichen muss an einem spezifischen Ort hinterlegt sein, der hier verlinkt ist. | URI | |
