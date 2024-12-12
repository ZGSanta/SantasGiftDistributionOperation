# 🎅 Santas Gift Distribution Operation (SGDO)

Ho Ho Ho! Willkommen auf dem Repository der **SGDO**, der Santas Gift Distribution Operation. Hier werden die neusten Algorithmen und Programme entwickelt, mit denen Santa die Geschenke an die Menschen bringt.

## 🎄 Die Mission

Eine kleine Gruppe Elfen arbeitet mit Hochdruck daran, die diesjährige Gift Distribution Operation fertigzustellen. Doch Weihnachten rückt immer näher, und die Elfen haben allerhand zu tun. Die Geschenkeproduktion läuft auf Hochtouren, die Rentiere müssen versorgt werden, und der Algorithmus für die optimale Routenplanung muss noch debuggt werden!

## 🎁 Deine Aufgabe

Hilf den Elfen, ihren Code fertigzustellen, damit alle ihre Geschenke rechtzeitig bekommen! In diesem Repository findest du verschiedene Coding Challenges, die direkt aus der Werkstatt am Nordpol kommen. Von der Optimierung der Verpackungsmaschiene bis hin zur Kalibrierung des Navigationssytems von Santas Schlitten.



## ‼️ Problem 1: ✅

Oh nein! Die Geschenke-Einpack-Maschiene steht still! Es hat nicht genug Geschenkpapier. Finde heraus wieviel noch benötigt wird und mache eine Bestellung bei `santa.clause@bluewin.ch`.

Die Elfen haben dir eine Liste (`input.txt`) mit den Dimensionen von allen noch fehlenden Geschenken bereitgestellt und haben auch schon angefangen ein kleines Programm (`problem1.py`) für die Berechnung zu schreiben.

Du findest beides im Ordner `problem 1`.


---

Super! Mit deiner Hilfe konnte das fehlende Papier gerade noch rechtzeitig bestellt und geliefert werden. Die Geschenke-Einpack-Maschine läuft wieder einwandfrei.

---

## 🏙️ Problem 2: ✅

Schnell! Ein Elf aus der Logistik Abteilung II hat gerade gemeldet, dass der neue Santa-Navigator-V2 vorraussichtlich nicht rechtzeitig fertiggestellt werden kann. V2 soll besser für Mehrfamilienhäuser geeignet sein, da es einen neuen Algorithmus für die Stockwerkbestimmung erhalten hat. Helfe den Elfen, den Algorithmus fertigzustelllen und mache einen `Pull Request`.

Um den Algorithmus zu testen haben dir die Elfen wieder eine Liste (`input.txt`) und ein angefangenes Programm (`problem2.py`) zur Verfügung gestellt. Du findest beides im Ordner `problem 2`.

Im `input.txt` findest du die Kodierung des Stockwerks für ein Beispiel Gebäude.

Eine sich öffnende Klammer `(` bedeutet Santa soll ein Stockwerk nach oben gehen. Eine sich schliessende Klammer `)` entsprechend ein Stockwerk nach unten. 

Zum Beispiel:

- `()` ergiebt Stockwerk 0 (Erdgeschoss)
- `((()` ergiebt Stockwerk 2
- `))()())(` ergiebt Stockwerk -2

Man sagt, die Gebäude im Süden würden immer grösser und auch tiefer werden. Ein Elf hat berichtet ein Gebäude gesehen zu haben, dass höher in den Himmel ragte jedes andere Gebäude. Mir ist nicht ganz klar was er damit meint, auf jedenfall soll der Algorithmus für "unendlich" hohe und tiefe Gebäude funktionieren.

---

Whoooah vielen lieben Dank! Wie sind wir nicht selber auf diese tolle Lösung gekommen?

---

## 📮 Problem 3:

Die Geschenke-Einpack-Maschiene läuft auf hochtouren, der Santa-Navigator-V2 konnte rechtzeitig fertiggestellt werden und die ersten Geschenke sind bereits auf dem Weg in lokale `GiftDistributionHeadquarters`. 

Als Dankeschön für deine grosse Hilfe, hat dir ZG Santa ein persönliches Geschenk organisiert. Doch leider sind die `Tracking Numbers` in einem heftigen Schneesturm durcheinander geraten und nun wissen wir nicht so genau wo das Geschenk ist. Kannst du dein Geschenk finden?

Die erste Spalte im `input.txt` beschreibt den Namen, die zweite die `Tracking Number`. 

`Elf 4` weiss, dass die Namen jeweils aus dem Produkt der Positionen der einzelnen Buchstaben im Alphabet kodiert sind. `Bob` zum Beispiel wäre als 60 kodiert, da `2 * 15 * 2 = 60`.
Sortiere beide Spalten individuell der Grösse nach aufsteigend, dann findest du für deinen Namen die richtige `Tracking Number`.  (Hier kannst du nachlesen, wie man effizient mit Python sortiert: [Python Sorting](https://docs.python.org/3/howto/sorting.html))

Natürlich haben die Elfen schon fleissig vorarbeit geleistet und dir bereits ein fast fertiges Programm (`problem3.py`) zur Verfügung gestellt. Du findest es wie gewohnt im Ordner `problem 3`. 
