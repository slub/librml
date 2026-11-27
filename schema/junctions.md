# Verküpfungen von Constraints und Actions

Die Einschränkungen (`constraints`) können logisch miteinander verbunden werden.

## Konjunktion (Und-Verknüpfung)

Im folgenden Beispiel wird das Objekt dem/der Nutzenden nur angezeigt, wenn er/sie als Benutzende(r) angemeldet ist _und_ sich innerhalb der Bibliothek aufhält.

```xml
  <action type="read" permission="true">
    <restriction type="group" groups="user" />
    <restriction type="location" inside="library" />
  </action>
```

```json
{
  "actions": [{
    "type": "read",
    "permission": true,
    "restrictions": [
      {
        "type": "group",
        "groups": [
          "user"
        ]
      },
      {
        "type": "location",
        "inside": "library"
      }
    ]
  }]
}
```

## Disjunktion (Oder-Verknüpfung)

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
{
  "actions": [{
    "type": "read",
    "permission": true,
    "restrictions": [
      {
        "type": "group",
        "groups": [
          "user"
        ]
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
  }]
}
```

Bei Token-Listen (wie z.B. in `groups`) greift ebenfalls eine Oder-Verknüpfung.
Im folgenden Beispiel kann die nutzende Person das Objekt nur ausdrucken, wenn sie sich auf dem "Campus" _oder_ sich innerhalb der "Bibliothek" aufhält.

```xml
  <action type="print" permission="true">
    <restriction type="location" groups="Campus Bibliothek" />
  </action>
```

```json
{
  "actions": [{
    "type": "print",
    "permission": true,
    "restrictions": [
      {
        "type": "group",
        "groups": [
          "Campus",
          "Bibliothek"
        ]
      }
    ]
  }]
}
```
