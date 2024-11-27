tool = False
bridge = True
pos = 0
choice = ""
debug = False
enter = "\n\n[press ENTER to continue]"
lnc = ("\n" * 10)  # line clear

# I recommend listening to Magnatron 2.0 (album) while playing this :)
text = """
███╗   ███╗███████╗████████╗ █████╗ ██╗      ██████╗ ███╗   ██╗
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║     ██╔═══██╗████╗  ██║
██╔████╔██║█████╗     ██║   ███████║██║     ██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║     ██║   ██║██║╚██╗██║k
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗╚██████╔╝██║ ╚████║k
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝c
"""


print(lnc + text)
if debug:
    pos = int(input("room"))
    print(pos)
else:
    input("\n" + (5 * "*") + "press ENTER to start" + (5 * "*"))
    input(lnc + "\n> You wake up." + enter)


# I would've used a loop but we're not supposed to do that
for i in "you-only-live-so-long-no-matter-what-choices-you-make":
    print(lnc)
    if debug:
        print("loop")

# 0 wakeuproom
    if pos == 0:
        print("> You find yourself in a marmor looking beton room,")
        print("> it's grudgey, but really just empty.")
        print("> A gentle humming lays in the greasy air")
        # choices:
        print("\n==== You see a narrow hallway out of the Room ====")
        print("\n- you can \"look around\" the room \n- or \"leave\" to follow hallway")
        choice = input("What do you do? ")
        if choice == "look around":
            input(lnc + "You look around the room..." + enter)
            pos = -1  # looking around startup room
            continue
        elif choice == "leave":
            input(lnc + "\nYou're walking out of the room, through the narrow corridor.\nThe humming gets louder..." + enter)
            pos = 1  # to corridor
            continue
        else:
            continue

# -1 wakeuproom lookaround
    elif pos == -1:
        print("> The room has no ceeling and appears to be some kind of shaft.")
        print("> You can't make out the top of it. Pipes are running down its sides.")
        print("> Some pipes disappear into an opening in the wall,...")
        # choices:
        # question
        print("\n==== You can make out a space behind the opening, but you can't quite fit through. ====")
        print("\n- you can try to \"break through\" the wall \n- or \"leave\" it be")
        choice = input("What do you do? ")
        if choice == "leave":
            pos = 0  # to main room view
            continue
        elif choice == "break through":
            if tool:
                input(
                    lnc + "\nYou feel the heavy metal object in your pocket.\nYou take it out." + enter)
                input(lnc + "\nIt feels familar as it lies cold in your hand." + enter)
                input(
                    lnc + "\nIt starts sirring as you point it at the wall.\nYou feel the heat building up in your palms." + enter)
                input(
                    lnc + "\nThe blast knocks you against the wall in your back, the other doesn't exist anymore." + enter)
                pos = 20  # to hallway
                continue
            else:
                input(
                    lnc + "\nYou throw yourself against the wall, but the wall doesn't care, you give up..." + enter)
                pos = 0  # to main room view
                continue
        else:
            continue

# 1 Corridor
    elif pos == 1:
        print("> You reach an intersection where the corridor takes a 90° turn.")
        print("> From one side you can hear the humming sound,")
        print("> but you also notice a narrow gap leading away, a dim glow shining from the thin passage.")
        # choices:
        # question
        print("\n==== It's barely wide enough for you to squeeze through. ====")
        print("\n- You can \"follow the humming\",\n- \"go back\" to the room you woke up in \n- or \"follow the light\" in the wall")
        choice = input("What do you do? ")
        if choice == "follow the humming":
            input(lnc + "\nYou follow the humming..." + enter)
            pos = 2
            continue
        elif choice == "go back":
            input(lnc + "\nYou turn away from the glowing gap and walk back into the room where you first came from" + enter)
            pos = 0
            continue
        elif choice == "follow the light":
            input(lnc + "\nYou squeze yourself through the narrow gap,\nyou have to walk sideways, step by step, you come closer to the light..." + enter)
            pos = 4
            continue
        else:
            continue

# 2 Entrance -Terminal Room
    elif pos == 2:
        print("> The corridor continues.")
        print("> There are now doors left and right,")
        print("> one of the doors is slightly open.")
        # choices:
        # question
        print("\n==== You can hear loud electrical humming and clicking noises from inside ====")
        print("\n- You can \"open the door\" to enter the room,\n- walk down the corridor to the \"right\" of the door,\n- or follow the corridor \"left\" from the door")
        choice = input("What do you do? ")
        if choice == "open the door":  # to terminal (15)
            input(
                lnc + "\nYou press against the door, it resists, but opens with a squeak..." + enter)
            pos = 15
            continue
        elif choice == "right":
            input(lnc + "\nYou turn right..." + enter)
            pos = 1  # back to corridor1
            continue
        elif choice == "left":  # to corridor 3
            input(lnc + "\nYou turn left..." + enter)
            pos = 3
            continue
        else:
            continue

