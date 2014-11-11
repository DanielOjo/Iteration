#Daniel Ogunlana
#11/11/2014
#Iteration Spot Check Q1 part D

number = 0
total = 0

while number != -1:
    number = int(input("please enter a number: "))
    total = total + (number*number)

print("The total is",format(total))
