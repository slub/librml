# Bestehende Elemente für Retrodigitalisate

## Allgemeine Informationen

Grundlage der Dokumentation ist: [Untersuchung - 02-01 LibRML | Bestehende Elemente für Retrodigitalisate](https://wiki.dnb.de/x/aNgtFw).
Ziel ist unter anderem die Erstellung eines Anwendungsprofils für Retrodigitalisate entsprechend [AP 5 Anpassung LibRML](https://wiki.dnb.de/x/VhmpG).

## Actions

* **archive**
  * **Relevanz:** Nein
  * **Bemerkung:**
  * Dies wird in der SLUB Dresden nicht mit/in Kitodo.Presentation gesteuert und muss nicht mit LibRML beschrieben werden.
* **displaymetadata**
  * **Relevanz:** Ja
  * **Bemerkung:**
    * Metadaten einschließlich der Nutzungshinweise werden in den Digitalen Sammlungen angezeigt, auch wenn die Objekte nicht frei zugänglich sind.
    * Dies betrifft die Listenansicht und Werkansicht.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher.md)
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **distribute**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
    * Dies kann in einem Nutzungshinweis beschrieben werden - insbesondere auch, was nicht erlaubt ist, falls das digitale Objekt heruntergeladen werden kann - wie zum Beispiel in [SLUB VE-WE 1.0](https://nutzungshinweis.slub-dresden.de/ve-we/1.0/) oder [SLUB FO-ZW 1.0](https://nutzungshinweis.slub-dresden.de/fo-zw/1.0/).
* **download**
  * **Relevanz:** Ja
  * **Bemerkung:**
    * Bestimmte Elemente des digitalen Objekts können flexibel heruntergeladen werden, wie zum Beispiel: Dateigruppen, IIIF-Manifeste, METS-Datei.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher.md)
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **index**
  * **Relevanz:** Ja
  * **Bemerkung:**
    * Die Metadaten der digitalen Objekte können gesucht und angezeigt werden.
    * Wenn die Metadaten nicht indexiert werden dürfen, ist eine Aufnahme des digitalen Objekts in die Digitalen Sammlungen nicht notwendig.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher.md)
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **lend**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
    * Dies kann in einem Nutzungshinweis beschrieben werden - insbesondere auch, was nicht erlaubt ist, falls das digitale Objekt heruntergeladen werden kann - wie zum Beispiel in [SLUB VE-WE 1.0](https://nutzungshinweis.slub-dresden.de/ve-we/1.0/) oder [SLUB FO-ZW 1.0](https://nutzungshinweis.slub-dresden.de/fo-zw/1.0/).
* **modify**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
    * Dies kann in einem Nutzungshinweis beschrieben werden - insbesondere auch, was nicht erlaubt ist, falls das digitale Objekt heruntergeladen werden kann - wie zum Beispiel in [SLUB VE-WE 1.0](https://nutzungshinweis.slub-dresden.de/ve-we/1.0/) oder [SLUB FO-ZW 1.0](https://nutzungshinweis.slub-dresden.de/fo-zw/1.0/).
* **move**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
* **print**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
    * Dies kann in einem Nutzungshinweis beschrieben werden - insbesondere auch, was nicht erlaubt ist, falls das digitale Objekt heruntergeladen werden kann - wie zum Beispiel in [SLUB VE-WE 1.0](https://nutzungshinweis.slub-dresden.de/ve-we/1.0/) oder [SLUB FO-ZW 1.0](https://nutzungshinweis.slub-dresden.de/fo-zw/1.0/).
* **publish**
  * **Relevanz:** Ja
  * **Bemerkung:**
    * Die Bereitstellung über Schnittstellen kannbeschrieben werden (Interface-IIIF, Interface-OAI-PMH).
    * Die Veröffentlichung als Verlagsveröffentlichung wird nicht mit/in Kitodo.Presentation gesteuert.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher.md)
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **read**
  * **Relevanz:** Ja
  * **Bemerkung:**
    * Anzeige der Bestandteile des digitalen Objekts. Bestimmte Elemente werden flexibel angezeigt
      * _Werkansicht_: Qualität der Bilddaten in der Vollansicht
      * _Werkansicht_: Anzeige der Volltexte (falls Volltexte in einigen Fällen nur für die Indexierung angewendet werden dürfen)
      * _Listenansicht_: Thumbnail-Anzeige erlaubt - jedoch keine Ansicht des digitalen Objekts in höherer Qualität in der Vollansicht
      * ...
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher.md)
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **reproduce**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert.
    * Dies kann in einem Nutzungshinweis beschrieben werden - insbesondere auch, was nicht erlaubt ist, falls das digitale Objekt heruntergeladen werden kann - wie zum Beispiel in [SLUB VE-WE 1.0](https://nutzungshinweis.slub-dresden.de/ve-we/1.0/) oder [SLUB FO-ZW 1.0](https://nutzungshinweis.slub-dresden.de/fo-zw/1.0/).
* **reuse**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert.
      * Dies kann in einem Nutzungshinweis beschrieben werden - insbesondere auch, was nicht erlaubt ist, falls das digitale Objekt heruntergeladen werden kann - wie zum Beispiel in [SLUB VE-WE 1.0](https://nutzungshinweis.slub-dresden.de/ve-we/1.0/) oder [SLUB FO-ZW 1.0](https://nutzungshinweis.slub-dresden.de/fo-zw/1.0/).
* **run**
  * **Relevanz:** Nein
  * **Bemerkung:**
    * Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.

## Constraints

* **age**
  * **Relevanz:** Nein
  * **Bemerkung:** Die Beschränkung des Objekts durch dieses Constraint ist vorerst nicht vorgesehen.
* **agreement**
  * **Relevanz:** Ja
  * **Bemerkung:** Zum Beispiel ist ein wissenschaftliches Interesse für die Nutzung/Ansicht des digitalen Objekts zu bestätigen.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
* **concurrent**
  * **Relevanz:** Ja
  * **Bemerkung:** Ein digitales Objekt wird nur für eine bestimmte Anzahl gleichzeitiger Zugriffe angeboten (z. B. Durchsetzung "Einzelplatz").
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher)
* **count**
  * **Relevanz:** Nein
  * **Bemerkung:** Die Beschränkung des Objekts durch dieses Constraint ist vorerst nicht vorgesehen.
* **date**
  * **Relevanz:** Ja
  * **Bemerkung:** Ein digitales Objekt wird nicht angezeigt, wenn eine Embargo-Frist besteht.
* **duration**
  * **Relevanz:** ?
  * **Bemerkung:** Zeitliche Beschränkungen werden durch Zeitpunkte (date) beschrieben.
* **group**
  * **Relevanz:** Ja
  * **Bemerkung:** Kann für zwei Anwendungsfälle genutzt werden: Nutzergruppen (wissenschaftliche Nutzende, SLUB-Nutzende) oder IP-Adressenbereiche (Arbeitsplätze Mediathek/Lesesaal), um IP-Erfassung in METS zu vermeiden.
  * **Beispiele:**
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **location**
  * **Relevanz:** ja
  * **Bemerkung:** Einschränkung auf IP-Adressen oder auf textlich formulierte Arbeitsplätze.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher)
* **parts**
  * **Relevanz:** Ja
  * **Bemerkung:** Kann genutzt werden, um  zu beschreiben, dass zum Beispiel nur 10 % eines Objekts gespeichert werden darf.
* **quality**
  * **Relevanz:** Ja
  * **Bemerkung:** Auswertung der Bild-Derivate in unterschiedlicher Qualität.
* **watermark**
  * **Relevanz:** Nein
  * **Bemerkung:** Die Beschränkung des Objekts durch dieses Constraint ist vorerst nicht vorgesehen.

## Attributes

* **count**
  * **Relevanz:** Nein
  * **Bemerkung:** Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
* **fromdate**
  * **Relevanz:** Ja
  * **Bemerkung:** Ein digitales Objekt wird nicht angezeigt, wenn eine Embargo-Frist besteht.
* **groups**
  * **Relevanz:** Ja
  * **Bemerkung:** -
  * **Beispiele:**
    * [Sächsische Zeitung](/adjustments/saechsischezeitung.md)
* **inside**
  * **Relevanz:** Ja
  * **Bemerkung:** Beschreibung der Arbeitsplätze...
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher)
* **maxage**
  * **Relevanz:** Nein
  * **Bemerkung:** Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
