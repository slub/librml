# Anwendungsprofil für Kitodo (Entwurf)

Ein technisch durchsetzbares Anwendunsprofil von LibRML für [Kitodo.Production](https://www.kitodo.org/software/kitodoproduction) beschränkt sich auf Nutzungsarten und Einschränkungen, die auf Präsentationsebene direkt maschinell geprüft und erzwungen werden können (z. B. über IP-Filter, Authentifizierung oder Zeitstempel). Rein moralische oder nicht-technisch überprüfbare Appelle (wie „Nicht-kommerzielle Nutzung“) entfallen.

Das LibRML-Anwendunsprofil ist auf das [METS-Anwendungsprofil für digitalisierte Medien](https://dfg-viewer.de/fileadmin/groups/dfgviewer/METS-Anwendungsprofil_2.3.1.pdf) zugeschnitten.

## Verpflichtende Nutzungsarten (Actions)

- **displaymetadata** muss immer auf `true` gesetzt sein.\
  Wiederholbar: nein

In nicht-integrierten Umgebungen, wo üblicheweise Katalog und Präsentationsebene getrennt sind, lässt sich diese Nutzungsart nicht vernünftig einsetzen.

## Empfohlene Nutzungsarten (Actions)

- **download**\
  Wiederholbar: ja
- **index**\
  Wiederholbar: ja
- **print**\
  Wiederholbar: ja
- **read**\
  Wiederholbar: ja
- **run**\
  Wiederholbar: ja

## Empfohlene Einschränkungen (Constraints)

- **age**
- **agreement**
- **mets**\
  NB: In der METS-Datei sind die Maße eines Objektes nicht hinterlegt, daher würde die Einschränkung - - **quality** höchstens implizit greifen.
- **concurrent**
- **date**
- **duration**\
  NB: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
- **group**
- **location**

Alle anderen Nutzungsarten und Einschränkungen sind nicht verfügbar.
