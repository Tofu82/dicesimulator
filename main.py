import random
import time

#Intro prompt
def intro():
    exit = False
    while exit is False:
      print ("""
Exit - To exit
Dice - Roll the dice sim""")
      choice = input("Enter your choice: ")
      if choice.upper() == "EXIT":
        print("Exiting...")
        time.sleep(1)
        quit()
      elif choice.upper() =="DICE":
        main()
      else:
          print("Invalid choice")

#Main dice sim functioin
def main():
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    rolls = input("Dice rolls: ")

    #Check if valid number input
    if rolls.isdigit():
      rolls = int(rolls)
    else:
      print("Invalid input (must be a number)")
      main()

    #Roll the dice
    for i in range(rolls):
      dice = random.randint(1,6)
      if dice == 1:
        print("1")
        ones +=1
      if dice == 2:
        print("2")
        twos +=1
      if dice == 3:
        print("3")
        threes +=1
      if dice == 4:
        print("4")
        fours +=1
      if dice== 5:
        print("5")
        fives+=1
      if dice ==6:
        print("6")
        sixes+=1
        
    #Calculate percentages function
    def percent(x):
      return x/rolls*100
      
  #Print percentages
    print (f"""
Amount | Int | Float
1s: {ones} / {int(percent(ones))}% / {percent(ones)}%
2s: {twos} / {int(percent(twos))}% / {percent(twos)}%
3s: {threes} / {int(percent(threes))}% / {percent(threes)}%
4s: {fours} / {int(percent(fours))}% / {percent(fours)}% 
5s: {fives} / {int(percent(fives))}% / {percent(fives)}%
6s: {sixes} / {int(percent(sixes))}% / {percent(sixes)}% 
""")
    total_dice_rolls = (int(ones+twos+threes+fours+fives+sixes))
    print (f"Total dice rolls: {total_dice_rolls}")
    time.sleep(0.5)
    intro()
intro()
    