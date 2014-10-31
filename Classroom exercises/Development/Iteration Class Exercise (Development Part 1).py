#DanielOgunlana
#30-10-2014
#Iteration Class Exercise (Development Part 1)

#Pretty much a times table
#May need to make more variables and make them *Each other

#First vrison would not multiply number result
#---------------------------------------------
#user_number = int(input("Please enter a number:"))
#for numbers in range(1,user_number):
#    print(numbers)
#    print("-------------")

   
user_number = int(input("Please enter a number:"))
number_display = int(input("How many times would you like this to display?:"))
for numbers in range(1,number_display+1):
    print(numbers)
    print(numbers*user_number)
    print("-------------")
   
