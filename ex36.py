from sys import exit
from rooms import *
from secondfloorrooms import *
from basementrooms import *

def generic_room():
    print genericroom

    next = raw_input("> ")

    if next == "n" or "north":
        foyer()
    elif next == "e" or "east":
        charred_room()
    elif next == "w" or "west":
        creeky_hall()
    elif next == "s" or "south":
        south()    
    else:
        dead("You stumble around the room until you starve.")

def creeky_hall():
    print creekyhall

    next = raw_input("> ")

    if (next == "b") or "back":
        entrance_hall()
    elif (next == "w") or "west":
        ball_room()  
    else:
        dead("You stumble around the room until you starve.")

def dead(why):
    print why, "Good Job!!"
    exit(0)

def entrance_hall():
    print entrancehall

    next = raw_input("> ")

    if next == "n":
        generic_room()
    elif next == "e":
        generic_room()
    elif next == "w":
        creeky_hall()
    else:
        dead("You stumble around the room until you starve.")

def outside():
    print outsidedesc

    next = raw_input("> ")

    if (next == "y") or "yes":
        entrance_hall()
    else: 
        dead("The were wolf catches you and eats you.")

print intro
raw_input ("> ")
outside()
