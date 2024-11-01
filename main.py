from tippspielkalender import Tippspielkalender
from tippspiel import Tippspiel

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