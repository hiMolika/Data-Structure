def armstrong_no(n):
    dup=n
    sum=0
    while(n>0):
        last_dig=n%10
        sum=sum+last_dig**3
        n=n//10
    if (sum==dup):
        return True
    else:
        return False

n=153
print(armstrong_no(n))