#import math

#oddSquare = 0
#oddSquareCounter = 0
#x = 1

#while oddSquareCounter < 307000:
    #if math.sqrt(x).is_integer() and math.sqrt(x) % 2 != 0:
   #     oddSquare += x
  #      oddSquareCounter += 1
 #   x += 1

#print(oddSquare)

#The above code was too ineffient as it iterated through every single number until the millions, couldn't even run because it was too energy inefficient

oddSquare = 0 #sets the sum of odd squares
n = 1 #base number as the smallest odd integer

while n <= 307000: #iterates while the number is lower than 307,000 , NOT while the number of odd squares is lower than 307,000
    oddSquare += n^2 #adds the odd square to the sum
    n += 2 #iterates to the next odd number

print(oddSquare)