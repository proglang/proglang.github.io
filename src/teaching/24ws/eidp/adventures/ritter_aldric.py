import math

# RNG Funktionen


def RNG(Würfel, dx):
    W = int((math.pi * (10**(Würfel + dx + 8))) % 10)
    return W


def RNG100N(Würfel):
    L = []
    for i in range(1, 12):
        k = RNG(Würfel, i) * 2
        L.append(RNG(Würfel, k))
    W = sum(L) + 1
    return W

# Gegner


def Golem(Würfel, Runde):
    BaseAngriff = 2
    BaseLeben = 10
    BaseAgilität = 1
    RNG100 = RNG100N(Würfel)
    if Runde == 1:
        if 1 <= RNG100 <= 80:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 81 <= RNG100 <= 90:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 91 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 2:
        if 1 <= RNG100 <= 30:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 31 <= RNG100 <= 83:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 84 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 3:
        if 1 <= RNG100 <= 10:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 11 <= RNG100 <= 50:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 51 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 4:
        if 1 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 10)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 10)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 10)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats


def Kobold(Würfel, Runde):
    BaseAngriff = 5
    BaseLeben = 3
    BaseAgilität = 9
    RNG100 = RNG100N(Würfel)
    if Runde == 1:
        if 1 <= RNG100 <= 80:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 81 <= RNG100 <= 90:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 91 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 2:
        if 1 <= RNG100 <= 30:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 31 <= RNG100 <= 83:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 84 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 3:
        if 1 <= RNG100 <= 10:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 11 <= RNG100 <= 50:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 51 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 4:
        if 1 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 10)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 10)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 10)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats


def Barbar(Würfel, Runde):
    BaseAngriff = 4
    BaseLeben = 6
    BaseAgilität = 5
    RNG100 = RNG100N(Würfel)
    if Runde == 1:
        if 1 <= RNG100 <= 80:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 81 <= RNG100 <= 90:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 1 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 100 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 2:
        if 1 <= RNG100 <= 30:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 31 <= RNG100 <= 83:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 1 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 100 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 1 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 3:
        if 1 <= RNG100 <= 10:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 11 <= RNG100 <= 40:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 41 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 4:
        if 1 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 10)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 10)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 10)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats


def Bandit(Würfel, Runde):
    BaseAngriff = 4
    BaseLeben = 5
    BaseAgilität = 5
    RNG100 = RNG100N(Würfel)
    if Runde == 1:
        if 1 <= RNG100 <= 80:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 81 <= RNG100 <= 90:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 91 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 2:
        if 1 <= RNG100 <= 30:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 31 <= RNG100 <= 83:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 84 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 3:
        if 1 <= RNG100 <= 10:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 11 <= RNG100 <= 50:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 51 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 4:
        if 1 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 10)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 10)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 10)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats


def Wichtel(Würfel, Runde):
    BaseAngriff = 3
    BaseLeben = 4
    BaseAgilität = 9
    RNG100 = RNG100N(Würfel)
    if Runde == 1:
        if 1 <= RNG100 <= 80:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 81 <= RNG100 <= 90:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 91 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 2:
        if 1 <= RNG100 <= 30:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 31 <= RNG100 <= 99:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 1 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 100 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 3:
        if 1 <= RNG100 <= 10:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 11 <= RNG100 <= 50:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

        if 51 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats

    if Runde == 4:
        if 1 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 10)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 10)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 10)
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, 0]
            return Stats


def Drache(Würfel, Runde):
    BaseAngriff = 4
    BaseLeben = 9
    BaseAgilität = 9
    BaseCK = 30
    RNG100 = RNG100N(Würfel)
    if Runde == 1:
        if 1 <= RNG100 <= 80:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            CK = ((RNG(Würfel, 12)) * 1) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

        if 81 <= RNG100 <= 90:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            CK = ((RNG(Würfel, 6)) * 2) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

        if 91 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            CK = ((RNG(Würfel, 69)) * 3) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

    if Runde == 2:
        if 1 <= RNG100 <= 30:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            CK = ((RNG(Würfel, 27)) * 1) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

        if 31 <= RNG100 <= 83:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            CK = ((RNG(Würfel, 35)) * 2) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

        if 84 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            CK = ((RNG(Würfel, 84)) * 3) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

    if Runde == 3:
        if 1 <= RNG100 <= 10:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 1)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 1)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 1)
            CK = ((RNG(Würfel, 2)) * 1) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

        if 11 <= RNG100 <= 50:
            Angriff = ((RNG(Würfel, 7)) / 2 + 3) * (1 + 2 * BaseAngriff)
            Leben = ((RNG(Würfel, 9)) / 2 + 3) * (1 + 2 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 11)) / 2 + 3) * (1 + 2 * BaseAgilität)
            CK = ((RNG(Würfel, 35)) * 2) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

        if 51 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 13)) / 2 + 3) * (1 + 3 * BaseAngriff)
            Leben = ((RNG(Würfel, 15)) / 2 + 3) * (1 + 3 * BaseLeben)
            Agilitätv = ((RNG(Würfel, 17)) / 2 + 3) * (1 + 3 * BaseAgilität)
            CK = ((RNG(Würfel, 38)) * 3) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats

    if Runde == 4:
        if 1 <= RNG100 <= 100:
            Angriff = ((RNG(Würfel, 1)) / 2 + 3) * (1 + BaseAngriff * 10)
            Leben = ((RNG(Würfel, 3)) / 2 + 3) * (1 + BaseLeben * 10)
            Agilitätv = ((RNG(Würfel, 5)) / 2 + 3) * (1 + BaseAgilität * 10)
            CK = ((RNG(Würfel, 5)) * 10) + BaseCK
            if Agilitätv <= 90:
                Agilität = Agilitätv
            else:
                Agilität = 90
            Stats = [Angriff, Leben, Agilität, CK]
            return Stats


# Kampf

# Begegnung
def Begegnung(Würfel, ProbG, ProbH, ProbN):
    B = (int(ProbG / 10))
    H = (int(ProbH / 10))
    N = (int(ProbN / 10))
    if RNG(Würfel, 64) < B:
        return 'Feind'
    if (H + B) > RNG(Würfel, 64) >= B:
        return 'Händler'
    if RNG(Würfel, 64) >= (B + H + N):
        return 'Nichts'


# Angriff Spieler
def AngriffS(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK):
    RNGtreffer = RNG(Würfel, 34)
    RNGcrit = RNG(Würfel, RNGtreffer)
    RNGagilität = RNG(Würfel, RNGcrit)
    dAgilität = (AGS - GegnerStats[2])  # Agilitätsdifferenz
    ProbTreffer = int((dAgilität + 90) * (70 / 90) / 10)  # 70 ist die Wahrscheinlichkeit zu treffen bei gleicher Agilität
    OUTPUT = []
    if Gegner == 'Bandit' or Gegner == 'Kobold' or Gegner == 'Drache':
        if RNGtreffer <= ProbTreffer:
            OUTPUT.append('treffer')
            if RNGcrit < int(CK / 10):
                Restleben = GegnerStats[1] - ATKS * 2
                OUTPUT[0] = 'kritischer treffer'
            else:
                Restleben = GegnerStats[1] - ATKS

            if Restleben > 0:
                OUTPUT.append('lebt')
                if RNGagilität < int(100 - (100 * (Restleben / GegnerStats[1])) / 10):  # Agilität sinkt mit gewisser wahrscheinlichkeit wenn gegner getroffen. Wahrscheinlichkeit steigt wenn leben sinkt
                    Restagilität = int(GegnerStats[2] * 0.85)
                else:
                    Restagilität = GegnerStats[2]

            if Restleben <= 0:
                OUTPUT.append('tot')
                Restagilität = GegnerStats[2]
            OUTPUT.extend([GegnerStats[0], Restleben, Restagilität, GegnerStats[3]])
        else:
            OUTPUT.extend(['verfehlt', 'lebt', GegnerStats[0], GegnerStats[1], GegnerStats[2], GegnerStats[3]])

    else:
        if RNGtreffer <= ProbTreffer:
            OUTPUT.append('treffer')
            if RNGcrit < int(CK / 10):
                Restleben = GegnerStats[1] - ATKS * 2
                OUTPUT[0] = 'kritischer treffer'
            else:
                Restleben = GegnerStats[1] - ATKS

            if Restleben > 0:
                OUTPUT.append('lebt')
                Restagilität = GegnerStats[2]

            if Restleben <= 0:
                OUTPUT.append('tot')
                Restagilität = GegnerStats[2]
            OUTPUT.extend([GegnerStats[0], Restleben, Restagilität, GegnerStats[3]])
        else:
            OUTPUT.extend(['verfehlt', 'lebt', GegnerStats[0], GegnerStats[1], GegnerStats[2], GegnerStats[3]])

    return OUTPUT


# Angriff COM
def AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK):
    RNGtreffer = RNG(Würfel, 30)
    RNGcrit = RNG(Würfel, RNGtreffer)
    RNGagilität = RNG(Würfel, RNGtreffer)
    dAgilität = (GegnerStats[2] - AGS)  # Agilitätsdifferenz
    ProbTreffer = int((dAgilität + 90) * (70 / 90) / 10)  # 70 ist die Wahrscheinlichkeit zu treffen bei gleicher Agilität
    OUTPUT = []

    if RNGtreffer <= ProbTreffer:
        OUTPUT.append('treffer')
        Restleben = LEBS - GegnerStats[0]
        if RNGcrit < int(GegnerStats[3] / 10):
            Restleben = LEBS - GegnerStats[0] * 2
            OUTPUT[0] = 'kritischer treffer'
        else:
            Restleben = LEBS - GegnerStats[0]

        if Restleben > 0:
            OUTPUT.append('lebt')
            if RNGagilität < int(100 - (100 * (Restleben / LEBS)) / 10):
                Restagilität = int(AGS * 0.85)

        if Restleben <= 0:
            OUTPUT.append('tot')
            if RNGagilität < int(100 - (100 * (Restleben / LEBS)) / 10):
                Restagilität = int(AGS * 0.85)
        OUTPUT.extend([ATKS, Restleben, Restagilität])
    else:
        OUTPUT.extend(['verfehlt', 'lebt', ATKS, LEBS, AGS])
    return OUTPUT

# Ausweichtest


def AgilitätstestS(Würfel, AGS, GegnerStats):
    RNGF = RNG(Würfel, 47)
    dAgilität = (AGS - GegnerStats[2])  # Agilitätsdifferenz
    ProbAusweichen = int((dAgilität + 90) * (70 / 90) / 10)  # 70 ist die Wahrscheinlichkeit Auszuweichen bei gleicher Agilität
    if RNGF < ProbAusweichen:
        return 'verfehlt'
    if RNGF >= ProbAusweichen:
        return 'treffer'


def AgilitätstestCOM(Würfel, AGS, GegnerStats):
    RNGF = RNG(Würfel, 47)
    dAgilität = (GegnerStats[2] - AGS)  # Agilitätsdifferenz
    ProbAusweichen = int((dAgilität + 90) * (70 / 90) / 10)  # 70 ist die Wahrscheinlichkeit Auszuweichen bei gleicher Agilität
    if RNGF < ProbAusweichen:
        return 'verfehlt'
    if RNGF >= ProbAusweichen:
        return 'treffer'


def Überlebenstest(Würfel, AGS, Agilitätsanforderung, ProbT):
    RNGÜ = RNG(Würfel, 40)
    if AGS < Agilitätsanforderung or RNGÜ <= (ProbT / 10):
        return 'tot'
    if AGS >= Agilitätsanforderung and RNGÜ > (ProbT / 10):
        return 'lebt'


