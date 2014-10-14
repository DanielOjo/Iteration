#Daniel Ogunlana
#13-10-2014
#Iteration R&R task 3(3)


password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("Thank you. You have entered the correct password")
    else:
        print("Sorry the value entered in incorrect - try again")
