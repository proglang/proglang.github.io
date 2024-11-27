selection = str('1')  # The following lines are variables for the Progression of the Game

end = str('Du hast das Ende das Spiels Erreicht. Vielen Dank fürs Spielen')

advance = ("Bitte '1' drücken um fortzufahren")

wmdt1 = str("Was möchtest du tun? [1]")
wmdt2 = str("Was möchtest du tun? [1 / 2]")
wmdt3 = str("Was möchtest du tun? [1 / 2 / 3]")
wmdt4 = str("Was möchtest du tun? [1 / 2 / 3 / 4]")

Merge1 = str("0")
Merge2 = str("0")
Merge3 = str("0")

key = str("0")

# following are the variables that contain the story and the story options, S1 is the
# introduction, afterwads the first integer is reference to the number of the current branch
# and the 2nd integer is referece to which option was chosen in the branch before

S1 = str("""Die Sonne geht gerade unter, dir ist kalt, der Wind pfeift durch die Bäume und du hast
wieder seit Tagen nichts gegessen, am Stadtrand steht die alte Sommerresidenz einer Adelsfamilie
deren Namen du schon längst wieder vergessen hast, aber das ist auch echt nicht wichtig, du bist
nur hier im nach etwas von Wert in diesem Haus zu suchen dass du zu ein bisschen Geld machen kannst.
Durch die verbarrikadierten Fenster im Erdgesschoss bist du auf das Haus aufmerksam geworden,
sie Zeugen davon, wie lange schon niemand mehr hier wohnt.""")
S1opt1 = str("1. Du gehst weiter auf der Suche nach einem besseren Haus am nächsten Tag.")
S1opt2 = str("2. Du gehst in den Garten und schaust nach einem Weg einzubrechen.")
S1opt3 = str("3. Du versuchst die Haustür aufzubrechen.")

S21 = str("""Du gehst die lange spärlich beleuchtete Straße hinauf zur Bushaltestelle zurück,
dein knurrender Magen erinnert dich an deinen Hunger. An der Bushaltestelle angekommen
schaust du auf den Fahrplan, der nächste Bus kommt erst am Morgen. Du legst du dich auf
die Bank und schläfst frierend ein.""")

S22 = str("""Du gehst in den Garten und suchst nach einem Weg hinein. Dort findest du ein
eingeschlagenes Kellerfenster und kannst dich gerade so durchzwängen. Von hier aus springst du den
letzten Meter hinunter zum Boden. Unten angekommen schaust du dich um, Scheiße, das fenster ist viel
zu weit oben um wieder hindurch rnach draußen zu klettern. Du befindest dich in einem Weinkeller.
Überall um dich herum sind große schwere alte Weinfässer in die Wände eingelassen. Du öffnest
vorsichtig die Tür und siehst Licht am anderen Ende des Gangs. Außerdem hörst du die Schritte einer
Person und siehst einen leichten Schatten durch die Werkstatttür. Auf der rechten Seite des Gangs
befindet sich eine weitere angelehnte Tür. Dahinter ist es dunkel und eine Jacke hängt vor der Tür
am Haken. Direkt links von dir, befindet sich eine dünne Steintreppe welche nach oben führt, das
obere Ende der Treppe ist außerhalb deiner Sicht.""")

S22opt1 = str("1. Du entscheidest dich, die Treppe nach oben zu nehmen.")
S22opt2 = str("2. Du schleichst auf die Werkstatt zu um den dunklen Raum im Keller zu Erkunden.")

S23 = str("""Du läufst schnell und mit gebücktem Kopf zur Haustür, und drückst die Quietschende
Türklinke hinuter. Du ziehst mit einem starken Ruck an der Tür, doch diese bewegt sich
keinen Zentimeter, auch drücken hilft nichts. Du versuchst vergeblich die Tür mit einem
Ast aus dem Vorgarten aufzustemmen. Doch sie bleibt fest verschlossen.""")

