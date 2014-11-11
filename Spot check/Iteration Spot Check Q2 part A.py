#Daniel Ogunlana
#11/11/2014
#Iteration Spot Check Q2 part A

integer = int(input("Please enter an integer:"))

print("Times table for",format(integer))

for count in range (1,13):
    result = count*integer
    print("{0} * 9 ={1}".format(count,result))
