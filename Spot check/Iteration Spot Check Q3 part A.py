#Daniel Ogunlana
#11/11/2014
#Iteration Spot Check Q3 part A

guessed = False
number = random.randint(1,1000

noOfTurns = 0

while number != number:
    noOfTurns = noOfTurns + 1
    userGuess = int(input("Enter your guess for the number: "))
    if userGuess == number:
        guessed = True
    elif userGuess > number:
        print("The number you guessed is too high")
    else:
        print("The number you guessed is to low")

print("You took {0}'s turns to guess the number",format(noOfTurns))
    


