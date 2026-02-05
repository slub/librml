Übersicht der Beispiele hinsichtlich [Anpassung LibRML für Retrodigitalisate](adjustments.md).

# Gebrauchs- und Reklamegrafik

Diese LibRML-Beispiele reflektieren die Rechte- und Nutzungshinweise, die unter <https://nutzungshinweis.slub-dresden.de/ge-re/1.0/> zusammengefasst sind.

## Beispiel A: aktuelles LibRML

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ge-re/1.0/">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="true"/>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true"/>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel B: angepasstes LibRML

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="https://librml.org/index.html">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ge-re/1.0/">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="mets" sections="amdSec dmdSec structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="mets" filegroups="DEFAULT DOWNLOAD"/>
                            <libRML:restriction type="mets" fileformats="FULLTEXT-TXT FULLTEXT-XML IIIF-JSON"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" sections="dmdSec"/>
                            <libRML:restriction type="mets" filegroups="FULLTEXT"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="mets" filegroups="DEFAULT FULLTEXT THUMBS"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```
