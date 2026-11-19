number = 20 #minimum number that the answer could be

while True:
    for i in range(1, 21): #checking numbers between 1-20
        if number % i != 0: #checking remainder of division
            break
    else:
        print(number)
        break

    number += 20 #instead of checking through every single number, to save memory you can go up in increments of 20