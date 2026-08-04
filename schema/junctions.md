# Verküpfungen von Constraints und Actions

Die Einschränkungen (`constraints`) können logisch miteinander verbunden werden.

## Konjuktion (Und-Verknüpfung)

Im folgenden Beispiel wird das Objekt dem/der Nutzenden nur angezeigt, wenn er/sie als Benutzende(r) angemeldet ist _und_ sich innerhalb der Bibliothek aufhält.

```xml
  <action type="read" permission="true">
    <restriction type="group" groups="user" />
    <restriction type="location" inside="library" />
  </action>
```

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "groups",
      "groups": "user"
    },
    {
      "type": "location",
      "inside": "library"
    },
  ]
```

## Disjuktion (Oder-Verknüpfung)

Im folgenden Beispiel wird das Objekt dem/der Nutzenden nur angezeigt, wenn er/sie als Benutzende(r) angemeldet ist _oder_ sich innerhalb der Bibliothek aufhält.

```xml
  <action type="read" permission="true">
    <restriction type="group" groups="user" />
  </action>
  <action type="read" permission="true">
    <restriction type="location" inside="library" />
  </action>
```

```json
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "groups",
      "groups": "user"
    }
  ],
  "type": "read",
  "permission": true,
  "restrictions": [
    {
      "type": "location",
      "inside": "library"
    }
  ]
```

