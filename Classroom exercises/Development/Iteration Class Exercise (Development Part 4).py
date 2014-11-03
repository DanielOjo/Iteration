#DanielOgunlana
#03-11-2014
#Iteration Class Exercise (Development Part 4)

# largest_number = 0

#user_number_1 = int(input("Please enter a number:"))
#user_number_2 = int(input("Please enter a number:"))
#user_number_3 = int(input("Please enter a number:"))

#for count in range(1,4):
    #if (user_number_1 > user_number_2) and (user_number_1 > user_number_3):
        #largest_number = user_number_1
    #elif( user_number_2 > user_number_1) and (user_number_2 > 3):
        #largest_number = user_number_2
    #else:
        #largest_number = user_number_3
        
    #print("The largest number given is {0}".format(largest_number))

largest_number = 0

user_number_1 = int(input("Please enter a number:"))
user_number_2 = int(input("Please enter a number:"))
user_number_3 = int(input("Please enter a number:"))

for count in range(1,4):
    if (user_number_1 > user_number_2) and (user_number_1 > user_number_3):
        largest_number = user_number_1
    elif( user_number_2 > user_number_1) and (user_number_2 > 3):
        largest_number = user_number_2
    else:
        largest_number = user_number_3
        
    print("The largest number given is {0}".format(largest_number))

   
