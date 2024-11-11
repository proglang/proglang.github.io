# Übungen

## Abgaberegeln

Im folgenden sind die Regeln für die Abgabe der Übungen aufgelistet. Bitte lesen Sie sich diese sorgfältig durch.

### Programmiertechniken

Verwenden Sie nur Befehle und Programmiertechniken, die in den *bisherigen* Vorlesungen (bis zum Abgabetermin) und Übungsblättern behandelt wurden.

### Dateinamen und Dateiformate

Die einzelnen Aufgaben sind mit vollständigen Dateinamen versehen. Verwenden Sie genau diese Namen und die dazugehörigen Dateiformate für Ihre Abgabe. Um Tippfehler zu vermeiden, können Sie die Dateinamen auch einfach kopieren.

Ihre Dateien sollen immer im *Plaintext-Format* (UTF-8 codiert) vorliegen. Python-Code speichern Sie in Dateien mit der Endung `.py`. Für Texte können Sie zwischen `.txt` und `.md` ([Markdown](https://de.wikipedia.org/wiki/Markdown)) frei wählen. Markdown-Dateien bieten gegenüber einfachen `.txt`-Dateien zusätzliche Formatierungsmöglichkeiten, die Sie in Visual Studio Code mit der Tastenkombination `STRG + SHIFT + V` anzeigen lassen können. **Insbesondere sind also keine PDFs, keine Word-Dokumente und auch keine Bildschirmfotos erlaubt!**

### Funktionsnamen

In den Übungsblättern geben wir Funktionsnamen für die zu implementierenden Funktionen vor. Halten Sie sich an diese Vorgaben, da wir Ihre Lösungen automatisiert testen.

### Syntax-Fehler

Python-Skripte, die aufgrund eines SyntaxFehlers nicht ausführbar oder importierbar sind, werden mit 0 Punkten bewertet.

### Typeannotationen
Alle Funktionen, Klassen, Generatoren etc. sollen mit Typannotationen versehen werden. Für fehlende oder teilweise richtige
Typannotationen wird es Abzüge geben.

### Abgabeort

Geben Sie Ihre Aufgaben über unser [git-System](https://git.laurel.informatik.uni-freiburg.de/) ab. Abgaben per Mail können *nicht* berücksichtigt werden.

### Style Guidelines

Nachdem Sie Ihre Lösung hochgeladen haben, überprüft der Build-Server, ob Ihr Code die Stilrichtlinien von [`flake8`](https://flake8.pycqa.org/en/latest/) befolgt. Dieser Check muss erfolgreich sein. Sie sehen das daran, dass auf der Webplattform unseres git-Systems ein grüner Haken erscheint.

### Top-Level Statements

Setzen Sie alle Top-Level-Statements wie `print(...)`, `input(...)` oder Tests in hinter eine `if __name__ == "__main__"`-Verzeigung. Dadurch werden diese Statements nur ausgeführt, wenn das Python-Skript direkt gestartet wird, nicht aber beim Importieren von Funktionen. Alternativ können Sie vor der Abgabe einfach alle Top-Level-Statements entfernen.

## Tipp

Eine einfache Möglichkeit, diese Anforderungen zu erfüllen, besteht darin, alle Dateien mit Visual Studio Code zu erstellen oder zu bearbeiten. Wenn Sie zum Beispiel eine Datei mit der Endung `.txt` oder `.md` bearbeiten, behandelt Visual Studio Code diese wie eine normale Textdatei. Bei `.py`-Dateien zeigt Visual Studio Code `flake8`-Warnungen als gelbe Markierungen an, die Sie durch einen Mouseover erklärt bekommen.
