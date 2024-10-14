# Setup Guide für Einführung in die Programmierung

Das Setup Guide soll bei der Installation von der Programmiersprache Python und den Editor (IDE) Visual Studio Code helfen. Der Setup-Guide ist für das Betriebssystem Ubuntu geschrieben. Windows-Usern wird empfohlen Linux als Subsystem zu installieren. Für macOS werden die Befehle, die sich zu denen auf Ubuntu unterscheiden, angegeben. Es ist Ihnen freigestellt, welches Betriebssystem/IDE/... Sie nutzen, wir bieten allerdings nur Unterstützung für Ubuntu/VS Code an und empfehlen allen Nicht-Programmiererfahrenen Ubuntu/VS Code zu nutzen.

> Sie finden [weiter unten]((#installation-unter-macos)) ebenfalls eine vollständige Installationsanleitung für `macOS` mit VS Code. Diese wird Ihnen als zusätzlicher Service bereitgestellt und wir bieten begrenzte Unterstützung bei der Installation. Vollständige Unterstützung erhalten Sie aber **nur** für Ubuntu/WSL/VS Code. Sofern Sie der Installation für macOS folgen möchten, überspringen Sie die zuerst kommenden Anweisungen und springen Sie direkt zur [Installation unter macOS](#installation-unter-macos).

## Inhaltsübersicht

1. [Linux für Windows-User als Subsystem (WSL)](#linux-für-windows-user-als-subsystem-wsl)
    1. [PowerShell 7 installieren](#powershell-7-installieren)
    2. [WSL installieren](#wsl-installieren)
    3. [Ubuntu einrichten](#ubuntu-einrichten)
    4. [Account erstellen](#account-erstellen)
2. [Python3.12 installieren](#python312-installieren)
    1. [Packages Updaten](#packages-updaten)
    2. [Visual Studio Code (VS Code) installieren und einrichten](#visual-studio-code-vs-code-installieren-und-einrichten)
    3. [Extensions installieren](#extensions-installieren)
    4. [Extensions einrichten](#extensions-einrichten)
2. [Installation unter macOS](#installation-unter-macos)

## Linux für Windows-User als Subsystem (WSL)

> Der folgende Part ist nur für `Windows`-User relevant.

Alle anderen können direkt zur [Python3.12 Installation](#python312-installieren) springen.

### PowerShell 7 installieren

1. PowerShell öffnen (Windows Taste drücken -> `PowerShell` suchen -> anklicken)

2. Folgende zwei Befehle eingeben:

```PowerShell
winget search Microsoft.PowerShell

winget install --id Microsoft.PowerShell --source winget
```

### WSL installieren

1. Folgenden Befehl eingeben:

```PowerShell
wsl --install
```

2. Neustarten

### Ubuntu einrichten

`Ubuntu` sollte sich nach dem Neustart automatisch geöffnet haben. 
In neueren `PowerShell` versionen öffnet sich `Ubuntu` direkt in dem `PowerShell` Fenster, das könnt ihr daran erkennen, dass die Eingabeaufforderung grün ist.

Falls sich `Ubuntu` nicht automatisch öffnet, müssen Sie es manuell starten (Windows Taste drücken -> `Ubuntu` suchen -> anklicken)

### Account erstellen

1. Benutzername eingeben

2. Passwort festlegen

## Python3.12 installieren

Ab hier gehen wir von einem Ubuntu basierten Betriebssystem aus. Wir geben aber für `Windows`-User die alternativen Befehle an. Als `macOS`-User folgen Sie der [unten stehenden alternativen Installationsanleitung](#installation-unter-macos).

### Packages Updaten

Wir bringen nun die Software auf dem System auf den aktuellen Stand. Dafür muss ein Terminal geöffnet werden (Action Taste drücken -> `Terminal` suchen -> anklicken)

Auf Windows, bzw in der WSL befinden Sie sich bereits in einem Terminal.

1. Folgende zwei Befehle ausführen:

```bash
sudo apt update

sudo apt upgrade
```

Anschließend installieren wir Python.

2. Dafür im Terminal folgende Befehle ausführen:

```bash
# -------- für windows(wsl)/linux -----------

sudo apt install software-properties-common

# dieser schritt kann eventuell auf neueren linux distos übersprungen werden
sudo add-apt-repository ppa:deadsnakes/ppa # mit enter bestätigen

sudo apt install python3.12
```


### Visual Studio Code (VS Code) installieren und einrichten

1. Auf die [Website](https://code.visualstudio.com/Download) von VS Code gehen

2. VS Code runterladen
    2.1. Für `Windows`-User: Laden Sie VS Code für **Windows** herunter, trotz WSL
    2.2. Für Mac und Ubuntu jeweils die Version für Mac bzw. Linux (.deb)

3. Installation durchführen

4. Visual Studio Code öffnen

5. **Wichtig für `Windows`-User**: Links unten auf das blau hinterlegte `><` drücken, dann `WSL` auswählen.

#### Extensions installieren

In Visual Studio Code in der linken Leiste auf das Symbol mit den vier Quadraten drücken. In der Suchleiste folgende vier Extensions suchen und installieren:

1. `Python`

2. `Pylance`

3. `Flake8`

4. `autopep8`

#### Extensions einrichten

Links unten in Visual Stuido Code auf das Zahnrad drücken und die `Settings` öffnen.

1. Nach `Auto Save` suchen und auf `afterDelay` stellen.

2. Nach `Type Checking Mode` suchen und auf `basic` stellen.

3. Nach `Diagnostic Severity Overrides` suchen und auf `edit in settings.json` drücken. Hier nach folgendem Eintrag suchen:

```json
    "python.analysis.diagnosticSeverityOverrides": {

    },
```

und folgende zwei Einträge einfügen, sodass das ganze wie folgt aussieht:

```json
    "python.analysis.diagnosticSeverityOverrides": {
        "reportGeneralTypeIssues": "information",
        "reportWildcardImportFromLibrary": "none"
    },
```

4. `settings.json` wieder schließen.

5. Nach `autopep8` suchen und bei `autopep8: Args` auf `Add Item` drücken. Folgendes einfügen und anschließend auf `OK` drücken:

```
--ignore=F4,E123,E501,E704,E731,W5,C901
```

6. Nach `Flake8` suchen und bei `Flake8: Args` auf `Add Item` drücken. Folgendes einfügen und anschließend auf `OK` drücken:

```
--ignore=F4,E123,E501,E704,E731,W5,C901
```

7. Nach `Severity` suchen und bei `Flake8: Severity` alle Einträge unter `Value` auf `Warning` setzen. Dazu rechts auf den Stift zum Bearbeiten drücken und bei `Value` `Warning` auswählen (auch hier wieder mit `OK` bestätigen)

## Installation unter macOS

1. Hier wollen wir zuerst Python in Version `3.12` installieren. Sie können die Installationsdatei über diesen Link direkt herunterladen: [macOS 64-bit universal2 installer](https://www.python.org/ftp/python/3.12.7/python-3.12.7-macos11.pkg).

    <details>
    <summary>Manuelles Herunterladen der Installstionsdatei Schritt für Schritt (< Klick mich >)</summary>

    1. Auf [python.org](https://www.python.org/downloads/release/python-3127/) gehen und Version `3.12.x` wählen, wobei `x` eine beliebige Zahl sein darf. Bei Erstellung dieser Anleitung ist dies `3.12.7`.

    > Nehmen Sie **auf keinen Fall** `3.13.x`. Diese Version ist möglicherweise mit unserem Abgabesystem nicht kompatibel.

    2. Scrollen Sie bis zum Bereich `Files`.

    3. Wählen Sie [macOS 64-bit universal2 installer](https://www.python.org/ftp/python/3.12.7/python-3.12.7-macos11.pkg).

    </details>

2. Führen Sie nun die heruntergeladene Installationsdatei aus.

3. Folgen Sie nun den Schritten zu:
    -  [Visual Studio Code (VS Code) installieren und einrichten](#visual-studio-code-vs-code-installieren-und-einrichten)
    - [Extensions installieren](#extensions-installieren)
    - [Extensions einrichten](#extensions-einrichten)
