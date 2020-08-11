# -*- coding: utf-8 -*-
import time
import random
avenger = ['captain america', 'spider man ', 'hulk', 'thor']
avenger_chosen = random.choice(avenger)


def print_pause(message, seconds=2):
    """
    This function causes a short stop every time
    is of 2 seconds each time a message on it
    screen appears. At the same time I can too
    determine whether I stop correctly for certain messages
    longer or shorter.
    """

    print(message)
    time.sleep(seconds)


def play_again():
    """
    This function asks the player if they want to play again.
    Input:
        Play again ?: player must enter yes or no and this is possible
        are done with uppercase or lowercase letters.
    Behavior:
        If the player wants to play again, the game starts again.
        If the player does not want to play again, stop the game.
        If the player does not enter a valid value, the function remains
        ask for a valid value.
    """

    again = input('Would you like to play again? (yes/no)\n').lower()
    while True:
        if again == 'yes':
            print_pause('Excelent! Restarting the game...')
            global avenger_chosen
            avenger_chosen = random.choice(avenger)
            play_game()
            break
        elif again == 'no':
            print_pause('Alright. Thank you for playing!')
            break
        else:
            again = input("Please enter a 'yes' or 'no'.\n")


def intro():
    """
    This feature is the introduction to the game. This is what the player gets
    to see when the game starts.
    """

    print_pause('You are in  a avengers city'
                f" with high buildings and silent wind.", 2)
    print_pause('their is a rumour that {avenger_chosen} find somebody who'
                f" is honest and daring to save the earth and wants to take"
                f" that person with them in the rescue mission....."
                f'may be you are the lucky one.', 3)
    print_pause('In front of you their is a high rise building.')
    print_pause('To your right is  a old museum.')
    print_pause("you have a rescue bag with you in which"
                f" their is a torch,some food and your dagger.", 2)


def building(items):
    """

Function that determines what options the player has
    when he is in the building and how the game
    expires.

    Behavior:
        If the player has the items, he / she wins the game.
        If the player does not have the items, the choice is his
        given to fight anyway or to go back to the city.
        If the player does not enter a valid value, the function remains
        ask for a valid value.
    """

    print_pause('You approach the main door of the building.')
    print_pause("You are about to knock when the door "
                f"opens and out steps a {avenger_chosen} and say's."
                )
    print_pause(" This is a avengers's house ! and then come to attack you   "
                )
    decision = input('Would you like to (1) fight or (2) run away?\n')
    while True:
        if decision == '1':
            if 'iron man suit' in items:
                print_pause('As the {avenger_chosen} moves to attack'
                            f"you wear your new suit and geet ready.", 2)

                print_pause('The suit is like  iron man and Shield '
                            f"shine brightly in your possession as you brace"
                            f" yourself for the attack.\nBut the "
                            f"{avenger_chosen} takes one look at you iron man "
                            f"suit and go inside and take the team all avenger"
                            f" are came out and got that you are the one", 3)
                print_pause("Now you are ready to save the earth"
                            f"You are an avenger now!", 2)
                play_again()
                break
            else:
                print_pause('The {avenger_chosen} attacks you! You feel a'
                            f" bit under-prepared for this !you forget that"
                            f" you have iron man suit! what with only having"
                            f' a tiny sword.', 2)
                print_pause('You do your best...but your dagger is no match'
                            f' for the avenger.', 2)
                print_pause('You have been defeated.....you run away '
                            f'i think their is something in the museum!', 2)
                play_again()
                break
        elif decision == '2':
            print_pause('You run as fast as you can back into the city.'
                        )
            print_pause('You scared out, the {avenger_chosen} almost'
                        f'grabs you foot.'
                        )
            print_pause('You stand up and run as fast as you can back'
                        f" into the city safely, you are a coward"
                        f"why dont you use your iron man suit "
                        f'sorry you are not an avenger!!', 2)
            city(items)
            break
        else:
            decision = \
                input('Would you like to (1) fight or (2) run away?\n')


def cave(items):
    """
    This feature is only meant to grab the items to continue with
    the story to go.
    At the end, the iron man suit and shield are on the trick
    'items' added.
    """

    print_pause('You peer cautiously into the museum.')
    print_pause('It turns out to be a very dark muhseum and your'
                f'you use you torch, you find  a suit and sword near you ')
    print_pause(",but suddenly your  eye catches a bad villan in"
                f" front of you .  but You have found the iron "
                f"man  suit  and a shield.", 2)
    print_pause('You discard your silly old dagger and take the suit'
                f" with you.\n you wear the suit and use the sword "
                f'and kill the monster.. and get out from the museum', 3)
    items.append('iron man suit')
    building(items)


def city(items):
    """
    Function decides what options the player has
    when he is in the city.
    Input:
        items: player has the shield and sword (not?)
        Player chooses on the city whether he wants to go to the"
        f" building or to the cave.
    Behavior:
        When the player makes a choice, the corresponding
        functions are called.
        If the player does not enter a valid value, the function remains
        ask for a valid value.
    """

    print_pause('What would you like to do?')
    choice = \
        input('''Enter 1 to knock on the door of the tall building.
Enter 2 to peer into the old museum.
Please enter 1 or 2.
''')

    while True:
        if choice == '1':
            building(items)
            break
        elif choice == '2':
            cave(items)
            break
        else:
            choice = input("Please, enter '1' or '2'.\n")


def play_game():
    """
    This function brings the game together by listing the items
    define and ultimately the intro function and the city
    function.
    """

    items = []
    intro()
    city(items)


if __name__ == '__main__':
    play_game()
