# Attributes - Eigenschaften

## Allgemeine Informationen

Eigenschaften (`attributes`) spezifizieren die Einschränkungen (`constraints`) von Nutzungsarten (`actions`).
Jeder Eigenschaft **muss** ein Wert zugewiesen werden. Einschränkungen können mehreren Eigenschaften zugewiesen werden.

### XML

```xml
<restriction type="CONSTRAINT-NAME" ATTRIBUT-NAME="WERT"/>
```

### JSON

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
| fromdate | Start-Datum der Einschränkung | Datum | **Format**: ISO8601 (YYYY-MM-DD) |
| todate | End-Datum der Einschränkung | Datum | **Format**: ISO8601 (YYYY-MM-DD) |
| maxresolution | maximal erlaubte Auflösung für den Download eines digitalen Objekts | non-negative Integer | **Einheit**: DPI |
| maxbitrate | maximal erlaubte Bitrate für den Download eines digitalen Objekts | non-negative Integer | **Einheit**: Bit |
| count | Anzahl der erlaubten Action, z. B. die Anzahl der erlaubten Ausleihen | non-negative Integer | **Einheit**: — |
| sessions | Anzahl der erlaubten parallelen Zugriffe auf ein digitalen Objekt | non-negative Integer | **Einheit**: — |
| inside | Nutzung innerhalb eines geographischen Gebiets oder innerhalb einer Institution<br/><br/> | Name | **Einheit**: — |
| subnet | Innerhalb einer Einrichtung kann der Zugriff über ein Subnetz genauer spezifiziert werden. | IP, IP-Bereiche | **Format**: — |
| outside | Nutzung außerhalb eines geographischen Gebiets oder außerhalb einer Institution | Name | **Einheit**: —|
| watermarkvalue | Definition des Wasserzeichens. Das Wasserzeichen muss an einem spezifischen Ort hinterlegt sein, der hier verlinkt ist.| URI | **Format**: — |
| duration | Dauer eines Constraints | non-negative Integer | **Einheit**: Sekunden |
| minage | Mindestalter für eine Action. Zum Beispiel zur Beschreibung des Jugendschutzes genutzt. | non-negative Integer | **Einheit**: Jahre |
| maxage | Maximalalter für eine Action. Zum Beispiel in Einrichtungen genutzt, die Kinderbücher für Erwachsene unzugänglich machen. | non-negative Integer | **Einheit**: Jahre |
| required | "Erforderlich" (wird bei der Erforderlichkeit von externen Verträgen benutzt) | true/false | **Format**: — |
| parts | Teile des digitalen Objekts. | non-negative Integer | **Einheit**: — |
| groups | Gruppen, auf die eine Constraint zutrifft. | Tokenliste  | **Einheit**: — |
