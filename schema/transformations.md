# Transformationen

## XML nach JSON

Im Rahmen des [DFG-Projekts](adjustments.md) wird LibRML im XML-Format bereitgestellt, um eine Integration in METS-Dateien zu ermöglichen.

Sollte anstelle der XML-Repräsentation eine JSON-Repräsentation benötigt werden, kann die Konvertierung über das folgende XSLT-1.0-Skript durchgeführt werden.

{% highlight xml %}
{% include_relative librml.xsl %}
{% endhighlight %}
