# Transformationen

Für einige Anwendungsfälle kann es nützlich sein eine LibRML-Datei zu transformieren.
Hier werden entsprechende Szenarien und Hilfmittel präsentiert.

## XML nach JSON

Eine gängige Praxis ist es, nicht die XML-Repräsentation des LibRML direkt zu verarbeiten, sondern das entsprechende JSON. Hier ist ein Skript (XSLT 1.0), das diese Transformation durchführt.

{% highlight xml %}
{% include_relative librml.xsl %}
{% endhighlight %}
