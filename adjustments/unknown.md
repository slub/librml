# Unbekannt

Diese Beispiele werden als Fallback genutzt, wenn LibRML aus bestehenden Rechteinformationen abgeleitet wird, wie zum Beispiel im Fall ungültiger Kombinationen (<https://github.com/slub/librml/discussions/32>) oder Werte (<https://github.com/slub/librml/discussions/192>). Dies schützt vor unberechtigtem Zugang sowie unbefugter Nutzung digitaler Objekte, weil keine [Nutzungsart](../schema/actions.md) erlaubt ist.

Der Beschreibungstext ist auf <https://nutzungshinweis.slub-dresden.de/unknown/1.0/> verfügbar.

## Angepasstes LibRML

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="LibRML">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/unknown/1.0/"/>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Aktuelles LibRML

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="LibRML">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/unknown/1.0/"/>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```