# 15 Terminal room
    elif pos == 15:
        print("> You find yourself in a room full of cables and machinery")
        print("> It contrasts the empty hallways you've seen in every way.")
        print("> The Wall is plastered with monitors, the floor is mostly cables.")
        # choices:
        # question
        print("\n==== Amongst the lights and noise, you spot a terminal awaiting input... ====")
        print("\n- You can try to \"interact\" with the terminal,\n- or \"leave\" the room")
        choice = input("What do you do? ")
        if choice == "leave":  # to terminal (15)
            input(
                lnc + "\nYou turn away from the strange machinery and leave the room..." + enter)
            pos = 2
            continue
        elif choice == "interact":
            print(lnc + "\n> The terminal requests a password:")
            print("\n>>> USER::c§k-Kyri")
            if (input(">>> PASSWORD::") == "1226"):
                input(
                    ">>> PASSWORD ACCEPTED\n---welcome back, you have (1) new message---" + enter)
                pos = 14  # unlocked terminal
            else:
                input(
                    lnc + "The terminal informs you that the password was incorrect." + enter)
            continue
        else:
            continue

# 14 open terminal
    elif pos == 14:
        print("> Suddenly the machine starts to come to life.")
        print("> With a pneumatic sound of rushing air the machine opens up.")
        print("> It appears to be some kind of interface...")
        # choices:
        print("\n==== it has the shape of a body. ====")  # question
        print("\n- You can \"engage\" with the interface,\n- or \"log out\" of the terminal\n- you can also \"read the message\"")
        choice = input("What do you do? ")
        if choice == "log out":  # to terminal (15)
            input(
                lnc + "\nYou close the terminal and back off,\nthe machine closes itself again." + enter)
            pos = 15
            continue
        elif choice == "read the message":
            print(lnc + "\nBROADCAST MESSAGE: \nCONTACT WITH ADMINISTRATION LOST.")
            input(
                "FIND NET-TERMINAL-GENE TO REESTABLISH CONTROL OF THE CITY.\nEND OF LINE." + enter)
            continue
        elif choice == "engage":
            print(lnc + "\nYou step into the machine..." + enter)
            print(lnc + "\nThe machine closes itself around you connecting your mind to the flow of electrons..." + enter)
            # End: secret Netsphere Ending - You jack in and try to reach out to the administration, your journey from here on out is beyond the physical world
            input(
                lnc + "Your journey from here on out is going beyond the physical world..." + enter)
            pos = 99
            continue
        else:
            continue

# Corridor 5
    elif pos == 5:
        print("> You reach a crossing.")
        print(
            "> You stand at the intersection of a massive pipe large enough to walk through")
        print("> and a rectangular corridor, both made of the same concrete-like material.")
        # choices:
        print("\n==== You can make out an opening at the end of the pipe ====")
        print('\n- You can follow the pipe "forward" in the direction of the presumed exit')
        print('- Take the corridor to your "left"')
        print('- Take the corridor to your "right"')
        print('- or go "back" deeper into the pipe')
        choice = input("What do you do? ")
        if choice == "left":
            input(lnc + '\nYou step out of the pipe and onto flat ground...' + enter)
            pos = 6
            continue
        elif choice == "right":
            input(lnc + '\nYou take the right hallway. It gets darker.\nYou can make out window frames, but there are no windows.\nYou continue walking...' + enter)
            pos = 3
            continue
        elif choice == "forward":
            if bridge:
                input(lnc + '\nYou follow the pipe and finally step outside...' + enter)
                pos = 7
                continue
            else:
                input(
                    lnc + '\nYou find only the remains of a broken ledge over the abyss.' + enter)
                input(lnc + 'You return inside.' + enter)
                continue
        elif choice == "back":
            input(lnc + '\nYou walk further into the darkness, the pipe is getting smaller and smaller. \nYou have to crawl, but you can make out a strange glow in the distance' + enter)
            input(lnc + 'you get closer...' + enter)
            pos = 4
            continue
        else:
            continue


