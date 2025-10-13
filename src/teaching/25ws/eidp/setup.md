# Setup Guide für **Einführung in die Programmierung**

Dieses Dokument hilft Ihnen bei der Installation der Programmiersprache **Python 3.12** und der Entwicklungsumgebung **Visual Studio Code (VS Code)**.

Wählen Sie Ihr Betriebssystem:  
[Windows](#windows) | [Linux](#linux) | [Mac](#mac)

---

## Windows

Windows bietet die Möglichkeit, ein vollständiges Linux-System über das **Windows Subsystem for Linux (WSL)** zu nutzen. Dadurch können Sie bequem mit denselben Werkzeugen arbeiten wie auf einem Linux-System.

### 1. PowerShell 7 installieren

1. Öffnen Sie PowerShell (Windows-Taste drücken → „PowerShell“ eingeben → anklicken).  
2. Geben Sie folgende Befehle ein:

```PowerShell
winget search Microsoft.PowerShell
winget install --id Microsoft.PowerShell --source winget
```

### 2. WSL installieren

1. Führen Sie in PowerShell den folgenden Befehl aus:

```PowerShell
wsl --install
```

2. Starten Sie den PC anschließend **neu**.

### 3. Ubuntu einrichten

1. Starten Sie Ubuntu (Windows-Taste drücken → „Ubuntu“ eingeben → anklicken).  
2. Geben Sie einen **Benutzernamen** ein.  
3. Legen Sie ein **Passwort** fest. *(Hinweis: Beim Tippen wird das Passwort nicht angezeigt.)*  
4. Aktualisieren Sie das System:

```bash
sudo apt update
sudo apt upgrade
```

Weiter mit: [Editor installieren](#editor)

---

## Linux

### 1. System aktualisieren

Öffnen Sie ein Terminal (Super-/Action-Taste → „Terminal“ eingeben → anklicken) und führen Sie folgende Befehle aus:

```bash
sudo apt update
sudo apt upgrade
```

### 2. Python 3.12 installieren

Überprüfen Sie Ihre Ubuntu-Version:

```bash
lsb_release -r
```

Beispielausgabe:
```bash
No LSB modules are available.
Release:        24.04
```

Falls Ihre Version **älter als 24.04** ist, führen Sie diese Befehle aus:

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```

Installieren Sie anschließend Python 3.12:

```bash
sudo apt install python3.12
```

Weiter mit: [Editor installieren](#editor)

---

## Mac

### 1. Homebrew und Pakete aktualisieren

Öffnen Sie das Terminal (Spotlight → „Terminal“) und führen Sie folgende Befehle aus:

Falls Homebrew noch nicht installiert ist, führen Sie diesen Befehl aus:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Ansonsten führen Sie diesen Befehl aus:
```bash
brew update
```

### 2. Python 3.12 installieren

Falls Sie **zsh** als Shell verwenden:

```bash
echo "eval $(/opt/homebrew/bin/brew shellenv)" >> ~/.zshrc
```

Danach Python installieren:

```bash
brew install python@3.12
```

Weiter mit: [Editor installieren](#editor)

---

## Editor

Als Entwicklungsumgebung verwenden wir **Visual Studio Code (VS Code)**.

### 1. Installation von VS Code

1. Öffnen Sie die [Download-Seite von Visual Studio Code](https://code.visualstudio.com/Download).  
2. Laden Sie die passende Version herunter:  
   - **Windows:** Version für *Windows* (auch wenn Sie WSL nutzen)  
   - **Mac:** Version für *macOS*  
   - **Linux:** `.deb`-Paket für *Ubuntu*  
3. Führen Sie die Installation durch.  
4. Öffnen Sie VS Code.  
5. **Nur für Windows-Nutzer:** Klicken Sie unten links auf ![alt text](wsl-vsc.png) → **Connect to WSL** auswählen.

---

### 2. Extensions installieren

Klicken Sie in der linken Leiste auf das Symbol mit den vier Quadraten → In der Suchleiste nacheinander eingeben und installieren:

1. `Python`  
2. `Pylance`  
3. `Flake8`  
4. `autopep8`

---

### 3. Extensions konfigurieren

Öffnen Sie unten links das Zahnrad → **Settings**.

1. Nach **Auto Save** suchen → auf `afterDelay` stellen.  
2. Nach **Type Checking Mode** suchen → auf `basic` stellen.  
3. Nach **Diagnostic Severity Overrides** suchen → auf *edit in settings.json* klicken und den folgenden Eintrag anpassen:

```json
"python.analysis.diagnosticSeverityOverrides": {
    "reportGeneralTypeIssues": "information"
}
```

4. `settings.json` schließen.  
5. Nach **autopep8** suchen → bei `autopep8: Args` auf **Add Item** klicken → Folgendes einfügen und mit **OK** bestätigen:

```
--ignore=E501,E704,E731,W5,C901
```

6. Nach **Flake8** suchen → bei `Flake8: Args` auf **Add Item** klicken → ebenfalls Folgendes einfügen:

```
--ignore=E501,E704,E731,W5,C901
```

7. Nach **Severity** suchen → bei `Flake8: Severity` alle Werte auf **Warning** setzen (Stift-Symbol → `Warning` auswählen → **OK**).
