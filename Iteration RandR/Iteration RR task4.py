#Daniel Ogunlana
#13-10-2014
#Iteration R&R task 4

count = 0
while n:
    digit = n % 10
    if digit == 0 or digit == 5:
            count = count + 1
        n = n / 10
    return count
