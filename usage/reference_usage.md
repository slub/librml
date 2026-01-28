# Anwendung

Es können standardisierte Zugriffs- und Nutzungsbeschränkungen definiert werden, die von den jeweiligen Systemen (Präsentation, Repositorium, Rechtemanagementsystem, ...) umgesetzt werden, insofern sie über die notwendige Funktionalität verfügen. In den Metadaten kann unter anderem die jeweilige URI eingetragen werden, aus der dann die Beschreibung in LibRML abgeleitet wird (siehe ''[Reine Metadatenanzeige](../examples/metadataonly.md)'').

Jede Einrichtung kann spezifische Elemente oder Felder in den jeweiligen Metadatenstandards nutzen, um die Lizenz- und Rechtehinweise einzutragen und auszuwerten. Es sollten jedoch die [Empfehlungen für Rechteinformationen in Metadaten (3.0)](https://wiki.dnb.de/pages/viewpage.action?pageId=217533652) oder andere Empfehlungen/Standards berücksichtigt werden. Einige standardisierte Lizenz- und Rechtehinweise wurden mit LibRML beschrieben und stehen unter [Vorlagen](../tmpl/templates.md) zur Verfügung. Auch wenn die Objekte beschränkt zugänglich sind, sollte deren Beschreibung vereinheitlicht werden.

## Beispiele

Folgende Beispiele zeigen in ausgewählten Metadatenstandards die mögliche Erfassung von standardisierten Beschränkungen.

### Dublin Core Metadata Element Set - DCMES

In DCMES wird der URI der standardisierten Rechteinformation im Element `<dc:rights>` eingetragen:

```xml
<dc:rights>https://librml.org/examples/metadataonly.html</dc:rights>
```

### Metadata Encoding and Transmission Standard - METS

In METS wird der URI der standardisierten Rechteinformation im Element `<mets:mdRef>` eingetragen:

```xml
<mets:amdSec>
  <mets:rightsMD ID="RMD1">
    <mets:mdRef LABEL="Zugang nur zu Metadaten" xlink:href="https://librml.org/examples/metadataonly.html" LOCTYPE="PURL" MDTYPE="OTHER" OTHERMDTYPE="LibRML"/>
  </mets:rightsMD>
</mets:amdSec>
```

### Metadata Object Description Schema - MODS

In MODS wird der URI der standardisierten Rechteinformation im Element `<mods:accessCondition>` eingetragen:

```xml
<mods:accessCondition type="LibRML" xlink:href="https://librml.org/examples/metadataonly.html">
  Zugang nur zu Metadaten
</mods:accessCondition>
```
