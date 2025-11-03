# Übungen

## Abgaberegeln

Im Folgenden sind die Regeln für die Abgabe der Übungen aufgeführt. Bitte lesen Sie diese sorgfältig durch.

### Programmiertechniken

Verwenden Sie ausschließlich Befehle und Programmiertechniken, die in den _bisherigen_ Vorlesungen (bis zum jeweiligen Abgabetermin) und Übungsblättern behandelt wurden.

### Style Guidelines

Nach dem Hochladen Ihrer Lösung überprüft der Build-Server automatisch, ob Ihr Code den vorgegebenen Stilrichtlinien (_flake8_) entspricht und ob Sie in der Datei **NOTES.md** Ihre aufgewendete Bearbeitungszeit eingetragen haben. Der Build-Check muss erfolgreich abgeschlossen werden. Abgaben, die diesen Schritt nicht bestehen, werden mit **0 Punkten** bewertet.

### Dateinamen und Dateiformate

Die einzelnen Aufgaben sind mit vollständigen Dateinamen angegeben. Verwenden Sie **genau diese** Namen und die zugehörigen Dateiformate für Ihre Abgabe. Um Tippfehler zu vermeiden, können Sie die Dateinamen einfach kopieren.

Alle Dateien müssen im _Plaintext-Format_ (UTF-8-codiert) vorliegen. Python-Code speichern Sie in Dateien mit der Endung `.py`. Für Texte können Sie zwischen `.txt` und `.md` ([Markdown](https://de.wikipedia.org/wiki/Markdown)) wählen. Markdown-Dateien bieten zusätzliche Formatierungsmöglichkeiten, die Sie in Visual Studio Code mit der Tastenkombination `STRG + SHIFT + V` in der Vorschau anzeigen können.  
**Insbesondere sind keine PDFs, keine Word-Dokumente und keine Bildschirmfotos erlaubt!**

### Abgabeort

Reichen Sie Ihre Abgabe über unsere [Webplattform](https://git.laurel.informatik.uni-freiburg.de/) ein. Wir bewerten den _letzten_ Commit vor Ablauf der Abgabefrist des jeweiligen Blattes. Abgaben per E-Mail können _nicht_ berücksichtigt werden.

### Funktionsnamen

In den Übungsblättern sind die Namen der zu implementierenden Funktionen vorgegeben. Verwenden Sie **genau diese** Namen in Ihrer Lösung.

### Top-Level-Statements

Setzen Sie alle Top-Level-Statements (z. B. `print(...)`, `input(...)`, `assert`, ...) hinter eine `if __name__ == "__main__":` Abfrage. Dadurch werden diese Anweisungen nur ausgeführt, wenn das Python-Skript direkt gestartet wird – nicht jedoch beim Importieren von Funktionen. Alternativ können Sie vor der Abgabe einfach alle Top-Level-Statements entfernen.

### Typannotationen

Alle Funktionen, Klassen, Generatoren, usw. müssen mit Typannotationen versehen sein.  
Für fehlende oder unvollständige Typannotationen gibt es Punktabzug. Achten Sie darauf, die Typannotationen so **präzise wie möglich** zu gestalten (z. B. `list[int]` statt `list`).

## Tipp

Eine einfache Möglichkeit, alle Anforderungen zu erfüllen, besteht darin, Ihre Dateien mit Visual Studio Code zu erstellen oder zu bearbeiten.  
Wenn Sie beispielsweise eine Datei mit der Endung `.txt` oder `.md` öffnen, behandelt Visual Studio Code diese als normale Textdatei. Bei `.py`-Dateien zeigt Visual Studio Code _flake8_-Warnungen als gelbe Markierungen an, die Sie per Mouseover erläutert bekommen.
