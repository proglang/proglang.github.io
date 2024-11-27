def links(gameover):
    gameover = 0
    print("Du gehst nach links weiter und landest außerhalb der Burg in einem Zelt\n"
          ", eine kommt Margt kommt auf dich zugerannt  und zieht dir eine Rüstung an.\n"
          " Du fragst sie, was das soll, doch sie schubst dich nur aus dem Zelt raus, wo ein Pferd auf dich wartet\n"
          " und dir eine Lanze in die Hand gedrückt wurde. Als du dich umschaust siehst du eine Menschenmenge auf einer Tribüne,\n"
          "und in der Mitte den König sitzen, als dir Dämmert das du mitten in einem Lanzenstechen gelandet bist,\n"
          "  wo du gegen einen groß gewachsenen Ritter antreten sollst.")
    entscheidung2 = int(input("Stellst du dich der Herausforderung um somit deine Tapferkeit zu Beweise gegen den Ritter zu kämpfen?1=Ja,2=nein"))
    if entscheidung2 == 2:
        print("Du entscheidest dich dagegen und wirst von der gesamten Menschenmenge verspottet.\n"
              "Deine Reise endet hier voller scham")
        gameover = 1
        return gameover
    else:
        print("Du trittst zu dem Lanzenkampf an und gewinnst.\nAls Gewinner darfst du am Abend den eidschwur gegenüber dem könig ablegen was als große Ehre gilt.")
        return gameover


def rechts(gameover):
    gameover = 0
    print("Du gehst nach Rechts und landest bei der Stadtwache die dir zu verstehen gibt,\n auf das bereitstehende Pferd zu steigen, da ihr einen Kontroll ritt durch das Dorf an der Burg macht.\n Als ihr durch das Dorf reitet siehst du einen Jungen der am Straßenrand von anderen Kindern geärgert wird.")
    enscheidung3 = int(input("Was machst du?\n1. Ich steige ab und helfe ihm\n2. Ich bin Ritter, das ist nicht meine Aufgabe"))
    if enscheidung3 == 2:
        print("Du hast dich dagegen entschieden dem Jungen zu helfen, womit du gegen den Ritter Kodex verstößt, und somit dein recht auf einen schwur beim König verlierst.\ndeine Reise endet hier und du wandelst auf ewig als ehrloser im Mittelalter")
        gameover = 1
        return gameover
    else:
        print("Du hilfst dem Jungen und vertreibst die anderen.\n Anschließend beendest du deinen Kontroll ritt, und reitest zurück zur Burg")
        return gameover


def geradeaus(gameover):
    gameover = 0
    print("Du läufst Gerade aus und landest in einem Besprechungszimmer wo sich mehrere Lords unterhalten\n und einen putsch versuch planen . sie wollen dich überreden ihnen dabei zu helfen .")
    entscheidung4 = int(input("Willst du ihnen helfen?\n1=Ja\n2=Nein"))
    if entscheidung4 == 1:
        print("Du beschliest ihnen zu helfen den König zu stürzen, ihr werdet allerdings verraten und in den Kerker gespert.\nDeine Reise endet hinter schwedischen Gardinen")
        gameover = 1
        return gameover
    else:
        print("Du gehst sofort zum König und warnst ihn davor,\n womit du deine Treue gegenüber ihm unter Beweis stellst und mit Ruhm und Ehre Belohnt wirst.")
        return gameover


def ende():
    print("Es ist mittlerweile Abend und du darfst in den Festsaal gehen wo, du dem König durch deine vollbrachten Taten die Ehre hast,\n den Eidschwur abzulegen. Nachdem du den Schwur abgelegt hast wird dir aufgetragen,\n bei dem König in einer gemauerten Fensternische wache zu halten, wärend in dem Saal die Festigkeiten fortgeführt werden.")
    entscheidung7 = int(input("Was machst du?\n1. Ich stürze mich in den Saal und feiere mit\n2. Ich bleibe auf meinem Posten und bewache den König"))
    if entscheidung7 == 1:
        print("Du entscheidest dich deinen Posten zu verlassen und feierst mit.\n Doch Plötzlich gibt der gesamte Boden unter der Menschenmenge nach und du landest in der Abtrittgrube wo du ertrinkst.\n Deine Reise endet als trauriger Zeitzeuge des Erfuters Latrinensturzes")
    else:
        print("Du bleibst auf deinem Posten und bewachst den König wodurch du deine Treue zu ihm beweist.\n Plötzlich wird dir schwarz vor augen und dir erscheint der Heilige Gral.\n Als du die Augen wieder aufmachst bist du wieder im Haus deiner großeltern\n und hast es Erfolgreich geschafft alle Prüfungen zu erledigen. Glückwunsch!")