# Kampf
def Kampf(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK):
    RandomV = 0
    ZS = 'lebt'
    ZG = 'lebt'
    print('\n\n\n\n')
    print('\033[1;4mKampfverlauf:\033[0m')
    print('\n\n')
    print('\033[4mAnfangs-CharakterAttribute:\033[0m')
    print()
    print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS), '    \033[4m' + Gegner, ':\033[0m', 'Angriff:', int(GegnerStats[0]))
    print('        ', 'Leben: ', int(LEBS), '             ', 'Leben', int(GegnerStats[1]))
    print('        ', 'Agilität: ', int(AGS), '           ', 'Agilität', int(GegnerStats[2]))
    print()
    print('Du stürmst auf den ' + Gegner, 'zu um ihn anzugreifen')
    while ZS != 'tot' and ZG != 'tot':
        RandomV = RandomV + 3
        A1 = AngriffS(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
        GegnerStats = [A1[2], A1[3], A1[4], A1[5]]
        print()
        print('\033[4mVeränderte-CharakterAttribute:\033[0m')
        print()
        print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS), '    \033[4m' + Gegner, ':\033[0m', 'Angriff:', int(GegnerStats[0]))
        print('        ', 'Leben: ', int(LEBS), '             ', 'Leben', int(GegnerStats[1]))
        print('        ', 'Agilität: ', int(AGS), '           ', 'Agilität', int(GegnerStats[2]))

        if A1[0] == 'treffer' and A1[1] == 'lebt':  # type: ignore
            print()
            print('Du triffst den ' + Gegner, 'mit deinem Schwert. Jedoch hält der ' + Gegner, 'mehr aus als du gedacht hast und ist bereit anzugreifen.'
                  ' Der verwundete ' + Gegner, 'kontert mit einem Gegenangriff')
            Würfel = RNG(int(Würfel), RandomV)
            A1C = AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
            if A1C[0] == 'treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der ' + Gegner, 'trifft dich mit einem mit einem starken Schlag. Du taumelst kurz, aber gehst nicht zu Boden. Du musst zurückschlagen:')
            if A1C[0] == 'treffer' and A1C[1] == 'tot':
                print()
                print('Der ' + Gegner, 'trifft dich mit einem vernichtenden Schlag. Du spürst eine Klinge in deinem Bauch. Während du zu Boden sinkst,'
                      ' zieht dein Leben noch einmal an dir vorbei. Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                ZS = 'tot'
            if A1C[0] == 'verfehlt':
                print()
                print('Mit einem geschickten Sprung zur Seite weichst du dem Schlag aus, und bist direkt bereit zum Gegenangriff')

        if A1[0] == 'kritischer treffer' and A1[1] == 'lebt':
            print()
            print('Du landest einen kritischen treffer, doch selbst das scheint nicht genug zu sein.'
                  ' Der verwundete ' + Gegner, 'stürmt auf dich zu.')
            Würfel = RNG(int(Würfel), RandomV + 4)
            A1C = AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
            if A1C[0] == 'treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der' + Gegner, 'trifft dich mit einem mit einem starken Schlag. Du taumelst kurz, aber gehst nicht zu Boden. Du musst zurückschlagen:')
            if A1C[0] == 'treffer' and A1C[1] == 'tot':
                print()
                print('Der ' + Gegner, 'trifft dich mit einem vernichtenden Schlag. Du spürst eine Klinge in deinem Bauch. Während du zu Boden sinkst,'
                      ' zieht dein Leben noch einmal an dir vorbei. Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                ZS = 'tot'
            if A1C[0] == 'verfehlt':
                print()
                print('Der kritische Treffer scheint den ' + Gegner, ' verwundet zu haben, denn du kannst den Schlag '
                      'parrieren. Du setzt direkt zum Gegenangriff an.')

        if A1[0] == 'kritischer treffer' and A1[1] == 'tot':
            ZG = 'tot'
            print()
            print('Mit einem Schlag von solcher Präzision, wie ihn nur der große König Arthur beherrschte, triffst du den ' + Gegner, 'welcher zu Boden stürzt, und reglos liegen bleibt')

        if A1[0] == 'treffer' and A1[1] == 'tot':
            ZG = 'tot'
            print()
            print('Mit einem finalen Hieb triffst du den ' + Gegner, ', welcher zu Boden stürzt, und reglos liegen bleibt.')

        if A1[0] == 'verfehlt':
            print()
            print('Du hast den ' + Gegner, 'verfehlt, der ' + Gegner, 'stürmt auf dich zu')
            Würfel = RNG(int(Würfel), RandomV + 7)
            A1C = AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
            if A1C[0] == 'treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der ' + Gegner, 'trifft dich mit einem mit einem starken Schlag. Du taumelst kurz, aber gehst nicht zu Boden. Du musst zurückschlagen:')
            if A1C[0] == 'treffer' and A1C[1] == 'tot':
                print()
                print('Der ' + Gegner, 'trifft dich mit einem vernichtenden Schlag. Du spürst eine Klinge in deinem Bauch. Während du zu Boden sinkst,'
                      ' zieht dein Leben noch einmal an dir vorbei. Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                ZS = 'tot'
            if A1C[0] == 'verfehlt':
                print()
                print('Der ' + Gegner, 'scheint genau so viel Lack gesoffen zu haben wie du, denn auch er verfehlt dich. Diesmal musst du treffen, sonst sieht es aus als '
                      'kämpften hier zwei Informatikstudenten. Du versuchst erneut einen Schlag zu landen.')
    print()
    print()
    if ZS == 'tot':
        return [ZS, ATKS, LEBS, AGS]
    if ZS == 'lebt':
        print('Das war ein harter Kampf. Deine Werte haben sich wie folgt geändert:')
        print('Dein Angriff:  ', int(ATKS))
        print('Dein Leben:  ', int(LEBS))
        print('Deine Agilität:  ', int(AGS))
        print('\n')
        return [ZS, ATKS, LEBS, AGS]


def Endkampf(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK):
    RandomV = 0
    ZS = 'lebt'
    ZG = 'lebt'
    print('\n\n\n\n')
    print('\033[1;4mKampfverlauf:\033[0m')
    print('\n\n')
    print('\033[4mAnfangs-CharakterAttribute:\033[0m')
    print()
    print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS), '    \033[4m' + Gegner, ':\033[0m', 'Angriff:', int(GegnerStats[0]))
    print('        ', 'Leben: ', int(LEBS), '             ', 'Leben', int(GegnerStats[1]))
    print('        ', 'Agilität: ', int(AGS), '           ', 'Agilität', int(GegnerStats[2]))
    print()
    print('Du stürmst auf den ' + Gegner, 'zu um ihn anzugreifen')
    while ZS != 'tot' and ZG != 'tot':
        RandomV = RandomV + 3
        A1 = AngriffS(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
        GegnerStats = [A1[2], A1[3], A1[4], A1[5]]
        print()
        print('\033[4mVeränderte-CharakterAttribute:\033[0m')
        print()
        print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS), '    \033[4m' + Gegner, ':\033[0m', 'Angriff:', int(GegnerStats[0]))
        print('        ', 'Leben: ', int(LEBS), '             ', 'Leben', int(GegnerStats[1]))
        print('        ', 'Agilität: ', int(AGS), '           ', 'Agilität', int(GegnerStats[2]))

        if A1[0] == 'treffer' and A1[1] == 'lebt':  # type: ignore
            print()
            print('Du triffst den ' + Gegner, 'mit deinem Schwert. Doch den ' + Gegner, 'kümmert das kaum. Er schlägt mit seinen rießigen Flügeln,'
                  ' du spürst den Wind wie einen Orkan in deinem Gesicht. Er fliegt auf dich zu.')
            Würfel = RNG(int(Würfel), RandomV)
            A1C = AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
            if A1C[0] == 'treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der ' + Gegner, 'rammt dich zur seite. Du schlitterst über den Boden, kannst dich aber fangen, und wieder aufstehen. Du musst zurückschlagen:')
            if A1C[0] == 'kritischer treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der ' + Gegner, 'trifft dich mit einem mit einem mächtigen Feuerstoß. Du spürst die Hitze der Flammen, wie sie sich in deine Haut frisst, und dir'
                      ' große Schmerzen bereitet. Du musst zurückschlagen:')
            if A1C[0] == 'treffer' and A1C[1] == 'tot':
                print()
                print('Der ' + Gegner, 'trifft dich mit einem vernichtenden Schlag. Du wirst weggeschleudert und knallst gegen die Höhlendecke.'
                      'Du weißt, dass du dich von diesem Schlag unmöglich erholen kannst. Dein Leben zieht noch einmal an dir vorbei. Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                ZS = 'tot'
            if A1C[0] == 'verfehlt':
                print()
                print('Du springst zur Seite, und kannst dem ' + Gegner, 'knapp ausweichen und bist direkt bereit zum Gegenangriff.')

        if A1[0] == 'kritischer treffer' and A1[1] == 'lebt':
            print()
            print('Du landest einen kritischen treffer, zum ersten mal hast du das Gefühl, dass der ' + Gegner, 'schwächer wird.'
                  ' Der ' + Gegner, 'fliegt auf dich zu.')
            Würfel = RNG(int(Würfel), RandomV + 4)
            A1C = AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
            if A1C[0] == 'treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der ' + Gegner, 'rammt dich zur Seite. Du schlitterst über den Boden, kannst dich aber fangen, und wieder aufstehen. Du musst zurückschlagen:')
            if A1C[0] == 'treffer' and A1C[1] == 'tot':
                print()
                print('Der ' + Gegner, 'trifft dich mit einem vernichtenden Schlag. Du wirst weggeschleudert und knallst gegen die Höhlendecke.'
                      'Du weißt, dass du dich von diesem Schlag unmöglich erholen kannst. Dein Leben zieht noch einmal an dir vorbei. Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                ZS = 'tot'
            if A1C[0] == 'verfehlt':
                print()
                print('Der kritische Treffer scheint den ' + Gegner, 'wirklich verwundet zu haben, denn du kannst den Schlag '
                      'mit deinem Schild blocken, ohne zu Boden zu stürzen.')

        if A1[0] == 'kritischer treffer' and A1[1] == 'tot':
            ZG = 'tot'
            print()
            print('Du rutschst unter dem Drachen durch, und stößt ihm dein Schwert in den Bauch. Der Drache stößt ein mächtiges Brüllen aus, ehe er langsam zu Boden sinkt.')

        if A1[0] == 'treffer' and A1[1] == 'tot':
            ZG = 'tot'
            print()
            print('Mit einem finalen Hieb triffst du den ' + Gegner, ', welcher zu Boden fällt, und reglos liegen bleibt.')

        if A1[0] == 'verfehlt':
            print()
            print('Der ' + Gegner, 'kann deinem schwachen Schlag mit leichtigkeit ausweichen. Er schlägt mit seinen rießigen Flügeln,'
                  ' du spürst den Wind wie einen Orkan in deinem Gesicht. Er fliegt auf dich zu.')
            Würfel = RNG(int(Würfel), RandomV + 7)
            A1C = AngriffCOM(Würfel, Gegner, GegnerStats, ATKS, LEBS, AGS, CK)
            if A1C[0] == 'treffer' and A1C[1] == 'lebt':
                ATKS = A1C[2]
                LEBS = A1C[3]
                AGS = A1C[4]
                print()
                print('Der ' + Gegner, 'rammt dich zur seite. Du schlitterst über den Boden, kannst dich aber fangen, und wieder aufstehen. Du musst zurückschlagen:')
            if A1C[0] == 'treffer' and A1C[1] == 'tot':
                print()
                print('Der ' + Gegner, 'trifft dich mit einem vernichtenden Schlag. Du wirst weggeschleudert und knallst gegen die Höhlendecke.'
                      'Du weißt, dass du dich von diesem Schlag unmöglich erholen kannst. Dein Leben zieht noch einmal an dir vorbei. Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                ZS = 'tot'
            if A1C[0] == 'verfehlt':
                print()
                print('Der ' + Gegner, 'scheint genau so viel Lack gesoffen zu haben wie du, denn auch er verfehlt dich. Diesmal musst du treffen, sonst sieht es aus als '
                      'kämpften hier zwei Informatikstudenten. Du versuchst erneut einen Schlag zu landen.')
    print()
    print()
    if ZS == 'tot':
        return [ZS, ATKS, LEBS, AGS]
    if ZS == 'lebt':
        print('Das war der härteste Kampf deines Lebens. Deine Werte haben sich wie folgt geändert:')
        print('Dein Angriff:  ', int(ATKS))
        print('Dein Leben:  ', int(LEBS))
        print('Deine Agilität:  ', int(AGS))
        print('\n')
        return [ZS, ATKS, LEBS, AGS]


print('Regeln vorab:')
print('1. Immer nur die vom Spiel als Möglichkeit bereit gestellte Werte bei den Entscheidungen eingeben.')
print('2. Immer wenn du aufgefordert wirst zu Würfeln, sollst du eine Ganze Zahl zwischen 0 und 100 eingeben')
print()
print('Du bist Aldric, ein tapferer Ritter des Königreichs Aranthia. Nach Jahren des Friedens und des Wohlstands hat das Schicksal dich mit einer großen Prüfung konfrontiert: Deine geliebte Frau Liana'
      'leidet an einer mysteriösen und tödlichen Krankheit, die alle Heilmittel des Königreichs übersteigt. Die einzige Rettung scheint ein Elixier zu sein, das aus dem Herzen eines Drachens gewonnen werden kann.'
      'Doch das ist nicht irgendein Drache, sondern die uralte Bestie, die in einer Höhle des Everest hoch im Norden haust. Ein Wesen, dessen Herz eine scheinbar magische Lebenskraft besitzt.'
      'Ohne zu zögern, packst du deine Sachen, schnallst du dein Schwert um und machst dich auf die Reise. Du willst gerade zur Tür deines Hauses hinausstürmen, da fällt dir ein,'
      'dass du noch einen seltenen Stärketrank hast, den dein Vater beim Großen Turnier vor langer Zeit vom König bekommen hatte.'
      'Er meinte immer du sollst ihn für etwas wichtiges aufbewhren, und das hast du getan. Doch was könnte wichtiger sein,'
      'als die Rettung deiner Geliebten Liana? Also schnappst du dir den Trank aus deiner Truhe, und noch während du ihn trinkst, spürst du'
      'wie dich diese enorme Energie durchströmt. Ja, jetzt kann es endlich losgehen. Mögen dir alle Götter beistehen.')
print()
print('Der Stärketrank hat dir 20 Skillpunkte beschert. Du kannst sie auf folgende Eigenschaften aufteilen:')
print('Angriff: Je höher dein Angriff umso mehr Schaden kannst du verursachen')
print('Leben: Je höher dein Leben, um so mehr hältst du aus.')
print('Agilität: Bestimmt wie gut du Ausweichen kannst, deine Reaktionsgeschwindigkeit, aber auch wie gut deine Ausdauer ist.')
print('Kritische Treffer: Bestimmt wie hoch deine Chance ist kriische treffer zu landen, welche doppelten Schaden verursachen.')
print('Wähle weise:(du kannst maximal 10 Skillpunkte in ein Attribut stecken)')
print('Noch 20')
SP = 20
while SP != 0:
    ATKv = input('Angriff:')
    SP = SP - int(ATKv)
    if int(ATKv) <= 10:
        if SP < 0:
            while SP < 0:
                SP = SP + int(ATKv)
                print('So viele Skillpunkte hast du nicht mehr übrig.')
                ATKv = 0
                ATKv = input('Angriff:')
                SP = SP - int(ATKv)
    if int(ATKv) > 10:
        while not (0 < int(ATKv) <= 10):
            print('maximal 10!!')
            SP = SP + int(ATKv)
            ATKv = 0
            ATKv = input('Angriff:')
            SP = SP - int(ATKv)
    print('Noch ' + str(SP))

    LEBv = input('Leben:')
    SP = SP - int(LEBv)
    if int(LEBv) <= 10:
        if SP < 0:
            while SP < 0:
                SP = SP + int(LEBv)
                print('So viele Skillpunkte hast du nicht mehr übrig.')
                LEBv = 0
                LEBv = input('Leben:')
                SP = SP - int(LEBv)
    if int(LEBv) > 10:
        while not (0 < int(LEBv) <= 10):
            print('maximal 10!!')
            SP = SP + int(LEBv)
            LEBv = 0
            LEBv = input('Leben:')
            SP = SP - int(LEBv)
    print('Noch ' + str(SP))

    AGv = input('Agilität:')
    SP = SP - int(AGv)
    if int(AGv) <= 10:
        if SP < 0:
            while SP < 0:
                SP = SP + int(AGv)
                print('So viele Skillpunkte hast du nicht mehr übrig.')
                AGv = 0
                AGv = input('Agilität:')
                SP = SP - int(AGv)
    if int(AGv) > 10:
        while not (0 < int(AGv) <= 10):
            print('maximal 10!!')
            SP = SP + int(AGv)
            AGv = 0
            AGv = input('Agilität:')
            SP = SP - int(AGv)
    print('Noch ' + str(SP))

    CKv = SP
    SP = SP - CKv
print('Du hast folgende Aufteilung gewählt:')
print('Angriff:', ATKv, 'Leben:', LEBv, 'Agilität:', AGv, 'Kritische Treffer:', CKv)
ATKS = (25 * int(ATKv) / 10) + 2
LEBS = (400 * int(LEBv) / 10) + 30
AGS = (90 * int(AGv) / 10)
CK = 20 * CKv / 10 + 4   # Chance auf Kritische Treffer
AGSMAX = AGS  # Maximale Agilität
LEBMAX = LEBS
ATKA = ATKS
LEBA = LEBS
print()
print('Somit ergeben sich folgende Charakter Attribute')
print('\033[4mCharakter Attribute:\033[0m')
print()
print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
print('        ', 'Leben: ', int(LEBS))
print('        ', 'Agilität: ', int(AGS))
print('        ', 'Kritische Treffer: ', int(CK), '%')
print()
print('Dein Startgeld beträgt 410 Goldmünzen, dein ganzes erspartes.')
Gold = 410
print()
print()
print('Du begibst dich also auf die Reise zur Höhle des Drachen. Da die Höhle hoch oben im Norden ist, wird es eine lange Reise bis zum Fuße des Everest.'
      'Du holst deine Karte aus deiner Tasche um die Reise zu planen. Beim Studieren der Karten musst du zwischen 2 Pfaden wählen:')
print()
print('[1] Du kannst einen großen Teil des Weges auf der Haupthandelsstraße (von den Bürgern Aranthias auch "Königsweg" genannt) des Königreichs gehen, der Weg wäre länger aber gut begehbar.'
      'Da auf der Haupthandelsstraße viel lost ist, ist die Wahrscheinlichkeit auf Banditen, aber auch auf Händler zu treffen stark erhöht.')
print()
print('[2] Du nimmst einen Pfad Abseits der Haupthandelsstraße, den Schimmerweg. Der Weg wäre deutlich kürzer, aber auch sehr anstrengend. Die Wahrscheinlichkeit auf Banditen, aber auch auf Händler zu treffen ist stark reduziert.')

Entscheidungsvariable = EV = 0
Händlervariable = 0
CHECKOBDULEBST = 0
Kampfvariable = 0

# Inventar
LebenstränkeG = 0
AgilitätstränkeG = 0

while CHECKOBDULEBST == 0:
    for k in range(0, 3):
        print()
        E = int(input('Für welchen der Wege entscheidest du dich? ([1] für Haupthandelsstraße; [2] für Abseits der Haupthandelsstraße; [3] wenn du dich nicht entscheiden kannst):'))
        if E == 1:
            print('\n\n')
            print('\033[1mDu entscheidest dich also für den Königsweg.\033[0m')
            EV = 1
            break

        if E == 2:
            print('\n\n')
            print('\033[1mDu entscheidest dich Abseits des Königsweges zu gehen. In der Hoffnung noch vor Sonnenuntergang am Fuße des Everest anzukommen.\033[0m')
            EV = 2
            break

        if E == 3 and k != 1:
            print('\n\n')
            print('\033[1mDu solltest dich besser schnell entscheiden. Es ist nie gut zu lange still zu stehen.\033[0m')
            Würfel = RNG(int(input('Würfel:')), 89)
            Was = Begegnung(Würfel, 100, 0, 0)
            if Was == 'Feind':
                print()
                print('Du bist so vertieft in deine Karten, dass du nicht bemerkst wie sich ein Bandit angeschlichen hat. Als der Bandit angreift, bemerkst du ihn grade noch rechtzeitig.'
                      'Du ziehst dein Schwert und kannst schlimmeres verhindern, jedoch gelingt es dem Banditen dir eine kleine Schnittwunde am Bein zuzufügen.')
                print()
                print('[Deine Agilität sinkt um 20%]')
                print()
                AGS = (int(AGS) / 10) * 8
                print('Du hast den ersten Schock des Überraschungsangriffs überwunden und holst zum Gegenangriff aus.')
                Würfel = RNG(int(input('Würfel:')), 9)
                StatsBandit = Bandit(Würfel, 1)
                KAMPF = Kampf(Würfel, 'Bandit', StatsBandit, ATKS, LEBS, AGS, CK)
                if KAMPF[0] == 'tot':
                    CHECKOBDULEBST = 1
                    break
                Kampfvariable = Kampfvariable + 1
                ATKS = KAMPF[1]
                LEBS = KAMPF[2]
                AGS = KAMPF[3]
                print('Nachdem du dich etwas beruhigt hast, schaust du wieder auf die Karte. Es wird Zeit sich für einen Weg zu entscheiden bevor noch mehr Banditen kommen.')
                print()
                print('[Beim durchsuchen des Banditen hast du 100 Gold gefunden.]')
                Gold = Gold + 100

        if E == 3 and k == 1:
            print('Du bist schon wieder so sehr in deine Karten vertieft, dass du nicht bermerkst, dass die Bande des Banditen gekommen ist um Rache zu nehmen. '
                  ' 2 Banditen springen auf dich und machen dich Bewegungsunfähig. Der dritte holt seine Axt heraus.')
            Würfel = 5
            print()
            print('[Dein Angriff sinkt um 70%]')
            print('[Dein Leben sinkt um 60%]')
            print('[Deine Agilität sinkt um 90%]')
            Was = Begegnung(Würfel, 100, 0, 0)
            if Was == 'Feind':
                AGS = (int(AGS) / 10) * 1
                ATKS = (int(ATKS) / 10) * 3
                LEBS = (int(LEBS) / 10) * 2
                print('Du bist in völliger Schockstarre und kannst deine Beine kaum mehr bewegen, jedoch vesuchst du dich trotzdem irgendwie zu verteidigen. Du ziehst dein'
                      ' Schwert, und Schwingst verzweifelt nach dem Banditen mit der Axt.')
                Würfel = RNG(int(input('Würfel:')), 9)
                StatsBandit = Bandit(Würfel, 4)
                KAMPF = Kampf(Würfel, 'Bandit', StatsBandit, ATKS, LEBS, AGS, CK)
                if KAMPF[0] == 'tot':
                    CHECKOBDULEBST = 1
                    break
    print('\n\n')

    if CHECKOBDULEBST == 1:
        break

    if EV == 1:
        if Kampfvariable == 1:
            print('Wie erwartet ist der Weg sehr leicht. Die Reise läuft lange reibungslos. Das Wetter ist gut, und von Banditen bisher keine Spur.'
                  ' Als sich der Tag langsam dem Ende zuneigt merkst du wie du langsam müde wirst. Du schaust auf die Karte. Wärst du abseits des Königsweges gegangen '
                  'hättest du um diese Zeit vermutlich bereits den Fuße des Everest erreicht. Trotzdem glaubst du das der Königsweg die bessere Wahl war. '
                  'Die Chance einen Händler zu treffen ist es Wert den längeren Weg auf sich zu nehmen, vor allem weil du von dem Kampf mit dem Banditen noch verletzt bist, und '
                  'einen Heiltrank gebrauchen könntest. Mittlerweile ist es dunkel geworden.Du entscheidest dich einen Schlafplatz etwas abseits des Weges zu suchen.')
            print()
            print('[Nach dem langen Marsch ist deine Agilität um 20 Prozent gesunken]')
            AGS = AGS * 0.8
            print()
            print('Als du durch das Gestrüpp gehst bemerkst du ein Licht. Vermutlich hat hier noch jemand sein Lager aufgeschlagen. '
                  'Du könntest nachsehen denkst du. Wenn es ein Händler ist, kannst du Möglicherweise etwas zur Stärkung kaufen, und etwas freudnliche Gesellschaft kann schön sein'
                  ' und bringt Sicherheit. Aber falls es ein Feind ist müsstest du möglicherweise Kämpfen, und da du noch geschwächt bist vom letzten Kampf,'
                  ' überstehst du das möglicherweise nicht.')
            print()

        if Kampfvariable == 0:
            print()
            print('Wie erwartet ist der Weg sehr leicht. Die Reise läuft lange reibungslos. Das Wetter ist gut, und von Banditen bisher keine Spur.'
                  ' Als sich der Tag langsam dem Ende zuneigt merkst du wie du langsam müde wirst. Du schaust auf die Karte. Wärst du abseits des Königsweges gegangen '
                  'hättest du um diese Zeit vermutlich bereits den Fuße des Everest erreicht. Trotzdem glaubst du das der Königsweg die bessere Wahl war. '
                  'Die Chance einen Händler zu treffen ist es Wert den längeren Weg auf sich zu nehmen. Außerdem bist du so fitter da der Weg nicht so holprig ist denkst du, und das musst du auch sein, '
                  'denn der Drache wird dir sein Herz sicher nicht freiwillig geben. Jetzt ist es bereits dunkel geworden. Du entscheidest dich einen Schlafplatz etwas abseits des Weges zu suchen.')
            print()
            print('[Nach dem langen Marsch ist deine Agilität um 20 Prozent gesunken]')
            AGS = AGS * 0.8
            print()
            print('Als du durch das Gestrüpp gehst bemerkst du ein Licht. Vermutlich hat hier noch jemand sein Lager aufgeschlagen. '
                  'Du könntest nachsehen denkst du. Wenn es ein Händler ist, kannst du Möglicherweise etwas zur Stärkung kaufen, und etwas freudnliche Gesellschaft kann schön sein'
                  ' und bringt Sicherheit. Aber falls es ein Feind ist müsstest du möglicherweise Kämpfen. Wofür entscheidest du dich?')
            print()

        E = input('Wofür entscheidest du dich? ([1] für nachsehen; [2] für nicht nachsehen)')
        print('\n')
        if int(E) == 1:
            print('\033[1mDu entscheidest dich nachzusehen und gehst vorsichtig auf das Licht zu.\033[0m')
            Würfel = RNG(int(input('Würfel:')), 29)
            Was = Begegnung(Würfel, 50, 50, 0)

            if Was == 'Feind':
                GegnerStats = Kobold(Würfel, 1)
                print()
                print('Oh Nein, hättest du lieber nicht nachgesehen, dann  könntest du jetzt einfach friedlich schlafen. '
                      'Zu deinem Pech triffst du auf einen Kobold, der bereit ist sich zu verteidigen. Er schießt mit seiner Steinschleuder auf dich.')
                Würfel = RNG(int(input('Würfel:')), 24)
                Ausweichen = AgilitätstestS(Würfel, AGS, GegnerStats)
                if Ausweichen == 'treffer':
                    print('Nach dem langen Marsch bist du wohl entwas eingerostet. Der Kobold trifft dich mit der Steinschleuder.')
                    print()
                    print('[Dein Leben sinkt um 5%]')
                    LEBS = LEBS * 0.95
                    print('[Deine Agilität um 10%]')
                    AGS = AGS * 0.9
                if Ausweichen == 'verfehlt':
                    print()
                    print('Trotz des sehr anstrengenden Tages bisher,  reagierst schnell und kannst dem Schuss ausweichen.')
                print()
                print('Du stürmst au den Kobold zu.')
                KAMPF = Kampf(Würfel, 'Kobold', GegnerStats, ATKS, LEBS, AGS, CK)
                if KAMPF[0] == 'tot':
                    CHECKOBDULEBST = 1
                    break
                Kampfvariable = Kampfvariable + 1
                ATKS = KAMPF[1]
                LEBS = KAMPF[2]
                AGS = KAMPF[3]
                print('Du bist völlig fertig. Wenn du morgen keinen Händler findest hältst du nicht mehr lange durch. Du scheinst dich der Höhle zu nähern, denn '
                      'Kobolde sind magische Wesen und laufen eigentlich nicht einfach so herum. Wenn du die Höhle des Drachen erreichst wirst du bestimmt noch '
                      'weiteren magischen Wesen begegnen. Einen Voteil hatte der Kampf aber: Du hast '
                      'ein fertig gerichtetes Lager, mit Lagerfeuer. In der Hoffnung etwas nützliches zu finden, durchsuchst du die Sachen des Kobolds. '
                      'Und tatsächlich wirst du fündig! Ein kleiner Lebenstrank, ein kleiner Schadenstrank, und etwas Gold. Nichts besonderes, aber eine willkommene Hilfe.')
                print()
                print('[20%, deiner Lebenspunkte werden wiederhergestellt.]')
                LEBS = LEBS + abs(LEBMAX - LEBS) * 0.2
                print('[Dein Schaden erhöht sich um 10%]')
                ATKS = ATKS * 1.1
                print('[Du hast 100 Goldmünzen gefunden]')
                Gold = Gold + 100
                print()
                print('Jetzt wird es aber Zeit zu schlafen. Du suchst dir ein bequemes Plätzchen am Lagerfeuer und schläfst ein.')
                print()
                print('Als du am nächsten morgen aufwachst steht die Sonne bereits sehr hoch am Himmel. Du hast den Schlaf wohl gebraucht.'
                      'Über Nacht sind deine Wunden auch etwas verheilt.')
                print()
                print('[Deine Agilität ist vollständig regeneriert.]')
                AGS = AGSMAX
                print('[Dein Leben ist um 10%, regeneriert]')
                LEBS = LEBS + (LEBMAX - LEBS) * 0.1
                print('\n')

            if Was == 'Händler':
                Händlervariable = Händlervariable + 1
                print()
                print('Zum Glück! Es ist ein Händler. Auf Banditen hattest du gar keinen Bock. Du der Händler begrüßt dich, und du frägst ihn, '
                      'ob du dich ihm für diese Nacht anschließen kannst. Der Händler hat nichts dagegen, und bietet dir an sich seine Waren anzusehen.'
                      'Der Händler hat 5 Dinge zur Auswahl: ')
                print()
                print('[1] Zwei Große Lebenstränke [Kosten: 100 Gold pro stück]')
                print('[2] Ein Langschwert (Angriff: +60%; MaximaleAgilität: -10%;) [Kosten: 400 Gold]')
                print('[3] Ein Magsiches Kurzschwert (Angriff: + 30%; MaximaleAgilität: +10%; Kritsiche Treffer: +10%) [Kosten: 500 Gold]')
                print('[4] Ein Silberner Barbarenhelm (Leben: +30%) [Kosten: 300 Gold]')
                print('[5] Zwei Große Agilitätstränke [Kosten: 50 Gold pro Stück]')
                print()
                print('[Du hast ', Gold, ' Gold]')
                print()
                print('[Wenn du nichts mehr kaufen willst tippe "fertig" ein.]')
                print()
                Kauf = 0
                LT = 2
                LS = 1
                MKS = 1
                SBH = 1
                AGT = 2
                while Kauf != 'fertig' and Kauf != 'Fertig' and Gold > 0:
                    Kauf = input('Was willst du Kaufen? (Zahlen zwischen [1] und [4]; [fertig] für beenden)')
                    if Kauf == 'fertig' or Kauf == 'Fertig':
                        break
                    if int(Kauf) == 1:
                        if LT == 0:
                            print('Der Händler hat keine Lebenstränke mehr.')
                        if Gold < 100:
                            print('Du hast nicht genügend Gold')
                        if LT > 0 and Gold >= 100:
                            Gold = Gold - 100
                            LebenstränkeG = LebenstränkeG + 1
                            LT = LT - 1
                            print('Du hast einen Großen Lebenstrank gekauft.')
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 2:
                        if LS == 0:
                            print('Du hast das Langschwert schon gekauft.')
                        if Gold < 400:
                            print('Du hast nicht genügend Gold')
                        if LS > 0 and Gold >= 400:
                            Gold = Gold - 400
                            LS = LS - 1
                            print('Du hast das Langschwert gekauft.')
                            ATKS = ATKS * 1.6
                            AGSMAX = AGSMAX * 0.9
                            AGS = AGS * 0.9
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 3:
                        if MKS == 0:
                            print('Du hast das Magische Kurzschwert schon gekauft.')
                        if Gold < 500:
                            print('Du hast nicht genügend Gold')
                        if MKS > 0 and Gold >= 500:
                            Gold = Gold - 500
                            MKS = MKS - 1
                            print('Du hast das magische KUrzschwert gekauft.')
                            ATKS = ATKS * 1.30
                            CK = CK + 10
                            AGSMAX = AGSMAX * 1.1
                            AGS = AGS * 1.1
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 4:
                        if SBH == 0:
                            print('Du hast den silbernen Barbarenhelm schon gekauft.')
                        if Gold < 300:
                            print('Du hast nicht genügend Gold')
                        if SBH > 0:
                            Gold = Gold - 300
                            SBH = SBH - 1
                            print('Du hast den silbernen Barbarenhelm gekauft.')
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 5:
                        if AGT == 0:
                            print('Der Händler hat keine Lebenstränke mehr.')
                        if Gold < 50:
                            print('Du hast nicht genügend Gold')
                        if AGT > 0 and Gold >= 50:
                            Gold = Gold - 50
                            AgilitätstränkeG = AgilitätstränkeG + 1
                            AGT = AGT - 1
                            print('Du hast einen Großen Lebenstrank gekauft.')
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                print()
                print('Der Händler bedankt sich für deinen Einkauf.')
                print()
                print('\033[4mVeränderte-CharakterAttribute:\033[0m')
                print()
                print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
                print('        ', 'Leben: momentan:', int(LEBS), ' maximal: ', int(LEBMAX))
                print('        ', 'Agilität: momentan:', int(AGS), ' maximal: ', int(AGSMAX))
                print('\n')
                if int(LEBS) != int(LEBMAX) and LebenstränkeG > 0:
                    print(' Du bist verletzt: Leben:', LEBS, '/', LEBMAX)
                    Konsum = input('Willst du einen Lebenstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
                    if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                        print()
                        print('Du entscheidest dich dazu einen Großen Heiltrank zu trinken.')
                        print()
                        print('[Dein volles Leben wird wiederhergestellt]')
                        print()
                        LEBS = LEBMAX
                        LebenstränkeG = LebenstränkeG - 1
                    if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                        print()
                        print(' Du entscheidest dich dagegen einen Heiltrank zu trinken.')
                        print()

                if int(AGS) != int(AGSMAX) and AgilitätstränkeG > 0:
                    print(' Du bist erschöpft: Agilität:', AGS, '/', AGSMAX)
                    Konsum = input('Willst du einen Agilitätstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
                    if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                        print()
                        print('Du entscheidest dich dazu einen Großen Agilitätstrank zu trinken.')
                        print()
                        print('[Deine volle Agilität wird wiederhergestellt]')
                        print()
                        AgilitätstränkeG = AgilitätstränkeG - 1
                        AGS = AGSMAX
                    if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                        print()
                        print(' Du entscheidest dich dagegen einen Agilitätstrank zu trinken.')
                        print()
                print('Du und der Händler unterhaltet euch noch ein Weilchen, und geht dann irgendwann schlafen.')
                print()
                print('Als du am nächsten Morgen aufwachst ist der Händler bereits weg. Du hast den Schlaf wohl wirklich gebraucht.')
                print()
                print('[Deine Agilität ist vollständig regeneriert.]')
                AGS = AGSMAX
                if LEBS < LEBMAX:
                    print()
                    print('[Dein Leben ist um 10%, regeneriert]')
                    LEBS = LEBS + (LEBMAX - LEBS) * 0.1
                print('\n')

        if int(E) == 2:
            print()
            print('Du entscheidest dich lieber kein Risiko einzugehen, und läufst noch ein kleines Stückchen weiter von dem Licht weg.'
                  ' Du findest eine kleine Einbuchtung in einem Felsen, und entschließt dich hier dein Lager aufzuschlagen. '
                  ' Du willst dein Lagerfeuer machen, doch dann fällt die ein wie leicht doch das Licht des Unbekannten zu sehen war. '
                  ' Ob das eine Gute idee Ist?')
            print()
            Lagerfeuer = input('Willst du ein Lagerfeuer machen? ([Ja] oder [Nein] eintippen)')
            if Lagerfeuer == 'Nein' or Lagerfeuer == 'NEIN' or Lagerfeuer == 'NEin' or Lagerfeuer == 'neIN' or Lagerfeuer == 'nEIn' or Lagerfeuer == 'nEin' or Lagerfeuer == 'neIn' or Lagerfeuer == 'neiN':
                print('\033[1mDu entscheidest dich lieber kein Lagerfeuer zu machen, um keine Aufmerksamkeit auf dich zu ziehen.\033[0m')
                print()
                print('Das wird eine kalte Nacht, aber dafür hoffentlich eine Nacht ohne böse Überraschungen. Du legst dich schlafen.')
                print()
            if Lagerfeuer == 'Ja' or Lagerfeuer == 'jA' or Lagerfeuer == 'JA' or Lagerfeuer == 'ja':
                print('\033[1mDu entscheidest dich dafür ein Lagerfeuer zu machen.\033[0m')
                print()
                print('Du willst unbedingt einen erholsamen Schlaf, denn du brauchst deine Kräfte. Du hast noch eine lange Reise vor dir.'
                      ' Du entfachst also ein Lagerfeuer. Du genießt noch etwas die angenehme Wärme, bevor du friedlich einschläfst.')
                print()
                Würfel = RNG(int(input('Würfel:')), 1)
                Was = Begegnung(Würfel, 60, 0, 40)
                if Was == 'Feind':
                    print('Du wachst in der Nacht auf, weil du ein Rascheln im Gestrüpp hörst. Du versuchst dir einen Vorteil zu verschaffen'
                          ' indem du, was auch immer es ist, zuerst angreifst.')
                    GegnerStats = Barbar(Würfel, 1)
                    Würfel = RNG(int(input('Würfel:')), 1)
                    KAMPF = Kampf(Würfel, 'Barbar', GegnerStats, ATKS, LEBS, AGS, CK)
                    if KAMPF[0] == 'tot':
                        CHECKOBDULEBST = 1
                        break
                    Kampfvariable = Kampfvariable + 1
                    ATKS = KAMPF[1]
                    LEBS = KAMPF[2]
                    AGS = KAMPF[3]
                    print('Zum Glück bist du rechtzeitig aufgewacht, sonst hätte das ganz anders ausgehen können.'
                          ' Du durchsuchst den Barbaren und findest etwas Gold, sonst nichts. Völlig erschöpft legst du dich schlafen.'
                          ' Hoffentlich war das die einzige Überraschung diese Nacht.')
                    print()
                    print('[Du hast 150 Gold erhalten]')
                    print()
                    Gold = Gold + 150
                if Was == 'Nichts':
                    print('Die Nacht verläuft ruhig. Durch das Lagerfeuer ist es schön warm, und du kannst dich gut erholen')
                    print()

                print('Als du am nächsten Morgen aufwachst ist der Händler bereits weg. Du hast den Schlaf wohl wirklich gebraucht.')
                print()
                print('[Deine Agilität ist vollständig regeneriert.]')
                AGS = AGSMAX
                if LEBS < LEBMAX:
                    print()
                    print('[Dein Leben ist um 10%, regeneriert]')
                    LEBS = LEBS + (LEBMAX - LEBS) * 0.1
                print('\n')
        print('Du packst deine Sachen zusammen, schnallst dein Schwert um, und machst dich wieder auf den Weg. Du schaust auf die Karte:'
              ' Wenn alles nach Plan läuft solltest du gegen Sonnenuntergang am Fuße des Everest ankommen. Und lange läuft auch alles nach Plan.'
              ' Du merkst wie das Klima kühler wird. Du scheinst dich dem Berg zu nähern. Wenn du dich umsiehst siehst du immer wieder blaue '
              'Punkte aufleuchten in den Wäldern abseits des Weges. Das müssen die Feen sein von denen dir dein Vater als Kind erzählt hat. '
              'Ja. Die Magie wird definitiv stärker, die Höhle des Drachen kann nicht mehr so weit sein. Die Wahrscheilichkeit auf magische Wesen '
              ' wie Kobolde, Hexen, Wichtel, Steingolems und was es sonst noch alles gibt, zu treffen ist stark erhöht. Und die meisten dieser Wesen sind nicht friedfertig.'
              ' Zur Sicherheit hältst du dein Schwert griffbereit.')
        print()
        print('Als du so vor dich hinmarschierst, hörst du eine Kutsche hinter dir. Es ist ein Händler. Doch du merkst das etwas nicht stimmt.'
              ' Neben dem Händler am Wegesrand wackeln die Bäume, raschelt das Gebüsch und hörst du Gelächter. Das sind doch Wichtel! Geldgierige kleine Biester.'
              ' Sie halten nicht viel aus, aber sind flink, und wissen wie man mit einem Dolch umgeht. Normalerweise greifen Wichtel nicht von selbst an,'
              ' aber wenn sie Gold riechen gibt es kein halten mehr. Sie wollen sicher den Händler überfallen!')
        print()
        print('Was tust du?')
        print()
        print('[Du kannst deine Charakterattribute gleich mit "Stats" eintippen, einsehen um dir bei deiner Entscheidungsfindung zu helfen.]')
        print()
        print('[1] Du versuchst dem Händler zu helfen.')
        print('[2] Du hilfst dem Händler nicht.')
        print('[[Stats] Charakteattribute einsehen.]')
        print('\n')
        EH = 0
        while EH != '1' and EH != '2':
            EH = input('Entscheide dich!:')
            if EH == 'stats' or EH == 'Stats':
                print('\033[4mCharakter Attribute:\033[0m')
                print()
                print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
                print('        ', 'Leben: ', int(LEBS), '/', int(LEBMAX))
                print('        ', 'Agilität: ', int(AGS), '/', int(AGSMAX))
                print('\n')

        while int(EH) == 1:
            print('Du versuchst den Händer mit rufen zu warnen. Doch im selben moment starten die Wichtel ihren überfall. Zum '
                  'Glück hat fast jeder Händler immer einen persönlichen Beschützer dabei, weil alleine zu Reisen als Händler'
                  ' quasi Selbstmord ist. Der Beschützer kann viele der Wichtel abwehren. Doch kurz bevor du die Kutsche erreichst wird'
                  ' Er vom Anführer der Wichtelbande, welcher deutlich größer und stärker als die anderen wirkt, brutal niedergestreckt.'
                  ' Als dieser sich dem dem Händler zuwenden will, kannst du gerade noch dazwischen springen. Doch jetzt stehst du dem Rießigen Wichtel gegenüber.'
                  ' Noch kannst du fliehen, und deine eigene Haut retten. Wie eintscheidest du dich?')
            print()

            EH2 = input('[1] Du hilfst dem Händler; [2] Du rettest dich selbst:')
            if int(EH2) == 1:
                print()
                print('\033[4mDu greifst den Wichtelbandenanführer an.\033[0m')
                print()
                Würfel = RNG(int(input('Würfel:')), 49)
                GegnerStats = Wichtel(Würfel, 2)
                KAMPF = Kampf(Würfel, 'Rießenwichtel', GegnerStats, ATKS, LEBS, AGS, CK)
                if KAMPF[0] == 'tot':
                    CHECKOBDULEBST = 1
                    break
                Kampfvariable = Kampfvariable + 1
                ATKS = KAMPF[1]
                LEBS = KAMPF[2]
                AGS = KAMPF[3]
                print('Der Händler ist dir unglaublich dankbar, wärst du nicht gekommen wäre er mit Sicherheit gestorben.'
                      'Der Händler schenkt dir einen Großen Heiltrank und einen Großen Agilitätstrank, welche du sofort trinkst.')
                print()
                print('[Dein Leben wurde vollständig wiederhergestellt]')
                print('[Deine Agilität wurde vollständig wiederhergestellt]')
                LEBS = LEBMAX
                AGS = AGSMAX
                print()
                print('Da nun der Beschützer des Händlers gestorben ist, bittet der Händler dich sein neuer Beschützer zu werden.'
                      ' Du wirst sehr gut bezahlt werden meint der Händler. Du erklärst Ihm dein Dilemma mit deiner Frau, dass du unbedingt'
                      ' diesen Drachen besiegen musst, und dass du keine Zeit dafür hast. Der Händer bittet dich ihn wenigstens bis zur nächsten Siedlung'
                      ' zu begleiten, wo er einen neuen Beschützer anheuern könne. Als Belohnung bekämst du einen Großen Heiltrank, und dürftest dir eine Sache'
                      ' aus seinem Laden als geschenk aussuchen. Was tust du?')
                print()
                EH3 = input('[1] Du nimmst das Angebot an; [2] Du lehnst das Angebot ab')
                print()
                print('\n')
                if int(EH3) == 1:
                    print('\033[1mDu nimmst das Angebot des Händlers an. Da das nächste Dorf (Freiburg) sowieso auf dem Weg liegt, verschwendest du auch keine Zeit.\033[0m')
                    print('\n')
                    EH = 3
                if int(EH3) == 2:
                    print('Du wünschst dem Händler alles Gute auf seiner Reise, aber lehnst das Angebot ab. Du willst lieber'
                          ' nicht in die Zielscheibe weiterer Gegner geraten.')
                    print('\n')
                    EH = 4
                    break

            if int(EH2) == 2:
                EH = 2
                print('Du entscheidest dich dazu deine eigene Haut zu retten. Du weißt nicht ob du den Wichtelanführer besiegen kannst, und '
                      'musst auch an das Leben deiner geliebten Liana denken. Du weichst dem Schlag des Wichtels aus, und rennst um dein Leben.')
                print('\n')
        if CHECKOBDULEBST == 1:
            break
        if int(EH) == 2:
            print('Du rennst um so weit weg wie möglich zu kommen. Als du glaubst weit genug weg zu sein, setzt du deine Reise in normalem '
                  'Tempo fort.')
            print()
        if int(EH) == 4 or int(EH) == 2:
            print('Du schaust auf die Karte. Du musst dem Weg weiter folgen bis nach Freiburg. Hier musst du dann von dem'
                  ' Königsweg eine Abzweigung zum Everest nehmen. Dann folgt noch ein Aufstieg bis zum Eingang der Höhle des Drachen.'
                  ' Die Reise bis zur Abzweigung nach Freiburg läuft ohne Zwischenfälle.')
            print()
            print('Als du zur Abzweigung des Schimmerpfades nach Freiburg kommst, blockiert ein Elite-Barbar den Weg.'
                  ' Vermutlich will er Händler abfangen, die Ihre Waren nach Freiburg bringen wollen. Um in die Stadt zu kommen musst du ihn aus dem '
                  'Weg räumen.')
            print()
            if int(LEBS) != int(LEBMAX) and LebenstränkeG > 0:
                print(' Du bist verletzt: Leben:', LEBS, '/', LEBMAX)
                Konsum = input('Willst du einen Lebenstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
                if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                    print()
                    print('Du entscheidest dich dazu einen Großen Heiltrank zu trinken.')
                    print()
                    print('[Dein volles Leben wird wiederhergestellt]')
                    print()
                    LEBS = LEBMAX
                    LebenstränkeG = LebenstränkeG - 1
                if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                    print()
                    print(' Du entscheidest dich dagegen einen Heiltrank zu trinken.')
                    print()

            if int(AGS) != int(AGSMAX) and AgilitätstränkeG > 0:
                print(' Du bist erschöpft: Agilität:', AGS, '/', AGSMAX)
                Konsum = input('Willst du einen Agilitätstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
                if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                    print()
                    print('Du entscheidest dich dazu einen Großen Agilitätstrank zu trinken.')
                    print()
                    print('[Deine volle Agilität wird wiederhergestellt]')
                    print()
                    AgilitätstränkeG = AgilitätstränkeG - 1
                    AGS = AGSMAX
                if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                    print()
                    print(' Du entscheidest dich dagegen einen Agilitätstrank zu trinken.')
                    print()
            if LebenstränkeG <= 0:
                print()
                print('Du hast leider keine Lebenststränke mehr übrig. Du musst dich dem Barbar wohl so stellen.')
                print()
            if AgilitätstränkeG <= 0:
                print()
                print('Du hast leider keine Agilitätstränke mehr übrig. Du musst dich dem Barbar wohl so stellen.')
                print()
            print('Du rennst auf ihn zu, und greifst ihn an.')
            print()
            Würfel = RNG(int(input('Würfel:')), 47)
            GegnerStats = Barbar(Würfel, 3)
            KAMPF = Kampf(Würfel, 'Elite-Barbar', GegnerStats, ATKS, LEBS, AGS, CK)
            if KAMPF[0] == 'tot':
                CHECKOBDULEBST = 1
                break
            Kampfvariable = Kampfvariable + 1
            ATKS = KAMPF[1]
            LEBS = KAMPF[2]
            AGS = KAMPF[3]
            print('Du duchstuchst den Elitebarbaren. Der Elitebarbar hat vermutlich schon ein paar Händler überfallen, denn du findest 300 Gold.')
            Gold = Gold + 300
            print('Als du in Freiburg ankommst suchst du nach einem Händler.'
                  ' Du brauchst unbedingt bessere Ausrüstung, wenn du den den Aufstieg überleben willst, denn in der Nähe von Gebirgen trifft man'
                  ' oft auf Golems, welche sehr Mächtige Gegner sind. Du suchst den Freiburger Waffenschmied auf, um zu schauen was er anzubieten hat.')
            print('Der Waffenschmied hat 7 Dinge im Angebot:')
            print()
            print()
            print('[1] Zwei Große Lebenstränke [Kosten: 100 Gold pro stück]')
            print('[2] Arthurs Schwert (Angriff: +130%; MaximaleAgilität: -20%; Kritische Treffer: +20%;) [Kosten: 900 Gold]')
            print('[3] Elite Rüstung (MaximlesLeben: +60%; MaximaleAgilität: +20%; Kritische Treffer: +5%) [Kosten: 500 Gold]')
            print('[4] Gladiatorenhelm (MaximalesLeben: +30%; Kritsiche Treffer: +10%) [Kosten: 400 Gold]')
            print('[5] 10-mal Schadensverzauberung (Angriff: +5%) [Kosten: 50 Gold]')
            print('[6] 10-mal Kritische Treffer Verzauberung (Kritische Treffer: +3%) [Kosten: 50 Gold]')
            print('[7] Ein Kletterseil [Kosten: 10 Gold]')
            print()
            print('[Du hast ', Gold, ' Gold]')
            print()
            print('[Wenn du nichts mehr kaufen willst tippe [fertig] ein.]')
            print()
            Kauf = 0
            Geschenk = 1
            LT = 2
            AS = 1
            ER = 1
            GH = 1
            SV = 10
            KTV = 10
            SeilK = 1
            while Kauf != 'fertig' and Kauf != 'Fertig':
                Kauf = input('Was willst du Kaufen? (Zahlen zwischen [1] und [4]; [fertig] für beenden)')
                if Kauf == 'fertig' or Kauf == 'Fertig':
                    break
                if int(Kauf) == 1:
                    if Geschenk == 1:
                        Gold = Gold + 100
                    if LT == 0:
                        print('Der Händler hat keine Lebenstränke mehr.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if LT > 0 and Gold >= 100:
                        Gold = Gold - (100)
                        Geschenk = 0
                        LebenstränkeG = LebenstränkeG + 1
                        LT = LT - 1
                        print('Du hast einen Großen Lebenstrank gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 2:
                    if Geschenk == 1:
                        Gold = Gold + 900
                    if AS == 0:
                        print('Du hast das Arthurs Schwert schon gekauft.')
                    if Gold < 900:
                        print('Du hast nicht genügend Gold')
                    if AS > 0 and Gold >= 900:
                        Gold = Gold - (900)
                        Geschenk = 0
                        AS = AS - 1
                        print('Du hast das Arthurs Schwert gekauft.')
                        ATKS = ATKS + (ATKA * 2.3)
                        AGSMAX = AGSMAX * 0.8
                        AGS = AGS * 0.8
                        CK = CK + 20
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 3:
                    if Geschenk == 1:
                        Gold = Gold + 500
                    if ER == 0:
                        print('Du hast die Eliterüstung schon gekauft.')
                    if Gold < 500:
                        print('Du hast nicht genügend Gold')
                    if ER > 0 and Gold >= 500:
                        Gold = Gold - (500)
                        Geschenk = 0
                        ER = ER - 1
                        print('Du hast die Eliterüstung gekauft.')
                        LEBMAX = LEBMAX + (LEBA * 1.6)
                        CK = CK + 5
                        AGSMAX = AGSMAX * 1.2
                        AGS = AGS * 1.2
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 4:
                    if Geschenk == 1:
                        Gold = Gold + 400
                    if GH == 0:
                        print('Du hast den Gladiatorenhelm schon gekauft.')
                    if Gold < 400:
                        print('Du hast nicht genügend Gold')
                    if GH > 0:
                        Gold = Gold - (400)
                        Geschenk = 0
                        GH = GH - 1
                        LEBMAX = LEBMAX + (LEBA * 1.3)
                        CK = CK + 10
                        print('Du hast den Gladiatorenhelm gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 5:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if SV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if SV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        SV = SV - 1
                        ATKS = ATKS + (ATKA * 1.05)
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 6:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if KTV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if KTV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        KTV = KTV - 1
                        CK = CK + 3
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 7:
                    if Geschenk == 1:
                        Gold = Gold + 10
                    if SeilK == 0:
                        print('Der Händler hat kein Seil mehr übrig.')
                    if Gold < 10:
                        print('Du hast nicht genügend Gold')
                    if SeilK > 0:
                        Gold = Gold - (10)
                        Geschenk = 0
                        SeilK = SeilK - 1
                        Seil = 1
                        print('Du hast ein Seil gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

            print()
            print('Der Waffenschmied bedankt sich für deinen Einkauf.')
            print()
            print('\033[4mVeränderte-CharakterAttribute:\033[0m')
            print()
            print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
            print('        ', 'Leben: momentan:', int(LEBS), ' maximal: ', int(LEBMAX))
            print('        ', 'Agilität: momentan:', int(AGS), ' maximal: ', int(AGSMAX))
            print('\n')
            print('Nun bist du bereit weiterzureisen'
                  'Du schaust auf die Karte. Bei der nächsten Abzweigung musst du rechts. Wenn du diesem Weg dann '
                  'weiter folgst, bist du schon am Fuße des Everest. Der Weg bis dahin verläuft Reibungslos. Keine Banditen,'
                  ' keine Magischen Kreaturen, und auch sonst keine negativen Überraschungen. Als du den Everest erreichst machst du dich bereit für den Aufstieg.')
            print('\n')
            Everest = 1

        if int(EH) == 3:
            print('Also reisen du und der Händler gemeinsam weiter. Ein bisschen Gesellschaft mach die Reise auch etwas spannender'
                  ' und die Zeit vergeht wie im Flug. Als ihr zur Abzweigung des Königsweges nach Freiburg kommt, blockiert ein Elite-Barbar den Weg.'
                  ' Vermutlich will er Händler abfangen, die Ihre Waren nach Freiburg bringen wollen. Um in die Stadt zu kommen musst du ihn aus dem '
                  'Weg räumen. Da er das letzte Hinderniss ist, welches deinem Versprechen den Händler sicher nach Freiburg zu eskortieren, im Wege steht,'
                  ' suchst du dir schon jetzt deine Belohnung aus. Die erste Sache die du beim Händler kaufst ist gratis. Alles danach kostet.'
                  ' Der Händler hat 7 Dinge anzubieten:')
            print()
            print()
            print('[1] Zwei Große Lebenstränke [Kosten: 100 Gold pro stück]')
            print('[2] Arthurs Schwert (Angriff: +130%; MaximaleAgilität: -20%; Kritische Treffer: +20%;) [Kosten: 900 Gold]')
            print('[3] Elite Rüstung (MaximlesLeben: +60%; MaximaleAgilität: +20%; Kritische Treffer: +5%) [Kosten: 500 Gold]')
            print('[4] Gladiatorenhelm (MaximalesLeben: +30%; Kritsiche Treffer: +10%) [Kosten: 400 Gold]')
            print('[5] 10-mal Schadensverzauberung (Angriff: +5%) [Kosten: 50 Gold]')
            print('[6] 10-mal Kritische Treffer Verzauberung (Kritische Treffer: +3%) [Kosten: 50 Gold]')
            print('[7] Ein Kletterseil [Kosten: 10 Gold]')
            print()
            print('[Du hast ', Gold, ' Gold]')
            print()
            print('[Wenn du nichts mehr kaufen willst tippe [fertig] ein.]')
            print()
            Kauf = 0
            Geschenk = 1
            LT = 2
            AS = 1
            ER = 1
            GH = 1
            SV = 10
            KTV = 10
            SeilK = 1
            while Kauf != 'fertig' and Kauf != 'Fertig':
                Kauf = input('Was willst du Kaufen? (Zahlen zwischen [1] und [4]; [fertig] für beenden)')
                if Kauf == 'fertig' or Kauf == 'Fertig':
                    break
                if int(Kauf) == 1:
                    if Geschenk == 1:
                        Gold = Gold + 100
                    if LT == 0:
                        print('Der Händler hat keine Lebenstränke mehr.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if LT > 0 and Gold >= 100:
                        Gold = Gold - (100)
                        Geschenk = 0
                        LebenstränkeG = LebenstränkeG + 1
                        LT = LT - 1
                        print('Du hast einen Großen Lebenstrank gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 2:
                    if Geschenk == 1:
                        Gold = Gold + 900
                    if AS == 0:
                        print('Du hast das Arthurs Schwert schon gekauft.')
                    if Gold < 900:
                        print('Du hast nicht genügend Gold')
                    if AS > 0 and Gold >= 900:
                        Gold = Gold - (900)
                        Geschenk = 0
                        AS = AS - 1
                        print('Du hast das Arthurs Schwert gekauft.')
                        ATKS = ATKS + (ATKA * 2.3)
                        AGSMAX = AGSMAX * 0.8
                        AGS = AGS * 0.8
                        CK = CK + 20
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 3:
                    if Geschenk == 1:
                        Gold = Gold + 500
                    if ER == 0:
                        print('Du hast die Eliterüstung schon gekauft.')
                    if Gold < 500:
                        print('Du hast nicht genügend Gold')
                    if ER > 0 and Gold >= 500:
                        Gold = Gold - (500)
                        Geschenk = 0
                        ER = ER - 1
                        print('Du hast die Eliterüstung gekauft.')
                        LEBMAX = LEBMAX + (LEBA * 1.6)
                        CK = CK + 5
                        AGSMAX = AGSMAX * 1.2
                        AGS = AGS * 1.2
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 4:
                    if Geschenk == 1:
                        Gold = Gold + 400
                    if GH == 0:
                        print('Du hast den Gladiatorenhelm schon gekauft.')
                    if Gold < 400:
                        print('Du hast nicht genügend Gold')
                    if GH > 0:
                        Gold = Gold - (400)
                        Geschenk = 0
                        GH = GH - 1
                        LEBMAX = LEBMAX + (LEBA * 1.3)
                        CK = CK + 10
                        print('Du hast den Gladiatorenhelm gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 5:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if SV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if SV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        SV = SV - 1
                        ATKS = ATKS + (ATKA * 1.05)
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 6:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if KTV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if KTV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        KTV = KTV - 1
                        CK = CK + 3
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 7:
                    if Geschenk == 1:
                        Gold = Gold + 10
                    if SeilK == 0:
                        print('Der Händler hat kein Seil mehr übrig.')
                    if Gold < 10:
                        print('Du hast nicht genügend Gold')
                    if SeilK > 0:
                        Gold = Gold - (10)
                        Geschenk = 0
                        SeilK = SeilK - 1
                        Seil = 1
                        print('Du hast ein Seil gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

            print()
            print('Der Händler bedankt sich für deinen Einkauf.')
            print()
            print('\033[4mVeränderte-CharakterAttribute:\033[0m')
            print()
            print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
            print('        ', 'Leben: momentan:', int(LEBS), ' maximal: ', int(LEBMAX))
            print('        ', 'Agilität: momentan:', int(AGS), ' maximal: ', int(AGSMAX))
            print('\n')

            print('Jetzt bist du bereit den Elite-Barbaren anzugreifen. Du rennst auf ihn zu, und greifst ihn an.')
            print()
            Würfel = RNG(int(input('Würfel:')), 47)
            GegnerStats = Barbar(Würfel, 3)
            KAMPF = Kampf(Würfel, 'Elite-Barbar', GegnerStats, ATKS, LEBS, AGS, CK)
            if KAMPF[0] == 'tot':
                CHECKOBDULEBST = 1
                break
            Kampfvariable = Kampfvariable + 1
            ATKS = KAMPF[1]
            LEBS = KAMPF[2]
            AGS = KAMPF[3]
            print('Du hast den Elitebarbaren erfolgreich besiegt. Der Händler kann nun gefahrenlos nach Freiburg. Ihr verabschiedet euch,'
                  ' und jeder geht seines Weges. Du schaust auf die Karte. Bei der nächsten Abzweigung musst du rechts. Wenn du diesem Weg dann '
                  'weiter folgst, bist du schon am Fuße des Everest. Der weg bis dahin verläuft Reibungslos. Keine Banditen,'
                  ' keine Magischen Kreaturen, und auch sonst keine negativen Überraschungen. Als du den Everest erreichst machst du dich bereit für den Aufstieg.')
            print('\n')
            Everest = 1

    if EV == 2:
        if Kampfvariable == 1:
            print()
            print('Wie erwartet ist der Weg sehr anstengend. Immer wieder musst du Gestrüpp durchschneiden, oder über kleinere Hindernisse wie Baumstämme drüberklettern.'
                  ' Als sich der Tag langsam dem Ende zuneigt merkst du wie erschöpft du bist. Du schaust auf die Karte. Wärst du entlang des Königsweges gegangen '
                  'wäre der Weg sicher nicht so anstrengend. Trotzdem glaubst du das der Schimmerweg die bessere Wahl war. '
                  'Du musst dich beeilen um deine geliebte Liana zu retten, da kannst du es dir nicht leisten den langen gemütlichen Weg zu nehmen.'
                  ' Mittlerweile ist es dunkel geworden.Du entscheidest dich einen Schlafplatz etwas abseits des Weges zu suchen.')
            print()
            print('[Nach dem langen Marsch ist deine Agilität um 50 Prozent gesunken]')
            AGS = AGS * 0.5
            print()
            print('Als du durch das Gestrüpp gehst bemerkst du ein Licht. Vermutlich hat hier noch jemand sein Lager aufgeschlagen. '
                  'Du könntest nachsehen denkst du. Wenn es ein Händler ist, kannst du Möglicherweise etwas zur Stärkung kaufen, und etwas freundliche Gesellschaft kann schön sein'
                  ' und bringt Sicherheit. Aber falls es ein Feind ist müsstest du möglicherweise Kämpfen, und da du noch geschwächt bist vom letzten Kampf,'
                  ' überstehst du das möglicherweise nicht.')
            print()

        if Kampfvariable == 0:
            print()
            print('Wie erwartet ist der Weg sehr anstengend. Immer wieder musst du Gestrüpp durchschneiden, oder über kleinere Hindernisse wie Baumstämme drüberklettern.'
                  ' Als sich der Tag langsam dem Ende zuneigt merkst du wie erschöpft du bist. Du schaust auf die Karte. Wärst du entlang des Königsweges gegangen '
                  'wäre der Weg sicher nicht so anstrengend. Trotzdem glaubst du das der Schimmerweg die bessere Wahl war. '
                  'Du musst dich beeilen um deine geliebte Liana zu retten, da kannst du es dir nicht leisten den langen gemütlichen Weg zu nehmen.'
                  ' Mittlerweile ist es dunkel geworden.Du entscheidest dich einen Schlafplatz etwas abseits des Weges zu suchen.')
            print()
            print('[Nach dem langen Marsch ist deine Agilität um 50 Prozent gesunken]')
            AGS = AGS * 0.5
            print()
            print('Als du durch das Gestrüpp gehst bemerkst du ein Licht. Vermutlich hat hier noch jemand sein Lager aufgeschlagen. '
                  'Du könntest nachsehen denkst du. Wenn es ein Händler ist, kannst du Möglicherweise etwas zur Stärkung kaufen, und etwas freudnliche Gesellschaft kann schön sein'
                  ' und bringt Sicherheit. Aber falls es ein Feind ist müsstest du möglicherweise Kämpfen. Wofür entscheidest du dich?')
            print()

        E = input('Wofür entscheidest du dich? ([1] für nachsehen; [2] für nicht nachsehen)')
        print('\n')
        if int(E) == 1:
            print('\033[1mDu entscheidest dich nachzusehen und gehst vorsichtig auf das Licht zu.\033[0m')
            Würfel = RNG(int(input('Würfel:')), 29)
            Was = Begegnung(Würfel, 80, 20, 0)

            if Was == 'Feind':
                GegnerStats = Kobold(Würfel, 1)
                print()
                print('Oh Nein, hättest du lieber nicht nachgesehen, dann  könntest du jetzt einfach friedlich schlafen. '
                      'Zu deinem Pech triffst du auf einen Kobold, der bereit ist sich zu verteidigen. Er schießt mit seiner Steinschleuder auf dich.')
                Würfel = RNG(int(input('Würfel:')), 24)
                Ausweichen = AgilitätstestS(Würfel, AGS, GegnerStats)
                if Ausweichen == 'treffer':
                    print('Nach dem langen Marsch bist du wohl entwas eingerostet. Der Kobold trifft dich mit der Steinschleuder.')
                    print()
                    print('[Dein Leben sinkt um 5%]')
                    LEBS = LEBS * 0.95
                    print('[Deine Agilität um 10%]')
                    AGS = AGS * 0.9
                if Ausweichen == 'verfehlt':
                    print()
                    print('Trotz des sehr anstrengenden Tages bisher,  reagierst schnell und kannst dem Schuss ausweichen.')
                print()
                print('Du stürmst au den Kobold zu.')
                KAMPF = Kampf(Würfel, 'Kobold', GegnerStats, ATKS, LEBS, AGS, CK)
                if KAMPF[0] == 'tot':
                    CHECKOBDULEBST = 1
                    break
                Kampfvariable = Kampfvariable + 1
                ATKS = KAMPF[1]
                LEBS = KAMPF[2]
                AGS = KAMPF[3]
                print('Du bist völlig fertig. Wenn du morgen keinen Händler findest hältst du nicht mehr lange durch. Du scheinst dich der Höhle zu nähern, denn '
                      'Kobolde sind magische Wesen und laufen eigentlich nicht einfach so herum. Wenn du die Höhle des Drachen erreichst wirst du bestimmt noch '
                      'weiteren magischen Wesen begegnen. Einen Voteil hatte der Kampf aber: Du hast '
                      'ein fertig gerichtetes Lager, mit Lagerfeuer. In der Hoffnung etwas nützliches zu finden, durchsuchst du die Sachen des Kobolds. '
                      'Und tatsächlich wirst du fündig! Ein mittlerer Lebenstrank, ein kleiner Schadenstrank, und etwas Gold. Nichts besonderes, aber eine willkommene Hilfe.')
                print()
                print('[20%, deiner Lebenspunkte werden wiederhergestellt.]')
                LEBS = LEBS + abs(LEBMAX - LEBS) * 0.5
                print('[Dein Schaden erhöht sich um 10%]')
                ATKS = ATKS * 1.1
                print('[Du hast 100 Goldmünzen gefunden]')
                Gold = Gold + 100
                print()
                print('Jetzt wird es aber Zeit zu schlafen. Du suchst dir ein bequemes Plätzchen am Lagerfeuer und schläfst ein.')
                print()
                print('Als du am nächsten morgen aufwachst steht die Sonne bereits sehr hoch am Himmel. Du hast den Schlaf wohl gebraucht.'
                      'Über Nacht sind deine Wunden auch etwas verheilt.')
                print()
                print('[Deine Agilität ist vollständig regeneriert.]')
                AGS = AGSMAX
                print('[Dein Leben ist um 10%, regeneriert]')
                LEBS = LEBS + (LEBA - LEBS) * 0.1
                print('\n')

            if Was == 'Händler':
                Händlervariable = Händlervariable + 1
                print()
                print('Zum Glück! Es ist ein Händler. Auf Banditen hattest du gar keinen Bock. Der Händler begrüßt dich, und du frägst ihn, '
                      'ob du dich ihm für diese Nacht anschließen kannst. Der Händler hat nichts dagegen, und bietet dir an sich seine Waren anzusehen.'
                      'Der Händler hat 5 Dinge zur Auswahl: ')
                print()
                print('[1] Zwei Große Lebenstränke [Kosten: 100 Gold pro Stück]')
                print('[2] Ein Langschwert (Angriff: +60%; MaximaleAgilität: -10%;) [Kosten: 400 Gold]')
                print('[3] Ein Magisches Kurzschwert (Angriff: + 30%; MaximaleAgilität: +10%; Kritische Treffer: +10%) [Kosten: 500 Gold]')
                print('[4] Ein Silberner Barbarenhelm (Leben: +30%) [Kosten: 300 Gold]')
                print('[5] Zwei Große Agilitätstränke [Kosten: 50 Gold pro Stück]')
                print()
                print('[Du hast ', Gold, ' Gold]')
                print()
                print('[Wenn du nichts mehr kaufen willst tippe "fertig" ein.]')
                print()
                Kauf = 0
                LT = 2
                LS = 1
                MKS = 1
                SBH = 1
                AGT = 2
                while Kauf != 'fertig' and Kauf != 'Fertig' and Gold > 0:
                    Kauf = input('Was willst du Kaufen? (Zahlen zwischen [1] und [4]; [fertig] für beenden)')
                    if Kauf == 'fertig' or Kauf == 'Fertig':
                        break
                    if int(Kauf) == 1:
                        if LT == 0:
                            print('Der Händler hat keine Lebenstränke mehr.')
                        if Gold < 100:
                            print('Du hast nicht genügend Gold')
                        if LT > 0 and Gold >= 100:
                            Gold = Gold - 100
                            LebenstränkeG = LebenstränkeG + 1
                            LT = LT - 1
                            print('Du hast einen Großen Lebenstrank gekauft.')
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 2:
                        if LS == 0:
                            print('Du hast das Langschwert schon gekauft.')
                        if Gold < 400:
                            print('Du hast nicht genügend Gold')
                        if LS > 0 and Gold >= 400:
                            Gold = Gold - 400
                            LS = LS - 1
                            print('Du hast das Langschwert gekauft.')
                            ATKS = ATKS * 1.6
                            AGSMAX = AGSMAX * 0.9
                            AGS = AGS * 0.9
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 3:
                        if MKS == 0:
                            print('Du hast das Magische Kurzschwert schon gekauft.')
                        if Gold < 500:
                            print('Du hast nicht genügend Gold')
                        if MKS > 0 and Gold >= 500:
                            Gold = Gold - 500
                            MKS = MKS - 1
                            print('Du hast das magische KUrzschwert gekauft.')
                            ATKS = ATKS * 1.30
                            CK = CK + 10
                            AGSMAX = AGSMAX * 1.1
                            AGS = AGS * 1.1
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 4:
                        if SBH == 0:
                            print('Du hast den silbernen Barbarenhelm schon gekauft.')
                        if Gold < 300:
                            print('Du hast nicht genügend Gold')
                        if SBH > 0:
                            Gold = Gold - 300
                            SBH = SBH - 1
                            print('Du hast den silbernen Barbarenhelm gekauft.')
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                    if int(Kauf) == 5:
                        if AGT == 0:
                            print('Der Händler hat keine Lebenstränke mehr.')
                        if Gold < 50:
                            print('Du hast nicht genügend Gold')
                        if AGT > 0 and Gold >= 50:
                            Gold = Gold - 50
                            AgilitätstränkeG = AgilitätstränkeG + 1
                            AGT = AGT - 1
                            print('Du hast einen Großen Lebenstrank gekauft.')
                            print('[Du hast noch ', Gold, ' Gold]')
                            print()

                print()
                print('Der Händler bedankt sich für deinen Einkauf.')
                print()
                print('\033[4mVeränderte-CharakterAttribute:\033[0m')
                print()
                print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
                print('        ', 'Leben: momentan:', int(LEBS), ' maximal: ', int(LEBMAX))
                print('        ', 'Agilität: momentan:', int(AGS), ' maximal: ', int(AGSMAX))
                print('\n')
                if int(LEBS) != int(LEBMAX) and LebenstränkeG > 0:
                    print(' Du bist verletzt: Leben:', LEBS, '/', LEBMAX)
                    Konsum = input('Willst du einen Lebenstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
                    if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                        print()
                        print('Du entscheidest dich dazu einen Großen Heiltrank zu trinken.')
                        print()
                        print('[Dein volles Leben wird wiederhergestellt]')
                        print()
                        LEBS = LEBMAX
                        LebenstränkeG = LebenstränkeG - 1
                    if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                        print()
                        print(' Du entscheidest dich dagegen einen Heiltrank zu trinken.')
                        print()

                if int(AGS) != int(AGSMAX) and AgilitätstränkeG > 0:
                    print(' Du bist erschöpft: Agilität:', AGS, '/', AGSMAX)
                    Konsum = input('Willst du einen Agilitätstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
                    if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                        print()
                        print('Du entscheidest dich dazu einen Großen Agilitätstrank zu trinken.')
                        print()
                        print('[Deine volle Agilität wird wiederhergestellt]')
                        print()
                        AgilitätstränkeG = AgilitätstränkeG - 1
                        AGS = AGSMAX
                    if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                        print()
                        print(' Du entscheidest dich dagegen einen Agilitätstrank zu trinken.')
                        print()
                print('Du und der Händler unterhaltet euch noch ein Weilchen, und geht dann irgendwann schlafen.')
                print()
                print('Als du am nächsten Morgen aufwachst ist der Händler bereits weg. Du hast den Schlaf wohl wirklich gebraucht.')
                print()
                print('[Deine Agilität ist vollständig regeneriert.]')
                AGS = AGSMAX
                if LEBS < LEBMAX:
                    print()
                    print('[Dein Leben ist um 10%, regeneriert]')
                    LEBS = LEBS + (LEBA - LEBS) * 0.1
                print('\n')

        if int(E) == 2:
            print()
            print('Du entscheidest dich lieber kein Risiko einzugehen, und läufst noch ein kleines Stückchen weiter von dem Licht weg.'
                  ' Du findest eine kleine Einbuchtung in einem Felsen, und entschließt dich hier dein Lager aufzuschlagen. '
                  ' Du willst dein Lagerfeuer machen, doch dann fällt die ein wie leicht doch das Licht des Unbekannten zu sehen war. '
                  ' Ob das eine Gute idee Ist?')
            print()
            Lagerfeuer = input('Willst du ein Lagerfeuer machen? ([Ja] oder [Nein] eintippen)')
            if Lagerfeuer == 'Nein' or Lagerfeuer == 'NEIN' or Lagerfeuer == 'NEin' or Lagerfeuer == 'neIN' or Lagerfeuer == 'nEIn' or Lagerfeuer == 'nEin' or Lagerfeuer == 'neIn' or Lagerfeuer == 'neiN':
                print('\033[1mDu entscheidest dich lieber kein Lagerfeuer zu machen, um keine Aufmerksamkeit auf dich zu ziehen.\033[0m')
                print()
                print('Das wird eine kalte Nacht, aber dafür hoffentlich eine Nacht ohne böse Überraschungen. Du legst dich schlafen.')
            if Lagerfeuer == 'Ja' or Lagerfeuer == 'jA' or Lagerfeuer == 'JA' or Lagerfeuer == 'ja':
                print('\033[1mDu entscheidest dich dafür ein Lagerfeuer zu machen.\033[0m')
                print()
                print('Du willst unbedingt einen erholsamen Schlaf, denn du brauchst deine Kräfte. Du hast noch eine lange Reise vor dir.'
                      ' Du entfachst also ein Lagerfeuer. Du genießt noch etwas die angenehme Wärme, bevor du friedlich einschläfst.')
                print()
                Würfel = RNG(int(input('Würfel:')), 1)
                Was = Begegnung(Würfel, 70, 0, 30)
                if Was == 'Feind':
                    print('Du wachst in der Nacht auf, weil du ein Rascheln im Gestrüpp hörst. Du schaust dich vorsichtig um, und entdeckst einen Kobold, '
                          'der deine Sachen durchwühlt. Du könntest ihn ignorieren um einen Kampf zu vermeiden, oder ihn angreifen. '
                          'Was tust du?')
                    print()
                    EK = input('[1] Du greifst ihn an; [2] Du ignorierst ihn.')
                    print()
                    if int(EK) == 1:
                        print('\033[4mDu entscheidest dich dazu den Kobold anzugreifen. Du springst auf, und greifst den Kobold an.\033[0m')
                        GegnerStats = Kobold(Würfel, 2)
                        Würfel = RNG(int(input('Würfel:')), 1)
                        KAMPF = Kampf(Würfel, 'Kobold', GegnerStats, ATKS, LEBS, AGS, CK)
                        if KAMPF[0] == 'tot':
                            CHECKOBDULEBST = 1
                            break
                        Kampfvariable = Kampfvariable + 1
                        ATKS = KAMPF[1]
                        LEBS = KAMPF[2]
                        AGS = KAMPF[3]
                        print('Zum Glück bist du rechtzeitig aufgewacht, sonst hätte das ganz anders ausgehen können.'
                              ' Du durchsuchst den Kobold und findest sehr viel Gold. Du bist wohl nicht der erste, den er ausgeraubt hat.'
                              ' Völlig erschöpft legst du dich schlafen.'
                              ' Hoffentlich war das die einzige Überraschung diese Nacht.')
                        print()
                        print('[Du hast 250 Gold erhalten]')
                        print()
                        Gold = Gold + 250
                    if int(EK) == 2:
                        print('Du ignorierst den Kobold um keinen Kampf zu provozieren, und den Händler nich zu gefährden, bist aber bereit falls dich der Kobold angreifen sollte.')
                        print('Als der Kobold im dunklen Wald verschwindet, stehst du auf um zu gucken ob dir etwas fehlt. Und tatsächlich,'
                              ' der Kobold hat dir 100 Gold gestohlen. Der Händler weiß zu schätzen, dass du das wegen ihm getan hast, um sein Leben nicht in Gefahr zu bringen.'
                              ' Als dankeschön ersetzt er dir das gestohlene Gold und schenkt dir einen einfachen Verzauberungstrank für deine Rüstung.')
                        print()
                        print('[Dein Angriff erhöht sich um 10%]')
                        ATKS = ATKS + (ATKA * 1.1)
                        print('[Dein Leben erhöht sich um 10%]')
                        LEBS = LEBS + (LEBA * 1.1)
                        print('[Deine Agilität erhöht sich um 10%]')
                        AGS = AGS + (AGSMAX * 1.1)
                        print('[Deine Kritische Trefferchance erhöht sich um 5%]')
                        CK = CK + 5
                        print()
                        print('Du bedankst dich und ihr geht beide schlafen.')

                if Was == 'Nichts':
                    print('Die Nacht verläuft ruhig. Durch das Lagerfeuer ist es schön warm, und du kannst dich gut erholen')
                    print()
                print('\n')
                print('Als du am nächsten Morgen aufwachst ist der Händler bereits weg. Du hast den Schlaf wohl wirklich gebraucht.')
                print()
                print('[Deine Agilität ist vollständig regeneriert.]')
                AGS = AGSMAX
                if LEBS < LEBMAX:
                    print()
                    print('[Dein Leben ist um 10%, regeneriert]')
                    LEBS = LEBS + (LEBMAX - LEBS) * 0.1
                print('\n')
        print('Du packst deine Sachen zusammen, schnallst dein Schwert um, und machst dich wieder auf den Weg. Du schaust auf die Karte:'
              ' Wenn alles nach Plan läuft solltest du gegen Sonnenuntergang am Fuße des Everest ankommen. Und lange läuft auch alles nach Plan.'
              ' Du merkst wie das Klima kühler wird. Du scheinst dich dem Berg zu nähern. Auch wird der Weg immer breiter und besser begehbar. Wenn du dich umsiehst siehst du immer wieder blaue '
              'Punkte aufleuchten in den Wäldern abseits des Weges. Das müssen die Feen sein von denen dir dein Vater als Kind erzählt hat. '
              'Ja. Die Magie wird definitiv stärker, die Höhle des Drachen kann nicht mehr so weit sein. Die Wahrscheilichkeit auf magische Wesen '
              ' wie Kobolde, Hexen, Wichtel, Steingolems und was es sonst noch alles gibt, zu treffen ist stark erhöht. Und die meisten dieser Wesen sind nicht friedfertig.'
              ' Zur Sicherheit hältst du dein Schwert griffbereit.')
        print()
        print('Als du so vor dich hinmarschierst, hörst du eine Kutsche hinter dir. Es ist ein Händler. Doch du merkst das etwas nicht stimmt.'
              ' Neben dem Händler am Wegesrand wackeln die Bäume, raschelt das Gebüsch und hörst du Gelächter. Das sind doch Wichtel! Geldgierige kleine Biester.'
              ' Sie halten nicht viel aus, aber sind flink, und wissen wie man mit einem Dolch umgeht. Normalerweise greifen Wichtel nicht von selbst an,'
              ' aber wenn sie Gold riechen gibt es kein halten mehr. Sie wollen sicher den Händler überfallen!')
        print()
        print('Was tust du?')
        print()
        print('[Du kannst deine Charakterattribute gleich mit "Stats" eintippen, einsehen um dir bei deiner Entscheidungsfindung zu helfen.]')
        print()
        print('[1] Du versuchst dem Händler zu helfen.')
        print('[2] Du hilfst dem Händler nicht.')
        print('[[Stats] Charakteattribute einsehen.]')
        print('\n')
        EH = 0
        while EH != '1' and EH != '2':
            EH = input('Entscheide dich!:')
            if EH == 'stats' or EH == 'Stats':
                print('\033[4mCharakter Attribute:\033[0m')
                print()
                print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
                print('        ', 'Leben: ', int(LEBS), '/', int(LEBMAX))
                print('        ', 'Agilität: ', int(AGS), '/', int(AGSMAX))
                print('\n')

        while int(EH) == 1:
            print('Du versuchst den Händer mit rufen zu warnen. Doch im selben moment starten die Wichtel ihren überfall. Zum '
                  'Glück hat fast jeder Händler immer einen persönlichen Beschützer dabei, weil alleine zu Reisen als Händler'
                  ' quasi Selbstmord ist. Der Beschützer kann viele der Wichtel abwehren. Doch kurz bevor du die Kutsche erreichst wird'
                  ' Er vom Anführer der Wichtelbande, welcher deutlich größer und stärker als die anderen wirkt, brutal niedergestreckt.'
                  ' Als dieser sich dem dem Händler zuwenden will, kannst du gerade noch dazwischen springen. Doch jetzt stehst du dem Rießigen Wichtel gegenüber.'
                  ' Noch kannst du fliehen, und deine eigene Haut retten. Wie eintscheidest du dich?')
            print()

            EH2 = input('[1] Du hilfst dem Händler; [2] Du rettest dich selbst:')
            if int(EH2) == 1:
                print()
                print('\033[4mDu greifst den Wichtelbandenanführer an.\033[0m')
                print()
                Würfel = RNG(int(input('Würfel:')), 49)
                GegnerStats = Wichtel(Würfel, 2)
                print(GegnerStats[3])
                KAMPF = Kampf(Würfel, 'Rießenwichtel', GegnerStats, ATKS, LEBS, AGS, CK)
                if KAMPF[0] == 'tot':
                    CHECKOBDULEBST = 1
                    break
                Kampfvariable = Kampfvariable + 1
                ATKS = KAMPF[1]
                LEBS = KAMPF[2]
                AGS = KAMPF[3]
                print('Der Händler ist dir unglaublich dankbar, wärst du nicht gekommen wäre er mit Sicherheit gestorben.'
                      'Der Händler schenkt dir einen Großen Heiltrank und einen Großen Agilitätstrank, welche du sofort trinkst.')
                print()
                print('[Dein Leben wurde vollständig wiederhergestellt]')
                print('[Deine Agilität wurde vollständig wiederhergestellt]')
                LEBS = LEBMAX
                AGS = AGSMAX
                print()
                print('Da nun der Beschützer des Händlers gestorben ist, bittet der Händler dich sein neuer Beschützer zu werden.'
                      ' Du wirst sehr gut bezahlt werden meint der Händler. Du erklärst Ihm dein Dilemma mit deiner Frau, dass du unbedingt'
                      ' diesen Drachen besiegen musst, und dass du keine Zeit dafür hast. Der Händer bittet dich ihn wenigstens bis zur nächsten Siedlung'
                      ' zu begleiten, wo er einen neuen Beschützer anheuern könne. Als Belohnung bekämst du einen Großen Heiltrank, und dürftest dir eine Sache'
                      ' aus seinem Laden als geschenk aussuchen. Was tust du?')
                print()
                EH3 = input('[1] Du nimmst das Angebot an; [2] Du lehnst das Angebot ab')
                print()
                print('\n')
                if int(EH3) == 1:
                    print('\033[1mDu nimmst das Angebot des Händlers an. Da das nächste Dorf (Freiburg) sowieso auf dem Weg liegt, verschwendest du auch keine Zeit.\033[0m')
                    print('\n')
                    EH = 3
                if int(EH3) == 2:
                    print('Du wünschst dem Händler alles Gute auf seiner Reise, aber lehnst das Angebot ab. Du willst lieber'
                          ' nicht in die Zielscheibe weiterer Gegner geraten.')
                    print('\n')
                    EH = 4
                    break

            if CHECKOBDULEBST == 1:
                break

            if int(EH2) == 2:
                EH = 2
                print('Du entscheidest dich dazu deine eigene Haut zu retten. Du weißt nicht ob du den Wichtelanführer besiegen kannst, und '
                      'musst auch an das Leben deiner geliebten Liana denken. Du weichst dem Schlag des Wichtels aus, und rennst um dein Leben.')
                print('\n')
        if CHECKOBDULEBST == 1:
            break
        if int(EH) == 2:
            print('Du rennst um so weit weg wie möglich zu kommen. Als du glaubst weit genug weg zu sein, setzt du deine Reise in normalem '
                  'Tempo fort.')
            print()
        if int(EH) == 4 or int(EH) == 2:
            print('Du schaust auf die Karte. Du musst dem Weg weiter folgen bis nach Freiburg. Hier musst du dann von dem'
                  ' Königsweg eine Abzweigung zum Everest nehmen. Dann folgt noch ein Aufstieg bis zum Eingang der Höhle des Drachen.'
                  ' Die Reise bis zur Abzweigung nach Freiburg läuft ohne Zwischenfälle.')
            print()
            print('Als du zur Abzweigung des Schimmerpfades nach Freiburg kommst, blockiert ein Elite-Barbar den Weg.'
                  ' Vermutlich will er Händler abfangen, die Ihre Waren nach Freiburg bringen wollen. Um in die Stadt zu kommen musst du ihn aus dem '
                  'Weg räumen.')
            print('Du rennst auf ihn zu, und greifst ihn an.')
            print()
            Würfel = RNG(int(input('Würfel:')), 47)
            GegnerStats = Barbar(Würfel, 3)
            KAMPF = Kampf(Würfel, 'Elite-Barbar', GegnerStats, ATKS, LEBS, AGS, CK)
            if KAMPF[0] == 'tot':
                CHECKOBDULEBST = 1
                break
            Kampfvariable = Kampfvariable + 1
            ATKS = KAMPF[1]
            LEBS = KAMPF[2]
            AGS = KAMPF[3]
            print('Du duchstuchst den Elitebarbaren. Der Elitebarbar hat vermutlich schon ein paar Händler überfallen, denn du findest 300 Gold.')
            Gold = Gold + 300
            print('Als du in Freiburg ankommst suchst du nach einem Händler.'
                  ' Du brauchst unbedingt bessere Ausrüstung, wenn du den den Aufstieg überleben willst, denn in der Nähe von Gebirgen trifft man'
                  ' oft auf Golems, welche sehr Mächtige Gegner sind. Du suchst den Freiburger Waffenschmied auf, um zu schauen was er anzubieten hat.')
            print('Der Waffenschmied hat 7 Dinge im Angebot:')
            print()
            print()
            print('[1] Zwei Große Lebenstränke [Kosten: 100 Gold pro stück]')
            print('[2] Arthurs Schwert (Angriff: +130%; MaximaleAgilität: -20%; Kritische Treffer: +20%;) [Kosten: 900 Gold]')
            print('[3] Elite Rüstung (MaximlesLeben: +60%; MaximaleAgilität: +20%; Kritische Treffer: +5%) [Kosten: 500 Gold]')
            print('[4] Gladiatorenhelm (MaximalesLeben: +30%; Kritsiche Treffer: +10%) [Kosten: 400 Gold]')
            print('[5] 10-mal Schadensverzauberung (Angriff: +5%) [Kosten: 50 Gold]')
            print('[6] 10-mal Kritische Treffer Verzauberung (Kritische Treffer: +3%) [Kosten: 50 Gold]')
            print('[7] Ein Kletterseil [Kosten: 10 Gold]')
            print()
            print('[Du hast ', Gold, ' Gold]')
            print()
            print('[Wenn du nichts mehr kaufen willst tippe [fertig] ein.]')
            print()
            Kauf = 0
            Geschenk = 1
            LT = 2
            AS = 1
            ER = 1
            GH = 1
            SV = 10
            KTV = 10
            SeilK = 1
            while Kauf != 'fertig' and Kauf != 'Fertig':
                Kauf = input('Was willst du Kaufen? (Zahlen zwischen [1] und [4]; [fertig] für beenden)')
                if Kauf == 'fertig' or Kauf == 'Fertig':
                    break
                if int(Kauf) == 1:
                    if Geschenk == 1:
                        Gold = Gold + 100
                    if LT == 0:
                        print('Der Händler hat keine Lebenstränke mehr.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if LT > 0 and Gold >= 100:
                        Gold = Gold - (100)
                        Geschenk = 0
                        LebenstränkeG = LebenstränkeG + 1
                        LT = LT - 1
                        print('Du hast einen Großen Lebenstrank gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 2:
                    if Geschenk == 1:
                        Gold = Gold + 900
                    if AS == 0:
                        print('Du hast das Arthurs Schwert schon gekauft.')
                    if Gold < 900:
                        print('Du hast nicht genügend Gold')
                    if AS > 0 and Gold >= 900:
                        Gold = Gold - (900)
                        Geschenk = 0
                        AS = AS - 1
                        print('Du hast das Arthurs Schwert gekauft.')
                        ATKS = ATKS + (ATKA * 2.3)
                        AGSMAX = AGSMAX * 0.8
                        AGS = AGS * 0.8
                        CK = CK + 20
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 3:
                    if Geschenk == 1:
                        Gold = Gold + 500
                    if ER == 0:
                        print('Du hast die Eliterüstung schon gekauft.')
                    if Gold < 500:
                        print('Du hast nicht genügend Gold')
                    if ER > 0 and Gold >= 500:
                        Gold = Gold - (500)
                        Geschenk = 0
                        ER = ER - 1
                        print('Du hast die Eliterüstung gekauft.')
                        LEBMAX = LEBMAX + (LEBA * 1.6)
                        CK = CK + 5
                        AGSMAX = AGSMAX * 1.2
                        AGS = AGS * 1.2
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 4:
                    if Geschenk == 1:
                        Gold = Gold + 400
                    if GH == 0:
                        print('Du hast den Gladiatorenhelm schon gekauft.')
                    if Gold < 400:
                        print('Du hast nicht genügend Gold')
                    if GH > 0:
                        Gold = Gold - (400)
                        Geschenk = 0
                        GH = GH - 1
                        LEBMAX = LEBMAX + (LEBA * 1.3)
                        CK = CK + 10
                        print('Du hast den Gladiatorenhelm gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 5:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if SV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if SV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        SV = SV - 1
                        ATKS = ATKS + (ATKA * 1.05)
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 6:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if KTV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if KTV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        KTV = KTV - 1
                        CK = CK + 3
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 7:
                    if Geschenk == 1:
                        Gold = Gold + 10
                    if SeilK == 0:
                        print('Der Händler hat kein Seil mehr übrig.')
                    if Gold < 10:
                        print('Du hast nicht genügend Gold')
                    if SeilK > 0:
                        Gold = Gold - (10)
                        Geschenk = 0
                        SeilK = SeilK - 1
                        Seil = 1
                        print('Du hast ein Seil gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

            print()
            print('Der Waffenschmied bedankt sich für deinen Einkauf.')
            print()
            print('\033[4mVeränderte-CharakterAttribute:\033[0m')
            print()
            print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
            print('        ', 'Leben: momentan:', int(LEBS), ' maximal: ', int(LEBMAX))
            print('        ', 'Agilität: momentan:', int(AGS), ' maximal: ', int(AGSMAX))
            print('\n')
            print('Nun bist du bereit weiterzureisen'
                  'Du schaust auf die Karte. Bei der nächsten Abzweigung musst du rechts. Wenn du diesem Weg dann '
                  'weiter folgst, bist du schon am Fuße des Everest. Der Weg bis dahin verläuft Reibungslos. Keine Banditen,'
                  ' keine Magischen Kreaturen, und auch sonst keine negativen Überraschungen. Als du den Everest erreichst machst du dich bereit für den Aufstieg.')
            print('\n')
            Everest = 1

        if int(EH) == 3:
            print('Also reisen du und der Händler gemeinsam weiter. Ein bisschen Gesellschaft mach die Reise auch etwas spannender'
                  ' und die Zeit vergeht wie im Flug. Als ihr zur Abzweigung des Königsweges nach Freiburg kommt, blockiert ein Elite-Barbar den Weg.'
                  ' Vermutlich will er Händler abfangen, die Ihre Waren nach Freiburg bringen wollen. Um in die Stadt zu kommen musst du ihn aus dem '
                  'Weg räumen. Da er das letzte Hinderniss ist, welches deinem Versprechen den Händler sicher nach Freiburg zu eskortieren, im Wege steht,'
                  ' suchst du dir schon jetzt deine Belohnung aus. Die erste Sache die du beim Händler kaufst ist gratis. Alles danach kostet.'
                  ' Der Händler hat 7 Dinge anzubieten:')
            print()
            print()
            print('[1] Zwei Große Lebenstränke [Kosten: 100 Gold pro stück]')
            print('[2] Arthurs Schwert (Angriff: +130%; MaximaleAgilität: -20%; Kritische Treffer: +20%;) [Kosten: 900 Gold]')
            print('[3] Elite Rüstung (MaximlesLeben: +60%; MaximaleAgilität: +20%; Kritische Treffer: +5%) [Kosten: 500 Gold]')
            print('[4] Gladiatorenhelm (MaximalesLeben: +30%; Kritsiche Treffer: +10%) [Kosten: 400 Gold]')
            print('[5] 10-mal Schadensverzauberung (Angriff: +5%) [Kosten: 50 Gold]')
            print('[6] 10-mal Kritische Treffer Verzauberung (Kritische Treffer: +3%) [Kosten: 50 Gold]')
            print('[7] Ein Kletterseil [Kosten: 10 Gold]')
            print()
            print('[Du hast ', Gold, ' Gold]')
            print()
            print('[Wenn du nichts mehr kaufen willst tippe [fertig] ein.]')
            print()
            Kauf = 0
            Geschenk = 1
            LT = 2
            AS = 1
            ER = 1
            GH = 1
            SV = 10
            KTV = 10
            SeilK = 1
            while Kauf != 'fertig' and Kauf != 'Fertig':
                Kauf = input('Was willst du Kaufen? (Zahlen zwischen [1] und [4]; [fertig] für beenden)')
                if Kauf == 'fertig' or Kauf == 'Fertig':
                    break
                if int(Kauf) == 1:
                    if Geschenk == 1:
                        Gold = Gold + 100
                    if LT == 0:
                        print('Der Händler hat keine Lebenstränke mehr.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if LT > 0 and Gold >= 100:
                        Gold = Gold - (100)
                        Geschenk = 0
                        LebenstränkeG = LebenstränkeG + 1
                        LT = LT - 1
                        print('Du hast einen Großen Lebenstrank gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 2:
                    if Geschenk == 1:
                        Gold = Gold + 900
                    if AS == 0:
                        print('Du hast das Arthurs Schwert schon gekauft.')
                    if Gold < 900:
                        print('Du hast nicht genügend Gold')
                    if AS > 0 and Gold >= 900:
                        Gold = Gold - (900)
                        Geschenk = 0
                        AS = AS - 1
                        print('Du hast das Arthurs Schwert gekauft.')
                        ATKS = ATKS + (ATKA * 2.3)
                        AGSMAX = AGSMAX * 0.8
                        AGS = AGS * 0.8
                        CK = CK + 20
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 3:
                    if Geschenk == 1:
                        Gold = Gold + 500
                    if ER == 0:
                        print('Du hast die Eliterüstung schon gekauft.')
                    if Gold < 500:
                        print('Du hast nicht genügend Gold')
                    if ER > 0 and Gold >= 500:
                        Gold = Gold - (500)
                        Geschenk = 0
                        ER = ER - 1
                        print('Du hast die Eliterüstung gekauft.')
                        LEBMAX = LEBMAX + (LEBA * 1.6)
                        CK = CK + 5
                        AGSMAX = AGSMAX * 1.2
                        AGS = AGS * 1.2
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 4:
                    if Geschenk == 1:
                        Gold = Gold + 400
                    if GH == 0:
                        print('Du hast den Gladiatorenhelm schon gekauft.')
                    if Gold < 400:
                        print('Du hast nicht genügend Gold')
                    if GH > 0:
                        Gold = Gold - (400)
                        Geschenk = 0
                        GH = GH - 1
                        LEBMAX = LEBMAX + (LEBA * 1.3)
                        CK = CK + 10
                        print('Du hast den Gladiatorenhelm gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 5:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if SV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if SV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        SV = SV - 1
                        ATKS = ATKS + (ATKA * 1.05)
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 6:
                    if Geschenk == 1:
                        Gold = Gold + 50
                    if KTV == 0:
                        print('Der Händler hat keine Verzauberungen mehr übrig.')
                    if Gold < 50:
                        print('Du hast nicht genügend Gold')
                    if KTV > 0:
                        Gold = Gold - (50)
                        Geschenk = 0
                        KTV = KTV - 1
                        CK = CK + 3
                        print('Du hast eine Schadensverzauberung gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

                if int(Kauf) == 7:
                    if Geschenk == 1:
                        Gold = Gold + 10
                    if SeilK == 0:
                        print('Der Händler hat kein Seil mehr übrig.')
                    if Gold < 10:
                        print('Du hast nicht genügend Gold')
                    if SeilK > 0:
                        Gold = Gold - (10)
                        Geschenk = 0
                        SeilK = SeilK - 1
                        Seil = 1
                        print('Du hast ein Seil gekauft.')
                        print('[Du hast noch ', Gold, ' Gold]')
                        print()

            print()
            print('Der Händler bedankt sich für deinen Einkauf.')
            print()
            print('\033[4mVeränderte-CharakterAttribute:\033[0m')
            print()
            print('\033[4mAldric:\033[0m ', 'Angriff: ', int(ATKS))
            print('        ', 'Leben: momentan:', int(LEBS), ' maximal: ', int(LEBMAX))
            print('        ', 'Agilität: momentan:', int(AGS), ' maximal: ', int(AGSMAX))
            print('\n')
            print('Jetzt bist du bereit den Elite-Barbaren anzugreifen. Du rennst auf ihn zu, und greifst ihn an.')
            print()
            Würfel = RNG(int(input('Würfel:')), 47)
            GegnerStats = Barbar(Würfel, 3)
            KAMPF = Kampf(Würfel, 'Elite-Barbar', GegnerStats, ATKS, LEBS, AGS, CK)
            if KAMPF[0] == 'tot':
                CHECKOBDULEBST = 1
                break
            Kampfvariable = Kampfvariable + 1
            ATKS = KAMPF[1]
            LEBS = KAMPF[2]
            AGS = KAMPF[3]
            print('Du hast den Elitebarbaren erfolgreich besiegt. Der Händler kann nun gefahrenlos nach Freiburg. Ihr verabschiedet euch,'
                  ' und jeder geht seines Weges. Du schaust auf die Karte. Bei der nächsten Abzweigung musst du rechts. Wenn du diesem Weg dann '
                  'weiter folgst, bist du schon am Fuße des Everest. Der weg bis dahin verläuft Reibungslos. Keine Banditen,'
                  ' keine Magischen Kreaturen, und auch sonst keine negativen Überraschungen. Als du den Everest erreichst machst du dich bereit für den Aufstieg.')
            print('\n')
            Everest = 1

    if Everest == 1:
        print('Du suchst nach einem Weg nach oben, doch findest keinen. Der einzige Weg ist die Felswand hochzulettern.')
        print()
        if Seil == 1:
            print('Zum Glück hast du beim Händler ein Seil gekauft. Dadurch schaffst du es erfolgreich die Felswand hinaufzuklettern. '
                  'Die Kletterei ist unglaublich anstrengend, aber Dank des Seils machbar. Nach einer Stunde, erreichst du die Kante der '
                  'Klippe. Mit letzter Kraft ziehst du dich über die Kante, und hast endlich den Eingang zur Drachenhöhle erreicht.')
            print('\n')
        if Seil != 1:
            print('Da du kein Seil hast, hast du keine andere Wahl als einfach so hochzuklettern.')
            print()
            print(' Die ersten Meter kletterst du noch recht sicher. Doch je höher du kommst, um so Kälter wird es, und um so anstrengender wird es.'
                  ' Du spürst wie deine Kräfte schwinden. Du kannst die Höhle schon sehen, da rutschst du mit deinem rechten Fuß plötzlich ab.')
            print()
            Würfel = RNG(int(input('Würfel:')), 79)
            print()
            Überleben = Überlebenstest(Würfel, AGS, 60, 10)
            if Überleben == 'lebt':
                print('Du schaffst es dich gerade noch so abzufangen. Das war knapp!')
                if EV == 1:
                    print('Zum Glück hast du dich für den Königsweg entschieden, sonst hätte deine Kraft möglicherweise nicht ausgereicht'
                          ' und du wärst in die Tiefe gestürzt. Du kämpfst dich die letzten Meter nach oben, und ziehst dich mit letzter '
                          'Kraft über die Kante. Und da siehst du ihn endlich. Den Eingang zur Höhle des Drachen.')
                    print()
                    print('[Nach dem harten Aufstieg sinkt deine Agilität um 70%]')
                    AGS = AGS * 0.3
                    print('\n')
                if EV == 2:
                    print('Obwohl du dich für den anstrengenden Schimmerweg entschieden hattest, hast du noch genug Kraft dich die letzten Meter'
                          ' bis zur Klippenkante nach oben zu ziehen. Und da siehst du ihn endlich. Den Eingang zur Höhle des Drachen.')
                    print()
                    print('[Nach dem anstrengenden Aufstieg, sinkt deine Agilität um 90%]')
                    AGS = AGS * 0.1
                    print('\n')
            if Überleben == 'tot':
                print('Du schaffst es nicht mehr dich abzufangen. Du hast einfach nicht mehr genügend Restkraft. Während du in die Tiefe stürzt siehst du dein Leben an dir vorbeiziehen.'
                      ' Du denkst an deine Kindheit zurück. Wie schön friedlich es damals war, so völlig frei von'
                      ' Sorgen. Was für eine schönes Leben du mit deiner Frau Liana hattest, die darauf wartet, dass du zurück kommst um sie von diesem schrecklichen Schicksal zu befreien.'
                      ' Doch dazu wird es wohl nie kommen, denn jetzt ist es vorbei, ganz vorbei, und nichts auf dieser Welt kann das verhindern.')
                CHECKOBDULEBST = 1
                break
        print('Nach dieser Anstrengung würdest du am liebsten eine Pause machen, doch dazu kommst du nicht. Aus der Wand des Höhleneingangs'
              ' lösen sich große Gesteinsbrocken, welche sich langsam zusammenfügen. Du weißt was das ist. Du weißt was das bedeutet.'
              ' Ein Steingolem der den Eingang der Höhle bewacht. Golems halten sehr viel aus, und sind sehr stark, '
              'aber selbst ein Rentner ohne Beine kann ihnen problemlos davon rennen. Doch das bringt dir nicht viel,'
              ' denn du musst an ihm vorbei um in die Höhle zu gelangen.')
        print('\n')
        if int(LEBS) != int(LEBMAX) and LebenstränkeG > 0:
            print(' Du bist verletzt: Leben:', LEBS, '/', LEBMAX)
            Konsum = input('Willst du einen Lebenstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
            if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                print()
                print('Du entscheidest dich dazu einen Großen Heiltrank zu trinken.')
                print()
                print('[Dein volles Leben wird wiederhergestellt]')
                print()
                LEBS = LEBMAX
                LebenstränkeG = LebenstränkeG - 1
            if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                print()
                print(' Du entscheidest dich dagegen einen Heiltrank zu trinken.')
                print()

        if int(AGS) != int(AGSMAX) and AgilitätstränkeG > 0:
            print(' Du bist erschöpft: Agilität:', AGS, '/', AGSMAX)
            Konsum = input('Willst du einen Agilitätstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
            if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                print()
                print('Du entscheidest dich dazu einen Großen Agilitätstrank zu trinken.')
                print()
                print('[Deine volle Agilität wird wiederhergestellt]')
                print()
                AgilitätstränkeG = AgilitätstränkeG - 1
                AGS = AGSMAX
            if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                print()
                print(' Du entscheidest dich dagegen einen Agilitätstrank zu trinken.')
                print()
        print('Du greifst den Golem an.')
        Würfel = RNG(int(input('Würfel:')), 9)
        StatsGolem = Golem(Würfel, 3)
        KAMPF = Kampf(Würfel, 'Golem', StatsGolem, ATKS, LEBS, AGS, CK)
        if KAMPF[0] == 'tot':
            CHECKOBDULEBST = 1
            break
        Kampfvariable = Kampfvariable + 1
        ATKS = KAMPF[1]
        LEBS = KAMPF[2]
        AGS = KAMPF[3]
        print('Nun ist der Weg frei. Zeit die Höhle zu betreten, und den Drachen zu erlegen. Jetzt ist deine letzte Chance noch irgendwelche Tränke'
              ' zu trinken. Das ist der letzte Kampf.')
        print()
        if int(LEBS) != int(LEBMAX) and LebenstränkeG > 0:
            print(' Du bist verletzt: Leben:', LEBS, '/', LEBMAX)
            Konsum = input('Willst du einen Lebenstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
            if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                print()
                print('Du entscheidest dich dazu einen Großen Heiltrank zu trinken.')
                print()
                print('[Dein volles Leben wird wiederhergestellt]')
                print()
                LEBS = LEBMAX
                LebenstränkeG = LebenstränkeG - 1
            if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                print()
                print(' Du entscheidest dich dagegen einen Heiltrank zu trinken.')
                print()

        if int(AGS) != int(AGSMAX) and AgilitätstränkeG > 0:
            print(' Du bist erschöpft: Agilität:', AGS, '/', AGSMAX)
            Konsum = input('Willst du einen Agilitätstrank zu dir nehmen? ("Ja" oder "Nein" eintippen):')
            if Konsum == 'JA' or Konsum == 'ja' or Konsum == 'Ja' or Konsum == 'jA':
                print()
                print('Du entscheidest dich dazu einen Großen Agilitätstrank zu trinken.')
                print()
                print('[Deine volle Agilität wird wiederhergestellt]')
                print()
                AgilitätstränkeG = AgilitätstränkeG - 1
                AGS = AGSMAX
            if Konsum == 'Nein' or Konsum == 'NEIN' or Konsum == 'NEin' or Konsum == 'neIN' or Konsum == 'nEIn' or Konsum == 'nEin' or Konsum == 'neIn' or Konsum == 'neiN':
                print()
                print(' Du entscheidest dich dagegen einen Agilitätstrank zu trinken.')
                print()
        if LebenstränkeG <= 0:
            print()
            print('Du hast leider keine Lebenststränke mehr übrig. Du musst dich der Bestie wohl so stellen.')
            print()
        if AgilitätstränkeG <= 0:
            print()
            print('Du hast leider keine Agilitätstränke mehr übrig. Du musst dich der Bestie wohl so stellen.')
            print()
        print('Du betrittst langsam die Höhle. Deine Lange Reise hat genau zu diesem Punkt geführt.'
              ' Das ist die letzte Prüfung. Wenn du das schaffst ist Liana gerettet. Du dringst immer tiefer in die Höhle vor.')
        print()
        print('Du hörst ein rumpeln, die Höhle wackelt. Das muss der Drache sein. Du gehst weiter vorsichtig vorwärts. Und gelangst in einen Großen Raum.'
              ' Und da siehst du Ihn. Die Bestie, dessen Leben du beenden musst, um Lianas zu retten. Du nimmst deinen ganzen Mut zusammen. Und stürmst auf den Drachen zu.')
        Würfel = RNG(int(input('Würfel:')), 29)
        GegnerStats = Drache(Würfel, 3)
        KAMPF = Endkampf(Würfel, 'Drache', GegnerStats, ATKS, LEBS, AGS, CK)
        if KAMPF[0] == 'tot':
            CHECKOBDULEBST = 1
            break
        Kampfvariable = Kampfvariable + 1
        ATKS = KAMPF[1]
        LEBS = KAMPF[2]
        AGS = KAMPF[3]
        print('Du hast es geschafft! Du hast den Drachen besiegt. Liana ist gerettet!')
        CHECKOBDULEBST = 2
        break


if CHECKOBDULEBST == 1:
    print('\n\n\n')
    print('\033[4mGame Over\033[0m')

if CHECKOBDULEBST == 2:
    print('\n\n\n')
    print('\033[4mAls du von deiner langen Reise zurückkommst übereichst du das Drachenherz direkt den Heilern, welche aus der Magie'
          ' des Drachenherzens eine Medizin herstellen die Liana vor dem Tode bewahrt. Ihr lebt glücklich zusammen, bis ans Ende eurer Tage.\033[0m')
