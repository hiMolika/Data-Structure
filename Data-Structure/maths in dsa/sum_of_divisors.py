def sumofdivisors(n):
    result = 0
    for i in range(1,n+1):
        result += i*(n//i)
    return result

n = 5
print(sumofdivisors(n))