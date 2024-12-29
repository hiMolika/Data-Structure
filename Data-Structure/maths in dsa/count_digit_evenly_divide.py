def evenlydivide(n):
    count = 0
    for digit in str(n):
        d= int(digit)
        if d!= 0 and n % d==0:
            count += 1
    return count
n=121
print(evenlydivide(n))