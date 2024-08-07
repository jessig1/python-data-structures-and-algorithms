def factorial(n):
    #base case when function stops mandatory
    if n == 0 :
        return 1
#function calls itself (recursive case) goes to base case
    return n * factorial(n-1)

#factorial(4)

#example of fibonnaci formula (double recursion)
def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)

# iteration of finding product of numbers in array

def array_product(arr):
    total = 1
    for n in arr:
        total *= n
    return total

#recursion of product of numbers in array

def array_product(arr):
    if not arr:
        return 1
    return arr[0] * array_product(arr[1:])

#recusion adds frames to the stack slower and more memory, iteration faster. However, recursion good for code simplicity
# by managing call stack

# Big O depends on how recursion is implemented, 
def b(n):
    if n<= 1:
        return
    b(n-2)
# time BigO O(n) space O(n)
def c(n):
    if n <= 1:
        return
    c(n/2)
#bigO O(logn)

def d(n):
    if n <=1:
        return
    d(n-1)
    d(n-1)
#O(2n) exponential

def f(n):
    #outer loop
    if n <= 1:
        return
    #inner loop
    for _ in range(n):
        print(n)
    f(n-1)
# time O(n2) space O(n)


