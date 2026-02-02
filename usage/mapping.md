# Mapping Rechtehinweise und Nutzungshinweise zu LibRML

## Beispiel 1: Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht 1.0

### Menschenlesbare Rechteinformationen

```xml
<mods:mods>
    <mods:accessCondition type="use and reproduction" xlink:href="https://creativecommons.org/publicdomain/mark/1.0/">Public Domain Mark 1.0</mods:accessCondition>
    <mods:accessCondition type="local terms of use" xlink:href="https://nutzungshinweis.slub-dresden.de/ez-am-pr/1-0/">Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht 1.0</mods:accessCondition>
    <mods:accessCondition type="restriction on access" xlink:href="http://purl.org/coar/access_right/c_16ec" displayLabel="Access Status">Restricted Access</mods:accessCondition>
</mods:mods>
```

### Mapping-Regeln

Prüfung: MODS enthält in den dafür vorgesehenen und konfigurierten Elementen folgende Werte

- `./mods:accessCondition[@type="use and reproduction"]/@xlink:href` contains `creativecommons.org/publicdomain/mark/1.0`
- AND
- `./mods:accessCondition[@type="local terms of use"]/@xlink:href` contains `nutzungshinweis.slub-dresden.de/ez-am-pr/1-0`
- AND
- `./mods:accessCondition[@type="restriction on access"]/@xlink:href` contains `purl.org/coar/access_right/c_16ec`

### Maschinenlesbare Rechteinformationen

Ist die Prüfung positiv, werden die zugehörigen gültigen Beschränkungen im LibRML-Code ausgewählt und in der METS-Datei ergänzt.

```xml
<libRML:libRML xmlns:libRML="http://librml.org/schema">
    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am-pr/1-0">
        <libRML:action type="displaymetadata" permission="true"/>
        <libRML:action type="index" permission="true"/>
        <libRML:action type="read" permission="true">
            <libRML:restriction type="location" inside="Lesesaal(Sammlungen)"/>
        </libRML:action>
    </libRML:item>
</libRML:libRML>
```

## Beispiel 2: Eingeschränkter Zugang - Arbeitsplätze Mediathek 1.0

### Menschenlesbare Rechteinformationen

```xml
<mods:mods>
    <mods:accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/InC/1.0/">Urheberrechtsschutz 1.0</mods:accessCondition>
    <mods:accessCondition type="local terms of use" xlink:href="https://nutzungshinweis.slub-dresden.de/ez-am/1.0/">Eingeschränkter Zugang - Arbeitsplätze Mediathek 1.0</mods:accessCondition>
    <mods:accessCondition type="restriction on access" xlink:href="http://purl.org/coar/access_right/c_16ec" displayLabel="Access Status">Restricted Access</mods:accessCondition>
</mods:mods>
```

### Mapping-Regeln

Prüfung: MODS enthält in den dafür vorgesehenen und konfigurierten Elementen folgende Werte

- `./mods:accessCondition[@type="use and reproduction"]/@xlink:href` contains `rightsstatements.org/vocab/InC/1.0`
- AND
- `./mods:accessCondition[@type="local terms of use"]/@xlink:href` contains `nutzungshinweis.slub-dresden.de/ez-am/1.0`
- AND
- `./mods:accessCondition[@type="restriction on access"]/@xlink:href` contains `purl.org/coar/access_right/c_16ec`

### Maschinenlesbare Rechteinformationen

Ist die Prüfung positiv, werden die zugehörigen gültigen Beschränkungen im LibRML-Code ausgewählt und in der METS-Datei ergänzt.

```xml
<libRML:libRML xmlns:libRML="http://librml.org/schema">
    <libRML:item usageguide="https://nutzungshinweis.slub-dresden.de/ez-am/1.0/">
        <libRML:action type="displaymetadata" permission="true"/>
        <libRML:action type="index" permission="true"/>
        <libRML:action type="read" permission="true">
            <libRML:restriction type="location" inside="SLUB-Arbeitsplätze"/>
        </libRML:action>
    </libRML:item>
</libRML:libRML>
```

## Beispiel 3: Public Domain Mark 1.0 + Open Access

### Menschenlesbare Rechteinformationen

```xml
<mods:mods>
    <mods:accessCondition type="use and reproduction" xlink:href="http://creativecommons.org/publicdomain/mark/1.0/">Public Domain Mark 1.0</mods:accessCondition>
    <mods:accessCondition type="restriction on access" xlink:href="http://purl.org/coar/access_right/c_abf2" displayLabel="Access Status">Open Access</mods:accessCondition>
</mods:mods>
```

### Mapping-Regeln

Prüfung: MODS enthält in den dafür vorgesehenen und konfigurierten Elementen folgende Werte

- `./mods:accessCondition[@type="use and reproduction"]/@xlink:href` contains `creativecommons.org/publicdomain/mark/1.0`
- AND
- `./mods:accessCondition[@type="restriction on access"]/@xlink:href` contains `purl.org/coar/access_right/c_abf2`

### Maschinenlesbare Rechteinformationen

Ist die Prüfung positiv, werden die zugehörigen gültigen Beschränkungen im LibRML-Code ausgewählt und in der METS-Datei ergänzt.

```xml
<libRML:libRML xmlns:libRML="http://librml.org/schema">
    <libRML:item usageguide="https://creativecommons.org/publicdomain/mark/1.0/">
        <libRML:action type="displaymetadata" permission="true"/>
        <libRML:action type="download" permission="true"/>
        <libRML:action type="index" permission="true"/>
        <libRML:action type="publish" permission="true"/>
        <libRML:action type="read" permission="true"/>
    </libRML:item>
</libRML:libRML>
```

**ACHTUNG**: In den LibRML-Vorlagen wird PDM 1.0 derzeit mit allen in LibRML verfügbaren Nutzungsarten beschrieben (https://librml.org/templates/PDMark1.html).
