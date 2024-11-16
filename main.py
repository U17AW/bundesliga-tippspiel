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
    while True:
        try:
            spieltag = int(input("Geben Sie den Spieltag ein: "))
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
    
    begegnungen = kalender.get_spieltage().get(spieltag, [])
    
    if not begegnungen:
        print(f"Spieltag {spieltag} existiert nicht.")
        return
    
    while True:
        spieler = input("Geben Sie den Namen des Spielers ein (oder 'stop' zum Beenden): ")
        if spieler.lower() == 'stop':
            break
        
        for begegnung in begegnungen:
            while True:
                try:
                    tipp = int(input(f"Geben Sie den Tipp für {begegnung} ein (1 = Sieg Heimmannschaft, 2 = Unentschieden, 3 = Sieg Gastmannschaft): "))
                    if tipp in [1, 2, 3]:
                        break
                    else:
                        print("Ungültige Eingabe. Bitte geben Sie 1, 2 oder 3 ein.")
                except ValueError:
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            heim_team, gast_team = begegnung.split(' vs ')
            if not is_valid_team_name(heim_team) or not is_valid_team_name(gast_team):
                print(f"Ungültige Teamnamen in der Begegnung: {begegnung}")
                continue
            print(f"Spieler: {spieler}, Begegnung: {begegnung}, Tipp: {tipp}")
            confirmation = input("Möchten Sie diesen Tipp bestätigen? (ja/nein): ")
            if confirmation.lower() == 'ja':
                spiel.tipp_abgeben(spieltag, spieler, begegnung, tipp)
            else:
                print("Tipp wurde nicht gespeichert.")
    
    # Beispiel-Ergebnisse (könnten auch dynamisch eingegeben werden)
    ergebnisse = {'TeamA vs TeamB': 1, 'TeamC vs TeamD': 2}
    
    # Punkte berechnen
    spiel.punkteberechnung(spieltag, ergebnisse)
    
    # Rangliste anzeigen
    rangliste = spiel.rangliste()
    print("Rangliste:", rangliste)

def is_valid_team_name(team_name):
    VALID_TEAM_NAMES = ['TeamA', 'TeamB', 'TeamC', 'TeamD', 'TeamE', 'TeamF', 'TeamG', 'TeamH']
    return team_name in VALID_TEAM_NAMES

if __name__ == "__main__":
    main()
