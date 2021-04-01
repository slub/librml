# API

Im Rahmen des Projektes ist geplant, eine API zu entwickeln die LibRML-Objekte erzeugt, validiert und konvertiert. Im Moment gibt es Python-Code der die Objekte als JSON oder XML einlesen kann, als JSON oder XML ausgeben kann und der ein LibRML-Objekt bereitstellt, welches über entsprechende Methoden Manipulationen an den Daten zulässt. Geplant ist, dass dieser Code um Funktionen erweitert wird, die die Objekte validieren, also Widersprüche und Fehler die **technisch** gegen das Schema verstoßen findet und anzeigt. Für Fehler **logischer** Art, also gegensätzliche Restrictions oder Kombinationen aus Restrictions wird dieser Validator nicht vorgehen.

Die API wird zudem Methoden enthalten, die eine **Auswertung** der in der LibRML festgehaltenen Regeln durchführt und für ein gegebenes Objekt und einen gegebenen Kontext eine Aussage über eine Aktion treffen wird, die als Ergebnis *true* der *false* liefert. Diese Methoden erlauben eine Abfrage in der Art:

> Kann das Objekt mit der ID: _123_ zum Zeitpunkt: _jetzt_ angezeigt werden, wenn der Fragende der Gruppe: _Staff_ angehört und sich im _Campus_ befindet.
>
>> TRUE

Für die Speicherung kommt Elasticsearch in Betracht oder eine andere Datenbank, die JSON-Objekte speichern kann. Es ist geplant, dass die API auch Funktionen enthält, die eine Suche und Auflistung von Objekten in einem Kontext mit zulässigen Aktionen liefert.