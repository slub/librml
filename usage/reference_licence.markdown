# Anwendung

LibRML kann aus standardisierten Rechteinformationen, wie zum Beispiel Lizenz- und Rechtehinweise abgeleitet werden, wenn die jeweiligen Systeme (Präsentation, Repositorium, Rechtemanagementsystem, ...) über die notwendige Funktionalität verfügen. Die Rechteinformationen sind in der Regel mit dem URI und/oder der Bezeichnung in den Metadaten der digitalen Objekte beschrieben. Vorteile dieser Anwendung sind unter anderem:

1. Redundante Metadaten werden vermieden, weil zum Beispiel der URI [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/) sowohl für die Anzeige im Katalog, als auch für die Ableitung von LibRML genutzt werden kann.
2. Anpassungen von Schutzfristen oder anderen Beschränkungen rechtlich geschützter digitalen Objekten können in den Systemen angepasst werden, anstatt Metadaten der digitalen Objekte anzupassen. Zum Beispiel, falls das Urheberrecht einmal erst 80 Jahren nach dem Tod der Urheberin/des Urhebers ablaufen sollte.

Jede Einrichtung kann spezifische Elemente oder Felder in den jeweiligen Metadatenstandards nutzen, um die Lizenz- und Rechtehinweise einzutragen und auszuwerten. Es sollten jedoch unter anderem die [Empfehlungen für Rechteinformationen in Metadaten (3.0)](https://wiki.dnb.de/pages/viewpage.action?pageId=217533652) oder andere Empfehlungen/Standards berücksichtigt werden. Einige standardisierte Lizenz- und Rechtehinweise sind bereits mit LibRML beschrieben und unter Vorlagen zur Nachnutzung verfügbar. Auch wenn es sich um beschränkt zugängliche Objekte handelt, sollte die Anwendung vereinheitlicht werden.

Gegebenenfalls werden auch mehrere Rechteinformationen ausgewertet, wie zum Beispiel der Access Status und der Rechtehinweis, um den Zugang zu urheberrechtlich geschützten Objekten korrekt abzuleiten:

1. [Urheberrechtsschutz 1.0 + Open Access
2. Urheberrechtsschutz 1.0 + Restricted Access

Weitere Informationen finden sich unter [Übersicht Abhängigkeiten zwischen den Rechteinformationen](https://wiki.dnb.de/pages/viewpage.action?pageId=212780200).

# Beispiele

## LibRML

Folgende Beispiele zeigen die Auswertung mehrerer Rechteinformationen, um urheberrechtlich geschützte Objekte mit LibRML zu beschreiben.

- [Urheberrechtsschutz + Open Access - LibRML](../examples/copyright_openaccess)
- [Urheberrechtsschutz + Restricted Access - LibRML](../examples/copyright_restrictedaccess)

Es können auch Creative Commons-Lizenzen ausgewertet und mit LibRML beschrieben werden.

- [CC BY 4.0](../tmpl/CCBY4)

## Standardisierte Rechteinformationen in Metadatenstandards

Folgende Beispiele zeigen die Notwendigkeit der standardisierten Erfassung von Rechteinformationen in den jeweiligen Metadatenstandards anhand der Creative Commons-Lizenz CC BY 4.0.

### Dublin Core Metadata Element Set - DCMES

In DCMES wird der URI der standardisierten Rechteinformation in dem folgenden Element eingetragen:

{% highlight XML %}<dc:rights>{% endhighlight %}

{% highlight XML %} <dc:rights>https://creativecommons.org/licenses/by/4.0/</dc:rights> {% endhighlight %}

Siehe: [https://wiki.dnb.de/pages/viewpage.action?pageId=217533660](https://wiki.dnb.de/pages/viewpage.action?pageId=217533660)

### Metadata Encoding and Transmission Standard - METS

In METS wird der URI der standardisierten Rechteinformation in dem folgenden Element eingetragen:

{% highlight XML %}<mets:mdRef xlink:href>{% endhighlight %}

{% highlight XML %}
<mets:amdSec>
  <mets:rightsMD ID="RMD1">
    <mets:mdRef LABEL="CC BY 4.0" xlink:href="https://creativecommons.org/licenses/by/4.0/" LOCTYPE="PURL" MDTYPE="OTHER" OTHERMDTYPE="Creative Commons"/>
  </mets:rightsMD>
</mets:amdSec>
{% endhighlight %}

Siehe: [https://wiki.dnb.de/pages/viewpage.action?pageId=217533670](https://wiki.dnb.de/pages/viewpage.action?pageId=217533670)

### Metadata Object Description Schema - MODS

In MODS wird der URI der standardisierten Rechteinformation in dem folgenden Element eingetragen:

{% highlight XML %}<mods:accessCondition xlink:href>{% endhighlight %}

{% highlight XML %}
<mods:accessCondition type="use and reproduction" xlink:href="https://creativecommons.org/licenses/by/4.0/">
  CC BY 4.0
</mods:accessCondition>
{% endhighlight %}

Siehe: [https://wiki.dnb.de/pages/viewpage.action?pageId=217533671](https://wiki.dnb.de/pages/viewpage.action?pageId=217533671)
