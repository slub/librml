# XML Beispiel

Eine urheberrechtsbehaftete e-Ressource der [SLUB Dresden](https://www.slub-dresden.de), die im Rahmen der Digitalisierung die dauerhafte Speicherung, Ablage in Datenbanken, und dem öffentlicher Zugriff erlaubt. Davon ausgenommen ist die Nutzung zu kommerziellen Zwecken. **Nicht erlaubt** ist das herunterladen, ausdrucken, vervielfältigen, bearbeiten, wiederverwenden und veröffentlichen der e-Ressource.

{% highlight xml %}

<?xml version="1.0" ?>
<libRML version="0.3">
    <!-- This XML is created using the LibRML Python code -->
    <item id="DE-611-HS-3665348" tenant="http://www.slub-dresden.de" copyright="true">
        <action type="displaymetadata" permission="true"/>
        <action type="index" permission="true"/>
        <action type="read" permission="true"/>
        <action type="distribute" permission="true">
            <restriction type="commercialuse" noncommercialuse="true"/>
        </action>
        <action type="archive" permission="true"/>
        <action type="move" permission="true">
            <restriction type="commercialuse" noncommercialuse="true"/>
        </action>
    </item>
</libRML>

{% endhighlight %}
