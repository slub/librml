---
title: LibRML
sidebar: librml
---

# Rechtebeschreibung und LibRML

## Rechtebeschreibung

Digitale Objekte, die von Kulturerbeeinrichtungen verwaltet werden, können rechtlichen Rahmenbedingungen unterliegen. Deren Nutzung ist dann unter Umständen spezifischen Einschränkungen unterworfen – sei es durch gesetzliche Vorgaben (Schranken des Urheberrechts), vertragliche Vereinbarungen mit Rechteinhabenden oder Lizenzverträge mit kommerziellen Anbietern. Davon ausgenommen sind gemeinfreie Objekte, die nach Ablauf der Schutzfristen frei nutzbar sind. Um Informationen bezüglich des rechtlichen Status, der Zugänglichkeit sowie der Einschränkungen eines digitalen Objekts effizient zu erfassen und zu vermitteln, sollten standardisierte Rechteinformationen angewendet werden.

In Kulturerbeeinrichtungen liegt ein Schwerpunkt derzeit auf der Beschreibung der Objekte mittels [Creative Commons](https://de.creativecommons.net/was-ist-cc/), [Rights Statements](https://rightsstatements.org/) oder den [COAR Access Rights](https://vocabularies.coar-repositories.org/access_rights/). Diese Standards sind weit verbreitet und werden unter anderem von der [Deutschen Digitalen Bibliothek](https://www.deutsche-digitale-bibliothek.de/) und der [Europeana](https://www.europeana.eu/) vorausgesetzt. Sie dienen hauptsächlich dazu, den Nutzenden den rechtlichen Status eines Objekts transparent zu vermitteln.

Für die Beschreibung konkreter technischer Berechtigungen oder Beschränkungen, die sich aus den Rechten, Verträgen oder Lizenzen ergeben, fehlen in Kulturerbeeinrichtungen bisher etablierte Standards, die eine ähnliche Verbreitung wie Rights Statements oder Creative Commons aufweisen.

## LibRML

Die Library Rights Machine-readable Language (LibRML) ist ein Modell zur formalen Beschreibung von Berechtigungen und Beschränkungen für digitale Objekte. Sie ordnet sich in die Gruppe der Rights Expression Languages (REL) wie [ODRL](https://www.w3.org/TR/odrl-model/) oder [MPEG-21](https://de.wikipedia.org/wiki/MPEG-21) ein, weist jedoch eine deutlich geringere Komplexität auf und ist auf Kulturerbeeinrichtungen zugeschnitten. 

Obwohl die Begriffe _**Rights** Expression Languages_ oder _Library **Rights** Machine-readable Language_ das Wort „Rechte“ im Namen tragen, liegt der Fokus der LibRML auf der technischen Abbildung von Berechtigungen, die innerhalb eines Systems maschinell durchgesetzt werden können. 
Während Creative Commons oder Rights Statements den rechtlichen Status oder die Lizenz beschreiben, definiert LibRML die sich daraus ergebenden funktionalen Spielräume (wie zum Beispiel Drucken, Download, Beschränkung auf spezifische Arbeitsplätze, ...). 

Im Rahmen eines [Projekts](https://schutzrechte.hypotheses.org/1261) in der [DFG-Pilotphase](https://schutzrechte.hypotheses.org/) wird das Modell 2025–2027 für retrodigitalisierte Objekte angepasst.
In diesem Zeitraum werden die Inhalte dieser Webseite kontinuierlich ergänzt, unter anderem in [Erweiterungen](https://librml.org/adjustments/adjustments.html).

Auf diesen Seiten finden Sie ausführliche Informationen zum [Konzept](schema/concept.md), auf dem LibRML basiert, [Beispiele aus der Praxis](examples/examples.md) sowie [Vorlagen](tmpl/templates.md).