S23opt1 = str("1.Du gehst weiter auf der Suche nach einem besseren Haus am nächsten Tag.")
S23opt2 = str("2. Du gehst in den Garten und schaust nach einem Weg einzubrechen.")

S24 = str("""Die Tür schwingt lautlos auf und du lehnst sie hinter dir wieder an.
Du traust dich nicht das Licht anzumachen, also muss der schwache Schein durch den Türschlitz genügen.
Von dem was du erkennen kannst befindest du dich in einem Heizungskeller,
du hörst das leise Rauschen von Wasser und Gas. Ansonsten ist der Raum eine Sackgasse.
Neben der Tür durch welche du hereingekommen bist, siehst du etwas metallisch glitzern.
Du gehst heran und findest einen Schlüssel. Er ist alt und angerostet, jedoch ist der Rost
an den Zähnen leicht abgekrazt als wäre er kürzlich verwendet worden.""")

S24opt1 = str("1. Du steckst den Schlüssel in deine Hosentasche")
S24opt2 = str("2. Du lässt den Schlüssel am Haken")

S25 = str("")


print(S1 + "\n")
print(wmdt3 + "\n" + S1opt1 + "\n" + S1opt2 + "\n" + S1opt3 + "\n")
selection = (input("Entscheide dich für eine Option:"))
print(" ")

if selection == '1':  # 2.1
    print(S21 + "\n")
    print(wmdt1 + "\n" + advance + "\n")
    selection = (input("Entscheide dich für eine Option:"))
    print(" ")
    if selection == '1':
        print(end)
        # Story ended
elif selection == '2':  # 2.2 Im Garten
    print(S22 + "\n")
    Merge1 = '1'

elif selection == '3':  # vor der Haustüre
    print(S23 + "\n")
    print(wmdt2 + "\n" + S23opt1 + "\n" + S23opt2 + "\n")
    selection = (input("Entscheide dich für eine Option:"))
    print(" ")
    if selection == '1':
        print(S21 + "\n")
        print(wmdt1 + "\n" + advance + "\n")
        selection = (input("Entscheide dich für eine Option:"))
        print(" ")
        if selection == '1':
            print(end)
            # Story ended

    if selection == '2':  # Im Garten
        print(S22 + "\n")
        Merge1 = '1'

if Merge1 == '1':
    print(wmdt2 + "\n" + S22opt1 + "\n" + S22opt2 + "\n")
    selection = (input("Entscheide dich für eine Option:"))
    print(" ")
    if selection == '1':  # Treppe Hoch
        Merge2 = '1'

    elif selection == '2':
        print(S24 + "\n")  # Heizungskeller
        print(wmdt2 + "\n" + S24opt1 + "\n" + S24opt2 + "\n")
        selection = (input("Entscheide dich für eine Option:"))
        print(" ")
        if selection == '1':
            key = '1'
        elif selection == '2':
            key = '0'
        Merge2 = '1'

if Merge2 == '1':  # Ab hier kommt das Erdgeschoss in welchem man sich frei bewegen kann
    print("""Du huscht leise aber zügig die Treppe hinauf, oben angekommen stehst du in einem Flur. Hinter dir hörst du auf einmal Schritte auf der Treppe, es gibt vier Türen, alle sind geschlossen,
an der Tür direkt rechts von dir hängt ein Schild mit der Aufschrift „Küche“. Du rennst in die Küche und schaust durch einen dünnen Spalt in der Türe auf den Flur. Das Licht im Flur geht,
an und du siehst eine Gestalt mit einem langen Messer aus der Kellertüre kommen. Du erkennst die Jacke von der Türe im Keller wieder. Allerdings hat die Gestalt die Kapuze so tief ins Gesicht gezogen, dass du sie nicht erkennst.
Du bekommst Panik und vergisst deinen Hunger. Finde einen Weg nach draußen und fliehe so schnell es geht!""")

    print("\n" + wmdt2)
    print("1. Du gehst durch die Tür mit der Aufschrift “Badezimmer”.")
    print("2. Du gehst zurück in den Flur.")
    print(' ')

