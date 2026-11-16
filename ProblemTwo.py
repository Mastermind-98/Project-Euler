def sum_even_fibonacci(limit): #function for the fibonacci sequence
    a, b = 1, 2 #first 2 values of the sequence
    even_sum = 0 #sum of even numbers
    
    while a <= limit: #loop that iterates until the current term is 4 million
        if a % 2 == 0: #checks if the current term is even
            even_sum += a #adds current term to the sum if it is even
        a, b = b, a + b # "a, b" is equal to "b, a+b" meaning that b is the old a term, and a+b is the new b term
        
    return even_sum #returns the even sum

result = sum_even_fibonacci(4000000)#calls the function with the limit parameter set to 4 million
print(result) # hence prints the summation of all even items in the fiboncci sequence until 4 million
