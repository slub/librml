# libRML
## Im Detail

LibRML (Library Rights Machine-readable Language) ist eine [Rights Expression Language](rel.markdown), also eine Sprache zur Formulierung von Rechten, hier im besonderen zur Formulierung von Nutzungsrechten im bibliothekarischen Bereich. 

Nutzungsrechte sollen in Zukumpft Maschinen-interpretierbar und durchsetzbar sein aber trotzdem für den Menschen lesbar bleiben. Auch im Katalog, soll der Nutzer letztendlich erfahren können was er mit der gesuchten Ressource machen darf oder nicht. 

Dies ist die Aufgabe der libRML. 

Was bedeutet jedoch "durchsetzbar"? Es bedeutet dass jede Einschränkung die eine von Maschinen verhinderbare Nutzung (hier Action) betrifft auch so durchgesetzt wird. 

Beispiele wären: ein Embargo, ein Limit in der Auflösung eines Bildes, ausschließliche Nutzung auf einem Rechner oder in einer Einrichtung, Zugangsverweigerung unter einem gegebenen Alter des Nutzers, usw. 


Konkret funkzioniert es so:

Zur Verknüpfung der libRML mit dem bearbeiteten Objekt, wird eine ID verwendet. Der folgen mehrere Grundinformationen wie der Inhaber der jeweiligen Rechte und Lizenzen sowie wichtige Haupteinschränkungen bezüglich der Namensnennung (Urheberrecht) oder weiter Verteilung unter gleichen Bedingungen und des Weiteren Benennung des Rechte/Lizenzen Typs und eventueller URL zur textuellen Beschreibung der gegebenen Nutzungsrechte.


Nach diesem „Header“ werden in der libRML die verschiedenen „Actions“, also die möglichen Arten der Nutzung, beschrieben mit ggf. ihren verschiedenen Einschränkungen.

Hier eine Liste der verschiedenen Actions: [Actions](schema/actions.markdown) (Nutzungsrechte)

Praktisch jede dieser Actions kann einer oder mehreren Einschränkungen unterliegen. Hier eine Liste der in der libRML vorgesehenen Einschränkungen (oder im Englischen „Constraints“): [Constraints](schema/constraints.markdown)


Nicht jede dieser Einschränkungen kann für jede Art der Nutzung verwendet werden da gewisse Kombinationen keinen Sinn ergeben würden. Daher sind in der libRML für jede „Action“ die möglichen (und nur jene) „Constraints“ schon vorgesehen.

Allgemein gilt dazu noch die Regel „Was nicht in der LibRML steht, ist untersagt“. In anderen Worten, nur Nutzungen die explizit bei der Beschreibung vorgesehen werden sind erlaubt und Nutzungen die nicht beschrieben werden dürfen nicht vom Nutzer oder der Bibliothek ausgeführt werden. Befindet sich zum Beispiel keine „print“ Action in der Rechtebeschreibung darf das Dokument auch nicht gedruckt werden.

Für alle betroffenen Actions sollen auch Embargos vorgesehen werden können. Somit können einzelne Nutzungsarten bei Beschreibung nach vorgegebenen Rechten erst ab gegebenem Datum automatisch freigeschaltet werden. 


Für allgemein bekannte und häufig benutze Lizenzen wie zum Beispiel Creative Commons, wurden Templates hergestellt die die Beschreibung der dazu gehörigen Nutzungsrechte vereinfachen werden. Weiteres zu den Templates sowie Beispiele dazu finden sie [hier](tmpl/templates.markdown).

Des Weiteren wird die libRML so gebaut das sie in bereits existierenden Metadaten Paketen die Rechteinformationen herausfiltert. Eine Wiedererkennung von Links zu dieser Art der Nutzungsrechte wurde bedacht damit diese in bereits beschriebenen Daten wiedererkannt und interpretiert werden kann. Dasselbe wurde für mögliche ODRL Beschreibungen getan und wird für Hausinterner Nutzungsrechte aufgebaut.

Sogenannte "Grauzonen" wie Unklarheiten bei den Rechtslagen oder Ungewissheit bezüglich des Urheberrechts können (noch) nicht von Maschinen geklärt werden. Die libRML wird allerdings als Werkzeug dienen können für allerlei geklärte Nutzungsrechte in unterschiedlichen Abteilungen der Bibliothek, sei es für Zeitschriften, eBooks oder Fotos. 

Wer sich näher mit dem Thema befassen möchte kann sich gerne [hier](schema/schema.markdown) Schemas, Beispiele und andere Details anschauen oder gar [hier](api/api.markdown) mit python code und API beschäftigen. 