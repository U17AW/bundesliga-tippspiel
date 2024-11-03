from typing import List, Dict

class Tippspielkalender:
    def __init__(self):
        # Initialisiert die Liste der Spieltage und deren Begegnungen
        self.spieltage: Dict[int, List[str]] = {}

    def spieltag_hinzufuegen(self, spieltag: int, begegnungen: List[str]):
        # Fügt einen Spieltag mit seinen Begegnungen zur Liste der Spieltage hinzu
        self.spieltage[spieltag] = begegnungen

    def get_spieltage(self) -> Dict[int, List[str]]:
        # Gibt die Liste der Spieltage und deren Begegnungen zurück
        return self.spieltage