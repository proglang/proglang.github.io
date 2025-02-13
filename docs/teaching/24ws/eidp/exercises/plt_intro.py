# Als erstes importieren wir das Modul
import matplotlib.pyplot as plt


def demo():
    # Wir erstellen eine Liste von x- und y-Werten
    x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    y = [-125, -64, -27, -8, -1, 0, 1, 8, 27, 64, 125]

    # ... und erstellen ein Linien-Diagramm,
    # dass die Punkte (x[n], y[n]) mit (x[n+1], y[n+1]) verbindet
    # Optional können wir auch eine Beschriftung mit dem label Parameter hinzufügen
    plt.plot(x, y, label="y = x^3")

    # Wir fügen noch eine zweites Liniendiagramm hinzu,
    # dem wir einen anderen Stil geben wollen
    # Die plot Funktion hat dazu noch einige nützliche Parameter:
    #   linestyle: Aussehen der Linie (zB: "--", ":", "-.", ...)
    #   color: Farbe der Linie (zB: "red", "blue", "green", ...)
    #   marker: Art des Punktes (zB: "o", "x", "s", ...)
    x2 = [-6, 1, 8, -6]
    y2 = [4, 70, 35, 4]
    plt.plot(x2, y2, linestyle="--", marker="s", color="purple", label="A Triangle")

    # Nun legen wir einen Titel fest, beschriften die Achsen und fügen eine Legende hinzu
    plt.title("Mein erster Plot")
    plt.xlabel("x-Achse")
    plt.ylabel("y-Achse")
    plt.legend()

    # Matplotlib passt die Achsen automatisch an die Daten an.
    # Manchmal ist es sinnvoll die Achsen auch manuell festzulegen:
    plt.xlim(-10, 10)
    plt.ylim(-150, 200)

    # Optional können wir auch ein Gitter hinzufügen
    plt.grid()

    # Abschließend zeigen wir das Diagramm an
    plt.show()


if __name__ == "__main__":
    demo()
