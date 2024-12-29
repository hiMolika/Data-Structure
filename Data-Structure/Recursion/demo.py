# print n times name using recursion
'''
def print_name(i,n):
    if (i>n):
        return
    else:
        print("Molika")
    return print_name(i+1,n)

n = int(input())
print(print_name(1,n))
'''

# print the 1 - n without loop using recursion
'''
def printno(n):
    if(n>0):
        printno(n-1)
        print(n,end=" ")


n = int(input())
print(printno(n))
'''

# print n - 1 
def printnos(i,n):
    if (i<1):
        return
    else:
        print(i,end=" ")
    return printnos(i-1,n)

n = int(input())
print(printnos(n,n))