# Constraints

## Einschränkungen

Eingeschränkte Nutzungsmöglichkeiten werden in der LibRML an den konkreten `Actions` festgelegt. Die Einschränkungen (`Constraints`) gelten explizit nur für die Action an der sie hinterlegt sind, um die maschinelle Auswertbarkeit zu gewährleisten. Einschränkungen, die sich auf mehrere Nutzungsrechte auswirken, müssen entsprechend wiederholt werden. Für die vereinfachte Bearbeitung können systematische Einschränkungen einmalig definiert und wiederverwendet werden (siehe Templates).

Einige `Constraints` werden durch `Attribute` [(siehe Attribute)](attributes.md) näher spezifiziert.

**JSON**

```json
"actions": [{
    "type": "ACTION-NAME",
    "permission": true,
    "restrictions": [{
        "type": "CONSTRAINT-NAME",
        "ATTRIBUTE": "X"
     }]
}]
```

**XML**

```xml
<action type="ACTION-NAME" permission="true">
  <restriction type="CONSTRAINT-NAME" ATTRIBUTE="X"/>
</action>
```

In der LibRML stehen folgende `Constraints` zur Einschränkung der `Actions` zur Verfügung.

| Constraint-Name | Übersetzung | Beschreibung | Beispiel |
| :-------------- | :--------- | :---------- |:------- |
| parts | Teile | Einschränkung der Action auf bestimmte Teile der Ressource. | [→&nbsp;Parts](#parts) |
| group | Nutzergruppe | Einschränkung der Action auf bestimmte Personen oder Personengruppen. | [→&nbsp;Group](#group)|
| age | Alter | Einschränkung der Action auf Nutzer eines bestimmten Alters. | [→&nbsp;Age](#age) |
| location | Ort | Geographisch (ein bestimmtes Gebiet z. B. Deutschland)<br/><br/>Institutionell (eine bestimmte Einrichtung z. B. SLUB Dresden) | [→&nbsp;Location](#location)|
| date | Zeitpunkt | Einschränkung der Action ab oder bis zu einem bestimmten Zeitpunkt (Embargo). | [→&nbsp;Date](#date)|
| duration | Dauer | Einschränkung der Action auf eine bestimmte Zeitdauer. | [→&nbsp;Duration](#duration) |
| count | Anzahl | Einschränkung der Action auf eine bestimmte Anzahl an Ausführungen, Benutzungen, ... | [→&nbsp;Count](#count)|
| concurrent | Gleichzeitig | Einschränkung der Action auf eine bestimmte Anzahl an gleichzeitigen Ausführungen, Benutzungen, ... | [→&nbsp;Concurrent](#concurrent) |
| watermark | Wasserzeichen | Einschränkung der Action auf eine Kennzeichnung der Ressource mit einem Wasserzeichen oder einer anderer Markierung. | [→&nbsp;Watermark](#watermark)|
| quality | Qualität | Einschränkung der Action auf eine maximale Qualität. | [→&nbsp;Quality](#quality)|
| agreement | Einwilligung | Einschränkung der Action hinsichtlich eines Vertrags oder Zustimmung zu Nutzungsbedingungen. | [→&nbsp;Agreement](#agreement)|

## Beispiele

### Parts

```json
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "parts",
      "parts": "1"
    },
```

### Group

```json
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "group",
      "groups": [
        "registered",
        "employee",
      ]
    },
```

### Age

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "age",
      "minage": "18"
    },
```

### Location

```json
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "location",
      "subnet": "192.168.0.0/16"
    },
```

### Date

```json
  "type": "distribute",
  "permission": true,
  "restrictions": [
    {
      "type": "date",
      "fromdate": "2035-01-01"
    },
```

### Duration

```json
  "type": "run",
  "permission": true,
  "restrictions": [
    {
      "type": "duration",
      "duration": 86400
    },
```

### Count

```json
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "count",
      "count": 10
    },
```

### Concurrent

```json
  "type": "lend",
  "permission": true,
  "restrictions": [
    {
      "type": "concurrent",
      "sessions": 4
    },
```

### Watermark

```json
  "type": "distribute",
  "permission": true,
  "restrictions": [
    {
      "type": "watermark",
      "watermarkvalue": "https://domain/watermark.png"
    },
```

### Quality

```json
  "type": "print",
  "permission": true,
  "restrictions": [
    {
      "type": "quality",
      "maxresolution": 300
    },
```

### Agreement

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "agreement",
      "required": true
    },
```
