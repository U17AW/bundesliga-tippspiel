from collections import defaultdict
from typing import List, Dict

class Tippspiel:
    def __init__(self):
        # Initialisiert die Datenstrukturen für Tippabgaben, Punkte und die Rangliste
        self.tippabgaben: Dict[int, Dict[str, List[int]]] = defaultdict(dict)
        self.punkte: Dict[str, int] = defaultdict(int)
        self.rangliste_dict: Dict[str, int] = {}

    def tipp_abgeben(self, spieltag: int, spieler: str, tipp: List[int]):
        # Fügt einen Tipp für einen bestimmten Spieltag und Spieler hinzu
        if spieltag not in self.tippabgaben:
            self.tippabgaben[spieltag] = {}
        self.tippabgaben[spieltag][spieler] = tipp

    def punkteberechnung(self, spieltag: int, ergebnisse: List[int]):
        # Berechnet die Punkte für jeden Spieler basierend auf den Ergebnissen des Spieltags
        if spieltag not in self.tippabgaben:
            print(f"Spieltag {spieltag} existiert nicht.")
            return

        for spieler, tipp in self.tippabgaben[spieltag].items():
            punkte = sum(1 for i in range(len(tipp)) if tipp[i] == ergebnisse[i])
            self.punkte[spieler] += punkte

    def rangliste(self) -> Dict[str, int]:
        # Sortiert die Spieler nach ihren Punkten in absteigender Reihenfolge und gibt die Rangliste zurück
        self.rangliste_dict = dict(sorted(self.punkte.items(), key=lambda x: x[1], reverse=True))
        return self.rangliste_dict