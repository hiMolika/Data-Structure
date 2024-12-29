# 3 
# output : 6 
# explanation : 1*2*3

def factorial(n):
    if (n==0):
        return 1
    return n*factorial(n-1)

n = int(input())
print(factorial(n))