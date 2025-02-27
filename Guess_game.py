""" We are going to write the  program that generates a random number and ask the user to guess it. If the player
guess is higher than the actaual number, the program displays "Lower number please." Similarly if the user's'
guess is too low. The program prints "Higher number please". When the user guess correct number, the program 
displays the number of guess player used to arrive at the number. """
 
import random
randNumber = random.randint(1, 100)
user = None
guess = 0

while(user != randNumber):
    user = int(input("Enter your guess number: "))
    guess += 1
    if (user == randNumber):
        print("Your guess is right.")
    else:
        if (user > randNumber):
             print("Your guess is wrong. Try smaller number.")
        else:
            print("Your guess is wrong. Try larger number.")

print(f"You guess the number in {guess} guess.")
