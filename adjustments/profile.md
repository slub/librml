# Anwendungsprofil für Kitodo (Entwurf)

Ein technisch durchsetzbares Anwendunsprofil von LibRML für [Kitodo.Production](https://www.kitodo.org/software/kitodoproduction) beschränkt sich auf Nutzungsarten und Einschränkungen, die auf Präsentationsebene direkt maschinell geprüft und erzwungen werden können (z. B. über IP-Filter, Authentifizierung oder Zeitstempel). Rein moralische oder nicht-technisch überprüfbare Appelle (wie „Nicht-kommerzielle Nutzung“) entfallen.

Das LibRML-Anwendunsprofil ist auf das [METS-Anwendungsprofil für digitalisierte Medien](https://dfg-viewer.de/fileadmin/groups/dfgviewer/METS-Anwendungsprofil_2.3.1.pdf) zugeschnitten.

## Nutzungsarten (Actions)

- **displaymetadata**\
  Kommentar: Muss immer auf `true` gesetzt sein. In nicht-integrierten Umgebungen, wo üblicheweise Katalog und Präsentationsebene getrennt sind, lässt sich diese Nutzungsart anders nicht vernünftig einsetzen.\
  Wiederholbar: nein\
  Verpflichtungsgrad: Verpflichtend
- **download**\
  Wiederholbar: ja\
  Verpflichtungsgrad: optional
- **index**\
  Kommentar: Bezieht sich für den Benutzer auf die Durchsuchbarkeit eines Volltextes; kann auch ohne vorhandenen Volltext gesetzt sein.\
  Wiederholbar: ja\
  Verpflichtungsgrad: optional
- **read**\
  Wiederholbar: ja\
  Verpflichtungsgrad: Verpflichtend
- **run**\
  Kommentar: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
  Wiederholbar: ja\
  Verpflichtungsgrad: optional

## Einschränkungen (Constraints)

- **age**
- **agreement**
- **mets**\
  Kommentar: In der METS-Datei sind die Maße eines Objektes nicht hinterlegt, daher würde die Einschränkung - - **quality** höchstens implizit greifen.
- **concurrent**
- **date**
- **duration**\
  Kommentar: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
- **group**
- **location**

Alle anderen Nutzungsarten und Einschränkungen sind nicht verfügbar.
