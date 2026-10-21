# Setup Guide: Einführung in die Programmierung

Diese Anleitung hilft Ihnen bei der Installation der Programmiersprache <img src="icons/python.svg" alt="" width="16" height="16" style="width: 1em; height: 1em; vertical-align: -0.125em;"> **Python 3.14** und der Entwicklungsumgebung <img src="icons/vscode.svg" alt="" width="16" height="16" style="width: 1em; height: 1em; vertical-align: -0.125em;"> **Visual Studio Code (VS Code)**.

> [!NOTE]
> Falls Sie Python 3.12 und VS Code bereits aus dem Programmier-Vorkurs installiert haben, können Sie direkt zum [Upgrade auf Python 3.14](#upgrade-von-python312-auf-python314) springen.

## <img src="icons/python.svg" alt="" width="16" height="16" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Python 3.14 installieren

Die Installation von Python 3.14 hängt von Ihrem Betriebssystem ab. Wählen Sie Ihr Betriebssystem:  
[<img src="icons/ubuntu.svg" alt="" width="16" height="16" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Linux (Ubuntu)](#linux-ubuntu) | [<img src="icons/windows.svg" alt="" width="16" height="16" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Windows](#windows) | [<img src="icons/apple.svg" alt="" width="16" height="16" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Mac](#mac)

### <img src="icons/ubuntu.svg" alt="" width="24" height="24" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Linux (Ubuntu)

#### System aktualisieren

Öffnen Sie ein Terminal (Windows-Taste → "Terminal" eingeben → anklicken) und führen Sie folgende Befehle aus:

```bash
sudo apt update
sudo apt upgrade
```

#### Python 3.14 installieren

Überprüfen Sie Ihre Ubuntu-Version mit folgendem Befehl:

```bash
lsb_release -a | grep Release
```

Falls Sie eine **ältere** Ubuntu-Version als **26.04** (z.B. 22.04 oder 24.04) verwenden, führen Sie die folgenden Befehle aus:

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

Installieren Sie anschließend Python 3.14:

```bash
sudo apt install python3.14
```

Überprüfen Sie die Installation mit:

```bash
python3.14 --version
```

Es sollte die Ausgabe `Python 3.14.x` erscheinen.

Weiter mit: [Visual Studio Code installieren](#visual-studio-code)

---

### <img src="icons/windows.svg" alt="" width="24" height="24" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Windows

Windows bietet die Möglichkeit, ein vollständiges Linux-System über das **Windows Subsystem for Linux (WSL)** zu nutzen. Dadurch können Sie bequem mit denselben Werkzeugen arbeiten wie auf einem Linux-System.

#### WSL installieren

Öffnen Sie PowerShell (Windows-Taste drücken → „PowerShell“ eingeben → anklicken) und führen Sie den folgenden Befehl aus:

```PowerShell
wsl --install -d Ubuntu-24.04
```

Am Ende der Installation werden Sie dazu aufgefordert, einen **Benutzernamen** und ein **Passwort** einzugeben, die Sie für die Anmeldung in Ihrem Ubuntu-System verwenden werden. *(Hinweis: Beim Tippen wird das Passwort nicht angezeigt.)*  

#### Ubuntu aktualisieren

1. Starten Sie Ubuntu (Windows-Taste drücken → „Ubuntu“ eingeben → anklicken).  

2. Aktualisieren Sie das System:

    ```bash
    sudo apt update
    sudo apt upgrade
    ```

3. Installieren Sie Python 3.14 im Ubuntu-Terminal über das deadsnakes-PPA:

    ```bash
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.14
    ```

4. Überprüfen Sie die Installation mit:

    ```bash
    python3.14 --version
    ```

    Es sollte die Ausgabe `Python 3.14.x` erscheinen.

Weiter mit: [Visual Studio Code installieren](#visual-studio-code)

---

### <img src="icons/apple.svg" alt="" width="24" height="24" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Mac

#### Homebrew installieren und Pakete aktualisieren

Öffnen Sie das Terminal (Spotlight → „Terminal“).
Falls Sie `brew` bereits installiert haben, gehen Sie direkt zu Schritt [Python 3.14 installieren](#mac-python-installieren).

Geben Sie zunächst diesen Befehl ein:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Es erscheint folgende Ausgabe:

```bash
==> Checking for `sudo` access (which may request your password)...
```

Geben Sie nun **Ihr Passwort** ein (Hinweis: Beim Tippen wird das Passwort nicht angezeigt) und bestätigen Sie mit **Enter**.

Nach kurzer Zeit erscheint die Ausgabe:

```bash
Press RETURN/ENTER to continue or any other key to abort
```

Drücken Sie erneut **Enter**, um die Installation fortzusetzen.

Nachdem die Installation abgeschlossen ist, integrieren Sie Homebrew in Ihre Shell:

```bash
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

<a id="mac-python-installieren"></a>

#### Python 3.14 installieren

Um Python 3.14 zu installieren, führen Sie die folgenden Befehle aus:

```bash
brew update
brew install python@3.14
```

Überprüfen Sie die Installation mit:

```bash
python3.14 --version
```

Es sollte die Ausgabe `Python 3.14.x` erscheinen.

Weiter mit: [Visual Studio Code installieren](#visual-studio-code)

## <img src="icons/vscode.svg" alt="" width="24" height="24" style="width: 1em; height: 1em; vertical-align: -0.125em;"> Visual Studio Code

Als Entwicklungsumgebung verwenden wir im Rahmen der Vorlesung **Visual Studio Code (VS Code)**.

### Installation von VS Code

1. Öffnen Sie die [Download-Seite von Visual Studio Code](https://code.visualstudio.com/Download).  
2. Laden Sie die passende Version für Ihr Betriebssystem herunter:  
   - **Windows:** Version für *Windows* (auch wenn Sie WSL nutzen)  
   - **Mac:** Version für *macOS*
   - **Linux (Ubuntu):** `.deb`-Paket für *Ubuntu*  
3. Öffnen Sie die heruntergeladene Datei und folgen Sie den Installationsanweisungen.
4. Öffnen Sie Visual Studio Code.  
5. **Nur für Windows-Nutzer:** Klicken Sie unten links auf <img src="icons/remote.svg" alt="Remote-Verbindung öffnen" height="14"> und wählen Sie **Connect to WSL** aus.

### Extensions installieren

Klicken Sie in der linken Leiste auf <img src="icons/extensions.svg" alt="Erweiterungen" height="18">, um Ihre Extensions zu verwalten. Installieren Sie die folgenden Extensions, indem Sie die IDs in das Suchfeld eingeben und auf installieren klicken.

| Erweiterung | ID für die Suche |
| --- | --- |
| Python | `@id:ms-python.python` |
| Flake8 | `@id:ms-python.flake8` |

### Extensions konfigurieren

Klicken Sie unten links auf <img src="icons/settings-gear.svg" alt="Einstellungen" height="18"> und wählen Sie **Settings** aus.

**Nur für Windows-Nutzer:** Wählen Sie in der oberen Zeile `Remote [WSL: Ubuntu-24.04]` aus.

1. Nach **@id:python.defaultInterpreterPath** suchen → auf `python3.14` stellen.
2. Nach **@id:files.autoSave** suchen → auf `afterDelay` stellen.  
3. Nach **@id:python.analysis.typeCheckingMode** suchen → auf `basic` stellen.  
4. Nach **@id:python.analysis.diagnosticSeverityOverrides** suchen → auf *edit in settings.json* klicken und den folgenden Eintrag anpassen:

    ```json
    "python.analysis.diagnosticSeverityOverrides": {
        "reportGeneralTypeIssues": "information"
    }
    ```

5. `settings.json` schließen.  
6. Nach **@id:flake8.args** suchen → auf **Add Item** klicken → `--ignore=E501,E704,E731,W5,C901` hinzufügen.

7. Nach **@id:flake8.severity** suchen → alle Werte auf **Warning** setzen (Auf <img src="icons/pencil.svg" alt="Stift-Symbol" height="18"> klicken → `Warning` auswählen → **OK**).

Ihre Installation ist nun abgeschlossen! :)

## Upgrade von Python3.12 auf Python3.14

Dieser Abschnitt ist nur relevant, falls Sie bereits Python3.12 mit VSCode installiert haben (z.B. aus dem Programmier-Vorkurs) und auf Python3.14 upgraden möchten.

Folgende Schritte sind noch notwendig:

1. Installieren Sie Python3.14 wie [oben](#python-314-installieren) beschrieben. Falls Sie **Windows + WSL** nutzen, müssen Sie die WSL nicht erneut installieren, sondern nur Python3.14 in Ihrem Ubuntu-Terminal installieren.
2. Öffnen Sie Visual Studio Code und setzen Sie den default Python Interpreter auf Python3.14 (siehe [Extensions konfigurieren](#extensions-konfigurieren)). Alle weiteren Einstellungen haben Sie bereits vorgenommen.
