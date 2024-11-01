from typing import List

class Tippspielkalender:
    def __init__(self):
        # Initialisiert die Liste der Spieltage
        self.spieltage: List[int] = []

    def spieltag_hinzufuegen(self, spieltag: int):
        # Fügt einen Spieltag zur Liste der Spieltage hinzu
        self.spieltage.append(spieltag)

    def get_spieltage(self) -> List[int]:
        # Gibt die Liste der Spieltage zurück
        return self.spieltage