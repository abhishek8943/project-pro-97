import random
number = random.randint(1,9)
print(" * The number ranges from 1-9. *")
print(" * You have only 5 attempts to guess the number right * ")

chances=0


while chances < 5:
      guess = int(input("Enter your guess: "))

      if guess == number:
        print("Congratulation YOU WON !!!")
        break

      if not chances < 5:
              print (f"YOU LOSE!!! The number is ", number)