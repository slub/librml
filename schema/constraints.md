# Constraints - Einschränkungen

## Allgemeine Informationen

Einschränkungen (`constraints`) spezifizieren die Zugangs- und Nutzungsbeschränkungen der Nutzungsarten (`action`).
Die Einschränkungen gelten ausdrücklich nur für die `action`, der sie zugewiesen sind. Einschränkungen, die für mehrere Nutzungsarten gelten, müssen jeder `action` zugewiesen werden. 

Einschränkungen können durch [Attributes (Eigenschaften)](attributes.md) weiter spezifiziert werden.

### XML

```xml
  <action type="ACTION-NAME" permission="true">
    <restriction type="CONSTRAINT-NAME" ATTRIBUT-NAME="WERT"/>
  </action>
```

### JSON

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

In LibRML stehen folgende Einschränkung zur Verfügung.

| Constraint-Name | Übersetzung | Beschreibung | Beispiel |
| :-------------- | :--------- | :---------- |:------- |
| parts | Teile | Einschränkung der Action auf bestimmte Teile der Ressource. | [→&nbsp;Parts](#parts) |
| group | Nutzergruppen | Einschränkung der Action auf bestimmte Personen oder Personengruppen. | [→&nbsp;Group](#group)|
| age | Alter | Einschränkung der Action auf Nutzer eines bestimmten Alters. | [→&nbsp;Age](#age) |
| location | Ort | Geographisch (ein bestimmtes Gebiet z. B. Deutschland)<br/><br/>Institutionell (eine bestimmte Einrichtung z. B. SLUB Dresden). | [→&nbsp;Location](#location)|
| date | Zeitpunkt | Einschränkung der Action ab oder bis zu einem bestimmten Zeitpunkt (Embargo). | [→&nbsp;Date](#date)|
| duration | Dauer | Einschränkung der Action auf eine bestimmte Zeitdauer. | [→&nbsp;Duration](#duration) |
| count | Anzahl | Einschränkung der Action auf eine bestimmte Anzahl an Ausführungen, Benutzungen, ... | [→&nbsp;Count](#count)|
| concurrent | Gleichzeitig | Einschränkung der Action auf eine bestimmte Anzahl an gleichzeitigen Ausführungen, Benutzungen, ... | [→&nbsp;Concurrent](#concurrent) |
| watermark | Wasserzeichen | Einschränkung der Action auf eine Kennzeichnung der Ressource mit einem Wasserzeichen oder einer anderen Markierung. | [→&nbsp;Watermark](#watermark)|
| quality | Qualität | Einschränkung der Action auf eine maximale Qualität. | [→&nbsp;Quality](#quality)|
| agreement | Einwilligung | Einschränkung der Action hinsichtlich eines Vertrags oder Zustimmung zu Nutzungsbedingungen. | [→&nbsp;Agreement](#agreement)|

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
