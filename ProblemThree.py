def get_prime_factors(n):
    factors = []
    
    # Remove all factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
# To check if a number is prime/ to find the prime factors, you only need to check the factors until the square root of the number 
# n must be odd at this point, so it is possible to skip even numbers (i += 2)
    x = 3
    while x^2 <= n: #iterate until the square root of n
        while n % x == 0: #checking if x is a factor
            factors.append(x) #adding x to the factor list if it is a factor
            n //= x #assigning the new value of the number to the divisior result of the previous division
        x += 2 #going to the next odd number
        
    #If n is still greater than 2, the remaining n must be prime
    if n > 2:
        factors.append(n)
        
    return factors


print("Prime factors of" + str(600851475143)+ str(get_prime_factors(600851475143)))