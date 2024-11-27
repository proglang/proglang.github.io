# Warhammer?
# Lord of the rings?
# Custom Dnd campaign?
# Zombie? Walking dead/Last of us
# Fallout?
# Sci fi? Starwars?
print("You find yourself in the besieged city of praag. You are a captain commanding a unit of about 7 soldiers. The armies of Chaos amass on the gates of Praag. They prepare for an assault, you see" + "\n" + "large siege towers closing in on the walls, while simeoultaneously you see battering ramms close in on the gate. You are ordered to man the catapult on the gates. As the enemy designs move into range" + "\n" + "you know that you will only get 2 shots off before they reach the city walls. What do you do?")
print("1 = Do you shoot the siege tower? A more direct threat to your unit but less critical to the defense of the city")
print("2 = Do you shoot the batteruing ramm? A less direct threat to your unit but choose carefully, if the gates are breached the city is doomed.")

Choice_1 = input("Orders?! screams one of your men")
if Choice_1 == "1":
    print("Open fire! you scream moments before two siege towers go down in flames, along with their entire crew. The remaining 2 siege towers dock on the walls but for now the crews on the wall manage to" + "\n" + "hold back the tide of beastmen daemonettes. However looking on the grounds bellow you notice that by now the battering ramm has done severe damage to the gate and with an ershattering explosion the gate" + "\n" + "is blown wide open. A tide of heavily armored chaos warriors flood through the gate and the meager defenses are overwhelmed. You realize that the catapult is now useless.")
    print("1 = Do you order your squad to reeinforce the wall?")
    print("2 = Do you attempt to make a stand together with what remains of the garrisson on the streets?")
    Choice_1_2 = input("Wie möchtest du fortfahren?")
    if Choice_1_2 == "1":
        print("You bark at your men to get into formation and contest the siege towers, the fighting quickly gets brutal and you get pushed back slowly exhaustion and the overwhelming tide of chaos pushing you back." + "\n" + "Then you see a glimpse on the horizon you ponder what this glimpse could mean, until one of the lookouts screams 'The reeinforcements have arrived! The Tzarina is here!' the men fight with renewed vigour and you" + "\n" + "manage to push the invaders back into the towers. The city stood proud for hundreds of yours and it will continue to do so, it did not fall under your watch. Victory!")
    elif Choice_1_2 == "2":
        print("You order your men to descend into the streets of the city. The defenses on the ground have benn overwhelmed and you see looting and a massacre of the civilians and soldiers alike. You order your men into formation" + "\n" + "and rally to one of the few remaining defensable position still held by your allies. You are quickly surrounded by all sorts of vile opponents, they launch wave attacks in complete disregard for their lives. You see a fanatical frenzy" + "\n" + "in their eyes, its unlike anything you have ever seen before, so full of hate and corruption. The position holds fast in the oncoming avalanche of chaos warriors. The defenses, however, start to falter as you are slowly overwhelmed. You make a heroic last stand until you are finally felled.")
elif Choice_1 == "2":
    print("Target the Battering ram! You bellow at your men. Boulders are launched and they hit true. The threat to the gate has been dealt with. However the siege towers move forward unimpided. Four siege towers make contact with the wall" + "\n" + "a tide of chaos spills forth out of the towers. The fighting on the walls becomes chaotic and all sence of unit-cohesion and training is lost on such narrow terrain. Despite your best efforts the defenses start crumbling. Your men are being overwhelmed.")
    print("Do you order a retreat?")
    print("1 = Yes")
    print("2 = No")
    retreat = input("What do you do?:")
    if retreat == "1":
        print("As you begin to fall back you realized that you are already encircled and that you just ran into the weapons of the enemies behind you. You meet your end upon the walls you swore to defend.")
    else:
        print("You decide to make the ultimate sacrifice and die where the fighting is thickest. Just as you are about to succumb to your wounds you see a glimmer of hope upon the horizon. Could it be reeinforcements?. Wether it was or not you will not live to tell the tale.")
# Based on a warhammer campaign with some friends.
