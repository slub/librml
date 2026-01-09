---
title: LibRML
sidebar: librml
---

# Rechtebeschreibung mit LibRML

## Rechtebeschreibung

Digitale Objekte, die von Kulturerbeeinrichtungen verwaltet werden, sind in der Regel rechtlich geschützt und deren Nutzung durch unterschiedliche Gründe beeinflusst.
Unter anderem durch Gesetze (Schranken des Urheberrechts), vertragliche Abstimmungen mit den Rechteinhabenden oder Lizenzverträge mit kommerziellen Anbietern.
Ausgenommen sind gemeinfreie Objekte, die nicht (mehr) urheberrechtlich geschützt und frei nutzbar sind.
Die Rechteinformationen der Objekte sollen standardisiert erfasst und verwaltet werden.

In Kulturerbeeinrichtungen ist die Rechtebeschreibung der Objekte von mehreren Anforderungen abhängig. Zum einen von den Anwendungsgebieten, wie zum Beispiel Retrodigitalisierung, Elektronisches Publizieren oder Lizenzierung von kommerziellen Angeboten. Zum anderen von den angewendeten Systemen, wie zum Beispiel Verbundkatalogen, Repositorien, Digitalisierungssoftware, in denen die Rechteinformationen erfasst, verwaltet oder angezeigt werden.

Ein Schwerpunkt der Rechtebeschreibung liegt derzeit in der Beschreibung der Objekte nach [Creative Commons](https://de.creativecommons.net/was-ist-cc/), [Rights Statements](https://rightsstatements.org/), oder den [COAR Access Rights](https://vocabularies.coar-repositories.org/access_rights/). Diese Rechteinformationen sind standardisiert und werden breit angewendet. Unter anderem werden sie von der [Deutschen Digitalen Bibliothek](https://www.deutsche-digitale-bibliothek.de/) und der [Europeana](https://www.europeana.eu/) eingefordert. Diese Rechteinformationen dienen hauptsächlich der Vermittlung der Information an die Nutzenden.

Für die Beschreibung von Beschränkungen werden in Kulturerbeeinrichtungen bisher keine standardisierten Rechteinformationen im Umfang der Creative Commons oder Rights Statements Rechteinformationen angewendet.

## LibRML

Die Library Rights Machine-readable Language (LibRML) ist ein Modell, um Beschränkungen zu beschreiben, die sich aus den Rechten, Verträgen oder Lizenzen ergeben. LibRML ist eine Rights Expression Language (REL) wie zum Beispiel [ODRL](https://www.w3.org/TR/odrl-model/) oder [MPEG-21](https://de.wikipedia.org/wiki/MPEG-21), jedoch von geringerer Komplexität.

Mit LibRML wird die Trennung der Beschreibung der Rechte und der Beschränkungen, die für die Objekte gelten, durchgesetzt. Gründe für die Trennung sind unter anderem, dass die jeweiligen Rechteinformationen:

* unterschiedliche Funktionen erfüllen (Informationen an Nutzende; maschineninterpretierbare Informationen)
* in unterschiedlichen Systemen benötigt werden

LibRML wurde 2019–2021 im Rahmen eines [EFRE-Projekts](https://www.slub-dresden.de/ueber-uns/projekte/infrastruktur-und-softwareentwicklung/zentraler-hosting-service-fuer-eressourcen/) entwickelt. In dieser Entwicklungsphase lag der Fokus auf der Beschreibung lizenzierter Objekte.

Im Rahmen eines [Projekts](https://schutzrechte.hypotheses.org/1261) in der [DFG-Pilotphase](https://schutzrechte.hypotheses.org/) wird das Modell 2025–2027 für retrodigitalisierte Objekte angepasst.
In diesem Zeitraum werden die Inhalte dieser Webseite kontinuierlich angepasst.
Zum Beispiel durch [Beispiele für die Anpassung des Modells](https://librml.org/adjustments/adjustments.html).

Auf diesen Seiten finden Sie ausführliche Informationen zum [Konzept](schema/concept.md), auf dem LibRML basiert, zahlreiche [Beispiele aus der Praxis](examples/examples.md) sowie [Templates](tmpl/templates.md) für gebräuchliche Szenarien und [häufig vorkommende Lizenzmodelle](tmpl/beispiele.md).