# 6 Sackgasse there is nothing
    elif pos == 6:
        print("> You follow the corridor around a corner and another one.")
        print("> Suddenly the path ends.")
        print("> It's quiet here.")
        # choices:
        print("\n==== You find yourself in a dead end ====")
        print('\n- you can "go back"')
        print('- or "look around" maybe you find something interesting...')
        choice = input("What do you do? ")
        if choice == "go back":
            input(lnc + "\nYou go back." + enter)
            pos = 5
            continue
        elif choice == "look around":
            input(
                lnc + "\nNope, it's really just a dead end, there's nothing interesting here." + enter)
            continue
        else:
            continue

# 3 Corridor with Stairs
    elif pos == 3:
        print("> The corridor takes another turn.")
        print("> From one side you hear the humming sound, the other leads past some dead windows.")
        print("> There is also a flight of stairs leading away.")
        # choices:
        print("\n==== You can't see where they lead, but it doesn't seem far... ====")
        print('\n- you can "take the stairs"')
        print('- go "left" past the windows')
        print('- or go "right" towards the humming sound')
        choice = input("What do you do? ")
        if choice == "take the stairs":
            input(lnc + "\nThey lead you around a corner..." + enter)
            pos = 16
            continue
        elif choice == "left":
            input(lnc + "\nYou walk past some windows with nothing in them,\nit's just the frame and wall, walk further..." + enter)
            pos = 5
            continue
        elif choice == "right":
            input(
                lnc + "\nYou walk past some closed doors, the humming gets louder" + enter)
            pos = 2
            continue
        else:
            continue

# 16 Tool Room
    elif pos == 16:
        print("> You enter a small circular room.")
        print("> Columns are lining the wall,")
        print("> some giving space to the outside.")
        # choices:
        print("\n==== There is a wide podest in the center. ====")
        print('\n- You can "leave" the room')
        print('- or "inspect" the podest')
        choice = input("What do you do? ")
        if choice == "leave":
            input(lnc + "\nYou take the stairs back..." + enter)
            pos = 3  # Back to corridor
            continue
        elif choice == "inspect":
            if not tool:
                input(lnc + "\nYou step closer, there is a symbol on the podest:\n -|- \nIt seems strangely familiar. You feel something in your pocket,..." + enter)
                input(lnc + "You take it out." + enter)
                input(lnc + "A small metal object rests in your hand, on it you see engraved the same symbol:\n"
                      " -|- \nIt feels like it has a special meaning to you, but you don't know since when you have it or where you got it from." + enter)
                input(lnc + "You put the metal object back in your pocket." + enter)
                tool = True
                continue
            else:
                input(lnc + "\nThe symbol reminds you of something..." + enter)
                continue
        else:
            continue

# 4 Lichtbrunnen
    if pos == 4:
        print("> You come to a room seemingly hidden away in the structure.")
        print("> In its center there is a fountain of light, emitting an eerie glow.")
        print(
            "> There is no real way in or out, but you see a big pipe-opening in the wall")
        print("> and a gap in the concrete on the opposite side of the room....")
        # choices:
        print("\n==== Both are barely wide enough for you to fit through. ====")
        print('\n- You can "inspect" the fountain,')
        print('- try to "squeeze through" the gap,')
        print('- or "crawl in pipe"')
        choice = input("What do you do? ")
        if choice == "inspect":
            print(lnc + "In the middle of the room there stands a Fountain of light.")
            print("   The mesmerizing shimmer draws one in.")
            print("   From the two spouts at the peak,")
            print("   cascade two harmonious streams of light,")
            print("   glowing down the bizarre six-sided fountain.")
            input(
                "You try to touch the liquid, but your hand just glides through the rays." + enter)
            continue
        elif choice == "squeeze through":
            input(lnc + "\nYou have to walk sideways but you fit through..." + enter)
            pos = 1
            continue
        elif choice == "crawl in pipe":
            input(lnc + "\nThe pipe is close to the ceiling, you first have trouble reaching it, \nit gets wider after a while and merges with many smaller pipes.\nYou can almost walk up straight now..." + enter)
            pos = 5
            continue
        else:
            continue


