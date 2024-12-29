# wap to list all the factorial numbers less than or equal to an input number n
'''
n = 3
1 2 3 counter
1 2 6 factorial
'''
def fact(n):
    result = []
    fact = 1
    i = 1
    while fact<=n:
        result.append(fact)
        i+=1
        fact *= i
    return result
n = int(input())
print(fact(n))
