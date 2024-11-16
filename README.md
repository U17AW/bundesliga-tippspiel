# bundesliga-tippspiel
Einfaches Github Tutorial

## Neue Funktionen zur Eingabevalidierung und Fehlerbehandlung

Das Bundesliga-Tippspiel wurde um folgende Funktionen zur Eingabevalidierung und Fehlerbehandlung erweitert:

1. **Eingabevalidierung für Teamnamen**:
   - Eine Liste gültiger Teamnamen wurde definiert, um sicherzustellen, dass Benutzer nur gültige Teamnamen eingeben können.
   - Eine Funktion wurde implementiert, um zu überprüfen, ob der eingegebene Teamname gültig ist, indem er mit der Liste der gültigen Teamnamen verglichen wird.
   - Detaillierte Fehlermeldungen werden bereitgestellt, um Benutzer zu unterstützen, wenn sie einen ungültigen Teamnamen eingeben.

2. **Eingabevalidierung für Spielergebnisse**:
   - Eine Funktion wurde implementiert, um sicherzustellen, dass Benutzer nur gültige Spielergebnisse eingeben können (1 = Sieg Heimmannschaft, 2 = Unentschieden, 3 = Sieg Gastmannschaft).
   - Detaillierte Fehlermeldungen werden bereitgestellt, um Benutzer zu unterstützen, wenn sie ein ungültiges Spielergebnis eingeben.

3. **Bestätigungsschritt vor der Abgabe des Tipps**:
   - Ein Bestätigungsschritt wurde hinzugefügt, bevor der Tipp des Benutzers abgegeben wird, um dem Benutzer die Möglichkeit zu geben, seine Eingaben zu überprüfen und eventuelle Fehler zu korrigieren.

4. **Fehlerbehandlung in den Methoden**:
   - In den Methoden `tipp_abgeben` und `punkteberechnung` in `tippspiel.py` sowie in den Methoden `spieltag_hinzufuegen` und `get_spieltage` in `tippspielkalender.py` wurde eine Fehlerbehandlung für ungültige Teamnamen und Spielergebnisse implementiert.

## Was kann ich hier machen

Das Bundesliga-Tippspiel bietet folgende Funktionen:

- **Spieltag hinzufügen**: Fügen Sie Spieltage mit Begegnungen hinzu.
- **Tipp abgeben**: Geben Sie Tipps für die Begegnungen eines Spieltags ab.
- **Punkte berechnen**: Berechnen Sie die Punkte basierend auf den Ergebnissen der Begegnungen.
- **Rangliste anzeigen**: Zeigen Sie die Rangliste der Spieler basierend auf ihren Punkten an.
