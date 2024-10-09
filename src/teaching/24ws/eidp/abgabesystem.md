## Abgabe über das Web-Interface

Loggen Sie sich im [Abgabesystem](https://git.laurel.informatik.uni-freiburg.de/) ein.

Die Anmeldedaten dafür sind die selben wie auch bei HisInOne und Ilias (RZ-Account).

Treten Sie dem Kurs `2024WS-EidP` bei.

Nach der Anmeldung klicken Sie auf den Ordner mit ihrem Kürzel (= Ihr "Repository").

Sie sehen eine Übersicht mit 14 Ordnern der Übungsblätter.

Eine Zeile kann beispielsweise so aussehen:

exercise-01     |   Initial commit   |  grading in process  |   3 minutes ago

Um für exercise-XY eine Abgabe zu machen, klicken Sie auf den Ordner exercise-XY. (Nicht auf die commit-Nachricht daneben).

Dort sehen Sie Ihre bisherigen Abgaben für exercise-XY.

Klicken Sie oben rechts auf "Upload File".

Bei "Drop files or click here to upload" wählen Sie Ihre Datei(en) aus.

Klicken Sie ganz unten auf "Commit Changes"

Die hochgeladenen Dateien sollten nun in der Ansicht sichtbar sein.

## Tests des Build-servers

Bei jeder Abgabe werden Ihre Dateien auf code-style und Korrektheit der Syntax geprüft.

Dies sehen Sie jeweils in einem Ihrer exercise-XY Ordner, links neben der commit-Nachricht als eine der folgenden 3 Symbole:
- gelber Kreis: Der Build ist noch nicht abgeschlossen. Warten Sie ein paar Sekunden und laden Sie dann die Seite neu.
- grünes Häkchen: Ihre Abgabe hat keine Style- und Syntax-Fehler
- rotes Kreuz: Sie haben noch Fehler zu korrigieren.

Falls Sie ein rotes Kreuz sehen, klicken Sie darauf und anschließend auf "Details"

Es öffnet sich ein neues Fenster mit den Build-logs

Beheben Sie alle Probleme mit dem Status "Failure" und laden Sie Ihre korrigierte(n) Datei(en) erneut hoch.


## Abgabe mit git (optional und alternativ zur Abgabe über das Web-Interface.)

### Installation von git und ssh (einmalig)

Installieren Sie git und ssh, indem Sie ein neues Terminal (Ein Terminal in VS-Code ist ebenso möglich. Auf Windows: WSL-Konsole) öffnen und den folgenden Befehl eingeben:

```
sudo apt install git ssh -y
```

### Erstellung eines SSH-Keys (einmalig)

Erstellen Sie im Terminal ein ssh-Schlüsselpaar mit dem Command

```bash
ssh-keygen
```

Klicken Sie Enter um alle default-Einstellungen auszuwählen.

Es sollte nun ein Keypaar '~/.ssh/id_rsa' und '~/.ssh/id_rsa.pub' erstellt worden sein. 

Geben Sie ihren öffentlichen Schlüssel (die Datei mit der Endung .pub) aus.

```bash
cat ~/.ssh/id_rsa.pub
```

Die Ausgabe sollte ungefähr so aussehen:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQF9D2XAugGzjWY7qz2dmi1j2jzeqr3NRcp14gF3wyUHMeCk0SsLCMEC+iSwBlhd3n9VPCG0pOBwd3qvWbT1Uv5qH7KhMYgygci7xAv2phRyqHrDKVU1y7SIpJa6i7LO4NcPz4MpASsZ0N3GbpkXlZQPQ4Y2xv4Hn2iPq5Gi7zrH0fHTyQ1wOK7q+mTPP2bQY3aTTf/Nvoy6lmuYcfHFknUY9N6DXNf5JzuHcOzuq/wHYDbKMbhGGeOFd6aXGfHw9oGr3s4XymbVU1zSS3MQxAlPfkHxFsht4HivuaTiTgKWoLGXiz0uTYwF3jdFguZZ3XIUGou6LUJ3vo+kHJOqlC/+5xlZnoT6VkKjU+FCnkMj9rkaQ1mSwOniI103Ib5MK+9DMcf4L0wbMHI2Oqiafiond08HQvKEBOKxzuPU+BuDHPKGOsKI/x1ztZHFNGSC+uNMIHSGxgdxRgulzx1EbNyhDPmMkbLUjGSbvr1e6cweYyomI5OmefDD+kf5FaBhU= user@system
```

Loggen Sie sich nun auf dem [Abgabesystems](https://git.laurel.informatik.uni-freiburg.de/) ein und gehen Sie in die Einstellungen (rechts oben bei Ihrem Profilbild -> Settings).

Wählen Sie den Reiter "Keys" aus.

Fügen Sie bei "Manage SSH-Keys" einen neuen Key hinzu mit "Add Key".

Kopieren Sie den vollständigen Schlüssel aus Ihrer Konsole und fügen Sie ihn in "Content" ein.

Klicken Sie direkt darunter auf "Add Key". Der Schlüssel sollte nun eingefügt sein.

Wenn Sie von mehreren PCs aus arbeiten, empfiehlt es sich auf jedem Rechner einen seperates Schlüsselpaar anzulegen. Im Webinterface lassen sich mehrere öffentliche Schlüssel (.pub) hinterlegen.

### Repository klonen (einmalig)

Gehen Sie erneut zum Abgabesystem [Link](https://git.laurel.informatik.uni-freiburg.de/) und dort zu Ihrem Repository.

Kopieren Sie die ssh-url rechts oben.

Gehen Sie zurück zum Terminal und navigieren Sie sich zu einem Verzeichnis, in dem Sie Ihr Repository anlegen möchten.

Die wichtigsten Befehle dafür sind:

- `ls` : zeigt den Inhalt des aktuellen Verzeichnisses an
- `cd dirXYZ` : in das Verzeichnis "dirXYZ" gehen.

Wenn Sie sich in einem Verzeichnis befinden, das Sie wieder finden, klonen Sie dort Ihr git-Repository mit dem folgenden Befehl, in dem Sie `<ssh-url>` durch Ihre eben kopierte url ersetzen.

```bash
git clone <ssh-url>
```

Wenn Sie nun `ls` ausführen, sollten Sie ein Verzeichnis mit dem Namen Ihres Kürzels sehen. Dies ist nun Ihr lokales Repository.

### git einrichten (einmalig)

Geben Sie git **Ihren** Namen und **Ihre** Mail-Adresse an, damit das Programm weiß, wer Sie sind.

```bash
git config user.name "Ihr Name"
git config user.email your@mail.com
```

Wählen Sie zudem die default-pull Strategie "rebase" aus:

```bash
git config pull.rebase true
```

### Lokales Repository aktualisieren

Bewegen Sie sich mit `cd` in Ihr lokales Repository. Alle folgenden git-Commands funktionieren nur, wenn Sie sich im Terminal in Ihrem lokalen Repository befinden.


Vergewissern Sie sich, dass Sie keine lokalen Änderungen haben. Sind Sie sich nicht sicher, führen Sie den Command `git status` aus.

Werden dort Veränderungen aufgelistet, committen Sie diese zuerst alle. Siehe [unten](#änderungen-committen)

Führen Sie den folgenden Befehl aus:

```bash
git pull
```

Damit immer die selbe Strategie verwendet wird, um die Änderungen mit den lokalen Änderungen zusammenzuführen, führen Sie einmalig folgenden Befehl aus:


```bash
git config pull.rebase true
```

### Änderungen committen

Wenn Sie Dateien in Ihrem lokalen Repository verändert haben, müssen Sie diese zu einem Commit hinzufügen.

Führen Sie dazu den Befehl aus:

```bash
git add .
```

Dies fügt **alle** Änderungen in Ihrem Repository hinzu.

Wenn Sie nur einige Dateien committen möchten, können Sie diese auch separat hinzufügen. Z.B. `git add file1.txt file2.py file3.md`

Der eigentliche Commit wird dann mit dem folgenden Befehl erstellt:

```bash
git commit -m "arbitrary commit message"
```

Sie dürfen Ihrem Commit in der commit-message gerne eine sinnvolle Beschreibung hinzufügen.

### Änderungen hochladen

Bevor Sie Ihre Änderungen hochladen ist es sinnvoll, das Repository noch einmal zu aktualisieren. (Für den Fall, dass eine andere Person, also Ihr\*e Tutor\*in selbst Änderungen vorgenommen hat) 

Folgen Sie demnach der Beschreibung [lokales repository aktualisieren](#lokales-repository-aktualisieren)

Ist Ihr Repository aktualisiert und alle Änderungen committed, können Sie (alle) Commits hochladen mit dem Befehl

```bash
git push
```

Nach dem push sollte Ihre Änderung im Web-Interface des Abgabesystems sichtbar sein.

### Einfacher git-Workflow

Merken Sie sich die Reihenfolge: `pull`, Dateien verändern, `add`, `commit`, `pull`, `push`. Dann kann eigentlich nichts falsch laufen! Falls doch, kann `git status` helfen. Wenn das auch nicht hilft, fragen Sie gerne im Chat oder im Tutorat!

Beachten Sie, dass git noch sehr viele weitere Funktionen besitzt und auch andere Workflows etabliert sind. Falls Sie interessiert sind, finden Sie eine ausführliche Erklärung im [offiziellen Pro Git book](https://git-scm.com/book/en/v2)