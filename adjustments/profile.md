# Anwendungsprofil für Kitodo (Entwurf)

## Allgemeine Informationen

Das folgende LibRML-Anwendungsprofil ist auf das [METS-Anwendungsprofil für digitalisierte Medien](https://dfg-viewer.de/fileadmin/groups/dfgviewer/METS-Anwendungsprofil_2.3.1.pdf) sowie auf die Anwendung mit _[Kitodo.Presentation](https://www.kitodo.org/software/kitodopresentation)_ zugeschnitten.

## LibRML-Elemente

### Allgemeine Informationen

Das Anwendunsprofil beschränkt sich auf Nutzungsarten und Einschränkungen, die auf Präsentationsebene direkt maschinell geprüft und erzwungen werden können (z. B. über IP-Filter, Authentifizierung oder Zeitstempel).
Rein moralische oder nicht-technisch überprüfbare Appelle (wie „Nicht-kommerzielle Nutzung“) entfallen; diese Nutzungsarten sind im Konzept unter ([**Actions**](../schema/actions.md)) als _technisch nicht durchsetzbar_ gekennzeichnet.
Zudem werden in _Kitodo.Presemtation_ noch fehlende Funktionen nicht berücksichtigt.

## Header

- **copyright**\
  Kommentar: Das METS-Anwendungsprofil sieht vor, dass hierfür `dv:license` zu verwenden ist. Zur Vermeidung redundanter Informationen wird das Attribut in dem LibRML-Anwendungsprofil nicht berücksichtigt.
- **usageguide**\
  Kommentar: Verweist auf die Nutzungshinweise, die die Beschränkungen beschreiben oder begründen.\
  Verpflichtungsgrad: verpflichtend

## Nutzungsarten (Actions)

- **displaymetadata**\
  Kommentar: Muss immer auf `true` gesetzt sein. In nicht-integrierten Umgebungen, bei denen üblicherweise Katalog und Präsentationsebene getrennt sind, wie bei Kitodo.Presentation, lässt sich diese Nutzungsart nicht anders einsetzen.\
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
  Kommentar: Diese Nutzungart muss – unter Umständen mit entsprechenden Einschränkungen – immer angegeben werden.
- **run**\
  Kommentar: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
  Wiederholbar: ja\
  Verpflichtungsgrad: optional

### Einschränkungen (Constraints)

- **age**
- **agreement**
- **mets**\
  Kommentar: Es werden die auswertbaren Dateigruppen in der METS-Datei des Objekts bestimmt.
- **concurrent**
- **date**\
  Kommentar: Wird zur Bestimmung von Embargofristen verwendet.
- **duration**\
  Kommentar: Aktuell in Kitodo.Presentation noch nicht umsetzbar.
- **group**
- **location**

Alle anderen Nutzungsarten und Einschränkungen sind nicht verfügbar.

## Anwendung in METS

### Allgemeine Informationen

Wird LibRML in die METS-Datei eingebettet, muss berücksichtigt werden, dass zwei METS-Elemente `<mets:rightsMD ID="LibRML">` eingetragen werden.
Grund ist _2.6.2.1 Rechtedeklaration – mets:rightsMD_ ff. des [METS-Anwendungsprofil für digitalisierte Medien](https://dfg-viewer.de/fileadmin/groups/dfgviewer/METS-Anwendungsprofil_2.3.1.pdf), in dem bereits ein `<mets:rightsMD>` verpflichtend in der METS-Datei enthalten sein muss.

Weitere Beispiele sind in der Diskussion <https://github.com/slub/librml/discussions/192> enthalten oder können mit dem XSLT erstellt werden.

In dem Anwendungsprofil werden nur Rechteinformationen und Beschränkungen beschrieben, die für das vollständige Objekt gelten. 
Aus diesem Grund werden die `<mets:rightsMD>`-Elemente nur in eine `<mets:amdSec>` eingetragen.

### Anwendung

```xml
<mets:mets[…]>
  <mets:metsHdr[…]/>
  <mets:amdSec ID="AMD">
    <mets:rightsMD ID="dvrightsid" >
      <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="DVRIGHTS" >
        <mets:xmlData>
          <dv:rights>
            …
          </dv:rights>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:rightsMD>
    <mets:rightsMD>
      <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
        <mets:xmlData>
          <libRML:libRML xmlns:libRML="http://librml.org/schema">
            <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am/1.0/">
                <libRML:action type="displaymetadata" permission="true"/>
                <libRML:action type="download" permission="false"/>
                <libRML:action type="index" permission="true">
                    <libRML:restriction type="concurrent" sessions="1"/>
                    <libRML:restriction type="location" inside="SLUB-PC-Arbeitsplaetze-Mediathek"/>
                </libRML:action>
                <libRML:action type="read" permission="true">
                    <libRML:restriction type="concurrent" sessions="1"/>
                    <libRML:restriction type="location" inside="SLUB-PC-Arbeitsplaetze-Mediathek"/>
                </libRML:action>
            </libRML:item>
          </libRML:libRML>
        </mets:xmlData>
      </mets:mdWrap>
    </mets:rightsMD>
  </mets:amdSec>
