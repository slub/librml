# Anwendung

## Allgemeines

Es wird empfohlen, [Referenzen standardisierter Rechteinformationen](reference_licence.md) oder [Referenzen standardisierter Zugriffsbeschränkungen](reference_usage.md) anzuwenden. Wenn keine standardisierten Beschreibungen verfügbar sind, kann LibRML in einen Metadatenstandard eingetragen werden. Im Folgenden wird eine empfohlene Anwendung in METS und MODS beschrieben. Der LibRML-Code wird von den jeweiligen Systemen (Präsentation, Repositorium, Rechtemanagementsystem, ...) ausgewertet.

## METS

### Beispiel

In METS wird der XML-Code im Element `<rightsMD>` eingetragen.

#### METS

```xml
<mets:mets[...]>
  <mets:metsHdr[...]/>
  <mets:amdSec>
    <mets:rightsMD ID="RMD1">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="LibRML">
        <!--Here, LibRML can be embedded.-->
      </mets:mdWrap>
    </mets:rightsMD>
  </mets:amdSec>
</mets:mets>
```

### Elemente

`<mets:rightsMD>`

- LibRML wird in das METS-Element `<mets:rightsMD>` eingetragen.

`<mets:mdWrap>`

- LibRML wird in das METS-Element `<mets:mdWrap>` eingetragen.

`<mets:mdWrap MDTYPE>`

- In das METS-Attribut @MDTYPE wird immer "OTHER" eingetragen.

`<mets:mdWrap OTHERMDTYPE>`

- In das METS-Attribut @OTHERMDTYPE wird immer "LibRML" eingetragen.

### Wiederholbarkeit

Nein.
In der Metadatendatei eines Datensatzes darf nur ein LibRML-Element vorhanden sein.

### Verpflichtungsgrad

Optional.
Es ist jedoch verpflichtend, dass in der Metadatendatei eines Datensatzes eine auswertbare Rechteinformation enthalten ist. Diese kann entweder ausführlich oder als standardisierter URI in einem der jeweils zugelassenen Metadatenstandards enthalten sein.


## MODS

### Beispiel

In MODS wird der XML-Code im Element `<accessCondition type="LibRML">` eingetragen.

#### MODS

```xml
<mods:mods xmlns:mods="http://www.loc.gov/mods/v3">
  <mods:accessCondition type="LibRML">
    <!--Here, LibRML can be embedded.-->
  </mods:accessCondition>
</mods:mods>
```

### Elemente

`<mods:accessCondition>`
- LibRML wird in das MODS-Element `<mods:accessCondition>` eingetragen.

`<mods:accessCondition type="LibRML>`
- In das MODS-Attribut @type wird immer "LibRML" eingetragen.

### Wiederholbarkeit

Nein.
In der Metadatendatei eines Datensatzes darf nur ein LibRML-Element vorhanden sein.

### Verpflichtungsgrad

Optional.
Es ist jedoch verpflichtend, dass in der Metadatendatei eines Datensatzes eine auswertbare Rechteinformation enthalten ist. Diese kann entweder ausführlich oder als standardisierter URI in einem der jeweils zugelassenen Metadatenstandards enthalten sein.

## Beispiele

Die folgenden Beispiele nutzen das LibRML [Zugang nur innerhalb eines IP-Adressbereichs (z.B. Campusnetz)](../examples/location).

### METS

```xml
<mets:mets[...]>
  <mets:metsHdr[...]/>
  <mets:amdSec>
    <mets:rightsMD ID="RMD1">
      <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="LibRML">
        <libRML version="0.3">
            <item id="iprestricted-444" tenant="http://slub-dresden.de" commercialuse="false" template="IP">
            <action type="displaymetadata" permission="true"/>
            <action type="index" permission="true"/>
            <action type="archive" permission="true"/>
            <action type="read" permission="true">
              <restriction type="location" subnet="192.168.10.0/24"/>
            </action>
            <action type="download" permission="true">
              <restriction type="location" subnet="192.168.10.0/24"/>
            </action>
            <action type="print" permission="true">
              <restriction type="location" subnet="192.168.10.0/24"/>
            </action>
          </item>
        </libRML>
      </mets:mdWrap>
    </mets:rightsMD>
  </mets:amdSec>
</mets:mets>
```

### MODS

```xml
<mods:mods xmlns:mods="http://www.loc.gov/mods/v3">
    <mods:accessCondition type="LibRML">
        <libRML version="0.3">
              <item id="iprestricted-444" tenant="http://slub-dresden.de" commercialuse="false" template="IP">
                <action type="displaymetadata" permission="true"/>
                <action type="index" permission="true"/>
                <action type="archive" permission="true"/>
                <action type="read" permission="true">
                    <restriction type="location" subnet="192.168.10.0/24"/>
                </action>
                <action type="download" permission="true">
                    <restriction type="location" subnet="192.168.10.0/24"/>
                </action>
                <action type="print" permission="true">
                    <restriction type="location" subnet="192.168.10.0/24"/>
                </action>
            </item>
        </libRML>
    </mods:accessCondition>
</mods:mods>
```
