# Templates
## Erstellung von Templates und Beispiele


Aus der LibRML-Definition ergibt sich, dass eine Einschränkung immer wieder auf Aktionen angewendet wird und somit wohl vielfach wiederholt wird. Dies bedingt, dass ein schlaues Template-System gefunden werden muss. Nach einigen Versuchen kamen wir zu dem Entschluss, das in Python eingebaute Jinja2 System zu nutzen und um dieses nicht zu beschädigen oder erweitern zu müssen eine zusätzliche Datei mit Meta-Informationen zu dem Template zu speichern.

Ein Template mit dem aktuellen Stand besteht also aus 2 Dateien:

librml-tmpl-CustomType2.jinja

librml-tmpl-CustomType2.meta.json

Es gibt einen Basisnamen "librml-tmpl-CustomType2" und jeweils die Endung "jinja" und "meta.json". Die Konstruktion ist (im Moment) wichtig, weil die Templates nur geladen werden wenn sie die Endung jinja haben und aus dem Dateinamen der Name der Metainfo-Datei erzeugt wird.

Der Inhalt ist ein valides Jinja2-Template:


{% highlight jinja %}

{
  "template": "Group-Embargo",
  "actions": [
    {
      "type": "displaymetadata",
      "permission": true
    },
    {
      "type": "index",
      "permission": true
    },
    {
      "type": "read",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
      ]
    },
    {
      "type": "download",
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "print",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "reproduce",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "modify",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "reuse",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "distribute",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "publish",
      "permission": true,
      "restrictions": [
        {
          "type": "date",
          "fromdate": "{{embargodate}}"
        },
        {
           "type": "group",
           "groups": [{% for group in groups %}"{{ group }}",{% endfor %}]
         }
       ]
    },
    {
      "type": "archive",
      "permission": true
    },
    {
      "type": "move",
      "permission": true
    }
  ]
}

{% endhighlight %}

Und ein valides JSON:

{% highlight javascript %}

{
  "name": "Embargo und Nutzergruppen",
  "description": "Hier ist ein Datum und eine Nutzergruppe.",
  "author": "tbaer",
  "variables": [
    {
      "name": "embargodate",
      "datatype": "date",
      "readablename": "Embargo Ablauf",
      "description": "Das Datum, zu dem das Embargo fällt"
    },
    {
      "name": "groups",
      "datatype": "list",
      "readablename": "Zulässige Nutzergruppen",
      "description": "Die Liste der zugelassenen Nutzergruppen",
      "source": "usergroups"
    }
  ]
}

{% endhighlight %}


Man sieht, es gibt nur 2 Variablen, aber diese jeweils viele Male. In den Metainformationen zum Template ist beschrieben, welchen Datentyp die Variablen haben und ggf. eine Datenquelle (zum Beispiel für anderweitig gepflegte Listen) und außerdem Informationen die eine GUI braucht, um für die Variablen sinnvolle Elemente zu erzeugen. Also ein Datumwähler mit einem lesbaren Namen und einer Beschreibung.

Mit Jinja sind viele und gute Möglichkeiten gegeben, die ausreichend dokumentiert sind: https://jinja.palletsprojects.com/en/2.11.x/templates/#

Der Programmcode zieht aus dem Template die Variablen und liest deren Metainformationen aus der Zusatzdatei. Dies ist nur relevant, wenn man das in einer GUI verarbeitet. Im Programmcode kennt man die Variablen und übergibt sie:

{% highlight javascript %}
obj = LibRML.from_template(templateid='CC0-Embargo',
                           itemid='blafasel-id',
                           tenant='slubdd',
                           embargodate=date.fromisoformat('2021-01-01'),
                           groups=['group1', 'group2'])
{% endhighlight %}



Hier eine Liste der bereits erstellten Beispiele dank Templates und ihrer Beschreibungen.
Diese Liste dient der Vereinfachung der Nachprüfung. Sie wird mit der Zeit wachsen. 


Creative Commons


[CC0: Creative Commons Kein Urheberrecht / Public Domain](CC0.markdown)

[CC BY 4.0: Creative Commons mit Namensnennung](CCBY4.markdown)

[CC BY-SA 4.0: Creative Commons mit Namensnennung und „Share Alike“ (Abgeleitete Werke müssen denselben Bedingungen unterliegen)](CCBYSA4.markdown) 

[CC BY-ND 4.0: Creative Commons mit Namensnennung und keine Veränderungen/Ableitungen](CCBYND4.markdown)

[CC BY-NC 4.0: Creative Commons mit Namensnennung und nicht kommerziell](CCBYNC4.markdown)

[CC BY-NC-SA 4.0: Creative Commons mit Namensnennung, nicht kommerziell und „Share Alike“ (Abgeleitete Werke müssen denselben Bedingungen unterliegen)](CCBYNCSA4.markdown) 

[CC BY-NC-ND 4.0: Creative Commons mit Namensnennung, nicht kommerziell und keine Veränderungen/Ableitungen](CCBYNCND4.markdown)

[CC BY 3.0 DE: Creative Commons mit Namensnennung - Deutschland](CCBY3DE.markdown)

[CC BY-SA 3.0 DE: Creative Commons mit Namensnennung und „Share Alike“ (Abgeleitete Werke müssen denselben Bedingungen unterliegen) - Deutschland](CCBYSA3DE.markdown)

[CC BY-ND 3.0 DE: Creative Commons mit Namensnennung und keine Veränderungen/Ableitungen - Deutschland](CCBYND3DE.markdown)

[CC BY-NC 3.0 DE: Creative Commons mit Namensnennung und nicht kommerziell - Deutschland](CCBYNC3DE.markdown)

[CC BY-NC-SA 3.0 DE: Creative Commons mit Namensnennung, nicht kommerziell und „Share Alike“ (Abgeleitete Werke müssen denselben Bedingungen unterliegen) - Deutschland](CCBYNCSA3DE.markdown)

[CC BY-NC-ND 3.0 DE: Creative Commons mit Namensnennung, nicht kommerziell und keine Veränderungen/Ableitungen - Deutschland](CCBYNCND3DE.markdown)


Datenlizenzen Deutschland


[DL-DE Zero 2.0: Datenlizenz Deutschland Zero 2.0](DLDEzero2.markdown)

[DL-DE-BY 2.0: Datenlizenz Deutschland - Namensnennung 2.0](DLDEBY2.markdown)

[DL-DE-BY 1.0: Datenlizenz Deutschland - Namensnennung 1.0](DLDEBY1.markdown)  

[DL-DE-BY-NC 1.0: Datenlizenz Deutschland - Namensnennung - Nicht kommerziell 1.0](DLDEBYNC1.markdown)

