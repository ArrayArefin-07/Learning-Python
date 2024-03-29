

from random import randint

for x in range (1,6):     # using for loop for iteration
      gussNumber = int(input("Enter Your guess between 1 to 5 :"))
      randomNumber = randint(1,5)

      if gussNumber == randomNumber :
          print("You have won")
      else:
          print("You have lost")
          print("Random Number Was : ", randomNumber)





