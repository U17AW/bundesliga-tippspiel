from tippspielkalender import Tippspielkalender
from tippspiel import Tippspiel

def main():
    # Erstellt eine Instanz des Tippspielkalenders und fügt Spieltage mit Begegnungen hinzu
    kalender = Tippspielkalender()
    kalender.spieltag_hinzufuegen(1, [
        'FC Bayern München vs Borussia Dortmund', 
        'RB Leipzig vs Bayer 04 Leverkusen', 
        'VfL Wolfsburg vs Eintracht Frankfurt', 
        'Borussia Mönchengladbach vs 1. FC Köln', 
        'SC Freiburg vs TSG 1899 Hoffenheim', 
        '1. FSV Mainz 05 vs FC Augsburg', 
        'Hertha BSC vs VfB Stuttgart', 
        'Werder Bremen vs 1. FC Union Berlin', 
        'FC Schalke 04 vs Arminia Bielefeld'
    ])
    kalender.spieltag_hinzufuegen(2, [
        'Borussia Dortmund vs RB Leipzig', 
        'Bayer 04 Leverkusen vs FC Bayern München', 
        'Eintracht Frankfurt vs Borussia Mönchengladbach', 
        '1. FC Köln vs VfL Wolfsburg', 
        'TSG 1899 Hoffenheim vs SC Freiburg', 
        'FC Augsburg vs 1. FSV Mainz 05', 
        'VfB Stuttgart vs Hertha BSC', 
        '1. FC Union Berlin vs Werder Bremen', 
        'Arminia Bielefeld vs FC Schalke 04'
    ])

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
    ergebnisse = {
        'FC Bayern München vs Borussia Dortmund': 1, 
        'RB Leipzig vs Bayer 04 Leverkusen': 2, 
        'VfL Wolfsburg vs Eintracht Frankfurt': 3, 
        'Borussia Mönchengladbach vs 1. FC Köln': 1, 
        'SC Freiburg vs TSG 1899 Hoffenheim': 2, 
        '1. FSV Mainz 05 vs FC Augsburg': 3, 
        'Hertha BSC vs VfB Stuttgart': 1, 
        'Werder Bremen vs 1. FC Union Berlin': 2, 
        'FC Schalke 04 vs Arminia Bielefeld': 3
    }
    
    # Punkte berechnen
    spiel.punkteberechnung(spieltag, ergebnisse)
    
    # Rangliste anzeigen
    rangliste = spiel.rangliste()
    print("Rangliste:", rangliste)

def is_valid_team_name(team_name):
    VALID_TEAM_NAMES = [
        'FC Bayern München', 'Borussia Dortmund', 'RB Leipzig', 'Bayer 04 Leverkusen', 
        'VfL Wolfsburg', 'Eintracht Frankfurt', 'Borussia Mönchengladbach', '1. FC Köln', 
        'SC Freiburg', 'TSG 1899 Hoffenheim', '1. FSV Mainz 05', 'FC Augsburg', 
        'Hertha BSC', 'VfB Stuttgart', 'Werder Bremen', '1. FC Union Berlin', 
        'FC Schalke 04', 'Arminia Bielefeld'
    ]
    return team_name in VALID_TEAM_NAMES

if __name__ == "__main__":
    main()
