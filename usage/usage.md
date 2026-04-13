# Anwendung

## Allgemeine Informationen

LibRML kann flexibel und den jeweiligen Anforderungen entsprechend angewendet werden. Im Folgenden werden drei Möglichkeiten der Anwendung vorgestellt:

1. Referenzierung Lizenz- und Rechtehinweise
1. Referenzierung LibRML-Beschreibung
1. Eingebettetes LibRML in der Metadatendatei

## Referenzierung Lizenz- und Rechtehinweise

Es werden standardisierte Lizenz- und Rechtehinweise genutzt, die bereits in spezifischen Elementen des verwendeten Metadatenstandards (zum Beispiel METS, MODS) eingetragen sind. Die Informationen werden von einem System (Präsentation, Repositorium, Rechtemanagementsystem) ausgewertet und in LibRML übersetzt. 
Dadurch wird eine redundante Erfassung der Rechteinformationen in den Metadaten vermieden.

Siehe [Referenzen standardisierter Rechteinformationen](reference_licence)

## Referenzierung LibRML-Beschreibung

Es werden externe LibRML-Beschreibungen mittels URI in der Metadatendatei des digitalen Objekts referenziert. Die Informationen werden von einem System (Präsentation, Repositorium, Rechtemanagementsystem) über diesen URI aufgelöst und ausgewertet. 
Dadurch sind Anpassungen der LibRML-Beschreibung nur in der externen Quelle notwendig und müssen nicht in den einzelnen Metadatendateien der digitalen Objekte vorgenommen werden. 

Siehe [Referenzen standardisierter Beschränkungen](reference_usage)

## Eingebettetes LibRML in der Metadatendatei

Es werden LibRML-Beschreibungen direkt in die Metadatendatei des digitalen Objekts eingebettet. Die Informationen werden von einem System (Präsentation, Repositorium, Rechtemanagementsystem, …) unmittelbar ausgewertet.
Dies ermöglicht eine direkte Verarbeitung des LibRML-Codes ohne Abhängigkeiten von externen Quellen oder Mappings.

Siehe [Eingebettetes LibRML in den Metadaten](embedded)
