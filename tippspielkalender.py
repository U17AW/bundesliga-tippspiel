from typing import List, Dict

class Tippspielkalender:
    def __init__(self):
        # Initialisiert die Liste der Spieltage und deren Begegnungen
        self.spieltage: Dict[int, List[str]] = {}

    def spieltag_hinzufuegen(self, spieltag: int, begegnungen: List[str]):
        # Fügt einen Spieltag mit seinen Begegnungen zur Liste der Spieltage hinzu
        for begegnung in begegnungen:
            heim_team, gast_team = begegnung.split(' vs ')
            if not is_valid_team_name(heim_team) or not is_valid_team_name(gast_team):
                print(f"Ungültige Teamnamen in der Begegnung: {begegnung}")
                return
        self.spieltage[spieltag] = begegnungen

    def get_spieltage(self) -> Dict[int, List[str]]:
        # Gibt die Liste der Spieltage und deren Begegnungen zurück
        for spieltag, begegnungen in self.spieltage.items():
            for begegnung in begegnungen:
                heim_team, gast_team = begegnung.split(' vs ')
                if not is_valid_team_name(heim_team) or not is_valid_team_name(gast_team):
                    print(f"Ungültige Teamnamen in der Begegnung: {begegnung}")
                    return {}
        return self.spieltage

def is_valid_team_name(team_name):
    VALID_TEAM_NAMES = ['TeamA', 'TeamB', 'TeamC', 'TeamD', 'TeamE', 'TeamF', 'TeamG', 'TeamH']
    return team_name in VALID_TEAM_NAMES
