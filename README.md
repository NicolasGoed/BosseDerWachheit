# BosseDerWachheit

Python Projekt für Lasten-/Pflichtenhefte

Generelle Infs zu den Autoren und der Lizenz:

Autoren: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
Datum: 05.12.2021
Version: 0.0.1
License: Public Domain


#############################################################################################


FAQ:

#Wie starte ich die Anwenung?

Durch Ausführen der bereitgestellten .exe Datei in dem zugehörigen Dateipfad

#Wofür brauche ich die Anwendung?

Die Anwendung stellt ein in Python entwickeltes Projekt für Pflichten- und Lastenhefte dar. Es dient dem Erstellen und Verwalten von Projekten. Diesen Projekten können dann zusätzlich Anforderungen inklusive Spezifikationen hinzugefügt werden.

#Wo kann ich Fehler/Feedback melden? 

Ein solches Feature wird in einer späteren Version bereitgestellt.


#############################################################################################


Benutzer erstellen und einloggen:

Es öffnet sich zunächst ein Fenster "Willkommen! Bitte melden Sie sich an" zum Einloggen und erstellen eines neen
Benutzers.
Hier finden sich folgende Elemente mit der jeweiligen Funktion:
*Textfeld für den Username --> Hier kann der eigene Username eingegeben werden
*Textfeld für das Passwort --> Hier kann das eigene Passwort eingegeben werden
*Button zum Anmelden --> Falls die Anmeldedaten korrekt sind Anmeldung
*Button zum Abbrechen --> Abbruch und schließen des Programms

Dazu ein Button zum regestrieren eines neuen Benutzers, falls noch keiner Vorhanden.
Es öffnete sich ein neues Fenster "Bitte neue Daten eingeben" mit den Funktionen:
*Textefeld für den Username --> Hier kann der neue gewünschte Username eingegeben werden
*Textfeld für das Passwort --> Hier kann das gewünschte neue Passwort eingegeben werden
*Textfeld Passwort widerholen --> Benutzer muss sein gewünschtes Passwort erneut eingeben und sie müssen identisch sein

    
#############################################################################################

Erstellen, Bearbeiten und Löschen eines Projekts

Nach einem erfolgreichem Login öffnet sich ein neues Fenster für die Projekte
Dieses bietet folgende Elemente und Funktionen:
* Button Projekt öffnen --> Das Ausgewählte Projekt wird in einem Neuen Fenster zur Weiteren Bearbeitung geöffnet
* Liste aller existierenden Projekte --> Hier kann das zu öffnende oder löschende Projekt ausgewählt werden
* Textfeld für den Namen eines neuen Projekts --> Hier kann der Name des neuen Projekts eingegeben werden
* Button Projekt hinufügen --> Hier wird das eingegebene Projekt neu erstellt und hinzugefügt
* Button Projekt löschen --> Möglichkeit das Ausgewähle Projekt zu löschen


#############################################################################################

Lasten und Pflichten Fenster

Nach der Auswahl des Projekts wird das Fenster für Lasten und Pflichten ausgewählt.
Dies ist der zentrale Fenster, in welchem die Anforderungen für das Lasten- und Pflichtenheft erstellt, bearbeitet
und verwaltet werden können. 
Das Fenster ist wie folgt aufgebaut:

* Projektname -- > Zeigt den Projektnamne des aktuellen Projektes 
* Erstellen --> Button für die Erstellung einer neuen Anforderung 
* Bearbeiten --> Button für die Bearbeitung der in der Anforderungsliste ausgewählten Anforderung 
* Löschen --> Löscht die Anforderung, welche Sie in der Anfoderungsliste ausgewählt haben 
* Anforderungsliste -> Listet alle Anforderungen eines Projektes auf. Die Anforderungen werden dabei mit ihrem 
  Anforderungstext dargestellt
* Lastenheft --> Button zur Anzeige des Lastenheftes 
* Pflichtenheft --> Button zur Anzeige des Pflichtenheftes 


#############################################################################################

Anforderung Erstellen/Bearbeiten

In den Fenstern "Requirement erstellen" und "Requirement bearbeiten" können die Anforderungen erstellt, bzw. im 
Nachhinhein bearbeiten werden. Dabei können zu dem Anforderungstext auch zeitgleich der Spezifikationstext hin-
zugefügt werden. Die einzelnen Spezifikationen zu einer Anforderung können mit Absätzen getrennt werden.

* User --> zeigt den aktuell angemeldeten User an
* Projektname --> zeigt das aktuelle Projekt, in dem die Anforderungen erstellt werden
* Anderung --> Textfeld, in dem der Anforderungstext eingegeben werden kann
* Spezifikation/en --> Textfeld, in dem eine oder meherere Spezifikation/en zu einer Anforderung erfasst werden        können. Falls verschiedene Spezifikationen zu einer Anforderung hinzugefügt werden sollen, trennen Sie diese mit Absätzen, bzw. mit der Enter-Taste
* Speichern --> Speichert die neue Anforderung/ Die Änderungen zu der Anforderungen 


#############################################################################################

Lastenheft/Pflichtenheft 

Die Fenster Lasten-, bzw. Pflichenheft zeigen das Lasten- oder Pflichtenheft des Projektes an.

* Lastenheft --> Im Lastenheft-Fenster wird oben der Projektname angezeigt, zu dem das Lastenheft gehört. Darunter werden die Anforderungen aufgelistet. Dabei werden die Anforderungen nummeriert. Die Anforderungstexte befinden sich unter der Nummerierung. Einzelne Anforderungen werden durch eine Leerzeile getrennt. 
* Lastenheft --> Im Pflichtenheft-Fenster wird oben der Projektname angezeigt, zu dem das Pflichtenheft gehört. Darunter werden die Anforderungen mit ihren Spezifikationen aufgelistet. Dabei werden sowohl die Anforderungen als auch die Spezifikationen nummeriert. Spezifikationen werden durch eine Leerzeile getrennt, die einzelnen Anforderungen werden durch zwei Leerzeilen getrennt.
