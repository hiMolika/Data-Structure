'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

'''
def Fibonacci_no(n):
    if (n<=1):
        return n
    last = Fibonacci_no(n-1)
    slast = Fibonacci_no(n-2)
    return last + slast

n = int(input("enter: "))
print(Fibonacci_no(n))