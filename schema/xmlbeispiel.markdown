# XML Beispiel

Wie bei dem JSON Beispiel ([hier](json.markdown)), nehmen wir auch für dieses XML Beispiel ein e-Journal das auf dem Creative Common CC-BY-SA Template aufgebaut wird (Namensnennung und „Share Alike“, abgeleitete Werke müssen denselben Bedingungen unterliegen).
Allerdings diesmal allen möglichen zusätzlichen Einschränkungen, wie auch ein Embargo.

{% highlight xml %}

<?xml version="1.0" ?>
<libRML version="0.2">
    <!-- This XML is created using the libRML Python code -->
    <item id="doi:10.1371/journal.pbio.0020447" tenant="http://www.slub-dresden.de" mention="true" sharealike="true" usageguide="https://nutzungshinweis.slub-dresden.de/il-ma/1.0/" template="CCBYSA-V1">
        <action type="displaymetadata" permission="true"/>
        <action type="index" permission="true"/>
        <action type="read" permission="true">
            <restriction type="date" fromdate="2025-02-11"/>
        </action>
        <action type="print" permission="true">
            <restriction type="date" fromdate="2025-02-11"/>
            <restriction type="quality" maxresolution="300"/>
        </action>
        <action type="print" permission="true">
            <restriction type="date" fromdate="2030-02-11"/>
            <restriction type="quality" maxresolution="1200"/>
        </action>
        <action type="lend" permission="true">
            <restriction type="date" fromdate="2025-02-11"/>
            <restriction type="group">
                <group>student</group>
                <group>employee</group>
                <group>kecksesser</group>
            </restriction>
            <restriction type="count" count="3"/>
            <restriction type="concurrent" sessions="5"/>
            <restriction type="location" inside="in" outside="out">
                <subnet>192.168.10.0/24</subnet>
                <subnet>10.8.0.0/16</subnet>
                <machine>aa-bb-cc-dd-ee-ff</machine>
                <machine>11-22-33-44-55-66</machine>
            </restriction>
        </action>
        <action type="download" permission="true">
            <restriction type="commercialuse" noncommercialuse="true"/>
            <restriction type="quality" maxbitrate="256"/>
            <restriction type="date" fromdate="2025-02-11"/>
            <restriction type="parts">
                <part>datei1.jpg</part>
                <part>datei2.jpg</part>
                <part>datei3.jpg</part>
            </restriction>
            <restriction type="watermark" watermarkvalue="Keks Watermark"/>
            <restriction type="duration" duration="432000"/>
        </action>
    </item>
</libRML>

{% endhighlight %}