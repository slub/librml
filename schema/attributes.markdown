# Attributes
## Eigenschaften der verschiedenen Einschränkungen

Hier finden sie alle Attributes (sogenannte Eigenschaften) die, die in der LibRML beschrieben Einschränkungen beeinflussen können. 


- Fromdate
    - Ab gegebenem Datum
    - Angabe nach ISO-Standard (YYYY-MM-DD) 

- Todate 
    - Bis gegebenem Datum 
    - Angabe nach ISO-Standard (YYYY-MM-DD)

- Maxresolution 
    - Maximale Auflösung
    - Angabe in DPI

- Maxbitrate
    - Maximale Größe
    - Angabe in Bit

- Count 
    - Anzahl (z.B. für die Anzahl an Ausleihen)
    - Angabe als Zahl - Integer

- Sessions 
    - z.B. im Falle einer Ressource die nicht gleichzeitig auf zwei Rechnern angesehen werden darf
    - Angabe als Zahl - Integer

- Inside 
    - Innerhalb (Wird für Geographische Einschränkungen oder Einschränkungen bezüglich der Einrichtung benutzt)
    - Angabe: "in"

- Outside 
    - Außerhalb (Wird für Geographische Einschränkungen oder Einschränkungen bezüglich der Einrichtung benutzt)
    - Angabe: "out"

    > Im falle der Einschränkung bezüglich einer Einrichtung kann diese z.B. über das Subnet (Eine Gruppierung von IP Adressen die einem Teil des Netzwerks angehören) geschehen wofur das *Restriction Type* **Subnet** benutzt werden kann. 


- Noncommercialuse 
    - Nicht kommerzielle Nutzung
    - Angabe: "true"/"false"

- Commercialuse
    - Kommerzielle Nutzung
    - Angabe: "true"/"false"

- Watermarkvalue 
    - Bezeichnung des Wasserzeichens
    - Das *Watermark* muss an einem spezifischen Ort hinterlegt sein der hier verlinkt ist

- Duration 
    - Dauer
    - Angabe in non-negative Integer (Sekunden)

- Minage 
    - Mindestalter (Wird für Jugendschutz und dergleichen benutzt)
    - Angabe als Zahl - Integer