multiplesofthree = [] #list of multiples of three
multiplesoffive = [] #list of multiples of five
n = 1

while n < 1000: #continue iterating until given boundary
    if n % 3 == 0: #divides by 3 and checks if the remainder is 0
        multiplesofthree.append(n) #appends multiples of three to the list
    elif n % 5 == 0: #divides by 5 and checks if the remainder is 5
        multiplesoffive.append(n) #appends multiples of five to the list
    n += 1 #adds 1 every iteration to incremement
    # important note that line 10 should be outside either if statement, otherwise the program would start at 1 and would never increment by 1 because 1 doesnt fit into either if statement

print((sum(multiplesofthree)) + sum(multiplesoffive)) #prints the summation of the sum of each independent list
