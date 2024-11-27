deathmessage1 = str("Die Götter sind über deine Auswahl erzürnt und lassen dich von einem Blitz treffen. Starte das Programm erneut.")


def story_schatz():
    print("Ihr macht euch als Gruppe auf in den Wald hinein. Ihr kommt ziemlich schnell an eine Abzweigung.\nDie Gruppe will nach rechts, doch du bist dir sicher, dass ihr links müsst.\nZwischen euch kommt es zum Streit.")
    A4 = int(input("Möchtest du nach rechts mit der Gruppe oder alleine nach links gehen?\n1. Rechts\n2. Links\nWähle eine Option: "))
    if A4 == 1:
        print("Du gehst mit der Gruppe mit und streitest weiter mit ihnen.\nIrgendwann ist die Gruppe so genervt von dir, dass sie dich alleine zurück lassen.\nNach dem du einige Zeit orientierungslos im Wald herum gelaufen bist, legst du dich völlig erschöpft hin und schläfst ein.\nStarte das Programm erneut.")
    elif A4 == 2:
        print("Du gehst alleine nach links und findest nach ein paar Minuten die alte Burg, in der der Schatz sein soll.\nVor dir liegen 3 Gegenstände, du kannst jedoch nur eins davon tragen.")
        A41 = int(input("Welchen Gegenstand möchtest du wählen?\n 1. Einen Schlüssel\n 2. Ein Schwert \n 3. Eine Lammkeule\nDeine Wahl: "))
        if A41 == 1:
            print("Du hast den Schlüssel genommen und läufst in den Keller der Burg hinein. Vor dir erscheinen 2 Türen.\nDie Linke ist verschlossen und die Rechte ist offen.")
            A411 = int(input("Durch welche Tür möchtest du gehen?\n1. Links\n2. Rechts\nEntscheide weise: "))
            if A411 == 1:
                print("Du versuchst mit dem Schlüssel die linke Tür zu öffnen. Plötzlich öffnet sich eine Falltür unter dir und du stürzt in die Tiefe.\nDabei landest du unglücklich auf dem Kopf und du wirst ohnmächtig.\nStarte das Programm erneut.")
            elif A411 == 2:
                print("Du gehst durch die rechte Tür und stehst einem riesigen dreiköpfigen Hund gegenüber.\nMit dem Schlüssel kannst du dich nicht wehren. Der Hund gewinnt den Kampf und du fällst in ein Koma.\nStarte das Programm erneut")
            else:
                print(deathmessage1)
        elif A41 == 2:
            print("Du wählst das Schwert und läufst in den Keller der Burg hinein. Vor dir erscheint eine Tür. Dahinter befindet sich ein riesiger dreiköpfiger Hund.\nTrotz Schwert kannst du dich nicht gegen ihn durchsetzten und du verlierst den Kampf.\nAls der Hund sich von dir ablässt, bemerkst du, dass der Hund dich unglücklich erwischt hat.\nDu verlierst viel Blut und lehnst dich erschöpft an die Wand, bis du einnickst.\nStarte das Programm erneut.")
        elif A41 == 3:
            print("Du wählst die Lammkeule. Möchtest du sie essen?\n1. Ja\n2. Nein.")
            A413 = int(input("Wähle eine Option: "))
            if A413 == 1:
                print("Du isst die Keule und gehst anschließend in den Keller.\nVor dir erscheint eine Tür. Dahinter befindet sich ein riesiger dreiköpfiger Hund.\nOhne Lammkeule will der Hund nicht von dir ablassen und du verlierst den Kampf.\nAls der Hund dich endlich in Ruhe lässt, bemerkst du, dass der Hund dich unglücklich erwischt hat.\nDu verlierst viel Blut und lehnst dich erschöpft an die Wand, bis du einnickst.\nStarte das Programm erneut.")
            if A413 == 2:
                print("Du gehst mit der Lammkeule bewaffnet in den Keller. Vor dir erscheint eine Tür.\nDahinter befindet sich ein riesiger dreiköpfiger Hund.\nDu wirfst ihm die Lammkeule hin und er lässt dich an ihm vorbei.\nIn einer großen Kammer erwartet dich eine Kiste voller Gold.\nGlücklich ziehst du den Schatz an dem Hund vorbei aus der Burg.\nDort wirst du jedoch schon von der Schatzsucher-Gruppe erwartet.")
                A4131 = int(input("Möchtest du den Schatz mit ihnen teilen?\n1. Ja\n2. Nein\nWähle eine Option: "))
                if A4131 == 1:
                    print("Du gibst der Gruppe die Hälfte des Golds und ihr geht alle glücklich und reich zurück ins Dorf.\nE N D E")
                elif A4131 == 2:
                    print("Die Gruppe ist entzürnt und überwältigt und verletzt dich.\nOhne Geld und die Fähigkeit zu laufen, lassen sie dich bei der Burg.\nVöllig erschöpft von allen Geschehnissen schläfst du ein.\nStarte das Programm erneut.")
        else:
            print(deathmessage1)
    else:
        print(deathmessage1)


