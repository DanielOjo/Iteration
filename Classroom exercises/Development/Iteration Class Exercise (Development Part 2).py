#DanielOgunlana
#31-10-2014
#Iteration Class Exercise (Development Part 2)
 
number_stars = int(input("How many stars do you want on each row:"))
number_display = int(input("How many times would you like this to display?:"))
stars_printed = "*"

for stars in range(1,number_display+1):
    print(stars_printed*number_stars)
    

   
