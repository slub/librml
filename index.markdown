---
title: LibRML
sidebar: librml
---
# LibRML
## Nutzungsrechte und Lizenzen für Bibliotheken leicht gemacht

### Status Quo

Jede e-Ressource ist mit Nutzungsrechten und Lizenzen verbunden. Diese Informationen befinden sich zum Großteil in Vertragsdokumenten, E-Mails oder ausführlichen  Lizenztexten. In den Metadaten der e-Ressourcen werden diese Informationen häufig in Freitextfelder übertragen. Im Fall von standardisierten Lizenzen (CC-Lizenzen, Public Domain) befindet sich oft nur der Link zum eigentlichen Lizenztext am digitalen Objekt.

Dieser Umstand führt dazu, dass die maschinelle Auswertung der Nutzung eines digitalen Objekts nicht möglich ist. Freitextfelder können eine nahezu beliebige Fülle an Informationen enthalten, die sich in Reihenfolge und Schreibweise zwischen ähnlich lizenzierten Objekten unterscheiden kann. Die maschinelle Verarbeitung ist ohne Vereinheitlichung und eineindeutige Informationen nicht gegeben.

Standards für digitale Rechteverwaltung (ODRL, MPEG21, PREMIS) existieren bereits. Sie konnten sich aber in der bibliothekarischen Praxis bisher nicht bewähren. Ansätze aus der Wirtschaft sind oft sehr komplex und zu fein granular strukturiert. Studienprojekte die einfachere Ansätze verfolgen sind hingegen nicht ausgereift und decken nur triviale Szenarien ab.

Der Bedarf an Automatisierung zur Rechteerfassung sowie der technischen Auswertung von Berechtigungen ist groß, aber bisher existiert kein Standard der den Anforderungen der bibliothekarischen Praxis gerecht werden konnte.

### LibRML

Aus diesem Grund wurde die **Library Rights Machine-readable Language** (kurz **LibRML**) entwickelt. Als [Beschreibungssprache](rel.markdown)für den bibliothekarischen Sektor wird eine Brücke zwischen Komplexität und Verständlichkeit geschaffen. LibRML ist einfach genug um von Menschen gelesen zu werden, aber komplex genug um bibliothekarische Anwendungsfälle vollständig abzudecken.

<img src="{{site.baseurl}}/assets/images/librml1.png" alt="LibRML Teaser" class="center">

Rechteauszeichnung mit LibRML sind durch maschinelle Unterstützung einfach zu generieren und weiterzuverarbeiten und eröffnen so zahlreiche neue Möglichkeiten in der Automatisierung bibliothekarischer Workflows.

Mehr Informationen befinden [zum Konzept] von LibRML enthält geplante Nutzungsmöglichkeiten und Einschränkungen sowie JSON und XML Beispiele:

- [Rights Expression Language](rel.markdown)
- [Konzept hinter LibRML](schema/concept.markdown)
- [Vorlagen für häufig verwendete Lizenzen](tmpl/templates.markdown)

## FAQ

- [Häufig gestellte Fragen für Nutzer (FAQ)](allgfaq.markdown)
- [Häufig gestellte Fragen zum technischen Hintergrund](techfaq.markdown)
