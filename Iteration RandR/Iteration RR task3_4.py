#Daniel Ogunlana
#13-10-2014
#Iteration R&R task 3(4)

user_message = input("Please enter a message:")
message_number = int(input("how many times do you want your message to be shown on the screen?:"))

print("Your message is")
for counter in range(message_number):
    print(user_message)