print("Du bist in dem alten Haus deiner Großeltern welches du nach ihrem Tod geerbt hast.\n",
      "Als du durch das Haus streifst fällt dir eine Tür auf, die du schon als Kind interessant fandest aber nie rein durftest.\n",
      "Die Tür sieht aus wie aus dem Mittelater mit Holzverzierungen und einem verschnörkelten Knauf.\n",
      "Dich packt die Neugier und du willst wissen was hinter der Türe liegt.\n",
      "Du entscheidest dich durch die alte Tür zu gehen und versuchst sie zu öffnen.\n",
      "Jedoch geht sie nicht auf. Du mussterst die Tür und sieht eine inschrift mit Buchstaben „weise schieben öffnet die Tür“\n",
      "Unter den Buchstaben Fallen Dir Platten mit einem Muster auf .Du fängst an die Platten zu verschieben\n",
      "bis ein Bild vom Heiligen Gral rauskommt und die Tür sich öffnet.\n",
      "Du gehst durch die Tür und landest in einem Mittelterlich aussehenden Raum.\n",
      "Vor dir liegt alt ausschende Kleidung auf denen ein Zettel liegt wo drauf steht, zieh mich an.\n")

entscheidung1 = int(input("Ziehst du die Kleidung an?1=Ja,2=Nein:"))

if entscheidung1 == 2:
    print("Du entscheidest dich gegen die Kleidung und gehst aus dem Raum, wo du auf viele Ritter triffst die dich prompt\n"
          "Umstellen da du für sie fremde Kleidung anhast. Sie bringen dich zu ihrem König Heinrich VI, der gerade in Erfurt zu Besuch war\n"
          "Streit zu schlichten, der nach dem Sturz Heinrichs des Löwen zwischen Erzbischof Konrad I. von Mainz und dem Landgrafen Ludwig III. von Thüringen entbrannt war.\n"
          "Dieser beschliest dich hinrichten zu lassen, da er dich für eine Hexe hält aufgrund deiner modernen Kleidung\n"
          "Deine Reise endet in wärmenden Flammen")
else:
    print("Du entscheidest dich die Kleidung anzuziehen und als du die Jacke anziehst bemerkst du einen Zettel in der Tasche.\n"
          " Als du ihn öffnest erkennst du die Schrift deines Opas.\n"
          "``Wenn du diesen Zettel liest befindest du dich im Jahre 1184 in Erfurt am Hofe. König Heinrich VI ist gerade zu besuch, um den\n"
          "Streit zu schlichten, der nach dem Sturz Heinrichs des Löwen zwischen Erzbischof Konrad I. von Mainz und dem Landgrafen Ludwig III. von Thüringen entbrannt war.\n"
          "Beide sind auf der Suche nach dem heiligen Gral (ein Kelch der ein heiliges Symbol ist). Deine Aufgabe ist es genau diesen Ausfindig zu machen,\n"
          "damit du wieder in die Gegenwart reisen kannst. Dies schaffst du indem du dich in Prüfungen beweisten musst in denen es um, Tapferkeit Treue& Ehre geht\n"
          "Du liest die Nachrittzund beschliest dich aus dem Raum zu gehen, auf einen Flur der in 3 Richtungen führt")
    entscheidung5 = int(input("Welche Richtung wählst du?\n1=Links\n2=Rechts\n3=geradeaus"))
    if entscheidung5 == 1:
        gameover = 0
        gameover = links(gameover)
        if gameover == 0:
            print("Bis zum Abend willst du dir noich die Zeit vertreiben und gehts zurück zu dem Gang und hast die Wahl zwischen rechts und geradeaus")
            entscheidung6 = int(input("Wofür entscheidest du dich?\n1=Geradeaus\n2=Rechts"))
            if entscheidung6 == 1:
                gameover = 0
                gameover = geradeaus(gameover)
                if gameover == 0:
                    ende()
            else:
                gameover = 0
                gameover = rechts(gameover)
                if gameover == 0:
                    ende()
    elif entscheidung5 == 2:
        gameover = 0
        gameover = rechts(gameover)
        if gameover == 0:
            print("Bis zum Abend willst du dir noich die Zeit vertreiben und gehts zurück zu dem Gang und hast die Wahl zwischen links und geradeaus")
            entscheidung8 = int(input("Wofür entscheidest du dich?\n1=Links\n2=Geradeaus"))
            if entscheidung8 == 1:
                gameover = 0
                gameover = links(gameover)
                if gameover == 0:
                    ende()
            else:
                gameover = 0
                gameover = geradeaus(gameover)
                if gameover == 0:
                    ende()
    else:
        gameover = 0
        gameover = geradeaus(gameover)
        if gameover == 0:
            print("Bis zum Abend willst du dir noich die Zeit vertreiben und gehts zurück zu dem Gang und hast die Wahl zwischen rechts und links")
            entscheidung9 = int(input("Wofür entscheidest du dich?\n1=links\n2=Rechts"))
            if entscheidung9 == 1:
                gameover = 0
                gameover = links(gameover)
                if gameover == 0:
                    ende()
            else:
                gameover = 0
                gameover = rechts(gameover)
                if gameover == 0:
                    ende()
