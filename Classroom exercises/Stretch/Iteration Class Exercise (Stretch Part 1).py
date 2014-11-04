#DanielOgunlana
#04-10-2014
#Iteration Class Exercise (Stretch Part 1)

user_number = int(input("Please enter a number:"))
loop_number = user_number*-1

if user_number < 0:
    for count in range(1,loop_number):
        print(count)
        print(count*(user_number),count*(user_number*2), count*(user_number*3), count*(user_number*4), count*(user_number*5))
        print("-------------")

else:
    for count in range(1,user_number):
        print(count)
        print(count*(user_number),count*(user_number*2), count*(user_number*3), count*(user_number*4), count*(user_number*5))
        print("-------------")
   
