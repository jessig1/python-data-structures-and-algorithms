def factorial(n):
    #base case when function stops mandatory
    if n == 0 :
        return 1
#function calls itself (recursive case) goes to base case
    return n * factorial(n-1)

factorial(4)