# 7 Die brücke
    elif pos == 7:
        print("> You stand on sort of a bridge, it has no railing, just a straight path across.")
        print("> You can't make out an end to the structures at either side of it.")
        print("> There are bridges and openings scarcely scattered over the two seemingly endless walls at either end.")
        # choices:
        print("\n==== You see lightning is striking from one side to the other, loudly tearing the air ====")
        print('\n- "You can "go back"')
        print('- or "look" over the edge')
        print('- or "cross it" to get to the other side')
        choice = input("What do you do? ")
        if choice == "go back":
            input(lnc + "\nYou to turn and walk back into the structure..." + enter)
            pos = 5
            continue
        elif choice == "look":
            input(lnc + "\nLooking over the edge, you can see neither a floor, ceiling, nor end in any direction of the fissure." + enter)
            input(lnc + "\nJust as you are about to back off, lightning strikes the bridge, sending tremors up and down..." + enter)
            input(lnc + "\nYou try to grab something to hold onto..." + enter)
            input(lnc + "...but ultimately fall off the rumbling bridge..." + enter)
            pos = 10
            continue
        elif choice == "cross it":
            input(lnc + "\nYou walk across the wide bridge to the other side." + enter)
            input(lnc + "\nIt takes you some time." + enter)
            pos = 9
            continue
        else:
            continue

# 9 The Door
    elif pos == 9:
        print("> You reach the other side, but it's blocked.")
        print("> A massive metal door is locking you out.")
        print("> There is no obvious way of opening it.")
        # choices:
        print("\n==== It seems like it hasn't opened in a long time ====")
        print('\n- You can try to "knock"')
        print('- "force" it open')
        print('- or "go back"')
        choice = input("What do you do? ")
        if choice == "knock":
            input(
                lnc + "\nYou knock firmly, a metallic echo roars through the fissure." + enter)
            input(lnc + "\nNothing happens." + enter)
            continue
        elif choice == "force":
            if not tool:
                input(
                    lnc + "\nYou try to force it open by hand, but it does not give in." + enter)
                continue
            else:
                input(
                    lnc + "\nYou remember the heavy metal object in your pocket.\nYou take it out." + enter)
                input(lnc + "\nIt feels familiar as it lies cold in your hand." + enter)
                input(
                    lnc + "\nIt starts stirring as you point it at the door.\nYou feel the heat building up in your palms." + enter)
                input(
                    lnc + "\nThe blast throws you a few meters on your back, you land on the bridge." + enter)
                print(
                    lnc + "\n\n\n> There now is a massive hole in the structure where the door used to be,")
                print("> but you took out part of the bridge too.")
                print(
                    "> You hear the metal screeching below you as you feel the bridge slowly starting to fall.")
                bridge = False
                # choices:
                print(
                    "\n==== The door is now open, but there is a gap between you and it... ====")
                print('\n- You can "run back" to the other side')
                print('- or try to make the "jump"')
                choice = input("What do you do? ")
                if choice == "run back":
                    input(
                        lnc + "\nYou run as fast as you can and barely make it back, as the bridge collapses behind you." + enter)
                    pos = 5
                    continue
                elif choice == "jump":
                    input(lnc + "\nYou stand up and run." + enter)
                    input(
                        lnc + "\nThe bridge already starts falling as you take the leap..." + enter)
                    input(
                        lnc + "\nIt's too far... you touch the ledge but can't get a hold on it." + enter)
                    input(lnc + "\nYou fall...." + enter)
                    pos = 10
                    continue
                else:
                    input(
                        lnc + "\nIn panic, you stumble and fail to do anything at all. \nYou fall together with the bridge..." + enter)
                    pos = 10
                    continue
        elif choice == "go back":
            input(lnc + "\nYou walk back to the other side, it's a long way..." + enter)
            pos = 7
            continue
        else:
            continue


# 10 The Fall, you fall several minutes deeper and deeper into the structure, you couldn't have told where the light was coming from, but it's getting darker (just enter)
    elif pos == 10:
        print("> You fall deeper and deeper into the structure.")
        print("> You couldn't have told earlier where the light was coming from,")
        print("> but it's getting darker the longer you fall.")
        # choices:
        print("\n==== You've been falling for several minutes ====")
        input("\n- You continue to fall..." + enter)
        pos = 8
        continue


