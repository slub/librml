# Anwendungsprofil für Kitodo (Entwurf)

Ein technisch durchsetzbares Anwendunsprofil von LibRML für [Kitodo.Production](https://www.kitodo.org/software/kitodoproduction) beschränkt sich auf Nutzungsarten und Einschränkungen, die auf Präsentationsebene direkt maschinell geprüft und erzwungen werden können (z. B. über IP-Filter, Authentifizierung oder Zeitstempel). Rein moralische oder nicht-technisch überprüfbare Appelle (wie „Nicht-kommerzielle Nutzung“) entfallen.
In ([**Actions**](actions.md)) sind diese Nutzungsarten als _technisch nicht durchsetzbar_ gekennzeichnet.
Zudem werden Funktionen, die in Kitodo.Presemtation nicht vorhanden sind (_archive_, _print_, ...) nicht berücksichtigt. 

Das LibRML-Anwendunsprofil ist auf das [METS-Anwendungsprofil für digitalisierte Medien](https://dfg-viewer.de/fileadmin/groups/dfgviewer/METS-Anwendungsprofil_2.3.1.pdf) zugeschnitten.

## Nutzungsarten (Actions)

- **displaymetadata**\
  Kommentar: Empfehlung: `true`, weil das Objekt ansonsten nicht such- und auffindbar ist.\
  Wiederholbar: nein\
  Verpflichtungsgrad: verpflichtend
- **download**\
  Wiederholbar: ja\
  Verpflichtungsgrad: optional
- **index**\
  Kommentar: Bezieht sich für den Benutzer auf die Durchsuchbarkeit eines Volltextes; kann auch ohne vorhandenen Volltext gesetzt sein.\
  Wiederholbar: ja\
  Verpflichtungsgrad: optional
- **read**\
  Wiederholbar: ja\
  Verpflichtungsgrad: verpflichtend
  Kommentar: ...
- **run**\
  Kommentar: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
  Wiederholbar: ja\
  Verpflichtungsgrad: optional

## Einschränkungen (Constraints)

- **age**
- **agreement**
- **mets**\
  Kommentar: Es werden die auswertbaren Dateigruppen in der METS-Datei des Objekts angegeben.
- **concurrent**
- **date**
- **duration**\
  Kommentar: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
- **group**
- **location**

Alle anderen Nutzungsarten und Einschränkungen sind nicht verfügbar.
