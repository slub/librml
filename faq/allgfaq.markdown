# Häufig gestellte Fragen aus Anwendersicht

## Wofür steht LibRML?

**Lib**rary **R**ights **M**achine-readable **L**anguage.

## Wozu braucht man diese Beschreibungssprache?

Diese Sprache dient der Beschreibung von Nutzungsrechten für e-Ressourcen in Bibliotheken.

## Für welche Art von Ressourcen ist die LibRML gültig?

Alle Arten von e-Ressourcen einer typischen Bibliothek (Zeitschriften, eBooks, Fotos, Musik...).

## Kann ich mit der LibRML auch Nutzungsrechte für analoge Ressourcen beschreiben?

Wenn Metadaten zu den analogen Medien in den technischen Systemen der Bibliothek hinterlegt sind und es klare Angaben zu Nutzungsrechten gibt, lassen sich auch analoge Ressourcen mit LibRML zu beschreiben.

## Wer kann/darf die LibRML benutzen?

Jeder der mit der Verknüpfung von Rechteinformationen und Metadaten arbeiten z. B. (System-)Bibliothekare, Verlage, Datenmanager und viele weitere.

## Funktioniert LibRML auch für komplette Ressourcen-Pakete?

Solange ein Paket mit einer eindeutigen ID für alle inbegriffenen Ressourcen verknüpfbar ist, kann LibRML auch für Pakete benutzt werden.

## Wie gehe ich damit um, wenn die Lizenz-/Nutzungsrechte nicht in den Metadaten, sondern anderweitig zu finden sind?

Wenn keine eineindeutige Lizenz aus den Metadaten abzuleiten ist (CC-BY, Public Domain, …) dann muss eine LibRML Beschreibung (mit maschineller Unterstützung) erstellt werden.

## Welche Lizenzen sind schon als Vorlagen vorhanden?

Creative Commons und andere Datenlizenzen für Deutschland (Siehe [Beispiele](tmpl/beispiele.markdown))

## Was wenn die zutreffenden Einschränkungen noch nicht in der LibRML vorgesehen sind?

Besteht die Anforderung weitere [Actions](schema/actions.markdown), [Attributes](schema/attributes.markdown) oder [Constraints](schema/constraints.markdown) zu ergänzen stehen wir gern zum Austausch bereit.

## Können verschiedene Einschränkungen je nach Nutzungsszenario beschrieben werden?

Ja. Diese müssen dann an dem entsprechenden [Nutzungsrecht](schema/actions.markdown) hinterlegt werden.

## Können Einschränkungen global auf alle Nutzungsszenarien eingestellt werden?

Datum (Embargo), Namensnennung, Share Alike (Abgeleitete Werke müssen denselben Bedingungen unterliegen) können global für die e-Ressource als Einschränkung definiert werden.

## Kann man die in die LibRML eingegebenen Daten später korrigieren?

Ja, analog zu Metadaten können auch die Rechteauszeichnungen durch libRML korrigiert werden.

## An wen kann ich mich wenden, falls ich Fragen habe? Gibt es ein Feld dafür?

Schreiben Sie uns eine <a target="_blank" href="mailto:librml@slub-dresden.de">e-Mail </a> oder nutzen Sie das <a target="_blank" href="https://github.com/slub/librml/issues">Github-Issue-System</a> um an der Diskussion teilzunehmen.

## Wie wird die LibRML mit den restlichen Daten verknüpft?

Durch eine eindeutige ID lassen sich die Rechteinformationen mit den Metadaten der Ressource oder dem Paket maschinell verknüpfen.

## Wie hilft die LibRML dem Bibliotheken-Nutzer?

Durch das Einsetzen einer Menschen- und Maschinenlesbaren Sprache vereinfacht die LibRML das Anzeigen von Nutzungsrechten im Katalog. So kann der Nutzer deutlich über seine Rechte aufgeklärt werden und weiß somit was er mit den gewünschten Ressourcen tun darf oder nicht.

## Welchen Vorteil hat die LibRML auf den Bibliothekskatalog?

Eine bessere Repräsentation der Nutzungsrechte und klare Linien für die Benutzung der Ressourcen für Nutzer und Bibliothekare.

## Wie kann man die Nutzungsrechte einsehen, wenn sie erstmal gespeichert sind?

Die Nutzungsrechte können im Bibliothekskatalog neben den bibliothekarischen Metadaten zur Ressource angezeigt.

## Was wenn 2 (oder mehr) gegensätzliche Bedingungen auftauchen?

Komplexere Rechtesituationen müssen intellektuell gelöst werden. LibRML ist nur in der Lage die von Menschen getroffenen Entscheidungen in maschinen- und menschenlesbarer Form abzubilden und durchsetzbar zu machen.