# 8 the Pit
    elif pos == 8:
        print("> Your impact shatters the concrete below your feet,")
        print("> the thin layer of liquid lingering in the muddy down below shoots up and creates a rain of black water.")
        print("> Everything that falls eventually lands here, as have you.")
        # choices:
        print(
            "\n==== You see a creature crawling out from the filth. It comes closer... ====")
        print('\n- You can try to "fight it off"')
        print('- or try to "run"')
        choice = input("What do you do? ")
        if choice == "fight it off":
            if tool:
                pos = 111  # fight with tool
                continue
            else:
                pos = 11  # Fight without the tool
                continue
        elif choice == "run":
            input(
                lnc + "\nYour feet start moving, but the thick sludge won't allow you to run." + enter)
            print(
                lnc + "\n\n\n> The creature with shiny black skin seems to have no such problems,")
            print("> As you look over your shoulder you see its pointy legs,")
            print(
                "> like needles they stab with ease through the ground, as it comes closer...")
            print("\n====  It's not really a chase; you're not running away. ====")
            # choices:
            print('\nYou can "continue to flee" or try to "fight it off"')
            choice = input("What do you do? ")
            if choice == "continue to flee":
                input(
                    lnc + "\nYou try to hasten your pace, but the ground won't allow it." + enter)
                input(
                    lnc + "\nYou feel the stab in your back, before your one body turns to plural..." + enter)
                pos = 97  # End of the journey
                continue
            elif choice == "fight it off":
                if tool:
                    pos = 111
                    continue
                else:
                    pos = 11  # Fight without the tool
                    continue
            else:
                continue
        else:
            continue

# 111 fight with tool
    elif pos == 111:
        input("Your instinct lets you grab the metal object you've found." + enter)
        input(lnc + "\nYou blow a crater into the ground before you. \nThe knockback sends you flying with a cloud of wet filth stirred up from the previous ground..." + enter)
        input(lnc + "\nYou are safe for now.\nIt's a long way up, but you can defend yourself now. \nThe hot iron in your hand reminds you what you were looking for..." + enter)
        pos = 98
        continue

# 11: fight no tool
    elif pos == 11:
        print("You let the creature come closer, it's hard to move around here.")
        input(lnc + "\nAs it comes into reach, you're ready and throw a punch directly into what you assume to be the creature's face." + enter)
        input(lnc + "\nThe sharp teeth of the creature remove your arm from where it used to be." + enter)
        print(lnc + '\n- You can throw another "punch"\n- try to "rip off" the creature\'s leg \n- or try to "flee")')
        choice = input("What do you do? ")
        if choice == "punch":
            input(lnc + "\nThe creature doesn't bother with your fist; the last thing you see are sharp teeth closing around you." + enter)
            pos = 97  # Journey ends here
            continue
        elif choice == "rip off":
            input(lnc + "\nYou change your tactic and grab one of the creature's legs; you rip it off with force." + enter)
            input(
                lnc + "The creature sends a howl echoing through the ravine. It didn't expect this move." + enter)
            input(
                lnc + "You take the hard sharp hull and send it through the hurt creature's center." + enter)
            input(lnc + "The creature collapses. You've won and pull your separated arm out of the corpse. It is going to heal..." + enter)
            input(lnc + "You are safe for now and it's a long way up, but have proven you can fight for yourself." + enter)
            pos = 98
            continue
        elif choice == "flee":
            input(lnc + "\nThere is no running away now; the creature is right in front of you. \nBefore you can turn around, you're impaled by the creature..." + enter)
            pos = 97  # Journey ends here
            continue
        else:
            continue

# 20 Stairway to the great above
    # you go up (player gets no choice of going back)
    # End: the Great ABOVE
    elif pos == 20:
        print("> You step through the glowing stone hole, where there used to be a wall.")
        print("> Liquid dripping from the remains of pipes, hissing on the hot stone")
        print(
            "> There is a staircase, but the path back, or down is now blocked by rubble.")
        # choices:
        print("\n==== The only way is up ====")  # question
        print("\n- you can \"go up\"")
        choice = input("what do you do? ")
        if choice == "go up":
            print(lnc + "\nYou walk up the several hundred stairs.")
            input("The stairs finally end, bringing you to the surface..." + enter)
            print(
                lnc + "\n\n\n> You stand on top of the flat structure's roof, spanning out as far as you can see.")
            print(
                "> Ravines are scattered like a grid, reaching down into the structure.")
            print("> There are towers reaching up to what first seemed like a sky ...")
            print("\n==== You realize the illuminated ceiling could be just the underbelly of an even bigger structure... ====")
            input("\n- Your journey from here on out continues further up to reach the top and whatever lies above..." + enter)
            pos = 99
            continue
        else:
            continue

# 97: Death ending
    elif pos == 97:
        input("\nYour journey ends here." + enter)  # Death ending
        pos = 99
        continue

# 98: Continuing Through the Trench
    elif pos == 98:
        input("Your journey from here on out continues through the muddy waters of the trench..." + enter)
        pos = 99
        continue

    elif pos == 99:
        print("========= THE END =========")
        print(" *     +     *  . *    +\n    + .    *   + *   .  *\nThanks for playing my game <3\n")


if debug:
    print(pos)
if pos != 99:
    print("program has teminated: You have lost your way.")
