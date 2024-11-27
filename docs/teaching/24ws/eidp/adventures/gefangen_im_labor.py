if __name__ == "__main__":
    print(" Du bist im Labor eines verrückten Wissenschaftlers"
          + "\ngefangen. Es ist dunkel. Mit dem letzten Rest deines"
          + "\nHandyakkus findest du noch etwas Luminol, brauchst"
          + "\naber noch eine zweite Substanz, um Chemolumineszenz"
          + "\nzu erzeugen. Was verwendest du?")
    res = input(" Verwendest du\nA) Wasserstoffperoxid oder\nB)"
                + " Schwefelsäure\n ... ")
    if res == "A" or res == "a":
        res2 = input(" Du weißt auch, dass du für die Reaktion noch"
                     + "\neinen Katalysator brauchst. Verwendest du"
                     + "\nA) Eisen\nB) Periodat\nC) oder verwendest"
                     + "\n du die Nadel auf dem Tisch und"
                     + "\ndesinfizierst sie vor Verwendung, um dein"
                     + "\neigenes Blutbeizumischen?\n ... ")
        if res2 == "C" or res2 == "c":
            print(" Auch Blut ist ein guter Katalysator für die"
                  + "\nReaktion von Luminol. Dies wird auch in der"
                  + "\nKriminalistik verwendet. Du konntest etwas"
                  + "\nLicht ins Dunkel bringen und siehst endlich,"
                  + "\nwas um dich herum passiert. Vergiss aber"
                  + "\nnicht, ein Pflaster zu verwenden, sonst"
                  + "\nhinterlässt du noch überall Blutspuren.")
            res2b = input(" Verwendest du\nA) die Dino-Pflaster oder"
                          + "\nB) die Schmetterling-Pflaster?"
                          + "\n ... ")
            if res2b == "a" or res2b == "A":
                print(" Sehr cool! Wusstest du übrigens, dass das"
                      + "\nWort Dinosaurier aus dem Griechischen"
                      + "\nkommt? Deinos = schrecklich und Sauros ="
                      + "Eidechse.")
            else:
                print(" Sehr hübsch! Wusstest du übrigens, dass"
                      + "\nSchmetterlinge kurzsichtig sind und nur"
                      + "\n10 bis 12 Meter weit sehen können?")
        else:
            print(" Du konntest etwas Licht ins Dunkel bringen und"
                  + "\nsiehst endlich, was um dich herum passiert.")
    else:
        print(" Das hat leider nicht funktioniert. Probiere es noch"
              + " einmal.")
        exit(1)

    print(" Nun, da du etwas siehst, bemerkst du, dass sich im Labor"
          + "\nein Safe befindet, der sich nur durch ein Rätsel"
          + "\nöffnen lässt.")
    print(" Du findest aber auch eine Brechzange mit der du"
          + "\nversuchen könntest, das Schloss an der Labortür zu"
          + "öffnen.")
    res2a = input(" Was möchtest du tun?\nA) Die Brechzange"
                  + " verwenden\nB) Das Rätsel lösen.\n ... ")
    if res2a == "A" or res2a == "a":
        print(" Du versuchst, mit der Brechzange das Schloss an der"
              + "\nTür zu öffnen. Leider scheint es so, als sei"
              + "\ndurch das viele Arbeiten mit Schwefelsäure im"
              + "\nLabor die Brechzange zu korrodiert zu sein."
              + "\nWährend du noch versuchst, das Schloss"
              + "\naufzubrechen geht sie kaputt. Es bleibt dir wohl"
              + "\ndoch nichts anderes übrig, als dasRätsel zu"
              + "\nlösen...")
    else:
        print(" Du hast dich für das Rätsel entschieden."
              + "Viel Erfolg!")
    res3 = input(" In dem Rätsel musst du die Kationen einer Probe"
                 + "\ndurch Flammenfärbung bestimmen. Du kannst"
                 + "\neine grüne Färbung sowie eine rote Färbung"
                 + "\nerkennen. Wodurch kann die grüne"
                 + "\nFlammenfärbung erzeugt werden?\nA) Be\nB) Mg"
                 + "\nC) Ca\nD) Sr\nE) Ba\n ...")
    if res3 == "E" or res3 == "e":
        print(" Richtig, jetzt musst du noch die rote Farbe"
              + "\nerklären.")
    else:
        print(" Das stimmt leider nicht :(")
        exit(1)
    res4 = input(" Wodurch kann die rote Flammenfärbung erzeugt"
                 + "\nwerden?\nA) Li\nB) Na\nC) K\nD) Rb\nE) Cs"
                 + "\n... ")
    if res4 == "A" or res4 == "D" or res4 == "a" or res4 == "d":
        print(" Richtig, es gibt aber noch eine andere Möglichkeit.")
        if res4 == "A" or res4 == "a":
            res5 = input(" Ist die andere Möglichkeit:"
                         + "\nA) Na\nB) K\nC) Rb\nD) Cs\n ... ")
            if res5 == "C" or res5 == "c":
                print(" Richtig!")
            else:
                print(" Das stimmt leider nicht :(")
                exit(1)
        if res4 == "D" or res4 == "d":
            res5 = input(" Ist die andere Möglichkeit:"
                         + "\nA) Li\nB) Na\nC) K\nD) Cs\n ... ")
            if res5 == "A" or res5 == "a":
                print(" Richtig!")
            else:
                print(" Das stimmt leider nicht :(")
                exit(1)
    else:
        print(" Das stimmt leider nicht :(")
        exit(1)
    print(" Nun ist das Problem, dass du kein Spektroskop finden"
          + "\nkannst und daher nicht die Rottöne von Li und Rb"
          + "\nunterscheiden kannst. Entsprechend musst du einfach"
          + "\nausprobieren, welche PIN richtig ist. Schreibe zuerst"
          + "\ndie Ordnungszahlen von Ba, Li und Rb auf:")
    res6 = input(" Ordnungszahl von Ba: ")  # 56
    res7 = input(" Ordnungszahl von Li: ")  # 3
    res8 = input(" Ordnungszahl von Rb: ")  # 37
    if res6 == "56" and res7 == "3" and res8 == "37":
        print(" Jetzt musst du nur noch die Richtige Kombination"
              + "\nherausfinden. Du stellst außerdem fest, dass die"
              + "\nPIN 4-stellig ist. Probiere nun aus:")
    else:
        print(" Da ist dir wohl ein Fehler unterlaufen. :(")
        exit(1)
    res9 = input(" PIN: ")
    if res9 == "3756":
        print(" Heureka! Der Safe hat sich geöffnet!")
    elif res9 == "5637":
        print(" Dann muss es wohl andersherum sein... ")
        res9a = input(" PIN: ")
        if res9a == "3756":
            print(" Heureka! Der Safe hat sich geöffnet!")
    else:
        print(" Wie bist du denn auf diese Zahlen gekommen? :o")
        exit(1)

    print(" In dem Safe befindet sich eine Box, die sich durch ein"
          + "\nRätsel öffnen lässt.")
    resx = input("Nenne zuerst eine Zahl zwischen 1 und 4\n... ")
    if resx == "1":
        res10 = input(" Nenne die Ordnungszahl des Elements, das bei"
                      + "\nca. 40 Grad Celsius eine goldene"
                      + "\nFlüssigkeit ist\n ... ")
        if res10 == "55":
            print(" Richtig, es handelt sich um Cs.")
        else:
            print(" Das stimmt leider nicht :(")
            exit(1)
    elif resx == "2":
        res11 = input(" Nenne die Ordnungszahlen von zwei Elementen,"
                      + "\ndie bei Raumtemperatur flüssig sind"
                      + "\n(durch Leerzeichen getrennt)\n ... ")
        if res11 == "35 80" or res11 == "80 35":
            print(" Richtig, die Elemente sind Br und Hg.")
        else:
            print(" Das stimmt leider nicht :(")
            exit(1)
    elif resx == "3":
        res12 = input(" Die Beimengung geringer Mengen welchen/-r"
                      + "\nElements/-e zu Saphir wird als Rubin"
                      + "\nbezeichnet?\nA) Fe und Ti\nB) Cr\nC) Ti"
                      + "\nD) V\n ... ")
        if res12 == "B" or res12 == "b":
            print(" Richtig, ein Saphir mit Cr wird rot und als"
                  + "\nRubin bezeichnet. Mit Fe und Ti wird die"
                  + "\nFarbe blau, mit Ti rosa und mit V violett.")
        else:
            print(" Das stimmt leider nicht :(")
            exit(1)
    elif resx == "4":
        res13 = input(" Welchen Druck in GPa braucht man, um Diamant"
                      + "\nsynthetisch herzustellen?\nA) 3\nB) 4"
                      + "\nC) 6\nD) 7\n... ")
        if res13 == "C" or res13 == "c":
            print(" Richtig, zur synthetischen Herstellung von"
                  + "\nDiamant wird ein Druck von 6 GPa und eine"
                  + "\nTemperatur von 1500 Grad Celsius benötigt.")
        else:
            print(" Das stimmt leider nicht :(")
            exit(1)
    else:
        print(" Das war aber keine Zahl zwischen 1 und 4 ;)")
        exit(1)

    print(" In der Box befindet sich ein Schlüssel! Herzlichen"
          + "\nGlückwunsch, du hast es aus dem Labor geschafft!")
