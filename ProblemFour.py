listOfPalindromicNumbers = []

for y in range(100, 1000): # y and z iterate through all possible 3 digit numbers, giving every possible factor pair
    for z in range(y, 1000): # nested loop for all possible factor pairs
        x = str(y * z) #string product of the factors, converted into string so it can be reflected

        if x == x[::-1]: #checking if the number is the same if reflected (hence paolindromic)
            listOfPalindromicNumbers.append(int(x)) #appends the number to the list if palindromic

print(max(listOfPalindromicNumbers)) #returns the maximum number in the list