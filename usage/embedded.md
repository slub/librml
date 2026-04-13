# Eingebettetes LibRML in den Metadaten

## Allgemeine Informationen

LibRML kann in eine Metadatendatei eingetragen werden. Im Folgenden wird eine Anwendung in [METS](https://www.loc.gov/standards/mets/) und [MODS](https://www.loc.gov/standards/mods/) beschrieben. Der LibRML-Code wird von den jeweiligen Systemen (Präsentation, Repositorium, Rechtemanagementsystem, …) ausgewertet.

Sind bereits Rechtehinweise oder Nutzungshinweise verfügbar, kann der LibRML-Code daraus abgeleitet und in die Metadaten eingetragen werden, wie zum Beispiel in METS durch [XSLT](https://github.com/slub/librml/discussions/32#discussioncomment-15669157).

## METS

### Elemente

In METS wird der XML-Code im Element `<rightsMD>` eingetragen.

```xml
<mets:mets[...]>
  <mets:metsHdr[...]/>
  <mets:amdSec>
    <mets:rightsMD ID="LibRML">
      <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
        <!--Here, LibRML can be embedded.-->
      </mets:mdWrap>
    </mets:rightsMD>
  </mets:amdSec>
</mets:mets>
```

`<mets:rightsMD>`

- LibRML wird in das METS-Element `<mets:rightsMD>` eingetragen.

`<mets:mdWrap>`

- LibRML wird in das METS-Element `<mets:mdWrap>` eingetragen.

`<mets:mdWrap MDTYPE>`

- In das METS-Attribut @MDTYPE wird immer "OTHER" eingetragen.

`<mets:mdWrap OTHERMDTYPE>`

- In das METS-Attribut @OTHERMDTYPE wird immer "LibRML" eingetragen.

### Beispiel

In dem folgenden Beispiel wird [Zugang nur innerhalb eines IP-Adressbereichs (z.B. Campusnetz)](../examples/location) angewendet.

```xml
<mets:mets[...]>
  <mets:metsHdr[...]/>
  <mets:amdSec>
    <mets:rightsMD ID="LibRML">
      <mets:mdWrap MDTYPE="OTHER" MIMETYPE="text/xml" OTHERMDTYPE="LibRML">
        <libRML:libRML version="0.4" xmlns:libRML="http://librml.org/schema">
          <libRML:item commercialuse="false">
            <libRML:action type="displaymetadata" permission="true"/>
            <libRML:action type="index" permission="true"/>
            <libRML:action type="archive" permission="true"/>
            <libRML:action type="read" permission="true">
              <libRML:restriction type="location" inside="SLUB"/>
            </libRML:action>
            <libRML:action type="download" permission="true">
              <libRML:restriction type="location" inside="SLUB"/>
            </libRML:action>
            <libRML:action type="print" permission="true">
              <libRML:restriction type="location" inside="SLUB"/>
            </libRML:action>
          </libRML:item>
        </libRML:libRML>
      </mets:mdWrap>
    </mets:rightsMD>
  </mets:amdSec>
</mets:mets>
```

## MODS

### Elemente

In MODS wird der XML-Code im Element `<accessCondition type="LibRML">` eingetragen.

```xml
<mods:mods xmlns:mods="http://www.loc.gov/mods/v3">
  <mods:accessCondition type="LibRML">
    <!--Here, LibRML can be embedded.-->
  </mods:accessCondition>
</mods:mods>
```

`<mods:accessCondition>`

- LibRML wird in das MODS-Element `<mods:accessCondition>` eingetragen.

`<mods:accessCondition type="LibRML>`

- In das MODS-Attribut @type wird immer "LibRML" eingetragen.

### Beispiel

Im folgenden Beispiel wird [Zugang nur innerhalb eines IP-Adressbereichs (z.B. Campusnetz)](../examples/location) angewendet.

```xml
<mods:mods xmlns:mods="http://www.loc.gov/mods/v3">
  <mods:accessCondition type="LibRML">
    <libRML:libRML version="0.4" xmlns:libRML="http://librml.org/schema">
      <libRML:item commercialuse="false">
        <libRML:action type="displaymetadata" permission="true"/>
        <libRML:action type="index" permission="true"/>
        <libRML:action type="archive" permission="true"/>
        <libRML:action type="read" permission="true">
          <libRML:restriction type="location" inside="SLUB"/>
        </libRML:action>
        <libRML:action type="download" permission="true">
          <libRML:restriction type="location" inside="SLUB"/>
        </libRML:action>
        <libRML:action type="print" permission="true">
          <libRML:restriction type="location" inside="SLUB"/>
        </libRML:action>
      </libRML:item>
    </libRML:libRML>
  </mods:accessCondition>
</mods:mods>
```
