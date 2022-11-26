import sys

wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

orc = "Orc"
orc_hp = 125
orc_damage = 35

dragon_hp = 300
dragon_damage = 50

while True:
    while True:
        print("Choose your character: ")
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        print("QUIT to quit")
        character_selection = input(
            "Please type a number to choose your character: ").lower()

        if character_selection == "1" or character_selection == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character_selection == "2" or character_selection == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character_selection == "3" or character_selection == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character_selection == "4" or character_selection == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif character_selection.lower() == "quit":
            sys.exit()
        else:
            print("UNKNOWN CHARACTER. YOU ARE EATEN BY THE DRAGON. YOUR CLONE, HAVING WATCHED THIS, HOPEFULLY FOLLOWS DIRECTIONS BETTER THAN YOU DID.")

    print(f"""
    You have chosen the character {character}.
    Health: {my_hp}
    Damage: {my_damage}
    """)

    while True:
        dragon_hp = dragon_hp - my_damage
        print(f"The {character} has done {my_damage} damage to the dragon!")
        if dragon_hp > 0 and dragon_hp <= 30:
            print(
                f"The dragon tires of this and bites the {character}. {character} dies. Game over.")
            break
        elif dragon_hp <= 0:
            print("The dragon is dead. You win, but at what cost?")
            break
        else:
            print(f"The dragon now has {dragon_hp} hit points!")
        my_hp = my_hp - dragon_damage
        if my_hp <= 0:
            print("I am now dead. How am I even talking? Just goes to show what happens to people who fight dragons.")
            break
        else:
            print(
                f"The dragon fights back! The {character}'s hit points are now {my_hp}.")
    while True:
        play_again = input("Play again? Y/N: ").lower()
        if play_again == "y":
            dragon_hp = 300
            break
        elif play_again == "n":
            print("Thanks for playing!")
            sys.exit()
        else:
            print(
                "DO YOU NOT KNOW HOW TO FOLLOW INSTRUCTIONS???")
