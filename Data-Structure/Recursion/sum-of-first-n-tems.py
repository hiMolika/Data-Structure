# n=5 
# output: 225 as explanation: 1^3+2^3+3^3+4^3+5^3

def sumOfseries(n):
    if (n==0):
        return 0
    return n**3 + sumOfseries(n-1)

n = int(input())
print(sumOfseries(n))