---
title: LibRML
sidebar: librml
---

# Nutzungsrechte und Lizenzen für Bibliotheken leicht gemacht

## Stand der Rechtebeschreibung in Bibliotheken

Jede e-Ressource ist mit Nutzungsrechten und Lizenzen verbunden. Diese Informationen befinden sich zum Großteil in Vertragsdokumenten, E-Mails oder ausführlichen Lizenztexten. In den Metadaten der e-Ressourcen werden diese Informationen häufig in Freitextfelder übertragen. Im Fall von standardisierten Lizenzen ([CC-Lizenzen](https://de.wikipedia.org/wiki/Creative_Commons#Lizenzen), [Public Domain](https://de.wikipedia.org/wiki/Gemeinfreiheit#Public_Domain)) befindet sich oft nur der Link zum eigentlichen Lizenztext am digitalen Objekt.

Der Bedarf an Automatisierung zur Rechteerfassung sowie der technischen Auswertung von Berechtigungen ist groß, aber bisher existiert kein Standard, der den Anforderungen der bibliothekarischen Praxis gerecht werden konnte.

## LibRML

Aus diesem Grund ist **Library Rights Machine-readable Language** (kurz **LibRML**) entstanden. Rechteauszeichnung mit LibRML sind durch maschinelle Unterstützung einfach zu generieren und weiterzuverarbeiten. LibRML kann in bestehende Metadatensätzen integriert werden oder unabhängig davon verarbeitet werden. Damit eröffnen sich zahlreiche Möglichkeiten in der Automatisierung bibliothekarischer Workflows. LibRML wurde gezielt für die Anforderungen und Bedarfe des bibliothekarischen Sektors entwickelt.

## Was unterscheidet LibRML von anderen Beschreibungssprachen?

Eine Rights Expression Language (REL) oder im Deutschen eine "Sprache zum Ausdruck von Rechten" ist keine neue Erfindung. Standards für die digitale Rechteverwaltung ([ODRL](https://en.wikipedia.org/wiki/ODRL), [MPEG21](https://de.wikipedia.org/wiki/MPEG-21), [PREMIS](https://de.wikipedia.org/wiki/Preservation_Metadata:_Implementation_Strategies) existieren bereits. Sie konnten sich aber in der bibliothekarischen Praxis bisher nicht bewähren. Ansätze aus der Wirtschaft sind oft sehr komplex und zu fein granular strukturiert. Studienprojekte die einfachere Ansätze verfolgen sind hingegen nicht ausgereift und decken nur triviale Szenarien ab. Dieser Umstand führt dazu, dass die maschinelle Auswertung der Nutzung eines digitalen Objekts mit diesen RELs nur sehr aufwändig möglich ist.

Die in der Praxis genutzten Freitextfelder zur Beschreibung von Rechten können eine nahezu beliebige Fülle an Informationen enthalten, die sich in Reihenfolge und Schreibweise zwischen ähnlich lizenzierten Objekten unterscheiden können. Für Menschen ist die Information klar ersichtlich, aber die maschinelle Verarbeitung ist ohne Vereinheitlichung und eineindeutige Informationen nicht möglich.

LibRML schafft eine Brücke zwischen Komplexität und Verständlichkeit. Sie ist einfach genug um von Menschen gelesen zu werden, aber komplex genug um bibliothekarische Anwendungsfälle vollständig abzudecken. Die Feldbelegungen sind [eindeutig spezifiziert](schema/xsdschema.md) und erlauben die maschinelle Weiterverarbeitung.

```javascript
  "type": "read",               <- Lesen
  "permission": true,           <- ist erlaubt
  "restrictions": [             <- mit Einschränkung
    {
      "type": "date",           <- eines Zeitpunkts
      "fromdate": "2035-01-01". <- ab dem 01.01.2035
    },
  ]
```

Auf diesen Seiten finden Sie ausführliche Informationen zum [Konzept](schema/concept.md) auf dem LibRML basiert, zahlreiche [Beispiele aus der Praxis](examples/examples.md) sowie [Templates](tmpl/templates.md) für gebräuchliche Szenarien und [häufig vorkommende Lizenzmodelle](tmpl/beispiele.md).

Sie können mit einem **visuellem Tool**, dem [LibRML-Builder](builder/index.html), die Erstellung von LibRML-JSON-Dateien ausprobieren und sich aus Aktionen und Einschränkungen ein Beispiel zusammen stellen.
