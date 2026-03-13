# Constraints - Einschränkungen

## Allgemeine Informationen

Einschränkungen (`constraints`) spezifizieren die Zugangs- und Nutzungsbeschränkungen der Nutzungsarten (`action`).
Die Einschränkungen gelten ausdrücklich nur für die `action`, der sie zugewiesen sind. Einschränkungen, die für mehrere Nutzungsarten gelten, müssen jeder `action` zugewiesen werden.

Einschränkungen können durch [Attributes (Eigenschaften)](attributes.md) weiter spezifiziert werden.

```xml
  <action type="ACTION-NAME" permission="true">
    <restriction type="CONSTRAINT-NAME" ATTRIBUT-NAME="WERT"/>
  </action>
```

```json
  "actions": [{
    "type": "ACTION-NAME",
    "permission": true,
    "restrictions": [{
        "type": "CONSTRAINT-NAME",
        "ATTRIBUT-NAME": "WERT"
     }]
  }]
```

## Liste

In LibRML stehen folgende Einschränkungen zur Verfügung.

| Constraint-Name | Übersetzung | Beschreibung | Beispiel |
| :-------------- | :--------- | :---------- |:------- |
| age | Alter | Einschränkung auf Nutzer eines bestimmten Alters. | [→&nbsp;Age](#age) |
| agreement | Einwilligung | Einschränkung hinsichtlich eines Vertrags oder Zustimmung zu Nutzungsbedingungen. | [→&nbsp;Agreement](#agreement) |
| concurrent | gleichzeitig | Einschränkung auf eine bestimmte Anzahl an gleichzeitigen Ausführungen, Benutzungen, o. Ä. | [→&nbsp;Concurrent](#concurrent) |
| count | Anzahl | Einschränkung auf eine bestimmte Anzahl an Ausführungen, Benutzungen, o. Ä. | [→&nbsp;Count](#count) |
| date | Zeitpunkt | Einschränkung ab oder bis zu einem bestimmten Zeitpunkt (Embargo). | [→&nbsp;Date](#date) |
| duration | Dauer | Einschränkung auf eine bestimmte Zeitdauer. | [→&nbsp;Duration](#duration) |
| group | Gruppe | Einschränkung auf bestimmte Personen oder Personengruppen. | [→&nbsp;Group](#group) |
| location | Ort | Einschränkung auf ein bestimmtes Gebiet (z. B. `Deutschland`)oder auf eine bestimmte Einrichtung (z. B. `SLUB`). | [→&nbsp;Location](#location) |
| parts | Teile | Einschränkung auf bestimmte Teile des digitalen Objekts. | [→&nbsp;Parts](#parts) |
| quality | Qualität | Einschränkung auf eine maximale Qualität. | [→&nbsp;Quality](#quality) |
| watermark | Wasserzeichen | Einschränkung auf eine Kennzeichnung des digitalen Objekts mit einem Wasserzeichen oder einer anderen Markierung. | [→&nbsp;Watermark](#watermark) |

## Beispiele

### Parts

```xml
  <action type="download" permission="true">
    <restriction type="parts" parts="1" />
  </action>
```

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

```xml
  <action type="print" permission="true">
    <restriction type="group" groups="registered employee" />
  </action>
```

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

```xml
  <action type="read" permission="true">
    <restriction type="age" suminagebnet="18" />
  </action>
```

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

```xml
  <action type="download" permission="true">
    <restriction type="location" inside="library" />
  </action>
```

```json
  "type": "download",
  "permission": true,
  "restrictions": [
    {
      "type": "location",
      "inside": "library"
    },
```

### Date

```xml
  <action type="distribute" permission="true">
    <restriction type="date" fromdate="2035-01-01" />
  </action>
```

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

```xml
  <action type="run" permission="true">
    <restriction type="duration" duration="86400" />
  </action>
```

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

```xml
  <action type="print" permission="true">
    <restriction type="count" count="10" />
  </action>
```

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

```xml
  <action type="lend" permission="true">
    <restriction type="concurrent" sessions="4" />
  </action>
```

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

```xml
  <action type="distribute" permission="true">
    <restriction type="watermark" watermarkvalue="https://domain/watermark.png" />
  </action>
```

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

```xml
  <action type="print" permission="true">
    <restriction type="quality" maxresolution="300" />
  </action>
```

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

```xml
  <action type="read" permission="true">
    <restriction type="agreement" required="true" />
  </action>
```

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "agreement",
      "required": true
    },
```