def story_voller_Tisch():
    print("Der Tisch erzählt von einem Schatz in der alten Burg und lädt dich ein mitzukommen.")
    A221 = int(input("Möchtest du mitkommen?\n1. Ja\n2. Nein\nEntscheide dich: "))
    if A221 == 1:
        story_schatz()
    elif A221 == 2:
        print("Nachdem die Gruppe den Schatz ohne dich suchen gegangen ist,\nverlässt du die Taverne und wirst überwältigt. Dabei verlierst du dein Bewusstsein.\nStarte das Programm erneut.")
    else:
        print(deathmessage1)


print("Du wachst auf. Langsam nimmst du deine Umgebung war.\nDir fehlt jeglicher Orientierungssinn.\nAber trotzdem fühlst du dich, als ob du schon einmal hiergewesen bist.\nDu überlegst, was du jetzt am besten machen solltest.\nDu hast drei Optionen:\n1. Spaziergang \n2. Taverne\n3. Rückwärtssalto")
A1 = int(input("Wähle eine Option: "))
if A1 == 1:
    print("Langsam beginnst du deinen Spaziergang.\nNach einiger Zeit kommst du an eine Kreuzung.\nDu kannst 1. links, 2. rechts oder 3. geradeaus gehen.")
    A11 = int(input("Wohin möchtest du weiterlaufen? "))
    if A11 == 1:
        print("Der Weg führt dich in einem Kreis zurück zu deinem Startpunkt.\nVollkommen erschöpft legst du dich auf den Boden und schläfst ein.\nStarte das Programm erneut.")
    elif A11 == 2:
        print("Du folgst dem Weg geradeaus. Nach wenigen Minuten erhebt sich vor dir eine Kirche.\nAus einiger Entfernung hörst du Geflüster.\nMöchtest du die Kirche trotzdem betreten?\n1. Ja\n2. Nein")
        A112 = int(input("Wähle weise: "))
        if A112 == 1:
            print("Du betrittst die Kirche und betest. Nach einer schönen Beteinheit begibst du dich auf den Heimweg.\nDabei wirst du ohne Vorwarnung hinterrücks überwältigt. Starte das Programm erneut.")
        elif A112 == 2:
            print("Du gehst dem Geräusch nach und siehst eine Gruppe an Abenteurern.\nSie erzählen dir von einem großen Schatz in der alten Burg.\nNach kurzer Überlegung schließt du dich ihnen an und gehst mit auf Schatzsuche!")
            story_schatz()
        else:
            print(deathmessage1)
    elif A11 == 3:
        print("Du gehst in den Wald hinein und siehst einen magischen Pilz, der sofort deine Aufmerksamkeit auf sich zieht.")
        A113 = int(input("Möchtest du den Pilz essen?\n1. Ja\n2. Nein\nWähle eine Option: "))
        if A113 == 1:
            print("Du isst den Pilz und fühlst dich auf einmal ganz komisch.\nDu denkst noch:'Der Pilz war wohl nicht essbar', als du langsam das Bewusstsein verlierst.\nStarte das Programm erneut.")
        elif A113 == 2:
            print("Du wendest deine Aufmerksamkeit wieder dem Wald zu.\nAuf einmal hörst du eine Gruppe an Abenteurern. Sie erzählen dir von einem von Legenden umwobenen Schatz.\nNach kurzem Überlegen schließt du dich ihnen an.")
            story_schatz()
        else:
            print(deathmessage1)
    else:
        print(deathmessage1)
elif A1 == 2:
    print("Du gehst in die Taverne. Dort gibt es noch freie Plätze an\n1. der Bar\n2. einem vollen Tisch\n3. einem leeren Tisch.")
    A2 = int(input("Wähle, wo du sitzen möchtest: "))
    if A2 == 1:
        print("Du setzt dich an die Bar und siehst eine Schale voll leckerer Nüsse")
        A21 = int(input("Möchtest du die Nüsse essen?\n1. Ja\n2. Nein\n. Wähle eine Option aus: "))
        if A21 == 1:
            print("Du fängst an die Nüsse zu essen. Nach ein paar Minuten fühlst du dich dann ganz komisch.\n Du reagierst allergisch auf die Nüsse und verlierst dein Bewusstsein.\n Starte das Programm erneut.")
        elif A21 == 2:
            print("Nach einer Weile wird dir langweilig und du setzt dich an den vollen Tisch.")
            story_voller_Tisch()
        else:
            print(deathmessage1)
    elif A2 == 2:
        print("Du setzt dich an den vollen Tisch.")
        story_voller_Tisch()
    elif A2 == 3:
        print("Du setzt dich an den leeren Tisch.")
        A23 = int(input("Möchtest du\n1. in Ruhe ein Getränk schlürfen oder dich\n2. an den vollen Tisch dazusetzen?\nEntscheide wohlüberlegt: "))
        if A23 == 1:
            print("Du trinkst in Ruhe dein Getränk und gehst spät Abends wieder zurück.\nAuf dem Heimweg wirst du überwältigt und wirst ohnmächtig.\nStarte das Programm erneut.")
        elif A23 == 2:
            print("Du setzt dich zu den anderen an den vollen Tisch")
            story_voller_Tisch()
        else:
            print(deathmessage1)
    else:
        print(deathmessage1)
elif A1 == 3:
    print("Du versuchst einen Rückwärtssalto und scheiterst kläglich.\nDu kommst unglücklich auf dem Kopf auf und verlierst dein Bewusstsein.\nStarte das Programm erneut.")
else:
    print(deathmessage1)
