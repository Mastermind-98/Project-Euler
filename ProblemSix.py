#basic idea is setting the value of the square sum and sum of squares 
# as 0, iterating through values of x from 1 to 101 and appending the values 
def differenceBetweenSumSquareAndSquares(): #defining the function
    sumOfSquares = 0 #defining the two variables
    totalSum = 0
    
    for x in range(1, 101): #loop from 1-100
        sumOfSquares += x ** 2 #appending each square of x to the total value
        totalSum += x #finding the sum
        
    squareOfSum = totalSum ** 2 #squaring the sum
    difference = squareOfSum - sumOfSquares #calculating the difference
    print(difference) 

differenceBetweenSumSquareAndSquares() #calling the function