people = input("How many people in your house? ")
cats = input("How many cats in your house? ")
dogs = input("How many dogs in your house? ")


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less then or equal to dogs."

if people == dogs:
    print "People are dogs."
    
