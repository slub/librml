# Anpassung LibRML für Retrodigitalisate

## Beispiel 1: Nachlass Herbert Collum

### Beispiel 1a: Nachlass Herbert Collum (aktuelles LibRML)

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/na-he-co/1-0">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="parts" parts="10"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Arbeitsplätze SLUB"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

### Beispiel 1b: Nachlass Herbert Collum (angepasstes LibRML)

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/na-he-co/1-0">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="mets" metsfilegroup="DEFAULT | DOWNLOAD"/>
                            <libRML:restriction type="parts" partspercentage="10"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" metssection="dmdSec"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Arbeitsplätze SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="DEFAULT | FULLTEXT | THUMBS"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 2: Künstlerbücher

### Beispiel 2a: Künstlerbücher (aktuelles LibRML)

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/kr-bu/1-0">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="parts" parts="10"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Arbeitsplätze SLUB"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

### Beispiel 2b: Künstlerbücher (angepasstes LibRML)

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/kr-bu/1-0">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="mets" metsfilegroup="DOWNLOAD"/>
                            <libRML:restriction type="mets" metsfileformat="FULLDOWNLOAD-PDF | FULLTEXT-TXT | FULLTEXT-XML | IIIF-JSON"/>
                            <libRML:restriction type="parts" partspercentage="10"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" metssection="dmdSec"/>
                            <libRML:restriction type="mets" metsfilegroup="FULLTEXT"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Arbeitsplätze SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="DEFAULT | FULLTEXT | THUMBS"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 3: Sächsische Zeitung

### Beispiel 3a: Sächsische Zeitung (aktuelles LibRML)

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/sc-zt/1-0">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                        </libRML:action>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

### Beispiel 3b: Sächsische Zeitung (angepasstes LibRML)

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/sc-zt/1-0">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="DOWNLOAD | ORIGINAL"/>
                            <libRML:restriction type="mets" metsfileformat="FULLDOWNLOAD-PDF | FULLTEXT-TXT | FULLTEXT-XML | IIIF-JSON"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="FULLTEXT"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="group" groups="Nutzende SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="DEFAULT | FULLTEXT | THUMBS"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 4: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht

### Beispiel 4a: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht (aktuelles LibRML)

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-pr/1.0/">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Sonderarbeitsplatz Lesesaal Sammlungen SLUB"/>
                            <libRML:restriction type="agreement" required="true"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

### Beispiel 4b: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht (angepasstes LibRML)

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-pr/1.0/">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" metssection="dmdSec"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Sonderarbeitsplatz Lesesaal Sammlungen SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="AUDIO | DEFAULT | VIDEO"/>
                            <libRML:restriction type="agreement" details="Unter Aufsicht"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 5: Eingeschränkter Zugang - Arbeitsplätze Mediathek

### Beispiel 5a: Eingeschränkter Zugang - Arbeitsplätze Mediathek (aktuelles LibRML)

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am/1.0/">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Gruppensichtungsplätze und Einzelsichtungsplätze der Mediathek SLUB"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

### Beispiel 5b: Eingeschränkter Zugang - Arbeitsplätze Mediathek (angepasstes LibRML)

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am/1.0/">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true"/>
                        <libRML:action type="publish" permission="false"/>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Gruppensichtungsplätze und Einzelsichtungsplätze der Mediathek SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="AUDIO | DEFAULT | VIDEO"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 6: Eingeschränkte Nutzung - Mediathek - Nur Ansicht

### Beispiel 6a: Eingeschränkte Nutzung - Mediathek - Nur Ansicht (aktuelles LibRML)

Umsetzung mit dem derzeit gültigen LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="http://librml.org/schema">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/en-ma/1.0/">
                        <libRML:action type="displaymetadata" permission="true"/>
                        <libRML:action type="download" permission="false"/>
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

### Beispiel 6b: Eingeschränkte Nutzung - Mediathek - Nur Ansicht (angepasstes LibRML)

Umsetzung mit einem angepassten LibRML-Modell

```xml
<mets:mets xmlns:mets="http://www.loc.gov/METS/">
    <mets:metsHdr CREATEDATE="2023-05-15T14:10:06.000+02:00" LASTMODDATE="2025-11-06T07:20:31.561+01:00"/>
    <mets:amdSec ID="AMD">
        <mets:rightsMD ID="RMD1">
            <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
                <libRML:libRML xmlns:libRML="https://librml.org/index.html">
                    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/en-ma/1.0/">
                        <libRML:action type="displaymetadata" permission="true">
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" metssection="dmdSec"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="mets" metsfilegroup="AUDIO | DEFAULT | VIDEO"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 7: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht

### Beispiel 7a: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht (aktuelles LibRML)

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
                            <libRML:restriction type="group" groups="Sonderarbeitsplatz Lesesaal Sammlungen SLUB"/>
                            <libRML:restriction type="agreement" required="true"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

### Beispiel 7b: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht (angepasstes LibRML)

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
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="false"/>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" metssection="dmdSec"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="concurrent" sessions="1"/>
                            <libRML:restriction type="group" groups="Sonderarbeitsplatz Lesesaal Sammlungen SLUB"/>
                            <libRML:restriction type="mets" metsfilegroup="AUDIO | DEFAULT | VIDEO"/>
                            <libRML:restriction type="agreement" details="Unter Aufsicht"/><!-- Unter Aufsicht -->
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```

## Beispiel 8: Gebrauchs- und Reklamegrafik

### Beispiel 8a: Gebrauchs- und Reklamegrafik (aktuelles LibRML)

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

### Beispiel 8b: Gebrauchs- und Reklamegrafik (angepasstes LibRML)

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
                            <libRML:restriction type="mets" metssection="amdSec | dmdSec | structMap"/>
                        </libRML:action>
                        <libRML:action type="download" permission="true">
                            <libRML:restriction type="mets" metsfilegroup="DEFAULT | DOWNLOAD"/>
                            <libRML:restriction type="mets" metsfileformat="FULLTEXT-TXT | FULLTEXT-XML | IIIF-JSON"/>
                        </libRML:action>
                        <libRML:action type="index" permission="true">
                            <libRML:restriction type="mets" metssection="dmdSec"/>
                            <libRML:restriction type="mets" metsfilegroup="FULLTEXT"/>
                        </libRML:action>
                        <libRML:action type="publish" permission="true">
                            <libRML:restriction type="interface" OAI-PMH="internal"/>
                        </libRML:action>
                        <libRML:action type="read" permission="true">
                            <libRML:restriction type="mets" metsfilegroup="DEFAULT | FULLTEXT | THUMBS"/>
                        </libRML:action>
                    </libRML:item>
                </libRML:libRML>
            </mets:mdWrap>
        </mets:rightsMD>
    </mets:amdSec>
</mets:mets>
```
