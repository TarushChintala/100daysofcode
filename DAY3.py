print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("Welcome to the adventure game!")
path = input("You are at a crossroads. Do you go down the left path or the right path?: left or right?\n").lower()
if path == "l":
    river = input("While walking down the path you come across a river. Do you try to swim across it or do you wait for a boat? swim or wait?\n").lower()
    if river == "wait":
        chest = input("On the other side of the river you see 3 chests. An ordinary looking wooden chest, a gold bejewelled chest and a monstrous looking chest. Which chest do you open? wooden, golden, monstrous?\n").lower()
        if chest == "wooden":
            print("You find supplies for your adventure. \nYOU WIN CHAPTER 1.")
        elif chest == "golden":
            print("Oh no! That chest was a mimic that gobbled you up. \nYOU DIED")
        else:
            print("You open the monstrous chest and get gobbled up it. What did you expect?\nYOU DIED")
    else:
        print("You try to swim across the river and get swept away by the current.\nYOU DIED")
else:
    print("While walking down the path, you get ambushed by bandits.\nYOU DIED")