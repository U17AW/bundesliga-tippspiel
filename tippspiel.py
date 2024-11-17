from collections import defaultdict
from typing import List, Dict

class Tippspiel:
    def __init__(self):
        # Initialisiert die Datenstrukturen für Tippabgaben, Punkte und die Rangliste
        self.tippabgaben: Dict[int, Dict[str, Dict[str, int]]] = defaultdict(lambda: defaultdict(dict))
        self.punkte: Dict[str, int] = defaultdict(int)
        self.rangliste_dict: Dict[str, int] = {}

    def tipp_abgeben(self, spieltag: int, spieler: str, begegnung: str, tipp: int):
        # Fügt einen Tipp für eine bestimmte Begegnung eines Spieltags und Spielers hinzu
        heim_team, gast_team = begegnung.split(' vs ')
        if not is_valid_team_name(heim_team) or not is_valid_team_name(gast_team):
            print(f"Ungültige Teamnamen in der Begegnung: {begegnung}")
            return
        if tipp not in [1, 2, 3]:
            print(f"Ungültiger Tipp für die Begegnung: {begegnung}. Bitte geben Sie 1, 2 oder 3 ein.")
            return
        self.tippabgaben[spieltag][spieler][begegnung] = tipp

    def punkteberechnung(self, spieltag: int, ergebnisse: Dict[str, int]):
        # Berechnet die Punkte für jeden Spieler basierend auf den Ergebnissen der Begegnungen des Spieltags
        if spieltag not in self.tippabgaben:
            print(f"Spieltag {spieltag} existiert nicht.")
            return

        for spieler, tipps in self.tippabgaben[spieltag].items():
            punkte = sum(1 for begegnung, tipp in tipps.items() if tipp == ergebnisse.get(begegnung, -1))
            self.punkte[spieler] += punkte

    def rangliste(self) -> Dict[str, int]:
        # Sortiert die Spieler nach ihren Punkten in absteigender Reihenfolge und gibt die Rangliste zurück
        self.rangliste_dict = dict(sorted(self.punkte.items(), key=lambda x: x[1], reverse=True))
        return self.rangliste_dict

def is_valid_team_name(team_name):
    VALID_TEAM_NAMES = [
        'FC Bayern München', 'Borussia Dortmund', 'RB Leipzig', 'Bayer 04 Leverkusen', 
        'VfL Wolfsburg', 'Eintracht Frankfurt', 'Borussia Mönchengladbach', '1. FC Köln', 
        'SC Freiburg', 'TSG 1899 Hoffenheim', '1. FSV Mainz 05', 'FC Augsburg', 
        'Hertha BSC', 'VfB Stuttgart', 'Werder Bremen', '1. FC Union Berlin', 
        'FC Schalke 04', 'Arminia Bielefeld'
    ]
    return team_name in VALID_TEAM_NAMES
