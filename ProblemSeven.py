def countingPrimes(n): #defining function
    count = 0 #count for number of primes
    candidate = 2 #the prime number itself
    
    while count < n:
        # Check if the current candidate is prime
        is_prime = True #boolean for if it's a prime
        for i in range(2, int(candidate ** 0.5) + 1): #using the rule that to check if a number
            # is prime, you only need to check until its square root, added 1 to ensure you count the square root itself
            if candidate % i == 0: #checking if its a factor
                is_prime = False # if it is a factor, it is not prime
                break
                
        if is_prime:
            count += 1 #adding 1 to the count of prime numbers if prime
            if count == n: #if the prime number count is equal to the nth prime we are looking for
                return candidate
                
        candidate += 1 #adding 1 to each number to be tested

print(countingPrimes(10001)) #printing the called function with the desired nth prime