choice = input("Entscheide dich für eine Option:")


def Badezimmer():
    print("5.1 Du befindest dich im dunklen Badezimmer. Hier war schon lange niemand mehr. Das Waschbecken ist vermodert und das Fenster ist zu klein zum Entkommen und sonst scheint es hier nichts Brauchbares zu geben.")
    print("\n" + wmdt2)
    print("1. Du gehst zurück in die Küche.")
    print("2. Du gehst durch eine Holztüre in den Flur.")
    print(' ')

    choice = input("Entscheide dich für eine Option:")

    if choice == "1":
        Küche()
    elif choice == "2":
        Flur()


def Flur():
    print("Du stehst im kalten Flur. Hier riecht es komisch und Wasser tropft von der Decke. Hier gibt es 4 Türen.")
    print("\n" + wmdt4)
    print("1. Du gehst durch die Holztüre ins Badezimmer")
    print("2. Du gehst zurück in die Küche")
    print("3. Du gehst durch eine Glastüre ins Foyer")
    print("4. Die Türe zum Wohnzimmer steht offen.")
    print(' ')

    choice = input("Entscheide dich für eine Option:")

    if choice == "1":
        Badezimmer()
    elif choice == "2":
        Küche()
    elif choice == "3":
        Foyer()
    elif choice == "4":
        Wohnzimmer()


def Küche():
    print("Du stehst wieder in der Küche. Es scheint ruhig und du findest nichts Neues. Dein Magen knurrt, weil du an Essen denkst.")
    print(wmdt2)
    print("1. Du gehst ins Bad")
    print("2. Du gehst zurück auf den Flur")
    print(' ')

    choice = input("Entscheide dich für eine Option:")

    if choice == "1":
        Badezimmer()
    elif choice == "2":
        Flur()


def Wohnzimmer():
    print("Du landest im Wohnzimmer. Hier liegt altes Kinderspielzeug herum. Die große Uhr in der Ecke schlägt 4 mal. Du erschreckst dich. Komisch, dass die Uhr in so einem alten Haus noch funktioniert. Es gibt 2 Türen.\n" +
          wmdt2)
    print("1. Du gehst zurück in Flur")
    print("2. Du gehst durch durch die große Flügeltür ins Foyer")
    print(' ')

    choice = input("Entscheide dich für eine Option:")

    if choice == "1":
        Flur()
    elif choice == "2":
        Foyer()


