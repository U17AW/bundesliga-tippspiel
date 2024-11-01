# Kommentiere den Code und füge die fehlenden Methoden hinzu, um ein einfaches Tippspiel zu implementieren.
# Ein Spieler kann für jeden Spieltag einen Tipp abgeben. Die Punkte werden berechnet, indem die Anzahl der richtigen Tipps gezählt wird.
# Die Rangliste zeigt die Spieler in absteigender Reihenfolge ihrer Punkte an.

class Tippspielkalender:
    def __init__(self):
        # Initialisiert die Liste der Spieltage
        self.spieltage = []

    def spieltag_hinzufuegen(self, spieltag):
        # Fügt einen Spieltag zur Liste der Spieltage hinzu
        self.spieltage.append(spieltag)

    def get_spieltage(self):
        # Gibt die Liste der Spieltage zurück
        return self.spieltage

class Tippspiel:
    def __init__(self):
        # Initialisiert die Datenstrukturen für Tippabgaben, Punkte und die Rangliste
        self.tippabgaben = {}
        self.punkte = {}
        self.rangliste_dict = {}

    def tipp_abgeben(self, spieltag, spieler, tipp):
        # Fügt einen Tipp für einen bestimmten Spieltag und Spieler hinzu
        if spieltag not in self.tippabgaben:
            self.tippabgaben[spieltag] = {}
        self.tippabgaben[spieltag][spieler] = tipp

    def punkteberechnung(self, spieltag, ergebnisse):
        # Berechnet die Punkte für jeden Spieler basierend auf den Ergebnissen des Spieltags
        for spieler, tipp in self.tippabgaben[spieltag].items():
            punkte = 0
            for i in range(len(tipp)):
                if tipp[i] == ergebnisse[i]:
                    punkte += 1
            if spieler not in self.punkte:
                self.punkte[spieler] = 0
            self.punkte[spieler] += punkte

    def rangliste(self):
        # Sortiert die Spieler nach ihren Punkten in absteigender Reihenfolge und gibt die Rangliste zurück
        self.rangliste_dict = dict(sorted(self.punkte.items(), key=lambda x: x[1], reverse=True))
        return self.rangliste_dict

def main():
    # Erstellt eine Instanz des Tippspielkalenders und fügt Spieltage hinzu
    kalender = Tippspielkalender()
    kalender.spieltag_hinzufuegen(1)
    kalender.spieltag_hinzufuegen(2)

    # Erstellt eine Instanz des Tippspiels
    spiel = Tippspiel()
    
    # Beispiel-Tipps abgeben
    spiel.tipp_abgeben(1, 'Alice', [1, 2, 3])
    spiel.tipp_abgeben(1, 'Bob', [1, 2, 4])
    
    # Beispiel-Ergebnisse
    ergebnisse = [1, 2, 3]
    
    # Punkte berechnen
    spiel.punkteberechnung(1, ergebnisse)
    
    # Rangliste anzeigen
    rangliste = spiel.rangliste()
    print("Rangliste:", rangliste)

if __name__ == "__main__":
    main()