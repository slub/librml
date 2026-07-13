# Authentifizierung

Zugang und Nutzung nur nach Authentifizierung. In LibRML wird dies durch Zugehörigkeit zu einer Gruppe beschrieben.

**Uneingeschränkte Nutzungsarten**:

- displaymetadata (Anzeigen der Metadaten)
- archive (Archivieren)

**Eingeschränkte Nutzungsarten**:

- index (Indexnutzung)
- read (Lesen)
- download (Herunterladen)
- print (Ausdrucken)

**Art der Einschränkung**:

- group (Gruppe)

{% highlight xml %}
{% include_relative authentification.xml %}
{% endhighlight %}

{% highlight json %}
{% include_relative authentification.json %}
{% endhighlight %}