def Foyer():
    print("Du stehst im Foyer. An der Decke hängt eine alte, flackernde Glühbirne. Seltsame Ölgemälde hängen an der Wand und ein Zebrafell liegt auf dem Boden. Hier gibt es eine Treppe nach oben. Die Stufen scheinen alt aber stabil.\n" +
          wmdt3)
    print("1. Du nimmst die Treppe nach oben.")
    print("2. Du gehst ins Wohnzimmer.")
    print("3. Du gehst zurück in den Flur.")
    print(' ')

    choice = input("Entscheide dich für eine Option:")

    if choice == "1":
        # Ab hier kommt das Obergeschoss
        print("""Du rennst die Treppe in den ersten Stock hinauf. Oben angekommen bemerkst du, dass etwas dir die Treppen hinauf folgt. Du rüttelst an der ersten Türe,
diese ist aber fest verschlossen. In Panik rennst du die Treppe weiter hinauf und gelangst so ins Dachgeschoss. Die Decken sind niedrig und schräg.
Du schlägst dir den Kopf an einer alten Lampe an und stolperst über eine große Holzkiste.""")
        print(wmdt2 + "\n")
        print("1. Du Versteckst dich in der Holzkiste" + "\n" + "2. Du rennst weiter auf der Suche nach einem Ausweg" + "\n")
        selection = (input("Entscheide dich für eine Option:"))

        if selection == '1':
            print("""Du reißt den Deckel der Holzkiste auf und bemerkst voller Schrecken, dass es sich um einen Sarg handelt.
Du hörst, wie die Dielen hinter dir knarzen. Du legst dich hektisch in den Sarg und schließt den Deckel hinter dir.
Das Knarzen kommt näher und scheint an dir vorbei zu ziehen. Du hältst den Atem an und versuchst, kein Geräusch von dir zu geben.
Plötzlich kommt das Knarzen wieder näher und es ist für einen Augenblick still. Dann hämmert es neben deinem Kopf und bemerkst,
dass dein Sarg gerade zugenagelt wird.""")
            print(wmdt1 + "\n" + advance + "\n")
            selection = (input("Entscheide dich für eine Option:"))
            print(" ")
            if selection == '1':
                print(end)
            # Story ended
        elif selection == '2':
            print("Du rennst gebückt weiter und siehst eine Türe, die scheinbar auf das Dach führt.")
            print(wmdt2 + "\n")
            print("1. Du Versteckst dich doch in der Kiste" + "\n" + "2. Du versuchst, die Tür zu öffnen" + "\n")
            selection = (input("Entscheide dich für eine Option:"))
            print(" ")
            if selection == '1':
                print("""Du reißt den Deckel der Holzkiste auf und bemerkst voller Schrecken, dass es sich um einen Sarg handelt.
Du hörst, wie die Dielen hinter dir knarzen. Du legst dich hektisch in den Sarg und schließt den Deckel hinter dir.
Das Knarzen kommt näher und scheint an dir vorbei zu ziehen. Du hältst den Atem an und versuchst, kein Geräusch von dir zu geben.
Plötzlich kommt das Knarzen wieder näher und es ist für einen Augenblick still. Dann hämmert es neben deinem Kopf und bemerkst,
dass dein Sarg gerade zugenagelt wird.""")
                print(wmdt1 + "\n" + advance + "\n")
                selection = (input("Entscheide dich für eine Option:"))
                print(" ")
                if selection == '1':
                    print(end)
            # Story ended
            if selection == '2' and key == '0':
                print("Die Türe ist fest verschlossen. Du hörst ein Geräusch und entscheidest dich doch in der Kiste zu verstecken")
                print("""Du reißt den Deckel der Holzkiste auf und bemerkst voller Schrecken, dass es sich um einen Sarg handelt.
Du hörst, wie die Dielen hinter dir knarzen. Du legst dich hektisch in den Sarg und schließt den Deckel hinter dir.
Das Knarzen kommt näher und scheint an dir vorbei zu ziehen. Du hältst den Atem an und versuchst, kein Geräusch von dir zu geben.
Plötzlich kommt das Knarzen wieder näher und es ist für einen Augenblick still. Dann hämmert es neben deinem Kopf und bemerkst,
dass dein Sarg gerade zugenagelt wird.""")
                print(wmdt1 + "\n" + advance + "\n")
                selection = (input("Entscheide dich für eine Option:"))
                print(" ")
                if selection == '1':
                    print(end)
            # Story ended
            if selection == '2' and key == '1':
                print("""Die Türe scheint fest verschlossen, doch dir fällt der rostige Schlüssel aus dem Keller ein.
Du überlegst nicht lange und oh Wunder - der Schlüssel passt und lässt sich drehen. Du entkommst aufs Dach und ziehst die Türe hinter dir wieder zu.
Die Sonne geht auf und du hast einen tollen Ausblick auf den Sonnenaufgang über der Stadt. Dir springt das Efeu ins Auge,
welches an der Seite des Hauses hinauf windet. Ohne nachzudenken kletterst du an diesem hinunter. Du bist gerettet.""")
                print(wmdt1 + "\n" + advance + "\n")
                selection = (input("Entscheide dich für eine Option:"))
                print(" ")
                if selection == '1':
                    print(end)
            # Story ended

    elif choice == "2":
        Wohnzimmer()
    elif choice == "3":
        Flur()


if choice == "1":
    Badezimmer()
elif choice == "2":
    Flur()
