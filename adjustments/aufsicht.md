Übersicht der Beispiele hinsichtlich [Anpassung LibRML für Retrodigitalisate](adjustments.md).

# Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht

## Beispiel A: aktuelles LibRML

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-ua/1.0/">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="location" inside="Lesesaal(Sammlungen)"/>
                            <libRML:restriction type="agreement" required="true"/><!-- Unter Aufsicht -->
                        </libRML:action>
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
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-ua/1.0/">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="mets" sections="amdSec dmdSec structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" sections="dmdSec"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="location" inside="Lesesaal(Sammlungen)"/>
                            <libRML:restriction type="mets" filegroups="AUDIO DEFAULT VIDEO"/>
                            <libRML:restriction type="agreement" details="Unter Aufsicht"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```
