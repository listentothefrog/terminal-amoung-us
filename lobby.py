import random
import sys
import time

players = ["Red", "Blue", "Green", "Yellow", "Orange", "Black", "White", "Purple"]

def set_lobby():
    imposter = random.choice(players)
    print("CREWMATE \nThere is 1 imposter amoung us"  )
    time.sleep(2)
    player_input = raw_input("Guess the imposter: ")

    if player_input == imposter:
        print("{}".format(player_input) + " was the imposter")
        print("VICTORY")
    else:
        print("{}".format(player_input) + " was not the imposter")
        player_input = raw_input("Guess the imposter: ")
        if player_input == imposter:
            print("{}".format(player_input) + " was the imposter")
            print("VICTORY")
        else:
            print("{}".format(player_input) + " was not the imposter")
            print("DEFEAT")
            sys.exit()
set_lobby()
