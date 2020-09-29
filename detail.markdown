# libRML
## Im Detail

LibRML (Library Rights Machine-readable Language) ist eine Rights Expression Language, also eine Sprache zur Formulierung von Rechten, hier im besonderen zur Formulierung von Nutzungsrechten im bibliothekarischen Bereich. 

Nutzungsrechte sollen hier zum einen Maschinen-interpretierbar, sprich durchsetzbar, sein und zum anderen auch für den Menschen lesbar. Auch im Katalog, soll der Nutzer letztendlich erfahren können was er mit der gesuchten Ressource machen darf oder nicht. 

Durchsetzbar soll hier bedeuten das jede Einschränkung die eine von Maschinen verhinderbaren Aktion betrifft auch so durchgesetzt wird. Beispiele wären ein Embargo, ein Limit in der Auflösung eines Bildes, ausschließliche Nutzung auf einem Rechner oder in einer Einrichtung, Zugangsverweigerung unter einem gegebenen Alter des Nutzers, usw. Sogenannte "Grauzonen" wie Unklarheiten bei den Rechtslagen oder Ungewissheit bezüglich des Urheberrechts können (noch) nicht von Maschinen geklärt werden. Die libRML wird allerdings als Werkzeug dienen können für allerlei geklärten Nutzungsrechten in unterschiedlichen Abteilungen der Bibliothek, sei es für Zeitschriften, eBooks oder Fotos. 



Konkreteres:

Zur Verknüpfung der libRML mit dem bearbeiteten Objekt, wird eine ID verwendet. Der folgen mehrere Grundinformationen wie der Inhaber der jeweiligen Rechte und Lizenzen sowie wichtige Haupteinschränkungen bezüglich der Namensnennung (Urheberrecht) oder weiter Verteilung unter gleichen Bedingungen und des Weiteren Benennung des Rechte/Lizenzen Typs und eventueller URL zur textuellen Beschreibung der gegebenen Nutzungsrechte.

Nach diesem „Header“, werden in der libRML die verschiedenen „Actions“ also die möglichen Arten der Nutzung beschrieben, mit ggf. ihren verschiedenen Einschränkungen.

Hier eine Liste der verschiedenen Actions: [Actions](schema/actions.markdown) (Nutzungsrechte)

Praktisch jede dieser Actions kann einer oder mehrerer Einschränkungen unterliegen. Hier eine Liste der in der libRML vorgesehenen Einschränkungen (oder im Englischen „Constraints“): [Constraints](schema/constraints.markdown)



Nicht jede dieser Einschränkungen kann für jede Art der Nutzung verwendet werden da gewisse Kombinationen keinen Sinn ergeben würden. Daher sind in der libRML für jede „Action“ die möglichen (und nur jene) „Constraints“ schon vorgesehen.

Generell gilt für das Beschreiben von Nutzungsrechte in libRML: was nicht Beschrieben ist, ist untersagt. Also sind nur die Nutzungen möglich die auch explizit bei der Beschreibung vorgesehen werden. Befindet sich zum Beispiel keine „print“ Action in der Rechtebeschreibung darf das Dokument auch nicht gedruckt werden.

Des Weiteren wird die libRML so gebaut das sie in bereits existierenden Metadaten Paketen die Rechteinformationen herausfiltert. Es wurden schon Templates für Creative Commons hergestellt aber auch eine Wiedererkennung von Links zu dieser Art der Nutzungsrechte damit diese in bereits beschriebenen Daten wiedererkannt und interpretiert werden kann. Dasselbe wurde für mögliche ODRL Beschreibungen getan und wird für Hausinterner Nutzungsrechte aufgebaut.

libRML wurde so Konzipiert das für alle betroffenen Actions auch Embargos vorgesehen werden können. Somit können einzelne Nutzungsarten bei Beschreibung nach vorgegebenen Rechten erst ab gegebenem Datum automatisch freigeschaltet werden. 



Technischeres:

In der Version 0.2 der LibRML an der wir gerade arbeiten werden die Nutzungsrechte nach Actions organisiert.

 Allgemein gilt die Regel „Was nicht in der LibRML steht, ist untersagt“. In anderen Worten, Actions die nicht beschrieben werden sind jene die nicht vom Nutzer oder der Bibliothek ausgeführt werden dürfen. Zum Beispiel würde man für eine Ressource die nicht gedruckt werden darf die Action „Print“ weglassen.

Zuerst bekommt die beschriebene eRessource „Attributes“. Damit wird diese Ressource dank einem ID identifiziert und es kann definiert werden von welcher Einrichtung sie verwaltet wird (tenant), der Name der eventuell benutzten „Template“ und die URL auf der sich die Richtlinien der dazu gehörigen Lizenz befinden (usageguide). Dann befinden sich in den Attributen noch zwei eventuelle generelle Einschränkungen: die Namensnennung (mention) und der Verpflichtung alle Derivate der Ressource unter denselben Bedingungen zu veröffentlichen (sharealike).

Erst danach werden die jeweiligen Actions mit ihren Constraints (Einschränkungen) beschrieben. Actions haben wiederum auch Attributen. Es wird erst der Typ benannt, dann die Genehmigung (hier „Permission“) eingeschaltet (also auf „true“ geschaltet). Zur Erinnerung, es werden in der LibRML keine Genehmigungen schriftlich ausgeschaltet (also auf „False“) da jene Actions die nicht genehmigt sind, weggelassen werden.

Dann erst werden eventuelle Einschränkungen beschrieben. Diese haben wieder Typ und True/False Schalter und wieder wird das „False“ nicht explizit benutzt, sondern die Einschränkung weggelassen, wenn diese nicht benutzt wird.

Zu den Einschränkungen gehören dann in manchen Fällen eine ganze Serie an Attributen. Diese Attribute sind von einer Einschränkung zur anderen relativ verschieden. Und selbst Einschränkungen die im Text ähnlich klingen könnten wie „von… bis…“ sind im gegebenen Kontext sehr verschieden.


Daher hier noch eine Liste diese Attribute für Einschränkungen:

Fromdate / Ab gegebenem Datum (Wird für Embargos und Zeiteinschränkungen benutzt)

Todate / Bis gegebenem Datum (Wird für Zeiteinschränkungen benutzt)

Maxresolution / Maximale Auflösung

Maxbitrate / Maximale Größe

Count / Anzahl (z.B. für die Anzahl an Ausleihen)

Sessions / Sessions (z.B. im Falle einer Ressource die nicht gleichzeitig auf zwei Rechnern angesehen werden darf)

Inside / Innerhalb (Wird für Geographische Einschränkungen oder Einschränkungen bezüglich der Einrichtung benutzt)

Outside / Außerhalb (Wird für Geographische Einschränkungen oder Einschränkungen bezüglich der Einrichtung benutzt)

Noncommercialuse / Nicht kommerzielle Nutzung

Commercialuse / Kommerzielle Nutzung

Watermarkvalue / Watermark, bzw. wo dieser Watermark zu finden ist

Duration / Dauer

Minage / Mindestalter (Wird für Jugendschutz und dergleichen benutzt)

Es wurden bereits diverse [Templates](tmpl/templates.markdown) für allgemein bekannte Lizenzen wie zum Beispiel die Creative Commons Lizenzen erstellt die die Beschreibung der dazu gehörigen Nutzungsrechte vereinfachen werden. Die LibRML wurde auch so konzipiert das bereits in Metadaten bestehenden Rechtebeschreibungen, wie einfache Verlinkungen zu CC Beschreibungen aber auch komplexere Beschreibungen wie auch die Nutzung von ODRL, gelesen und ins LibRML übersetzt werden können.
