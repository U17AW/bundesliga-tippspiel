from tippspielkalender import Tippspielkalender
from tippspiel import Tippspiel

def main():
    # Erstellt eine Instanz des Tippspielkalenders und fügt Spieltage mit Begegnungen hinzu
    kalender = Tippspielkalender()
    kalender.spieltag_hinzufuegen(1, ['TeamA vs TeamB', 'TeamC vs TeamD'])
    kalender.spieltag_hinzufuegen(2, ['TeamE vs TeamF', 'TeamG vs TeamH'])

    # Erstellt eine Instanz des Tippspiels
    spiel = Tippspiel()
    
    # Benutzereingaben für Tipps abfragen
    spieltag = int(input("Geben Sie den Spieltag ein: "))
    begegnungen = kalender.get_spieltage().get(spieltag, [])
    
    if not begegnungen:
        print(f"Spieltag {spieltag} existiert nicht.")
        return
    
    while True:
        spieler = input("Geben Sie den Namen des Spielers ein (oder 'stop' zum Beenden): ")
        if spieler.lower() == 'stop':
            break
        
        for begegnung in begegnungen:
            tipp = int(input(f"Geben Sie den Tipp für {begegnung} ein (1 = Sieg Heimmannschaft, 2 = Unentschieden, 3 = Sieg Gastmannschaft): "))
            spiel.tipp_abgeben(spieltag, spieler, begegnung, tipp)
    
    # Beispiel-Ergebnisse (könnten auch dynamisch eingegeben werden)
    ergebnisse = {'TeamA vs TeamB': 1, 'TeamC vs TeamD': 2}
    
    # Punkte berechnen
    spiel.punkteberechnung(spieltag, ergebnisse)
    
    # Rangliste anzeigen
    rangliste = spiel.rangliste()
    print("Rangliste:", rangliste)

if __name__ == "__main__":
    main()