* **maxbitrate**
  * **Relevanz:** Nein
  * **Bemerkung:** Die Verwaltung der Qualität wird mit den METS-Dateigruppen realisiert, um technische Anpassungen an Kitodo.Presentation zu vermeiden.
* **maxduration**
  * **Relevanz:** Unklar
  * **Bemerkung:** Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
* **maxresolution**
  * **Relevanz:** Nein
  * **Bemerkung:** Die Verwaltung der Qualität wird mit den METS-Dateigruppen realisiert, um technische Anpassungen an Kitodo.Presentation zu vermeiden.
* **minage**
  * **Relevanz:** Nein
  * **Bemerkung:** Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
* **outside**
  * **Relevanz:** Ja
  * **Bemerkung:** -
* **percentage**
  * **Relevanz:** Ja
  * **Bemerkung:** -
  * **Beispiele:**
    * [Künstlerbücher](/adjustments/kuenstlerbuecher)
* **required**
  * **Relevanz:** Ja
  * **Bemerkung:** Bestätigung des wissenschaftlichen Interesses oder anderen spezifischen Anforderungen.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Persönlichkeitsrecht](/adjustments/persrecht.md)
* **sessions**
  * **Relevanz:** Ja
  * **Bemerkung:** Anzahl der erlaubten parallelen Zugriffe auf eine Ressource.
  * **Beispiele:**
    * [Eingeschränkter Zugang - Arbeitsplätze Mediathek - Unter Aufsicht](/adjustments/aufsicht.md)
    * [Künstlerbücher](/adjustments/kuenstlerbuecher)
* **subnet**
  * **Relevanz:** Nein
  * **Bemerkung:** In der METS-Datei sollen keine IP-Adressen eingetragen werden: Stattdessen sollen "Nutzergruppen (group)" angewendet werden.
* **todate**
  * **Relevanz:** Ja
  * **Bemerkung:** Ein digitales Objekt wird nicht angezeigt, wenn eine Embargo-Frist besteht.
* **watermarkvalue**
  * **Relevanz:** Nein
  * **Bemerkung:** Dies wird nicht mit/in Kitodo.Presentation gesteuert und muss nicht maschinenlesbar beschrieben werden.
